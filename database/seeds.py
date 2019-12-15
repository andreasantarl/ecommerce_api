from models.base import Base, Session, db
from models import product


def seed_database():
    session = Session()
    Base.metadata.create_all(db)
    product_1 = product.Product(name="Product 1", description="This is a first description", price=3.21, in_stock=True,
                                quantity=15)
    product_2 = product.Product(name="Product 2", description="This is a second description", price=12.32, in_stock=False,
                                quantity=0)
    product_3 = product.Product(name="Product 3", description="This is a third description", price=291.43, in_stock=True,
                                quantity=2)
    product_4 = product.Product(name="Product 4", description="This is a fourth description", price=0.32, in_stock=True,
                                quantity=283)
    product_5 = product.Product(name="Product 5", description="This is a fifth description", price=43.54, in_stock=True,
                                quantity=15)
    session.bulk_save_objects([product_1, product_2, product_3, product_4, product_5])
    session.commit()
    session.close()