from entrada import Entrada

class Fita:
	def __init__(self, conteudo):
		self.estados = dict()
		self.conteudo = conteudo
		self.vazio = "B"

	def leitura(self, indice):
		#lê de acordo com a posição do cabeçote
		if indice < len(self.conteudo):
			return self.conteudo[indice]
		return self.vazio

class Cabecote:
	#representa o cabeçote de uma máquina de turing
	def __init__(self):
		self.fita = Fita("")
		self.posicao = 0

	def moverCabecote(self, movimento):
		self.posicao += movimento


	def leitura(self):
		return self.fita.leitura(self.posicao)

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

	def testaTransicao(self,estado, simbolos):
		for i in range(3):
			if (simbolos[i] != simbolosEntrada[i]) and (simbolosEntrada[i] != "/"):
				return False
		return True


	def checaAlfabeto(self):
		pass


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
#		for i in range(len(alfab)):
#			if alfab[i] not in alfab:
#				raise Exception("letra nao existe no alfabeto de entrada")
		self.alfabetoFita = list(alfab)

	def definirAlfabetoEntrada(self, alfab):
		self.alfabetoEntrada = list(alfab)


	def passo(self):
		leituraEntrada = fitas["entrada"].leitura()
		leituraHistorico = fitas["historico"].leitura()
		leituraSaida = fitas["saida"].leitura()

		for transicao in self.fitas["entrada"].estado[self.estadoAtual].transicoes:
			if transicao.testaTransicao([leituraEntrada, leituraHistorico, leituraSaida]):
				
				for i in range (3):
					if transicao.simbolosEntrada[i] == "/":
						self.cabecotes[i].movimento(transicao[i])
					else:
						pass
						#self.cabecotes[i].
				self.estadoAtual = fita.estadoVai
				break








def main():
	entrada = Entrada()
	m = Maquina()
	m.definirAlfabetoEntrada(entrada.alfabetoentrada)
	m.definirAlfabetoFita(entrada.alfabetofita)
	m.defineEstadoInicial(entrada.transicoes[0][0])
	m.estadoAtual = m.estadoInicial
	m.defineEstadoFinal(entrada.transicoes[entrada.numTransicoes-1][0])
	for i in range(entrada.estados):
		m.adicionaEstadoNaFita(entrada.listEstados[i], "entrada")

	for i in range(entrada.numTransicoes):
		t = Transicao(entrada.transicoes[i][0], [entrada.transicoes[i][1], entrada.transicoes[i][2], entrada.transicoes[i][3]],
		[entrada.transicoes[i+1][1], entrada.transicoes[i+1][2], entrada.transicoes[i+1][3]], entrada.transicoes[i+1][0]) 
		m.adicionaTransicao(t)
		i+=1

	m.adicionaEntradaNaFita(entrada.fita)

	m.passo()

main()