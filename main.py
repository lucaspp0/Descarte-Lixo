import matplotlib.pyplot as plt

# inicializar variaveis
notas = []
materias = []
alunos = []


# atualizar arqivvo csv com novos valores
def atualizarCsv(arquivo, valores):
	if( len(valores) < 1 ):
		print("valores vázios")
		return False
	with open(arquivo, "w") as csv:
		conteudo = []
		string = ""
		# adicionar o cabeçalho do arquivo csv com as chaves do dicionario
		for i in range( len(valores[0].keys()) ):
			if(i == ( len( list( valores[0].keys() ) ) - 1 ) ):
				string += ( list( valores[0].keys() )[i]+"\n" )
			else:
				string += ( list( valores[0].keys() )[i]+";" )
		if(not string == ""):
			conteudo.append(string)

		# adicionar os valores do arquivo csv
		for i in range( len(valores) ):
			total = len( valores[i].items() ) - 1
			cont = 0
			string = ""
			for keys, valor in valores[i].items():
				string += valor+"\n" if cont == total else valor+";"
				cont += 1
			conteudo.append(string)
		print(conteudo)
		csv.writelines(conteudo)
		

# ler or arquivos csv
def lerCsv( arquivo, campos ):
	array = []
	first = True
	with open(arquivo, "r") as csv:
		linhas = csv.readlines()
		for linha in linhas:
			arr = linha.split(";")
			if( len(arr) > 1 ):
				dicionario = {}
				# pula o cabeçalho (primeira linha) do csv
				if( first ):
					first = False
				else:
					for i in range( len( campos ) ):
						# percorre tanto a lista dos campos e os valores do csv para adicionar campos ao dicionario, e retira a quebra de linha dor csv (\n)
						if( i == (len(campos)-1) ):
							dicionario[campos[i]] = arr[i].replace("\n","")
						else:
							dicionario[campos[i]] = arr[i]
					array.append( dicionario )
	return array
	
def inicializar():
	global alunos, materias, notas
	alunos = lerCsv("alunos.csv", [ "id","nome" ])
	materias = lerCsv("materias.csv", [ "id","nome","peso" ])
	notas = lerCsv("notas.csv", [ "id" , "valor" , "aluno", "materia" ])
	

# Calcula a media e uma matéria esécifíca
def mediaNotas( materia ):
	soma = 0
	contador = 0
	for nota in notas:
		# verifica todas as notas especifícas da matéria passada pelo parametro
		if( nota["materia"] == materia["id"] ):
			soma += round( float( nota["valor"] ), 2 )
			contador += 1
	# cada prova vale 10, por isso multiplicar or 10 dara a porcentagem
	return ( soma / contador ) * 10

# Calcula a media e uma matéria esécifíca
def mediaAluno( materia, aluno ):
	soma = 0
	contador = 0
	for nota in notas:
		# verifica todas as notas especifícas da matéria passada pelo parametro
		if( nota["materia"] == materia["id"] and nota["aluno"] == aluno["id"] ):
			soma += round( float( nota["valor"] ), 2 )
			contador += 1
	# cada prova vale 10, por isso multiplicar or 10 dara a porcentagem
	return ( soma / contador ) * 10
	
def grade():
	global materias
	# pegar todas as médias das matérias
	medias = []
	for materia in materias:
		medias.append( mediaNotas( materia ) )
	# calcular a necessidade de cada materia
	necessidades = []
	for media in medias:
		necessidades.append( 100 - media )
	# igualar cada o valor de necessidade com regra de 3
	soma = sum(necessidades)
	nomeMaterias = []
	porcentagens = []
	for i in range( len(materias) ):
		porcentagem = ( 100 * necessidades[i] ) / soma
		porcentagem = round(porcentagem, 2)
		porcentagens.append( porcentagem )
		nomeMaterias.append( materias[i]["nome"] )
		# print("A turma terá {0}% de aulas da matéria {1}".format(porcentagem, materias[i]["nome"]))
	return [ nomeMaterias, porcentagens ]
		
def gradeAlunos( aluno ):
	global materias
	medias = []
	for materia in materias:
		medias.append( mediaAluno( materia, aluno ) )
	nomeMaterias = []
	porcentagens = []
	for i in range( len(materias) ):
		porcentagens.append( medias[i] )
		nomeMaterias.append( materias[i]["nome"][0:3] )
	# retorna uma lista pois será usava pra visualização do gráfico
	return [ nomeMaterias, porcentagens ]
	
def mostrarGrade():
	resultado = grade()
	
	labels = resultado[0]
	sizes = resultado[1]
	
	fig, ax = plt.subplots()
	ax.pie(sizes, labels=labels, autopct='%1.2f%%')
	ax.axis('equal')
	ax.set_title('Matérias da Escola')
	
	plt.show()
	
def procurarAluno(nome):
	# mostrar alunos
	for aluno in alunos:
		if( aluno["nome"] == nome):
			return aluno
	return -1
	
def rendimentoAluno():
	# mostrar alunos
	for aluno in alunos:
		print(aluno["nome"])
	nome = input("escreva o nome do aluno para visualizar seu rendimento: ")
	aluno = procurarAluno(nome)
	if( not aluno == -1 ):        
		resultado = gradeAlunos( aluno )
		
		labels = resultado[0]
		sizes = resultado[1]
		
		fig, ax = plt.subplots()
		plt.bar(labels, sizes, width=0.5)
		plt.figure(figsize=(20, 3))
		ax.set_ylabel('Nota')
		ax.set_xlabel('Matéria')
		ax.set_title('Rendimento do aluno')
		plt.show()
		
	else:
		print("aluno inválido")    
		
def opcoes():
	op = 0
	while(not op == 3):
		op = int( input('''
1 - ver a divisão de matérias da turma
2 - ver o rendimento de um aluno específico
3 - sair
        
Selecione uma das opções: ''') )
		if(op == 1):
			mostrarGrade()
		elif(op == 2):
			rendimentoAluno()
		elif(op == 3):
			print("Obrigado por usar o gerenciamento Estudantil")
		else:
			print("Opção inválida")
    
inicializar()
opcoes()