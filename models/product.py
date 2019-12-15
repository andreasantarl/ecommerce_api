import datetime
from sqlalchemy import Table, Integer, String, Column, DateTime, Numeric, Text, Boolean
from .base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric, nullable=False)
    in_stock = Column(Boolean, nullable=False)
    quantity = Column(Numeric, nullable=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, description, price, in_stock=False, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.in_stock = in_stock
        self.quantity = quantity