class Entrada:
	def __init__(self):

		self.estados = 0
		self.simbolosentrada = 0
		self.simbolosfita = 0
		self.numTransicoes = 0
		self.listEstados = list()
		self.alfabetoentrada = list()
		self.alfabetofita = list()
		self.transicoes = list()
		self.fita = ""

		linha = input().split(' ')
		self.estados = int(linha[0])
		self.simbolosentrada = int(linha[1])
		self.simbolosfita = int(linha[2])
		self.numTransicoes = int(linha[3])

		#print("Numero de estados: ", self.estados)
		#print("Numero de simbolos de entrada: ", self.simbolosentrada)
		#print("Numero de simbolos da fita ", self.simbolosfita)
		#print("Numero de transicoes: ", self.numTransicoes)

		self.listEstados = input().split(' ')
		#print("Estados : ", self.listEstados) 		

		self.alfabetoentrada = input().split(' ')
		#print("Alfabeto entrada: ", self.alfabetoentrada)

		self.alfabetofita = input().split(' ')
		#print("Alfabeto fita: ", self.alfabetofita)

		for i in range(self.numTransicoes):
			linha = input().replace('(',"").replace(')',"").split('=')
			self.transicoes.append(linha[0].split(','))
			self.transicoes.append(linha[1].split(','))
		#print("Transicoes: ", self.transicoes)	

		self.fita = input()
		#print("Entrada da fita: ", self.fita)
		



	
		
		
