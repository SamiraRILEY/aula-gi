import datetime
from uuid import uuid4

# Classe representando um aluno
class Aluno:
    # Construtor da classe
    def __init__(self, nome, nascimento, curso=None):
        self.nome = nome
        self.nascimento = nascimento
        self.matricula = str(uuid4())  # Gera um ID único
        self.ingresso = datetime.datetime.now()  # Registra data e hora de ingresso
        self.curso = curso
        self.notas = []  # Lista para armazenar notas
        self.provas = {}  # Dicionário para armazenar provas
        self.aulas_perdidas = {}  # Dicionário para armazenar aulas para reposição

    # Método para marcar uma prova
    def marcar_prova(self, data_prova, nome_prova):
        if nome_prova in self.provas:
            raise Exception("Prova já marcada para esse nome.")
        self.provas[nome_prova] = {
            "data": data_prova,
            "aluno": self.matricula
        }
        return f"Sua prova foi marcada para o dia {data_prova} com sucesso!"

    # Método para calcular a média das notas
    def fazer_media(self):
        if not self.notas:
            return "Nenhuma nota foi encontrada"
        media = sum(self.notas) / len(self.notas)
        return f"Sua média é de {media:.2f}"

    # Método para repor uma aula
    def repor_aula(self, nome_aula, data_reposicao):
        if nome_aula in self.aulas_perdidas:
            return "Você já fez esta aula"
        self.aulas_perdidas[nome_aula] = {
            "data_reposicao": data_reposicao,
            "aluno": self.matricula
        }
        return f"Sua aula foi marcada para dia {data_reposicao}"