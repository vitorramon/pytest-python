import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15, "A soma da lista não está correta"
    assert sum([]) == 0, "A soma de uma lista vazia deve ser 0"
    assert sum([1, 2, 3]) == 6, "A soma da lista [1, 2, 3] deve ser 6"

def test_length(sample_list):
    assert len(sample_list) == 5, "O comprimento da lista não está correto"
    assert len([]) == 0, "A lista vazia não tem comprimento zero"
    assert len([1, 2, 3, 4, 5]) == 5, "A lista de cinco elementos não tem comprimento cinco"