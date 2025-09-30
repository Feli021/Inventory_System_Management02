from db import db
from models import Supplier, Product, Order, OrderItem
from datetime import datetime
class InventorySystem:
    def __init__(self):
        pass

    # Create - Add product and suppliers
    def add_product(self, product):
        existing = Product.query.filter_by(name=product.name).first()
        if existing:
            existing.stock_quantity = existing.stock_quantity + product.stock_quantity
        else:
            db.session.add(product)
        db.session.commit()   # The Commit needs to leave out the conditional because both cases require confirmation of the change
        
    
    def add_supplier(self, supplier):
        existing = Supplier.query.filter_by(name=supplier.name).first()
        if not existing:
            db.session.add(supplier)
        db.session.commit()
    
    # READ - To list products and suppliers
    def list_product(self):
       products_ = Product.query.all()  # Return a list with the products
       if not products_:
            print("No registered product")
            return
       for product in products_:
            print(f"Name: {product.name}, Price: {product.price}, Stock_quantity: {product.stock_quantity}, Supplier: {product.supplier.name}")
   
    def list_supplier(self):
        suppliers_ = Supplier.query.all()
        if not suppliers_:
             print("no registered supplier")
             return     
        for supplier in suppliers_:
            print(f"Name: {supplier.name}, Contact: {supplier.contact}, Id: {supplier.id}")
   
    # Update - To update products, suppliers and stock
    def update_product(self, id, newname, newprice): # To Change the atributes of the products
        product_ = Product.query.get(id) 
        if product_:
                product_.name = newname
                product_.price = newprice
                db.session.commit()
                return "Product updated sucessfully"
        return "Product not found"
    
    def update_supplier(self, id, newname, newcontact):
        supplier_= Supplier.query.get(id)
        if supplier_:
                supplier_.name == newname
                supplier_.contact == newcontact
                db.session.commit()
                return "Supplier updated successfully"
        return "Supplier not found"
    def update_stock_quantity(self, id, newquantity):
        product_ = Product.query.get(id) 
        if product_: 
                product_.stock_quantity = product_.stock_quantity + newquantity
                db.session.commit()
                return "Stock quantity updated succesffuly"
        return "Product not found"
    # DELETE - To delete products and suppliers
    def delete_product(self, id):
        product = Product.query.get(id)
        if product:
                db.session.delete(product)
                db.session.commit()
                return "Product deleted successfully"
        return "Product not found"
    def delete_supplier(self, id):
        supplier= Supplier.query.get(id)
        if supplier:
            db.session.delete(supplier)
            db.session.commit()
            return "Supplier deleted successfully"
        return "Supplier not found"
    # Order processing - Where you create your order
    def place_order(self, customer_name, product_id, amount):
        try:
            # 1. To search the product

                product = Product.query.get(product_id)  
                if not product:
                    return "Product not found"   
            # 2. To verify sufficient stock
                if product.stock_quantity  < amount:
                        return "Insufficient stock for the order"
            # 3. To create the order
                new_order = Order(customer_name = customer_name, created_at = datetime.now())
                db.session.add(new_order)
                db.session.flush() 
            # 4. To create the item of order
                order_item = OrderItem(order_id = new_order.id, product_id = product_id, order_quantity=amount )
                db.session.add(order_item)
            # 5. To update the product stock
                product.stock_quantity = product.stock_quantity - amount
            # 6. To confirm everything in bank
                db.session.commit()
                return f"Pedido realizado com sucesso: {customer_name}: {amount} x {product.name}"
        except Exception as e:
            db.session.rollback()
            return f"Erro ao processar pedido: {str(e)}"


                    
                
            


    
                





    
    
