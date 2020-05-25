# Gerador de grafos

import random

class GeradorGrafo:

	def __init__(self, n):

		self.n = n
		self.grafo = [[] for i in range(n)]
		self.custos = {}

	def gerar_grafo(self):

		for i in range(self.n):
			for j in range(self.n):
				if i != j:
					if (i, j) and (j, i) not in self.custos:
						custo = random.randint(1, 100)
						self.custos[(i, j)] = custo
						self.custos[(j, i)] = custo
					self.grafo[i].append(j)

	def mostrar_grafo(self):

		for i in range(self.n):
			print('Adjacentes de %d:' % i, end=' ')
			for adj in self.grafo[i]:
				print('(custo %d) -> %d ->' % (self.custos[i, adj], adj), end=' ')
			print('')


gerador = GeradorGrafo(3)
gerador.gerar_grafo()
gerador.mostrar_grafo()