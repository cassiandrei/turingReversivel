class Maquina:

	def __init__(self):
		self.alfabetoFita = list()
		self.alfabetoEntrada = list()
		self.cabecotes = [Maquina.Cabecote() for i in range(3)]
		self.fitas = { "entrada" : self.cabecotes[0].fita,
					   "historico" : self.cabecotes[1].fita,
					   "saida" : self.cabecotes[2].fita }

		self.vazio = "B"			

	def definirAlfabetoFita(self, alfab):
		pass 

	def definirAlfabetoEntrada(self, alfab):
		self.alfabetoEntrada = list(alfab)


	class Fita:
		
		def __init__(self):



	class Cabecote:
		#representa o cabeçote de uma máquina de turing
		def __init__(self):
			fita = Fita("")
			self.posicao = 0


	def __init__(self):





def main():
	m = Maquina()

	pass







main()