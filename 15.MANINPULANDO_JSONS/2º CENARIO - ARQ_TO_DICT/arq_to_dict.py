import json

# O 'with open' cuida de abrir e fechar o arquivo automaticamente
# 'r' significa que estamos abrindo e modo de leitura (read)

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    # Passamos o objeto 'arquivo' para o json.load()
    dados_do_produto = json.load(arquivo)

# Agora, 'dados_do_produto' é um dicionário Python

# Agora, 'dados_do_produto' é um dicionário Python!
print(f"O produto é: {dados_do_produto['produto']}")
print(f"O preço é: R$ {dados_do_produto['preco']}")