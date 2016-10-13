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

		for i in self.transicoes:
			for j in i:
				contem = False
				if j != '/':
					for k in self.alfabetofita:
						if j == k or j == '/' or j == 'D' or j == 'E':
							contem = True
					for k in self.listEstados:
						if j == k:
							contem = True
					if contem == False:
						print(j)
						raise Exception ('Entrada invalida', 'Transicoes com alfabeto diferente da suportada!')

		self.fita = input()
		#print("Entrada da fita: ", self.fita)
		
		for i in list(self.fita):
			contem = False
			for j in self.alfabetoentrada:
				if i == j:
					contem = True
			if contem == False:
				raise Exception ('Entrada invalida', 'Entrada da fita com alfabeto diferente da suportada!')


	
		
		
