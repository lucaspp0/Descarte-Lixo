

notas = []
materias = []
alunos = []

def atualizarAlunos():
  global alunos
  with open('alunos.csv', 'w') as alunosCsv:
    string = []
    for i in range( len(alunos) ):
      string.append( str( alunos[i]["id"] ) + ";" + str( alunos[i]["nome"] ) + ";" ) 
    alunosCsv.writelines(string)

def atualizarMaterias():
  global materias
  with open('materias.csv', 'w') as materiasCsv:
    string = []
    for i in range( len(materias) ):
      string.append( str( materias[i]["id"]) + ";" + str( materias[i]["nome"] ) + ";" + str( materias[i]["peso"] ) ) 
    materiasCsv.writelines(string)

def atualizarNotas():
  global notas
  with open('notas.csv', 'w') as notasCsv:
    string = []
    for i in range( len(notas) ):
      string.append( str( notas[i]["valor"] ) + ";" + str( notas[i]["aluno"] ) + ";" + str( notas[i]["materia"] ) ) 
    notasCsv.writelines(string)

def lerAlunos():
  global alunos
  with open('alunos.csv', 'r') as alunosCsv:
    linhas = alunosCsv.readlines()
    for linha in linhas:
      arr = linha.split(";")
      aluno = {
        "id": arr[0],
        "nome": arr[1]
      }
      alunos.append( aluno )

def lerMaterias():
  global materias
  with open('materias.csv', 'r') as materiasCsv:
    linhas = materiasCsv.readlines()
    for linha in linhas:
      arr = linha.split(";")
      materia = {
        "id": arr[0],
        "nome": arr[1],
      }
      materias.append( materia )

def lerNotas():
  global notas
  with open('notas.csv', 'r') as notasCsv:
    linhas = notasCsv.readlines()
    for linha in linhas:
      nota = linha.split(";")
      notas.append( nota )

def mediaNotas(materia):
  soma = 0
  contador = 0
  for nota in notas:
    if( nota["materia"] == materia["id"] ):
      soma += nota["valor"]
      contador += 1
  # cada prova vale 10
  return ( soma / contador ) * 10

def procurarMateria(nome):
  global materias
  for materia in materias:
    print(" - ")
    print("*",materia["nome"].replace("\n", ""),"*")
    print("*",nome,"*")
    print(nome == materia["nome"])
    print(" - ")
    print(" ")
    if(materia["nome"] == nome):
      return materia
  return -1

def mostraGrade():
  mediaMat = mediaNotas( procurarMateria("Matematica") )
  mediaPor = mediaNotas( procurarMateria("Portugues") )
  mediaHis = mediaNotas( procurarMateria("Historia") )
  mediaGeo = mediaNotas( procurarMateria("Geografia") )

  print( mediaMat ) # 60% 40%
  print( mediaPor ) # 30% 70%
  print( mediaHis ) # 80% 20%
  print( mediaGeo ) # 10% 90%

  pesoMat = 100 - mediaMat
  pesoPor = 100 - mediaPor
  pesoHis = 100 - mediaHis
  pesoGeo = 100 - mediaGeo

  soma = pesoMat + pesoPor + pesoHis + pesoGeo

  mat = soma / pesoMat
  port = soma / pesoPor
  hist = soma / pesoHis
  geo = soma / pesoGeo

  print("matemática: ",mat)
  print("matemática: ",port)
  print("matemática: ",hist)
  print("matemática: ",geo)


def inicializar():
  lerAlunos()
  lerMaterias()
  lerNotas()

inicializar()
mostraGrade()

'''
atualizarAlunos()
atualizarMaterias()
atualizarNotas()
'''
