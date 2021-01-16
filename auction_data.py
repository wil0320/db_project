import mysql.connector
import typing
from typing import Tuple, Optional, List, Dict
import abc
import itertools

import config

# The base class that defines all basic operations of the class
class Entity(abc.ABC):
    @abc.abstractmethod
    def update(self):
        """
        Save every attribute into the db.
        """
        raise NotImplementedError

class Merchandise(Entity):
    def __init__(self):
        self.merchandise_id = None
        self.name = ""
        self.description = ""
        self.price = 0
        self.number_in_stock = 0
        self.number_sold = 0
        self.category = None
        self.seller = None

class Seller(Entity):
    def __init__(self):
        self.seller_id = None
        self.account = ""
        self.password = ""
        self.email = ""
        self.name = ""
        self.register_date = None
        self.register_time = None


class Customer(Entity):
    def __init__(self):
        self.customer_id = None
        self.name = ""
        self.account = ""
        self.password = ""
        self.email = ""
        self.register_date = None
        self.register_time = None
        self.bill_info = None


class OrderItem(Entity):
    def __init__(self):
        self.order_id = None
        self.merchandise_id = None
        self.trade_price = None
        self.number = None
        self.status = None


class Category(Entity):
    def __init__(self):
        self.category_id = None
        self.name = ""
        self.super_category = None


class Order(Entity):
    def __init__(self):
        self.order_id = None
        self.order_date = None
        self.order_time = None
        self.customer_id = None
        self.items = None     # A list of OrderItem
 

class Cart(Entity):
    def __init__(self):
        self.customer_id = None
        self.merchandise : Dict[Merchandise, int] = None

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
    def __init__(self):
        self.faq_id = None
        self.merchandise = None
        self.customer = None
        self.ask_date = None
        self.ask_time = None
        self.question = ""
        self.answer : Optional[str] = None


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
        c._cursor = c._connect.cursor()
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
