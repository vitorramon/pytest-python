import json

novo_usuario = {
    'nome': 'Carlos',
    'ativo': True,
    'cursos': ['Python Básico', 'APIs com Flask'],
    'id': None
}

# Abrimos o arquivo para escrita ('w' de write)
with open('usuario.json', 'w', encoding='utf-8') as arquivo:
    # Passamos O QUE salvar (novo_usuario) e ONDE salvar (arquivo)
    # Usando indent=4 para formatar o arquivo
    # ensure_ascii=False para usar acentos
    json.dump(novo_usuario, arquivo, indent=4, ensure_ascii=False)

print("Arquivo 'usuario.json' foi criado com sucesso!")

'''
A Regra de Ouro
Aqui vai a dica mais importante:

Se você usar ensure_ascii=False, é essencial que também especifique encoding='utf-8' na função open().

Pense neles como uma dupla inseparável.

ensure_ascii=False diz ao json: "Pode colocar os acentos aí".

encoding='utf-8' diz ao open(): "Prepare o arquivo para que ele saiba como escrever e ler esses acentos corretamente".

Sem o encoding='utf-8', provavelmente receberia um erro (UnicodeEncodeError) ao tentar salvar o arquivo.
'''
