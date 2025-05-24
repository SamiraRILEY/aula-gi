from app.logica_sistema import (
    cadastrar_aluno, listar_alunos, detalhar_aluno, deletar_aluno,
    cadastrar_curso, listar_cursos, detalhar_curso, excluir_curso,
    listar_alunos_aprovados, inserir_aluno_no_curso
)
from datetime import datetime
from app.logica_sistema import ALUNOS  # Importa a lista de alunos também

comando = ""

while comando != "sair":
    comando = input(f"""
Escolha uma opção:
1) Cadastrar Aluno
2) Listar Alunos
3) Detalhar Aluno
4) Deletar Aluno
5) Cadastrar Curso
6) Listar Cursos
7) Detalhar Curso
8) Excluir Curso
9) Listar Alunos Aprovados por Curso
10) Inserir Aluno no Curso
Digite 'sair' para sair do sistema
\n""")

    match comando:
        case "1":
            nome = input('Informe o nome do aluno: ')
            nascimento = input('Informe a data de nascimento do aluno (DD/MM/AAAA): ')
            curso = input('Informe o curso do aluno (ou deixe vazio): ')
            nascimento_dt = datetime.strptime(nascimento, "%d/%m/%Y")
            print(cadastrar_aluno(nome, nascimento_dt, curso))

        case "2":
            print(listar_alunos())

        case "3":
            matricula = input('Informe a matrícula do aluno: ')
            print(detalhar_aluno(matricula))

        case "4":
            matricula = input('Informe a matrícula do aluno para deletar: ')
            print(deletar_aluno(matricula))

        case "5":
            nome_curso = input('Informe o nome do curso: ')
            print(cadastrar_curso(nome_curso))

        case "6":
            print(listar_cursos())

        case "7":
            nome_curso = input('Informe o nome do curso para detalhar: ')
            print(detalhar_curso(nome_curso))

        case "8":
            nome_curso = input('Informe o nome do curso para excluir: ')
            print(excluir_curso(nome_curso))

        case "9":
            nome_curso = input('Informe o nome do curso: ')
            print(listar_alunos_aprovados(nome_curso))

        case "10":
            matricula = input('Informe a matrícula do aluno: ')
            nome_curso = input('Informe o nome do curso: ')

            # Procurar o aluno pelo número de matrícula
            aluno_obj = None
            for aluno in ALUNOS:
                if aluno.matricula == matricula:
                    aluno_obj = aluno
                    break

            if not aluno_obj:
                print("Aluno não encontrado.")
            else:
                print(inserir_aluno_no_curso(aluno_obj, nome_curso))

        case "sair":
            print("Saindo do sistema...")

        case _:
            print("Opção inválida. Tente novamente.")