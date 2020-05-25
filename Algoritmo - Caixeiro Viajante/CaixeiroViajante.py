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

	def pcv_random(self, iteracoes):

		melhor_circuito = []
		melhor_custo = None

		def gerar_circuito(melhor_circuito, melhor_custo):

			vertices = [i for i in range(1, self.n)]
			circuito = [0]
			custo_circuito = 0

			while len(vertices) > 0:
				e = random.choice(vertices)
				vertices.remove(e)
				custo_circuito += self.custos[(circuito[-1], e)]
				circuito.append(e)

			custo_circuito += self.custos[(circuito[-1], 0)]

			if melhor_custo is None:
				melhor_circuito = circuito[:]
				melhor_custo = custo_circuito
				print('Circuito inicial: %s - Custo: %d' % (str(melhor_circuito), melhor_custo))
			else:
				if custo_circuito < melhor_custo:
					melhor_circuito = circuito[:]
					melhor_custo = custo_circuito

			return (melhor_circuito, melhor_custo)

		for i in range(iteracoes):
			melhor_circuito, melhor_custo = gerar_circuito(melhor_circuito, melhor_custo)
			#print('Iter %d: Melhor circuito: %s - Custo: %d' % (i + 1, str(melhor_circuito), melhor_custo))

		print('Melhor circuito: %s - Custo: %d' % (str(melhor_circuito), melhor_custo))


gerador = GeradorGrafo(10)
gerador.gerar_grafo()
gerador.pcv_random(1000)