import mysql.connector
import typing
from typing import Tuple, Optional, List, Dict, TypeVar, Type, Iterable, Sequence
import abc
import itertools
import unittest
import datetime

import config



# The base class that defines all basic operations of the class
class Entity(abc.ABC):
    T = TypeVar('T', bound="Entity") # for type annotation. See https://stackoverflow.com/a/44644576/4281627

    @classmethod
    def _db_id_name(cls) -> Optional[str]:
        """
        The name of id.
        The entity updates its id after insertion.
        """
        return None

    @classmethod
    def _db_table_name(cls) -> str:
        return cls.__name__

    @classmethod
    def _select_equals(cls, cursor, attrs : Optional[Iterable[str]] = None, **conditions):
        assert conditions # Nonempty
        if attrs:
            attrs = ", ".join(attrs)
        else:
            attrs = "*"
        condition_str = " AND ".join(key + "=%s" for key in conditions.keys())
        query = f"SELECT {attrs} FROM {cls._db_table_name()} WHERE {condition_str}"
        return cursor.execute(query, tuple(conditions.values()))

    @classmethod
    def _delete_equals(cls, connection, **conditions):
        condition_str = " AND ".join(key + "=%s" for key in conditions.keys())
        query = f"DELETE FROM {cls._db_table_name()} WHERE {condition_str}"
        cursor = connection.cursor()
        cursor.execute(query, tuple(conditions.values()))
        connection.commit()

    @classmethod
    @abc.abstractmethod
    def _db_attr(cls) -> Tuple[str]:
        """All attributes for this enitity."""
        pass

    def update(self):
        """
        Save every attribute into the db.
        """
        raise NotImplementedError

    def insert(self):
        table_name = type(self).__name__
        attr_name = ", ".join(self._db_attr())
        attr_fstr = ", ".join("%s" for _ in self._db_attr())
        # getattr(self, "s", None) is equivalent to self.s if self.s is defined, else it's equivalent to None
        attr_val = [ getattr(self, name, None) for name in self._db_attr() ]
        cmd = f"INSERT INTO {table_name} ({attr_name}) VALUES ({attr_fstr})"
        cursor = self._connection.cursor()
        cursor.execute(cmd, attr_val)
        if self._db_id_name():
            setattr(self, self._db_id_name(), cursor.lastrowid)
        self._connection.commit()

    @classmethod
    def _from_seq(cls : Type[T], seq : Sequence) -> T:
        attrs = cls._db_attr()
        assert len(seq) == len(attrs)
        instance = cls()
        for name, val in zip(attrs, seq):
            setattr(instance, name, val)
        return instance

    @classmethod
    def _from_id(cls : Type[T], connection, entity_id : int) -> T:
        cursor = connection.cursor()
        table_name = cls.__name__
        attr_name = cls._db_attr()
        attr_id_name = cls._db_id_name()
        cls._select_equals(cursor, **{attr_id_name : entity_id})
        query_res = cursor.fetchone()
        instance = cls._from_seq(query_res)
        instance._connection = connection
        return instance




class Merchandise(Entity):
    @classmethod
    def _db_id_name(cls):
        return "merchandise_id"

    @classmethod
    def _db_attr(cls):
        return (
            "merchandise_id",
            "name",
            "price",
            "number_in_stock",
            "number_sold",
            "category_id",
            "seller_id",
            "description",
        )

class Seller(Entity):
    @classmethod
    def _db_id_name(self):
        return "seller_id"

    @classmethod
    def _db_attr(cls):
        return (
            "seller_id",
            "account",
            "password",
            "name",
            "register_time",
            "email",
        )


class Customer(Entity):
    @classmethod
    def _db_id_name(cls):
        return "customer_id"

    @classmethod
    def _db_attr(cls):
        return (
            "customer_id",
            "account",
            "password",
            "name",
            "register_time",
            "bill_info",
            "email",
        )


class OrderItem(Entity):
    @classmethod
    def _db_attr(cls):
        return (
            "order_id",
            "merchandise_id",
            "trade_price",
            "number",
            "status",
        )


class Category(Entity):
    @classmethod
    def _db_id_name(cls):
        return "category_id"

    @classmethod
    def _db_attr(cls):
        return (
            "category_id",
            "name",
            "parent_category",
        )


class Order(Entity):
    @classmethod
    def _db_id_name(cls):
        return "order_id"

    @classmethod
    def _db_attr(cls):
        return (
            "order_id",
            "customer_id",
            "order_time",
        )

class Cart(Entity):
    @classmethod
    def _db_attr(cls):
        return (
            "customer_id",
            "merchandise",
        )

    def cart_show(self) -> List[Tuple[Merchandise, int]]:
        """
        Return a list of (Merchandise, int)
        """
        raise NotImplementedError

    def cart_add(self, m : Merchandise, m_nums : int):
        raise NotImplementedError

    def cart_remove(self, m : Merchandise, m_nums : int):
        raise NotImplementedError


class Review(Entity):
    pass
    # I have no idea how to implement this

class Faq(Entity):
    @classmethod
    def _db_id_name(cls):
        return "faq_id"

    @classmethod
    def _db_attr(cls):
        return (
            "merchandise_id",
            "faq_id",
            "customer_id",
            "question_text",
            "question_time",
            "answer_text",
            "answer_time",
        )


class Auction:
    @staticmethod
    def connect_mysql(
            user : Optional[str] = None,
            password: Optional[str] = None,
            host : Optional[str] = None,
            database: Optional[str] = None
        ) -> "Auction":
        login_info = config.LOGIN_INFO.copy()
        var_names = ("user", "password", "host", "database")
        local_vars = locals()
        for var_name in var_names:
            var = local_vars[var_name]
            if var:
                local_vars[var_name] = var
        cnt = mysql.connector.connect(**login_info)
        return Auction(cnt)

    def __init__(self, connection):
        # connection is a type of mysql connection. (See Mysql connector document. )
        self.connection = connection
        self.cursor = self.connection.cursor()

    def customer_register(self, c : Customer):
        """ Create a new Customer in the db, and fills the id in c. """
        c._connection = self.connection
        c.register_time = datetime.datetime.now()
        c.insert()

    def seller_register(self, s : Seller):
        """ Create a new Seller in the db, and fills the id in c. """
        s._connection = self.connection
        s.register_time = datetime.datetime.now()
        s.insert()

    def _login(self, cls : Type[Entity.T], account : str, password : str) -> Optional[Entity.T]:
        cls._select_equals(self.cursor, account=account)
        query_res = self.cursor.fetchone()
        if query_res is None:
            return None
        instance = cls._from_seq(query_res)
        if password == instance.password:
            return instance
        else:
            return None

    def customer_login(self, account: str, password: str) -> Optional[Customer]:
        """ Returns a Customer if login succeeds, else return None. """
        return self._login(Customer, account, password)
        

    def seller_login(self, account: str, password: str) -> Optional[Seller]:
        """ Returns a Seller if login succeeds, else return None. """
        return self._login(Seller, account, password)

    def search_merchandise(self, filter_condition) -> List[int]:
        """
        Returns a list of merchandise id.
        TODO : filter condition not defined yet.
        """
        raise NotImplementedError

    def get_merchandise_data(self, merchandise_id: int) -> Merchandise:
        raise NotImplementedError

    def get_purchase_history(self, customer_id : int) -> List[int]:
        """
        Return a list of Order id.
        """

        raise NotImplementedError


    def new_cart(self, c : Customer) -> Cart:
        raise NotImplementedError

    def new_order(self, c : Cart) -> Order:
        """ Put everything in the cart into a new order """
        raise NotImplementedError

    def seller_history(self, s : Seller) -> List[int]:
        """
        Return a list of Order id.
        """
        raise NotImplementedError

    def get_order(self, order_id : int) -> Order:
        raise NotImplementedError

    def new_merchandise(self, s : Seller, m : Merchandise):
        raise NotImplementedError

    def set_merchandise_data(self, m : Merchandise) -> None:
        raise NotImplementedError

    def delete_merchandise(self, m : Merchandise) -> None:
        raise NotImplementedError

    def give_review(self, order : Order, s : Seller, r : Review):
        raise NotImplementedError

    def show_review(self, s : Seller) -> List[Review]:
        raise NotImplementedError

    def add_to_blacklist(self, c : Customer, s : Seller):
        raise NotImplementedError

    def show_blacklist(self, c : Customer) -> List[int]:
        """
        return a list of blacklisted seller id.
        """
        raise NotImplementedError

    def remove_from_blacklist(self, c : Customer, s : Seller):
        raise NotImplementedError

    def list_faq(self, m : Merchandise) -> List[int]:
        raise NotImplementedError

    def get_faq(self, m : Merchandise, faq_id : int) -> Faq:
        raise NotImplementedError

    def ask(self, c : Customer, m : Merchandise, question : str) -> Faq:
        raise NotImplementedError

    def answer(self, faq : Faq, answer : str):
        """
        Put the containt of anser into the faq, and update it to the db.
        """
        raise NotImplementedError

class classproperty():
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


class DBTestCase(unittest.TestCase):
    @classproperty
    def db_name(cls):
        return cls.__name__

    @classmethod
    def setUpClass(cls):
        login_info = config.LOGIN_INFO.copy()
        del login_info["database"]
        cls.connection = mysql.connector.connect(**login_info)
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute(f"CREATE DATABASE {cls.db_name} DEFAULT CHARACTER SET 'utf8'")
        cls.cursor.execute(f"USE {cls.db_name}")

    @classmethod
    def tearDownClass(cls):
        try:
            cls.cursor.fetchall()
        except mysql.connector.errors.InterfaceError:
            pass
        cls.cursor.execute(f"DROP DATABASE {cls.db_name}")
        cls.connection.commit()
        cls.connection.close()

    def tearDown(self):
        self.connection.rollback()


class EntityTest(DBTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cursor.execute(
            r"CREATE TABLE `TestEntity` ("
            r"  `Entity_id` int(11) NOT NULL,"
            r"  `Account` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL,"
            r"  `Password` varchar(32) COLLATE utf8mb4_unicode_520_ci NOT NULL"
            r") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;"
        )
        cls.cursor.execute(r"ALTER TABLE `TestEntity` ADD PRIMARY KEY (`Entity_id`)")
        cls.cursor.execute(r"ALTER TABLE `TestEntity` MODIFY `Entity_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;")
        cls.connection.commit()

    class TestEntity(Entity):
        @classmethod
        def _db_id_name(cls):
            return "entity_id"

        @classmethod
        def _db_attr(cls):
            return ("entity_id", "account", "password")

    def test_insert(self):
        c = self.TestEntity()
        c.account = "ACC"
        c.password = "pass"
        c._connection = self.connection
        c.insert()
        self.assertIsNotNone(c.entity_id)
        self.cursor.execute("SELECT * FROM `TestEntity` WHERE `Entity_id` = %s", (c.entity_id,))
        self.assertEqual(len(tuple(self.cursor)), 1)

    def test_from_id(self):
        self.cursor.execute("INSERT INTO `TestEntity` (`Entity_id`, `Account`, `Password`) VALUES (256, 'Acc', 'Pass')")
        entry = self.TestEntity._from_id(self.connection, 256)
        self.assertEqual(entry.entity_id, 256)
        self.assertEqual(entry.account, "Acc")
        self.assertEqual(entry.password, "Pass")

    def test_select(self):
        self.cursor.execute("INSERT INTO `TestEntity` (`Account`, `Password`) VALUES ('sname', 'spass')")
        self.TestEntity._select_equals(self.cursor, account="sname", password="spass")
        entry = self.cursor.fetchone()
        self.assertSequenceEqual(entry[1:], ("sname", "spass"))
        self.TestEntity._select_equals(self.cursor, account="sname")
        entry = self.cursor.fetchone()
        self.assertSequenceEqual(entry[1:], ("sname", "spass"))
        self.TestEntity._select_equals(self.cursor, account="NonExistentAccount")
        entry = self.cursor.fetchone()
        self.assertIsNone(entry)

    def test_delete(self):
        self.cursor.execute("INSERT INTO `TestEntity` (`Account`, `Password`) VALUES ('delete', 'me')")
        self.cursor.execute("SELECT * FROM `TestEntity` WHERE `Account`='delete'")
        select_res = [(acc, pas) for _, acc, pas in self.cursor.fetchall()]
        self.assertSequenceEqual(select_res, [('delete', 'me')])
        self.TestEntity._delete_equals(self.connection, Account = 'delete')
        self.cursor.execute("SELECT * FROM `TestEntity` WHERE `Account`='delete'")
        self.assertSequenceEqual(self.cursor.fetchall(), ())



class AuctionTest(DBTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with open("schema_dump.sql") as schema_file:
            schema = schema_file.read()
        for s in schema.split(';'):
            cls.cursor.execute(s)
        cls.connection.commit()


    def testFoo(self):
        pass
            



if __name__ == "__main__":
    unittest.main()
