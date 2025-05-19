def classifica_idade(idade):
    if idade < 13:
        return 'criança'
    elif idade < 20:
        return 'adolescente'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'