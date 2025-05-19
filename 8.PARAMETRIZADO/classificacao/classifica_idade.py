def classifica_idade(idade):
    """
    Classifica a idade em diferentes categorias.

    Args:
        idade (int): A idade a ser classificada.

    Returns:
        str: A categoria da idade.
    """
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"