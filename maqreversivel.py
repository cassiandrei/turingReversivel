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
		self.fita = Fita()
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


class Transicao:
	def __init__(self,estadoVeio, simbolosEntrada, simbolosSaida, estadoVai):
		self.estadoVeio = estadoVeio
		self.estadoVai = estadoVai
		self.simbolosEntrada = simbolosEntrada
		self.simbolosSaida = simbolosSaida

	def testa(self,estado, simbolos):
		if self.estadoVeio != estado:
			return False

		for i in range(3):
			if (simbolos[i] != simbolosEntrada) and (simbolosEntrada[i] != "/"):
				return False

		return True



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

		estadosDisponiveis = self.fitas["entrada"].estados.key()
		if transicao.estadoVeio not in estadosDisponiveis:
			raise Exception ('Maquina nao tem um estado {transicao.estadoVeio} registrado'.format(transicao=transicao))


	def definirAlfabetoFita(self, alfab):
#		for i in range(len(alfab)):
#			if alfab[i] not in alfab:
#				raise Exception("letra nao existe no alfabeto de entrada")
		self.alfabetoFita = alfab

	def definirAlfabetoEntrada(self, alfab):
		self.alfabetoEntrada = list(alfab)


	def passo(self):

		leituraEntrada = fita["entrada"].leitura()
		leituraHistorico = fitas["historico"].leitura()
		leituraSaida = fitas["saida"].leitura()

		

def main():
	m = Maquina()
	m.definirAlfabetoEntrada("01#")
	m.definirAlfabetoFita("01#xB")
	m.defineEstadoInicial = "1"
	m.defineEstadoFinal = "4"
	for i in range(4):
		m.adicionaEstadoNaFita(str(i), "entrada")

	t1 = Transicao("1", ["0", "B", "B"], ["x", "0", "B"], "2")
	t2 = Transicao("2", ["/", "/", "B"], ["D", "D", "B"], "3")
	t3 = Transicao("3", ["0", "B", "B"], ["x", "0", "B"], "4")

	m.adicionaEntradaNaFita("00")

main()