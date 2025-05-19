Nomeando Funções de Teste

Nome deve dizer claramente o que o teste faz

Convençções 

Test + Componente + Condição

def test_sum_positive_numbers_returns_correct_result():

Documentando Testes

Uso de docstring

def test_sum_with_empty_list_returns_zero():
    """
    Testa se a função sum retorna 0 para uma lista vazia. # Resumo
    #Linha em Branco
    #Linha Detalhada
    """
    assert sum([]) == 0