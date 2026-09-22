import json
import os
import streamlit as st

ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_RESULTADOS = "resultados.json"


def carregar_dados(arquivo):

    if not os.path.exists(arquivo):
        return []

    with open(
        arquivo,
        "r",
        encoding="utf-8"
    ) as arquivo_json:

        return json.load(arquivo_json)


def salvar_dados(arquivo, dados):

    with open(
        arquivo,
        "w",
        encoding="utf-8"
    ) as arquivo_json:

        json.dump(
            dados,
            arquivo_json,
            ensure_ascii=False,
            indent=4
        )


# CADASTRO

def cadastrar_usuario(nome, senha):

    usuarios = carregar_dados(
        ARQUIVO_USUARIOS
    )

    nome = nome.strip()

    for usuario in usuarios:

        if usuario["nome"].lower() == nome.lower():

            return "Esse usuário já existe."

    novo_usuario = {
        "nome": nome,
        "senha": senha
    }

    usuarios.append(novo_usuario)

    salvar_dados(
        ARQUIVO_USUARIOS,
        usuarios
    )

    return "Usuário cadastrado com sucesso!"


# LOGIN

def fazer_login(nome, senha):

    usuarios = carregar_dados(
        ARQUIVO_USUARIOS
    )

    nome = nome.strip()
    senha = senha.strip()

    for usuario in usuarios:

        if (
            usuario["nome"].lower() == nome.lower()
            and usuario["senha"] == senha
        ):

            return usuario["nome"]

    print("Usuário ou senha incorretos.")

    return None


# SALVAR RESULTADO

def salvar_resultado(usuario, pontuacao):

    resultados = carregar_dados(
        ARQUIVO_RESULTADOS
    )

    novo_resultado = {
        "usuario": usuario,
        "pontuacao": pontuacao
    }

    resultados.append(novo_resultado)

    salvar_dados(
        ARQUIVO_RESULTADOS,
        resultados
    )


# RANKING

def mostrar_ranking():
    resultados = carregar_dados(ARQUIVO_RESULTADOS)

    if not resultados:
        print("\nAinda não existem resultados.")
        st.info("Ainda não existem resultados.")
        return

    resultados.sort(
        key=lambda resultado: resultado["pontuacao"],
        reverse=True
    )

    print("\n===== RANKING =====")
    
    dados_frontend = []

    for posicao, resultado in enumerate(resultados[:10], start=1):
        # 1. Print no terminal (backend)
        print(f"{posicao}º - {resultado['usuario']} - {resultado['pontuacao']}/8")
        
        # 2. Dados estruturados para a tabela
        dados_frontend.append({
            "Posição": f"{posicao}º",
            "Usuário": resultado["usuario"],
            "Pontuação": f"{resultado['pontuacao']}/8"
        })

    # 3. Renderiza a tabela na tela do Streamlit (frontend)
    st.table(dados_frontend)