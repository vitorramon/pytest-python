import json

# String Original
dados_em_texto = '{"nome": "Ana", "idade": 28, "cidade": "Recife"}'
print(dados_em_texto)
print(f"O tipo da variável era: {type(dados_em_texto)}")

# Usamos json.loads para converter a string em um dicionário
dados_em_python = json.loads(dados_em_texto)

# Agora podemos trabalhar com os dados como um dicionário Python
print(f"A cidade é: {dados_em_python['cidade']}")
print(f"O nome é: {dados_em_python['nome']}")

# Vamos verificar o tipo da nova variável
print(f"O tipo da variável agora é: {type(dados_em_python)}")