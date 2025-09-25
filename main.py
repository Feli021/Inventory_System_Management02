from models import Supplier, Product, Order
from db import db
from Inventory_System import InventorySystem
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
system = InventorySystem()

with app.app_context():
    db.create_all()
    # Adding supplier
    supplier = Supplier(name="Fornecedor Teste", contact="teste@fornecedor.com")
    print(system.add_supplier(supplier))
    # Adding product
    product = Product(name="Caneta Azul", price=2.50, stock_quantity=100, type="SchoolSupplies")
    print(system.add_product(product))
    # To list products
    system.list_product()
    # To list suppliers
    system.list_supplier()
    # To update product
    print(system.update_product(id=1, newname="Caneta Preta", newprice=3.00))
    # To update stock
    print(system.update_stock_quantity(id=1, newquantity=50))
    # Place order
    print(system.place_order(customer_name="Jota", product_id=1, amount=10))
    # To deleted product
    print(system.delete_product(id=1))
    # To deleted supplier
    print(system.delete_supplier(id=1))
