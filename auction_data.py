import mysql.connector
import typing
from typing import Tuple, Optional, List, Dict
import abc
import itertools
import unittest
import datetime

import config

# The base class that defines all basic operations of the class
class Entity(abc.ABC):
    @property
    def _db_id_name(self) -> Optional[str]:
        # TODO: This should be a class method
        """
        The name of id.
        The entity updates its id after insertion.
        """
        return None

    @property
    @abc.abstractmethod
    def _db_attr(self) -> Tuple[str]:
        """All attributes for this enitity."""
        # TODO: Add typing
        # TODO: This should be a class method
        pass

    def update(self):
        """
        Save every attribute into the db.
        """
        raise NotImplementedError

    def insert(self):
        table_name = type(self).__name__
        attr_name = ", ".join(self._db_attr)
        attr_fstr = ", ".join("%s" for _ in self._db_attr)
        # getattr(self, "s", None) is equivalent to self.s if self.s is defined, else it's equivalent to None
        attr_val = [ getattr(self, name, None) for name in self._db_attr ]
        cmd = f"INSERT INTO {table_name} ({attr_name}) VALUES ({attr_fstr})"
        self._cursor.execute(cmd, attr_val)
        if self._db_id_name:
            setattr(self, self._db_id_name, self._cursor.lastrowid)
        self._connection.commit()

class Merchandise(Entity):
    @property
    def _db_id(self):
        return "merchandise_id"

    @property
    def _db_attr(self):
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
    @property
    def _db_id(self):
        return "seller_id"

    @property
    def _db_attr(self):
        return (
            "seller_id",
            "account",
            "password",
            "name",
            "register_time",
            "email",
        )


class Customer(Entity):
    @property
    def _db_id(self):
        return "customer_id"

    @property
    def _db_attr(self):
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
    @property
    def _db_attr(self):
        return (
            "order_id",
            "merchandise_id",
            "trade_price",
            "number",
            "status",
        )


class Category(Entity):
    @property
    def _db_id(self):
        return "category_id"

    @property
    def _db_attr(self):
        return (
            "category_id",
            "name",
            "parent_category",
        )


class Order(Entity):
    @property
    def _db_id(self):
        return "order_id"

    @property
    def _db_attr(self):
        return (
            "order_id",
            "customer_id",
            "order_time",
        )

class Cart(Entity):
    @property
    def _db_attr(self):
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
    @property
    def _db_id(self):
        return "faq_id"

    @property
    def _db_attr(self):
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

    def customer_register(self, c : Customer):
        """ Create a new Customer in the db, and fills the id in c. """
        c._connection = self.connection
        c._cursor = c._connection.cursor()
        c.register_time = datetime.datetime.now()
        c.insert()

    def seller_register(self, s : Seller):
        """ Create a new Seller in the db, and fills the id in c. """
        raise NotImplementedError

    def customer_login(self, account: str, password: str) -> Optional[Customer]:
        """ Returns a Customer if login succeeds, else return None. """
        raise NotImplementedError

    def seller_login(self, account: str, password: str) -> Optional[Seller]:
        """ Returns a Seller if login succeeds, else return None. """
        raise NotImplementedError

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

class DBTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login_info = config.LOGIN_INFO
        del login_info["database"]
        cls.connection = mysql.connector.connect(**login_info)
        cls.cursor = cls.connection.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()


class EntityTest(DBTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cursor.execute("CREATE DATABASE db_test DEFAULT CHARACTER SET 'utf8'")
        cls.cursor.execute("USE db_test")
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

    @classmethod
    def tearDownClass(cls):
        try:
            cls.cursor.fetchall()
        except mysql.connector.errors.InterfaceError:
            pass
        cls.cursor.execute("DROP DATABASE db_test")
        cls.connection.commit()
        super().tearDownClass()

    class TestEntity(Entity):
        @property
        def _db_id_name(self):
            return "entity_id"

        @property
        def _db_attr(self):
            return ("entity_id", "account", "password")

    def test_insert(self):
        c = self.TestEntity()
        c.account = "ACC"
        c.password = "pass"
        c._cursor = self.cursor
        c._connection = self.connection
        c.insert()
        self.assertIsNotNone(c.entity_id)
        self.cursor.execute("SELECT * FROM `TestEntity` WHERE `Entity_id` = %s", (c.entity_id,))
        self.assertEqual(len(tuple(self.cursor)), 1)

if __name__ == "__main__":
    unittest.main()
