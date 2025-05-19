import pytest
from exemplo_simples import soma

@pytest.mark.parametrize("a, b, esperado", [
    (1,2,3), (2,3,5), (3,4,7)
    ])
def test_soma(a, b, esperado):
    assert soma(a, b) == esperado, f"A soma de {a} e {b} deve ser {esperado}"
    