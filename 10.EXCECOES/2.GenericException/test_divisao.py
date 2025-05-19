import pytest
from divisao import dividir

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_dividir_por_zero_2():
    with pytest.raises(ZeroDivisionError) as excinfo:
        dividir(10, 0)
    assert str(excinfo.value) == "Divisão por zero não é permitida."

