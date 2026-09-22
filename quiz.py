import random
from perguntas import perguntas

def iniciar_rodada():
    return random.sample(perguntas, 8)

def verificar_resposta(resposta_usuario, resposta_correta):
    resposta_usuario = resposta_usuario.strip().lower()
    resposta_correta = resposta_correta.strip().lower()

    return resposta_usuario == resposta_correta
