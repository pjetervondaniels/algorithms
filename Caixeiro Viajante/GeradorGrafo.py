# Gerador de grafos

class GeradorGrafo:

	def __init__(self, n):

		self.n = n
		self.grafo = [[] for i in range(n)]

	def gerar_grafo(self):

		for i in range(self.n):
			for j in range(self.n):
				if i != j:
					self.grafo[i].append(j)

	def mostrar_grafo(self):

		for i in range(self.n):
			print('Adjacentes de %d:' % i, end=' ')
			for adj in self.grafo[i]:
				print('%d' % adj, end=' -> ')
			print('')


gerador = GeradorGrafo(4)
gerador.gerar_grafo()
gerador.mostrar_grafo()