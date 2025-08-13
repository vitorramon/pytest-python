Para LER (JSON -> Python):

De uma String: dados_python = json.loads(string_json)

De um Arquivo: with open(...) as f: dados_python = json.load(f)

Para ESCREVER (Python -> JSON):

Para uma String: string_json = json.dumps(dados_python)

Para um Arquivo: with open(...) as f: json.dump(dados_python, f, indent=4)