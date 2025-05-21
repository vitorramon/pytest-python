from app import Produto, Estoque
import pytest

def test_adicionar_verificar_quantidade():
    estoque = Estoque()

    produto1 = Produto("Produto A", 10)
    produto2 = Produto("Produto B", 5)

    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade("Produto A") == 10
    assert estoque.verifica_quantidade("Produto B") == 5

def test_adicionar_produto_existente():
    estoque = Estoque()

    produto1 = Produto("Produto A", 10)
    estoque.adicionar_produto(produto1)

    produto2 = Produto("Produto A", 5)
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade("Produto A") == 15