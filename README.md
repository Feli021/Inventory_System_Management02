### Inventory Management System com SQLite
## Descrição do Projeto
Este projeto consiste em um sistema de gerenciamento de inventário simples, desenvolvido em Python, com uso de banco de dados.
O projeto contém todas as operações de um CRUD
Ele permite adicionar, listar, atualizar, e deletar produtos e fornecedores
O sistema utiliza programação orientada a objetos (POO), incluindo classes para Produtos, Fornecedores e Pedidos, além de herança para diferentes tipos de produtos (Eletrônicos, Roupas, Material Escolar).
O banco de dados utilizado foi o SQLite que é excelente para projetos pequenos e médios.

## Funcionalidades
Adicionar produtos ao inventário
Adicionar fornecedores
Listar produtos
Listar fornecedores
Atualizar produtos
Atualizar fornecedores
Atualizar estoque
Deletar produtos
Deletar fornecedores
Processamento de pedidos com atualização do estoque

## Estrutura do Projeto
db.py - Arquivo com a criação do banco de daods
Inventory_System.py - Arquivo o qual gerenciamos todo nosso sistema. Inclui todas as funções para mexer no sistema
models.py – Contém todas as classes do sistema mapeadas no banco de dados
main.py – Script principal para rodar o sistema e testar funcionalidades.

## Requisitos:
Python 3.8 ou superior
(Opcional) Ambiente virtual para isolamento do projeto

## Como Rodar
Clone este repositório:
git clone <https://github.com/Feli021/Inventory_System_Management02.git>
## Entra dentro da pasta do projeto
cd Inventory_System_Management02
## (Opcional) Crie e ative um ambiente virtual:
 python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

## Execute o sistema: 
python main.py

## Exemplo de Saída
Após rodar main.py, você verá algo como:
Name: Caneta Azul, Price: 2.5, Stock_quantity: 100, Supplier: Fornecedor Teste  

Name: Fornecedor Teste, Contact: teste@fornecedor.com, Id: 1 

Product updated sucessfully  

Stock quantity updated succesffuly  

Name: Caneta Preta, Price: 3.0, Stock_quantity: 150, Supplier: Fornecedor Teste  

Pedido realizado com sucesso: Jota: 10 x Caneta Preta  

Name: Caneta Preta, Price: 3.0, Stock_quantity: 140, Supplier: Fornecedor Teste  

Product deleted successfully  

Supplier deleted successfully 

No registered product  

no registered supplier

## Tecnologias
Python 3 Orientação a Objetos
SQLite

## Autor
Felipe Ferreira Drummond
Email: felidrummond84@gmail.com LinkedIn: https://www.linkedin.com/in/felipe-drummond-8223a92bb/