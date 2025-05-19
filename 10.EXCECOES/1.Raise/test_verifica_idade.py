import pytest
from verifica_idade import verifica_idade

def test_verifica_idade_com_erro():
    with pytest.raises(ValueError) as excinfo:
        verifica_idade(17)
    assert str(excinfo.value) == "Acesso negado: Menores de idade não podem acessar."

def test_verifica_idade_sem_erro():
    resultado = verifica_idade(18)
    assert resultado == "Acesso permitido: Você é maior de idade."