import pytest
from classifica_idade import classifica_idade

@pytest.mark.parametrize(
    "idade, categoria_esperada", [
        (5, "Criança"),
        (15, "Adolescente"),
        (30, "Adulto"),
        (70, "Idoso"),
        (-1, "Idade inválida"),
        (18, "Adulto"),  # Limite entre Adolescente e Adulto
        (59, "Adulto"),  # Limite entre Adulto e Idoso
        (60, "Idoso")    # Limite entre Adulto e Idoso
    ]
)
def test_classifica_idade(idade, categoria_esperada):
    """
    Testa a função classifica_idade com diferentes idades e categorias esperadas.
    
    Args:
        idade (int): A idade a ser testada.
        categoria_esperada (str): A categoria esperada para a idade.
    """
    assert classifica_idade(idade) == categoria_esperada, f"A classificação para a idade {idade} deve ser {categoria_esperada}"