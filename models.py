class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.acertos = 0
        self.total_perguntas = 0

    def registrar_resposta(self, acertou):
        self.total_perguntas += 1

        if acertou:
            self.acertos += 1
            self.pontuacao += 1

    def calcular_porcentagem(self):
        if self.total_perguntas == 0:
            return 0

        return (self.acertos / self.total_perguntas) * 100


class Pergunta:
    def __init__(self, enunciado, resposta):
        self.enunciado = enunciado
        self.resposta = resposta

    def verificar_resposta(self, resposta_usuario):
        return resposta_usuario.strip().lower() == self.resposta.strip().lower()
