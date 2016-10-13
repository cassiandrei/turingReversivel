"""Feito por Cassiano Andrei Dias da Silveira Schneider e Pedro Langbecker Lima"""

from entrada import Entrada

class Fita:
	def __init__(self, conteudo):
		self.estados = dict()
		self.conteudo = conteudo
		self.vazio = "B"

	def leitura(self, indice):
		#lê de acordo com a posição do cabeçote
		if indice in range(len(self.conteudo)):
			return self.conteudo[indice]
		return self.vazio

	def escrever(self, posicao, escrita):

		tamanho = len(self.conteudo)
		#ajuste do cabeçote caso ele esteja em uma posicao negativa
		if posicao in range(tamanho):
			self.conteudo = self.conteudo[:posicao] + escrita + self.conteudo[posicao+1:]	
		elif escrita != self.vazio:
			if posicao < 0:
				self.conteudo = escrita.ljust(abs(posicao), self.vazio) + self.conteudo
			else:
				self.conteudo += escrita.rjust(posicao - tamanho - 1, self.vazio)

		


class Cabecote:
	#representa o cabeçote de uma máquina de turing
	def __init__(self):
		self.fita = Fita("")
		self.posicao = 0

	def moverCabecote(self, movimento, sentido=False):
		if movimento == "D":
			if not sentido:
				self.posicao += 1
			else:
				self.posicao -= 1
		elif movimento == "E":
			if not sentido:
				self.posicao -= 1
			else:
				self.posicao += 1

	def remover(self):
		self.fita.conteudo = self.fita.conteudo[:self.posicao] + self.fita.conteudo[self.posicao+1:]
		self.posicao -= 1

	def leitura(self):
		return self.fita.leitura(self.posicao)

	def escrever(self, escrito):
		self.fita.escrever(self.posicao, escrito)


class Estado:

	def __init__(self, nome, ehFinal=False):
		self.nome = nome
		self.transicoes = list()
		self.final = ehFinal

	def adicionaTransicao(self, transicao):
		self.transicoes.append(transicao)


class Transicao:
	def __init__(self,estadoVeio, simbolosEntrada, simbolosSaida, estadoVai):
		self.estadoVeio = estadoVeio
		self.estadoVai = estadoVai
		self.simbolosEntrada = simbolosEntrada
		self.simbolosSaida = simbolosSaida
		self.pertence_a = None

	def testaTransicao(self, simbolos):
		for i in range(3):
			if (simbolos[i] != self.simbolosEntrada[i]) and (self.simbolosEntrada[i] != "/"):
				return False
		return True

	def reverterTransicao(self):
		entrada = list()
		saida = list()
		for i in range(3):
			if self.simbolosEntrada[i] != "/":
				entrada.append(self.simbolosSaida[i])
				saida.append(self.simbolosEntrada[i])
			else:
				entrada.append("/")
				saida.append(self.simbolosSaida[i])
		return Transicao(self.estadoVai, entrada, saida, self.estadoVeio)

class Maquina:

	def __init__(self):
		self.alfabetoFita = list()
		self.alfabetoEntrada = list()
		self.cabecotes = [Cabecote() for i in range(3)]
		self.fitas = { "entrada" : self.cabecotes[0].fita,
					   "historico" : self.cabecotes[1].fita,
					   "saida" : self.cabecotes[2].fita }

		self.vazio = "B"
		self.estadoInicial = None
		self.estadoFinal = None
		self.travada = False
		self.estadoAtual = None


	def checarAlfabeto(self, alfabeto):
		pass


	def adicionaEntradaNaFita(self, fita):

		#testes de exceção
		self.fitas["entrada"].conteudo = str(fita)

	def defineEstadoInicial(self, i):
		self.estadoInicial = i

	def defineEstadoFinal(self, i):
		self.estadoFinal = i

	def adicionaEstadoNaFita(self, nome, fita, ehFinal=False):
		#cria uma instancia de Estado e atribui a fita
		self.fitas[fita].estados[nome] = Estado(nome,ehFinal)


	def adicionaTransicao(self, transicao):

		estadosDisponiveis = self.fitas["entrada"].estados.keys()
		if transicao.estadoVeio not in estadosDisponiveis:
			raise Exception ('Maquina nao tem um estado {transicao.estadoVeio} registrado'.format(transicao=transicao))


		transicao.pertence_a = self.fitas["entrada"].estados[transicao.estadoVeio]

		self.fitas["entrada"].estados[transicao.estadoVeio].adicionaTransicao(transicao)


	def definirAlfabetoFita(self, alfab):
		self.alfabetoFita = list(alfab)

	def definirAlfabetoEntrada(self, alfab):
		self.alfabetoEntrada = list(alfab)

	def printaFitas(self):
		if not self.fitas["entrada"].conteudo:
			print (self.fitas["entrada"].vazio)
		else:
			print (self.fitas["entrada"].conteudo)

		if not self.fitas["historico"].conteudo:
			print (self.fitas["historico"].vazio)
		else:
			print (self.fitas["historico"].conteudo)

		if not self.fitas["saida"].conteudo:
			print (self.fitas["saida"].vazio)
		else:
			print (self.fitas["saida"].conteudo)



	def passo(self):
		leituraEntrada = self.cabecotes[0].leitura()
		leituraHistorico = self.cabecotes[1].leitura()
		leituraSaida = self.cabecotes[2].leitura()
		
		print("Estagio inicial das fitas: ")
		self.printaFitas()
		for transicao in self.fitas["entrada"].estados[self.estadoAtual].transicoes:
			if transicao.testaTransicao([leituraEntrada, leituraHistorico, leituraSaida]):

				print ("transicao precisa ler " + str(transicao.simbolosEntrada))
				print ("transicao vai realizar " + str(transicao.simbolosSaida))

				for i in range (3):
					if transicao.simbolosEntrada[i] == "/":

						self.cabecotes[i].moverCabecote(transicao.simbolosSaida[i])
					else:
						self.cabecotes[i].escrever(transicao.simbolosSaida[i])
						#self.cabecotes[i].
				self.estadoAtual = transicao.estadoVai
				break

		if self.estadoAtual == self.estadoFinal:
			return False
		else:
			return True


	#simulando copia na maquina de turing (cabeçote se encontra no fim da fita de entrada)
	def copiaDeFita(self):

		#volta pro inicio do cabecote de entrada
		while (True):
			aux = self.cabecotes[0].leitura()
			if aux == " " or aux == "B":
				break
			self.cabecotes[2].escrever(aux)
			self.cabecotes[0].escrever(self.fitas["entrada"].vazio)
			self.cabecotes[0].moverCabecote("E")
			self.cabecotes[2].moverCabecote("E")
		

	def moverCabecoteSaida(self):
		while (self.cabecotes[2].leitura() == "B"):
			self.cabecotes[2].moverCabecote("D")
		while(self.cabecotes[2].leitura() != "B"):
			self.cabecotes[2].moverCabecote("D")
		self.cabecotes[2].moverCabecote("E")
		

	def configurarReversao(self):
		self.copiaDeFita()
		self.moverCabecoteSaida()
		#print(self.cabecotes[2].leitura())
		#print(self.cabecotes[2].posicao)
		#print("Conteudo: " + self.fitas["saida"].conteudo)
		aux = self.estadoInicial
		self.estadoInicial = self.estadoFinal
		self.estadoFinal = aux
		self.estadoAtual = self.estadoInicial

		#gera novos estados e transições reversas pra fita "saida"
		for nome in self.fitas["entrada"].estados.keys():
			self.fitas["saida"].estados[nome] = Estado(nome)
		
		for nome, estado in self.fitas["entrada"].estados.items():
			#print ("estado " + 	nome)
			for transicao in estado.transicoes:
				transicao = transicao.reverterTransicao()
				self.fitas["saida"].estados[transicao.estadoVeio].adicionaTransicao(transicao)
				

	def reverter(self):
		leituraEntrada = self.cabecotes[2].leitura()
		leituraHistorico = self.cabecotes[1].leitura()
		leituraSaida = self.cabecotes[0].leitura()

		for transicao in self.fitas["saida"].estados[self.estadoAtual].transicoes:
			
			if transicao.testaTransicao([leituraEntrada, leituraHistorico, leituraSaida]):
				print(transicao.simbolosEntrada)
				for i in range (3):
					if transicao.simbolosEntrada[i] == "/":
						self.cabecotes[2-i].moverCabecote(transicao.simbolosSaida[i], True)
					else:
						#print("escreveu\n")
						self.cabecotes[2-i].escrever(transicao.simbolosSaida[i])
						#self.cabecotes[i].
				self.estadoAtual = transicao.estadoVai
				break
		if self.estadoAtual == self.estadoFinal:
			return False
		else:
			return True


"""Do jeito implementado é necessário que o estadoInicial seja o primeiro estado que da primeira transição,
e o estadoFinal seja o ultimo estado da ultima transição, como no exemplo de entrada do site"""

def main():
	entrada = Entrada()
	m = Maquina()
	m.definirAlfabetoEntrada(entrada.alfabetoentrada)
	m.definirAlfabetoFita(entrada.alfabetofita)
	m.defineEstadoInicial(entrada.transicoes[0][0])
	m.estadoAtual = m.estadoInicial
	m.defineEstadoFinal(entrada.transicoes[entrada.numTransicoes*2-1][0])

	for i in range(entrada.estados):
		m.adicionaEstadoNaFita(entrada.listEstados[i], "entrada")

	for i in range(0,entrada.numTransicoes*2,2):
		t = Transicao(entrada.transicoes[i][0], [entrada.transicoes[i][1], entrada.transicoes[i][2], entrada.transicoes[i][3]],
		[entrada.transicoes[i+1][1], entrada.transicoes[i+1][2], entrada.transicoes[i+1][3]], entrada.transicoes[i+1][0]) 
		m.adicionaTransicao(t)

	m.adicionaEntradaNaFita(entrada.fita)

	while(m.passo()):
		pass
	
	m.configurarReversao()

	while(m.reverter()):

		pass
	m.reverter()


main()