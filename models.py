from db import db
from sqlalchemy import func


# Criando as classes e mapeando elas no banco de dados

class Supplier(db.Model): # db.Model diz ao SQLAlchemy que essa classe deve ser mapeada para uma tabela no banco.
    __tablename__ = "suppliers"

    # Criando as colunas
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    contact = db.Column(db.String(100))
    # Relacionamento com o produto
    products = db.relationship("Product", back_populates= "supplier", cascade="all,delete")

    def __repr__(self):
        return f"<Supplier {self.name}>"
    


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column( db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    type = db.Column(db.String(50)) # Eletronic, Clothes, SchoolSupplies

    # Campos específicos ( aceitam valor vazio):
    warranty = db.Column(db.Integer, nullable=True) # Eletronic
    size = db.Column(db.String(10),nullable=True) # Clothes
    color = db.Column(db.String(20), nullable=True)# Clothes

    # Associando um produto com seu supplier
    #supplier_id só vai aceitar valores que existirem na coluna 'id' da tabela 'suppliers'(Foreign Key)
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=True)
    # Relacionamento com o supplier
    supplier = db.relationship("Supplier", back_populates="products")

    def __repr__(self):
        return f"<Product {self.name} ({self.type})>"


    
    """  Na classe Product, o atributo 'supplier' está relacionado
         à classe Supplier  
         Product.supplier -> vou acessar o fornecedor do produto

        Na classe Supplier, o atributo 'products' está relacionado
        a classe Product
        Supplier.products -> vou acessar a lista de produtos do fornecedor
           """

""" É interessante separar a classe de pedidos (Order) em 2: uma cuidando das informações
do pedido, como quem comprou, quando, status, etc; e outra parte com os itens individuais do pedido (produto + quantidade) (OrderItem) 
"""
class Order(db.Model):
    __tablename__="orders"

    id = db.Column(db.Integer,primary_key=True)
    customer_name= db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default= func.now())


    items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order {self.id} - {self.customer_name}>"


class OrderItem(db.Model):
    __tablename__="orders_item"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)

    order = db.relationship("Order", back_populates="items")
    product = db.relationship("Product")
