import json

novo_usuario = {
    'nome': 'Carlos',
    'ativo': True,
    'cursos': ['Python Básico', 'APIs com Flask'],
    'id': None
}

# Usamos dumps para criar a string
string_json = json.dumps(novo_usuario)

print("--- Variável Python (Dicionário) ---")
print(novo_usuario)
print(type(novo_usuario))

print("\n--- Variável JSON (String) ---")
print(string_json)
print(type(string_json))

# Note as pequenas traduções que o json fez: True virou true e None virou null, que são os tipos de dados equivalentes em JSON.