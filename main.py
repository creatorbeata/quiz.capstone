from storage import (
    cadastrar_usuario,
    fazer_login,
    salvar_resultado,
    mostrar_ranking,
)

from quiz import iniciar_rodada


def menu_principal():

    print("\n===== QUIZ =====")
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    return opcao


def menu_usuario(usuario):

    print("\n===== MENU DO USUÁRIO =====")
    print("1 - Jogar")
    print("2 - Ranking")
    print("3 - Logout")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        return "jogar"

    elif opcao == "2":
        mostrar_ranking()
        return "continuar"

    elif opcao == "3":
        return "logout"

    else:
        print("Opção inválida.")
        return "continuar"


def sistema():

    usuario_logado = None

    while True:

        # =========================
        # USUÁRIO NÃO ESTÁ LOGADO
        # =========================

        if usuario_logado is None:

            opcao = menu_principal()

            if opcao == "1":

                nome = input("Digite seu nome: ").strip()
                senha = input("Digite sua senha: ").strip()

                mensagem = cadastrar_usuario(nome, senha)

                print(mensagem)

            elif opcao == "2":

                nome = input("Digite seu nome: ").strip()
                senha = input("Digite sua senha: ").strip()

                usuario_logado = fazer_login(nome, senha)

                if usuario_logado:
                    print(
                        f"\nBem-vindo(a), {usuario_logado}!"
                    )

            elif opcao == "3":

                print("Programa encerrado.")
                break

            else:

                print("Opção inválida.")

        # =========================
        # USUÁRIO ESTÁ LOGADO
        # =========================

        else:

            acao = menu_usuario(usuario_logado)

            # -------------------------
            # JOGAR
            # -------------------------

            if acao == "jogar":

                jogar_novamente = True

                while jogar_novamente:

                    pontuacao = iniciar_rodada()

                    salvar_resultado(
                        usuario_logado,
                        pontuacao
                    )

                    print(
                        f"\nSua pontuação foi: "
                        f"{pontuacao}/8"
                    )

                    resposta = input(
                        "\nDeseja jogar novamente? "
                        "(sim/nao): "
                    ).strip().lower()

                    if resposta == "sim":

                        print("\nIniciando nova rodada...")

                    else:

                        jogar_novamente = False
                        print("\nVoltando ao menu...")

            # -------------------------
            # LOGOUT
            # -------------------------

            elif acao == "logout":

                usuario_logado = None

                print("Logout realizado.")


if __name__ == "__main__":
    sistema()