import os

# subfuncoes

# funções

def logar():
  print("logar")

def cadastrar():
  print("logar")

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# programa principal

# variaveis principais

alunos = []
turmas = []
materias = []
notas = []

sistema = True

while(sistema):
    op = input(" 1 - logar \n 2 - cadastrar \n 3 - sair \n")
    if(op == "1"):
        logar()
    elif(op t "2"):
        cadastrar()
    elif(op == "3"):
        sistema = False
    else:
        print("Operacao invalida")
    limparTela()
print("Obrigado por usar o gerenciamneto estudantil")