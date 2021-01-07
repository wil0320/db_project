import mysql.connector
import typing
from typing import Tuple, Optional, List, Dict

# The base class that defines all basic operations of the class
class Entity:
    raise NotImplementedError

class Merchandise(Entity):
    def __init__(self):
        self.id = None
        self.name = ""
        self.description = ""
        self.price = 0
        self.number_in_stock = 0
        self.number_sold = 0
        self.category = None
        self.seller = None
    raise NotImplementedError

class Seller(Entity):
    def __init__(self):
        self.id = None
        self.account = ""
        self.password = ""
        self.email = ""
        self.name = ""
        self.register_date = None
        self.register_time = None

    raise NotImplementedError

class Customer(Entity):
    def __init__(self):
        self.name = ""
        self.account = ""
        self.password = ""
        self.email = ""
        self.register_date = None
        self.register_time = None
        self.bill_info = None

    raise NotImplementedError

class OrderItem(Entity):
    def __init__(self):
        self.order_id = None
        self.merchandise_id = None
        self.trade_price = None
        self.number = None
        self.order_date = None
        self.order_time = None
        self.status = None

    raise NotImplementedError

class Category(Entity):
    def __init__(self):
        self.id = None
        self.name = ""
        self.super_category = None
    raise NotImplementedError


class Order(Entity):
    def __init__(self):
        self.order_id = None
        self.order_date = None
        self.order_time = None
        self.customer = None
        self.items = None     # A list of OrderItem
 
    raise NotImplementedError

class Cart(Entity):
    def __init__(self):
        self.customer = None
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

    raise NotImplementedError

class Review(Entity):
    # I have no idea how to implement this
    raise NotImplementedError

class Faq(Entity):
    def __init__(self):
        self.id = None
        self.merchandise = None
        self.customer = None
        self.ask_date = None
        self.ask_time = None
        self.question = ""
        self.answer : Optional[str] = None
    raise NotImplementedError


class Auction:
    @staticmethod
    def from_db_login_info(account : str, password: str, host : str, db_name: str) -> "Auction":
        raise NotImplementedError

    def __init__(self, connection):
        # connection is a type of mysql connection. (See Mysql connector document. )
        raise NotImplementedError

    def customer_register(self, c : Customer):
        """ Create a new Customer in the db, and fills the id in c. """
        raise NotImplementedError

    def seller_register(self, s : Seller):
        """ Create a new Seller in the db, and fills the id in c. """
        raise NotImplementedError

    def customer_login(self, account: str, password: str) -> Optional[Customer]:
        """ Returns a Customer if login succeeds, else return None. """
        raise NotImplementedError

    def seller_login(self, account: str, password: str) -> Optional[Seller]:
        """ Returns a Seller if login succeeds, else return None. """
        raise NotImplementedError

    def customer_update_info(self, info: Customer) -> None:
        """ Write the new information back to the db """
        raise NotImplementedError

    def seller_update_info(self, info: Seller) -> None:
        """ Write the new information back to the db """
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
