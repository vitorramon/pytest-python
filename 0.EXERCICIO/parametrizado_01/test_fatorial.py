import pytest
from fatorial import fatorial

@pytest.mark.parametrize("n, esperado", [
    (-5, "Número negativo não é permitido"),
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
])
def test_fatorial(n, esperado):
    """
    Testa a função fatorial com diferentes valores de entrada.
    """
    if n < 0:
        with pytest.raises(ValueError) as excinfo:
            fatorial(n)
        assert str(excinfo.value) == esperado
    else:
        assert fatorial(n) == esperado