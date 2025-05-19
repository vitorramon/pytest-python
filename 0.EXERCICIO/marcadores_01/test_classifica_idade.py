import pytest
from classifica_idade import classifica_idade

@pytest.mark.crianca
@pytest.mark.parametrize("idade, esperado", [
    (0, 'criança'),
    (5, 'criança'),
    (12, 'criança')])
def test_idade_crianca(idade, esperado):
    """
    Testa a classificação de idade para crianças.
    """
    assert classifica_idade(idade) == esperado


@pytest.mark.adolescente
@pytest.mark.parametrize("idade, esperado", [
    (13, 'adolescente'),
    (15, 'adolescente'),
    (19, 'adolescente')])
def test_idade_adolescente(idade, esperado):
    """
    Testa a classificação de idade para adolescentes.
    """
    assert classifica_idade(idade) == esperado

@pytest.mark.adulto
@pytest.mark.parametrize("idade, esperado", [
    (20, 'adulto'),
    (30, 'adulto'),
    (59, 'adulto')])
def test_idade_adulto(idade, esperado):
    """
    Testa a classificação de idade para adultos.
    """
    assert classifica_idade(idade) == esperado

@pytest.mark.idoso
@pytest.mark.parametrize("idade, esperado", [
    (60, 'idoso'),
    (70, 'idoso'),
    (80, 'idoso')])
def test_idade_idoso(idade, esperado):
    """
    Testa a classificação de idade para idosos.
    """
    assert classifica_idade(idade) == esperado