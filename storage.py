import json

arquivo_usuarios = "usuarios.json"
arquivo_resultados = "resultados.json"

def carregar_dados(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def salvar_usuario(nome):
    usuarios = carregar_dados(arquivo_usuarios)

    usuarios.append({"nome": nome})

    salvar_dados(arquivo_usuarios, usuarios)

    def carregar_usuarios():
        return carregar_dados(arquivo_usuarios)

def salvar_resultado(nome, pontuacao, total):
    resultados = carregar_dados(arquivo_resultados)

    resultados.append({"nome": nome, "pontuacao": pontuacao, "total": total})

    salvar_dados(arquivo_resultados, resultados)

    def carregar_resultados():
        return carregar_dados(arquivo_resultados)