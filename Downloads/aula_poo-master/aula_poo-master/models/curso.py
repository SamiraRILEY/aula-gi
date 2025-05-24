class Curso:
    def _init_(self, nome, duracao, professor, materias):
        self.nome = nome
        self.alunos = {}  # {aluno: [notas]}
        self.duracao = duracao
        self.professor = professor
        self.materias = materias
        self.aulas = []

    def listar_alunos_aprovados(self):
        aprovados = []
        for aluno, notas in self.alunos.items():
            if notas:  # Se tem notas
                media = sum(notas) / len(notas)
                if media >= 7:  # Critério de aprovação
                    aprovados.append({
                        "aluno": aluno,
                        "media": media
                    })
        if not aprovados:
            return "Nenhum aluno aprovado."
        return aprovados

    def contabilizar_presenca(self, aluno, data):
        if aluno not in self.alunos:
            return f"Aluno {aluno} não está matriculado neste curso."
        # Adiciona presença na lista de aulas
        self.aulas.append({"aluno": aluno, "data": data})
        return f"Presença de {aluno} registrada na data {data}."