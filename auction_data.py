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
    def __init__(self):
        raise NotImplementedError

    def customer_register(self, info : Customer) -> int:
        raise NotImplementedError

    def seller_register(self, info : Seller) -> int:
        raise NotImplementedError

    def customer_login(self, account: str, password: str) -> Optional[int]:
        raise NotImplementedError

    def seller_login(self, account: str, password: str) -> Optional[int]:
        raise NotImplementedError

    def customer_update_info(self, info: Customer) -> None:
        raise NotImplementedError

    def seller_update_info(self, info: Seller) -> None:
        raise NotImplementedError

    def search_merchandise(self, filter_condition):
        raise NotImplementedError

    def get_merchandise_data(self, merchandise_id: int) -> Merchandise:
        raise NotImplementedError

    def get_purchase_history(self, customer_id : int) -> List[int]:
        raise NotImplementedError

    def cart_show(self, c : Customer) -> List[Tuple[Merchandise, int]]:
        raise NotImplementedError

    def cart_add(self, c : Customer, m : Merchandise) -> bool:
        raise NotImplementedError

    def cart_remove(self, c : Customer, m : Merchandise) -> bool:
        raise NotImplementedError

    def new_order(self, c : Customer) -> Order:
        """ Put everything in the cart into a new order """
        raise NotImplementedError

    def seller_history(self, s : Seller):
        raise NotImplementedError

    def new_merchandise(self, s : Seller, m : Merchandise) -> int:
        raise NotImplementedError

    def set_merchandise_data(self, m : Merchandise) -> None:
        raise NotImplementedError

    def delete_merchandise(self, m : Merchandise) -> None:
        raise NotImplementedError

    def give_review(self, order : Order, s : Seller, r : Review) -> bool:
        raise NotImplementedError

    def show_review(self, s : Seller) -> List[Review]:
        raise NotImplementedError

    def add_to_blacklist(self, c : Customer, s : Seller) -> bool:
        raise NotImplementedError

    def show_blacklist(self, c : Customer) -> List[int]:
        raise NotImplementedError

    def remove_from_blacklist(self, c : Customer, s : Seller) -> bool:
        raise NotImplementedError

    def list_faq(self, m : Merchandise) -> List[int]:
        raise NotImplementedError

    def get_faq(self, m : Merchandise, faq_id : int) -> Faq:
        raise NotImplementedError

    def ask(self, c : Customer, m : Merchandise, question : str) -> Faq:
        raise NotImplementedError

    def answer(self, faq : Faq, answer : str) -> None:
        raise NotImplementedError
