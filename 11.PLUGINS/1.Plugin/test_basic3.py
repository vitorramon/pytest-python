from funcoes import *

def test_email_vaalido():
    assert email_valido("exemplo@dominio.com") is True
    assert email_valido("exemplo@dominio") is False
    assert email_valido("exemplo.dominio.com") is False
    assert email_valido("exemplo.com") is False

def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(4, 0) is None