import pytest
import time

def somar(a, b):
    """
    Função que soma dois números.
    """
    return a + b

def multiplicar(a, b):
    """
    Função que multiplica dois números.
    """
    return a * b

def subtrair(a, b):
    """
    Função que subtrai dois números.
    """
    return a - b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert somar(2, 3) == 5

@pytest.mark.rapido 
def test_soma_rapida():
    assert somar(2, 3) == 5

@pytest.mark.lento
def test_multiplicacao_lenta():
    time.sleep(2)
    assert multiplicar(2, 3) == 6

@pytest.mark.rapido
def test_multiplicacao_rapida():
    assert multiplicar(2, 3) == 6

def test_subtracao():
    assert subtrair(5, 3) == 2

