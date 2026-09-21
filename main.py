import streamlit as st

from storage import (
    cadastrar_usuario,
    fazer_login,
    salvar_resultado,
    mostrar_ranking,
)

from quiz import iniciar_rodada


st.set_page_config(
    page_title="Quiz",
    page_icon="🎯"
)


# ==============================
# CONFIGURAÇÃO INICIAL
# ==============================

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None

if "quiz_iniciado" not in st.session_state:
    st.session_state.quiz_iniciado = False

if "resultado_salvo" not in st.session_state:
    st.session_state.resultado_salvo = False


# ==============================
# MENU PRINCIPAL
# ==============================

def menu_principal():

    st.title("🎯 QUIZ")

    opcao = st.radio(
        "Escolha uma opção:",
        ["Cadastrar", "Login", "Sair"]
    )

    if opcao == "Cadastrar":

        st.subheader("📝 Cadastro")

        nome = st.text_input("Digite seu nome:")
        senha = st.text_input(
            "Digite sua senha:",
            type="password"
        )

        if st.button("Cadastrar"):

            if nome and senha:

                mensagem = cadastrar_usuario(
                    nome.strip(),
                    senha.strip()
                )

                st.success(mensagem)

            else:

                st.warning(
                    "Preencha todos os campos."
                )

    elif opcao == "Login":

        st.subheader("🔐 Login")

        nome = st.text_input("Digite seu nome:")
        senha = st.text_input(
            "Digite sua senha:",
            type="password"
        )

        if st.button("Entrar"):

            if nome and senha:

                usuario = fazer_login(
                    nome.strip(),
                    senha.strip()
                )

                if usuario:

                    st.session_state.usuario_logado = usuario

                    st.rerun()

                else:

                    st.error(
                        "Nome ou senha incorretos."
                    )

            else:

                st.warning(
                    "Preencha todos os campos."
                )

    elif opcao == "Sair":

        st.info("Programa encerrado.")


# ==============================
# MENU DO USUÁRIO
# ==============================

def menu_usuario(usuario):

    st.title("🎯 QUIZ")

    st.write(
        f"Bem-vindo(a), **{usuario}**! 👋"
    )

    opcao = st.radio(
        "Escolha uma opção:",
        ["Jogar", "Ranking", "Logout"]
    )

    # ==============================
    # JOGAR
    # ==============================

    if opcao == "Jogar":

        st.subheader("🎮 Jogar")

        # ------------------------------
        # BOTÃO INICIAR
        # ------------------------------

        if not st.session_state.quiz_iniciado:

            st.write(
                "Você terá 8 perguntas."
            )

            if st.button("▶️ Iniciar rodada"):

                st.session_state.quiz_iniciado = True
                st.session_state.resultado_salvo = False

                # Limpa informações de uma rodada anterior
                st.session_state.pop(
                    "rodada",
                    None
                )

                st.session_state.pop(
                    "numero_pergunta",
                    None
                )

                st.session_state.pop(
                    "pontuacao",
                    None
                )

                st.session_state.pop(
                    "quiz_finalizado",
                    None
                )

                st.rerun()

        # ------------------------------
        # QUIZ
        # ------------------------------

        else:

            pontuacao = iniciar_rodada()

            # ------------------------------
            # FIM DO QUIZ
            # ------------------------------

            if pontuacao is not None:

                if not st.session_state.resultado_salvo:

                    salvar_resultado(
                        usuario,
                        pontuacao
                    )

                    st.session_state.resultado_salvo = True

                st.success(
                    f"🏆 Você fez {pontuacao}/8 pontos!"
                )

                if st.button(
                    "🔄 Jogar novamente"
                ):

                    st.session_state.quiz_iniciado = False

                    st.session_state.resultado_salvo = False

                    st.session_state.pop(
                        "rodada",
                        None
                    )

                    st.session_state.pop(
                        "numero_pergunta",
                        None
                    )

                    st.session_state.pop(
                        "pontuacao",
                        None
                    )

                    st.session_state.pop(
                        "quiz_finalizado",
                        None
                    )

                    st.rerun()

    # ==============================
    # RANKING
    # ==============================

    elif opcao == "Ranking":

        st.subheader("🏆 Ranking")

        mostrar_ranking()

    # ==============================
    # LOGOUT
    # ==============================

    elif opcao == "Logout":

        st.session_state.usuario_logado = None

        st.session_state.quiz_iniciado = False

        st.session_state.resultado_salvo = False

        st.session_state.pop(
            "rodada",
            None
        )

        st.session_state.pop(
            "numero_pergunta",
            None
        )

        st.session_state.pop(
            "pontuacao",
            None
        )

        st.session_state.pop(
            "quiz_finalizado",
            None
        )

        st.rerun()


# ==============================
# SISTEMA
# ==============================

def sistema():

    if st.session_state.usuario_logado is None:

        menu_principal()

    else:

        menu_usuario(
            st.session_state.usuario_logado
        )


# ==============================
# EXECUTAR
# ==============================

if __name__ == "__main__":
    sistema()