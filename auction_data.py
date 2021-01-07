import mysql.connector
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


class Cart(Entity):
    raise NotImplementedError


class Auction:
    raise NotImplementedError

