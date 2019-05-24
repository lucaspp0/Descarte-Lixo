
def lerAlunos():
  global alunos
  with open('alunos.csv', 'r') as alunos:
    print("teste")
    linhas = alunos.readlines()
    for linha in linhas:
      aluno = linha.split(";")
      alunos.append( { aluno[0] } )

def lermaterias():
  print("lerAlunos")

def lerNotas():
  print("lerAlunos")

def lerTurmas():
  print("lerAlunos")

notas = []
materias = []
alunos = []
turmas = []
