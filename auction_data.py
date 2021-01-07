import mysql.connector
# The base class that defines all basic operations of the class
class Entity(metaclass=EntityMeta):
    raise NotImplementedError

class Customer(Entity):
    raise NotImplementedError

class Cart(Entity):
    raise NotImplementedError


class Auction:
    raise NotImplementedError

