import random
from perguntas import perguntas

def iniciar_rodada():
    rodada = random.sample(perguntas, 8)
    pontuacao = 0

    print("====== NOVA RODADA ======")
    print("Você terá 8 perguntas.")
    print("Digite a sua resposta: ")

    for numero, pergunta in enumerate(rodada, start=1):
        print(f"Pergunta {numero}/8")
        print(pergunta["pergunta"])

        resposta_usuario = input("Resposta: ")
        resposta_usuario = resposta_usuario.strip().lower()
        resposta_correta = pergunta["resposta"].strip().lower()

        if resposta_usuario == resposta_correta:
            print("Resposta correta :)")
            pontuacao += 1
        else:
            print("Resposta incorreta :(")
            print(f"Resposta correta: {resposta_correta}")

        print()

    return pontuacao
