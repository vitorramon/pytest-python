def verifica_idade(idade):
    if idade < 18:
        raise ValueError("Acesso negado: Menores de idade não podem acessar.")
    return "Acesso permitido: Você é maior de idade."