Explicação sobre db.relationship arquivo models.py:

----------------------------------------------------------------------------
Classe Order:
    item = db.relationship("OrderItem", back_populates="Order")
Classe OrderItem:  
    order = db.relationship(Order, back_populates="OrderItem", cascade="all, delete-orphan")
    product = db.relationship("Product")

- Order tem vários OrderItem → items = db.relationship(...)
- OrderItem tem um Order → order = db.relationship(...)
- OrderItem tem um Product → product = db.relationship(...)
---------------------------------------------------------------------------------
Classe Supplier:
    products = db.relationship("Product", back_populates= "supplier", cascade="all,delete")
Classe Product:
    supplier = db.relationship("Supplier", back_populates="products")


- Supplier tem vários Product → products = db.relationship(...)
- Product tem um Supplier → supplier = db.relationship(...)

--------------------------------------------------------------------------------
Explicando a linha: created_at = db.Column(db.DateTime, server_default=db.func.now()) na classe Order 


db.Column(db.DateTime, ...) → define que a coluna created_at será do tipo DateTime no banco de dados. Ou seja, vai armazenar data e hora.

server_default= → significa que, se você não passar nenhum valor ao criar um registro, o banco de dados automaticamente preencherá essa coluna com um valor padrão.

db.func.now() → é um atalho do SQLAlchemy para chamar a função NOW() do banco de dados (a função nativa que pega a hora atual do servidor no momento da inserção).

🔎 Em outras palavras:
Sempre que você inserir uma nova linha na tabela (por exemplo, um novo pedido ou item), o campo created_at vai ser preenchido automaticamente com a data e hora atuais do banco
---------------------------------------------------------------------------------------------

def place_order(self, customer_name, product_id, quantity):
    # 1. Buscar o produto
    product = Product.query.get(product_id)
    if not product:
        return "Produto não encontrado"

    # 2. Verificar estoque suficiente
    if product.stock_quantity < quantity:
        return "Estoque insuficiente para o pedido"

### # 3. Criar o pedido (Order)
    new_order = Order(
        customer_name=customer_name,
        created_at=datetime.now()
    )
    db.session.add(new_order)
    db.session.flush() 
    

### Você está dizendo:
- customer_name à esquerda: é o nome do atributo da classe Order
- customer_name à direita: é o parâmetro recebido pela função
Mesmo que os nomes sejam iguais, o Python precisa dessa atribuição explícita para saber que você está passando o valor do parâmetro para o campo do objeto.


 db.session.flush() vs db.session.commit()
|  |  | 
| flush() |  | 
| commit() |  | 



### 🧠 O que flush() faz exatamente?
- Ele gera o ID do objeto recém-adicionado (new_order) e o deixa disponível na sessão.
- Isso é útil quando você precisa usar esse ID antes de dar o commit — como no seu caso, para criar o OrderItem.

Ex:
db.session.add(new_order)
db.session.flush()
print(new_order.id)  # Agora o ID está disponível!


###  # 4 . Criar o item do pedido
         order_item = OrderItem(order_id = new_order.id, product_id = product_id, order_quantity=amount )
product_id = product_id -> O campo product_id (esquerda) da tabela OrderItem recebe product_id (direita) que é parâmetro da função

----------------------------------------------------------------------------------------------------------
# def place_order(self, customer_name, product_id, amount):
     # 1. Buscar o produto
        product = Product.query.get(product_id)  
Aqui, product_id é um inteiro
product é o objeto completo recuperado do banco de dados.
Quando faço - Product.query.get(product_id) - estou procurando no meu banco de dados um objeto com essa id.
Quando ele acha ( se achar ) ele retorna todo o objeto daquele id

então em      # 6. Confirmar tudo no banco
        db.session.commit()
        return f"Pedido realizado com sucesso: {customer_name}: {amount} x {product.name}"
eu não poderia usar product_id.name em -  {customer_name}: {amount} x {product.name}" - pois product_id é um inteiro e não o objeto completo