import pytest
from fixtures_01 import soma_dobro

@pytest.fixture
def lista_numeros():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def lista_vazia():
    return []

def test_soma_dobro(lista_numeros):
    resultado = soma_dobro(lista_numeros)
    assert resultado == 30, f"Esperado 30, mas obteve {resultado}"

def test_soma_dobro_lista_vazia(lista_vazia):
    resultado = soma_dobro(lista_vazia)
    assert resultado == 0, f"Esperado 0, mas obteve {resultado}"