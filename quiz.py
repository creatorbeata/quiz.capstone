import random
import streamlit as st
from pergunta import perguntas


def iniciar_rodada():

    # Cria uma rodada com 8 perguntas
    if "rodada" not in st.session_state:

        st.session_state.rodada = random.sample(
            perguntas,
            8
        )

        st.session_state.numero_pergunta = 0
        st.session_state.pontuacao = 0
        st.session_state.resposta_enviada = False
        st.session_state.resposta_correta = False
        st.session_state.quiz_finalizado = False


    # Verifica se as 8 perguntas terminaram
    if st.session_state.numero_pergunta >= 8:

        st.session_state.quiz_finalizado = True

        return st.session_state.pontuacao


    # Pergunta atual
    pergunta = st.session_state.rodada[
        st.session_state.numero_pergunta
    ]

    numero = st.session_state.numero_pergunta + 1

    st.write(f"### Pergunta {numero}/8")

    st.write(
        f"**{pergunta['pergunta']}**"
    )


    # ==============================
    # RESPOSTA
    # ==============================

    resposta_usuario = st.text_input(
        "Digite sua resposta:",
        key=f"resposta_{numero}",
        disabled=st.session_state.resposta_enviada
    )


    # ==============================
    # BOTÃO RESPONDER
    # ==============================

    if not st.session_state.resposta_enviada:

        if st.button(
            "Responder",
            key=f"responder_{numero}"
        ):

            if not resposta_usuario.strip():

                st.warning(
                    "⚠️ Digite uma resposta antes de continuar."
                )

            else:

                resposta_usuario = (
                    resposta_usuario
                    .strip()
                    .lower()
                )

                resposta_correta = (
                    pergunta["resposta"]
                    .strip()
                    .lower()
                )


                # Verifica a resposta

                if resposta_usuario == resposta_correta:

                    st.session_state.pontuacao += 1

                    st.session_state.resposta_correta = True

                else:

                    st.session_state.resposta_correta = False


                st.session_state.resposta_enviada = True

                st.rerun()


    # ==============================
    # FEEDBACK
    # ==============================

    if st.session_state.resposta_enviada:

        if st.session_state.resposta_correta:

            st.success(
                "✅ Resposta correta!"
            )

        else:

            st.error(
                "❌ Resposta incorreta!"
            )

            st.info(
                f"💡 A resposta correta era: "
                f"**{pergunta['resposta']}**"
            )


        # ==============================
        # PRÓXIMA PERGUNTA
        # ==============================

        if st.button(
            "➡️ Próxima pergunta",
            key=f"proxima_{numero}"
        ):

            st.session_state.numero_pergunta += 1

            st.session_state.resposta_enviada = False

            st.session_state.resposta_correta = False

            st.rerun()


    return None