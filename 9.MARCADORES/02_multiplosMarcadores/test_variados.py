import pytest
import time

@pytest.mark.rapido
def test_soma_rapida():
    assert 2 + 3 == 5

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert 2 + 3 == 5

@pytest.mark.rapido
@pytest.mark.lento
def test_soma_mista():
    time.sleep(1)
    assert 2 + 3 == 5