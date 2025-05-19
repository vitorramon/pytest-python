def somar(a, b):
    return a + b

def comprimento(lista):
    return len(lista)

def test_somar_e_comprimento():
    assert somar(2, 3) == 5
    assert comprimento([1, 2, 3]) == 3
    assert comprimento([]) == 0
    assert comprimento([1, 2, 3, 4, 5]) == 5
    assert somar(0, 0) == 0

