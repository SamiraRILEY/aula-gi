from models.alunos import Aluno
from datetime import datetime

CURSOS = {}
ALUNOS = []


def cadastrar_aluno(nome, nascimento, curso):
    if not nome or not nascimento:
        return "Parâmetros inválidos"

    aluno_objeto = Aluno(nome, nascimento, curso)

    if curso:
        c = CURSOS.get(curso, {"alunos": [], "nome_curso": curso})
        c["alunos"].append(aluno_objeto)
        CURSOS[curso] = c

    ALUNOS.append(aluno_objeto)

    return {
        "nome_aluno": aluno_objeto.nome,
        "matricula": aluno_objeto.matricula,
        "curso": curso
    }


def listar_alunos():
    return ALUNOS


def detalhar_aluno(matricula):
    for aluno in ALUNOS:
        if aluno.matricula == matricula:
            return vars(aluno)
    return "Aluno não encontrado"


def deletar_aluno(matricula):
    global ALUNOS
    for aluno in ALUNOS:
        if aluno.matricula == matricula:
            ALUNOS.remove(aluno)
            return f"Aluno com matrícula {matricula} deletado."
    return "Aluno não encontrado"

def cadastrar_curso(nome_curso):
    if nome_curso in CURSOS:
        return f"Curso '{nome_curso}' já existe."
    CURSOS[nome_curso] = {"nome_curso": nome_curso, "alunos": []}
    return f"Curso '{nome_curso}' cadastrado com sucesso."

def listar_cursos():
    if not CURSOS:
        return "Nenhum curso cadastrado."
    return list(CURSOS.keys())

def detalhar_curso(nome_curso):
    curso = CURSOS.get(nome_curso)
    if not curso:
        return f"Curso '{nome_curso}' não encontrado."
    return {
        "nome_curso": curso["nome_curso"],
        "quantidade_alunos": len(curso["alunos"]),
        "alunos": [aluno.nome for aluno in curso["alunos"]]
    }

def excluir_curso(nome_curso):
    if nome_curso not in CURSOS:
        return f"Curso '{nome_curso}' não encontrado."
    del CURSOS[nome_curso]
    return f"Curso '{nome_curso}' excluído com sucesso."

def listar_alunos_aprovados(nome_curso):
    curso = CURSOS.get(nome_curso)
    if not curso:
        return f"Curso '{nome_curso}' não encontrado."

    resultado = []
    for aluno in curso["alunos"]:
        if not aluno.notas:
            media = 0
        else:
            media = sum(aluno.notas) / len(aluno.notas)

        if media >= 9:
            status = "aprovado com excelência"
        elif media > 6:
            status = "aprovado"
        else:
            status = "reprovado"

        resultado.append({
            "nome": aluno.nome,
            "media": media,
            "status": status
        })

    return resultado

def inserir_aluno_no_curso(aluno, nome_curso):
            curso = CURSOS.get(nome_curso)
            if not curso:
              return f"Curso '{nome_curso}' não encontrado."

            if aluno in curso["alunos"]:
               return f"Aluno '{aluno.nome}' já está matriculado no curso '{nome_curso}'."

            curso["alunos"].append(aluno)
            return f"Aluno '{aluno.nome}' inserido no curso '{nome_curso}' com sucesso."




# Exemplo de chamada
print(cadastrar_aluno(
    "Vitor",
    datetime.strptime("06/11/1996", "%d/%m/%Y"),
    "Python"
))