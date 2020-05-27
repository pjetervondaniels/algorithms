'''
	Exemplo de arquivo de configuração:

	7 2 2 100 0
	1.0 1.0
	1.5 2.0
	3.0 4.0
	5.0 7.0
	3.5 5.0
	4.5 5.0
	3.5 4.5

	Cada número da primeira linha em ordem:
		7 é a quantidade de data points
		2 é a quantidade de atributos
		2 é a quantidade de clusters
		100 é o máximo de iterações
		0 indica que o data point não possui nome
'''

import random
from math import *

class Ponto:

	def __init__(self, id_ponto, valores):
		self.id_ponto = id_ponto
		self.valores = valores
		self.total_valores = len(valores)
		self.id_cluster = -1

	def getID(self):
		return self.id_ponto

	def setCluster(self, id_cluster):
		self.id_cluster = id_cluster

	def getCluster(self):
		return self.id_cluster

	def getValor(self, indice):
		return self.valores[indice]

	def getTotalValores(self):
		return self.total_valores

	def addValor(self, valor):
		self.valores.append(valor)


class Cluster:

	def __init__(self, id_cluster, ponto):
		self.id_cluster = id_cluster
		self.total_valores = ponto.getTotalValores()
		self.valores_centrais = []
		self.pontos = []

		for i in range(self.total_valores):
			self.valores_centrais.append(ponto.getValor(i))

		self.pontos.append(ponto)

	def addPonto(self, ponto):
		self.pontos.append(ponto)

	def removerPonto(self, id_ponto):
		total_pontos = len(self.pontos)
		for i in range(total_pontos):
			if self.pontos[i].getID() == id_ponto:
				self.pontos.pop(i)
				return True
		return False

	def getValorCentral(self, indice):
		return self.valores_centrais[indice]

	def setValorCentral(self, indice, valor):
		self.valores_centrais[indice] = valor

	def getPonto(self, indice):
		return self.pontos[indice]

	def getTotalPontos(self):
		return len(self.pontos)

	def getID(self):
		return self.id_cluster

class KMeans:

	def __init__(self, K, total_pontos, total_valores, max_iter):
		self.K = K
		self.total_pontos = total_pontos
		self.total_valores = total_valores
		self.max_iter = max_iter
		self.clusters = []


	# retornar o centro mais próximo (usa a distância euclidiana)
	def getIDCentroProximo(self, ponto):

		soma = 0.0
		id_cluster_centro = 0

		for i in range(self.total_valores):
			soma += pow(self.clusters[0].getValorCentral(i) - ponto.getValor(i), 2.0)

		min_dist = sqrt(soma)

		for i in range(1, self.K):
			soma = 0.0
			for j in range(self.total_valores):
				soma += pow(self.clusters[i].getValorCentral(j) - ponto.getValor(j), 2.0)
			dist = sqrt(soma)
			if dist < min_dist:
				min_dist = dist
				id_cluster_centro = i

		return id_cluster_centro


	def executar(self, pontos):

		if self.K > self.total_pontos:
			print('Erro: quantidade de clusters é maior que a quantidade de pontos.')
			return

		indices_proibidos = []

		# escolhe K valores distintos para os centros do clusters
		for i in range(self.K):
			while True:
				indice_ponto = random.randint(0, self.total_pontos - 1)
				if indice_ponto not in indices_proibidos:
					indices_proibidos.append(indice_ponto)
					pontos[indice_ponto].setCluster(i)
					cluster = Cluster(i, pontos[indice_ponto])
					self.clusters.append(cluster)
					break

		iter_ = 1

		while True:

			done = True

			# associa cada ponto ao centro mais próximo
			for i in range(self.total_pontos):

				id_cluster_velho = pontos[i].getCluster()
				id_cluster_proximo = self.getIDCentroProximo(pontos[i])

				if id_cluster_velho != id_cluster_proximo:
					if id_cluster_velho != -1:
						self.clusters[id_cluster_velho].removerPonto(pontos[i].getID())
					pontos[i].setCluster(id_cluster_proximo)
					self.clusters[id_cluster_proximo].addPonto(pontos[i])
					done = False

			# recalcula os centros
			for i in range(self.K):
				for j in range(self.total_valores):
					total_pontos_cluster = self.clusters[i].getTotalPontos()
					soma = 0.0

					if total_pontos_cluster > 0:
						for k in range(total_pontos_cluster):
							soma += self.clusters[i].getPonto(k).getValor(j)
						self.clusters[i].setValorCentral(j, soma / total_pontos_cluster)

			if done == True or iter_ >= max_iter:
				print("Parou na iteracao %d" % iter_)
				break

			iter_+=1

		# mostra os elementos de cada cluster

		for i in range(self.K):
			total_pontos_cluster = self.clusters[i].getTotalPontos()
			print('\nCluster %d: ' % (i + 1), end='')
			for j in range(total_pontos_cluster):
				print('%d ' % (self.clusters[i].getPonto(j).getID() + 1), end='')



if __name__ == "__main__":

	arq = open('dataset.txt')
	linhas = arq.readlines()
	arq.close()
	primeira_linha = linhas[0].split()
	num_pontos, num_atributos, num_clusters, max_iter = [int(i) for i in primeira_linha]

	pontos = []
	for i in range(1, num_pontos + 1):
		atributos = linhas[i].split()
		valores = [float(i) for i in atributos]
		ponto = Ponto(i - 1, valores)
		pontos.append(ponto)

	kmeans = KMeans(num_clusters, num_pontos, num_atributos, max_iter)
	kmeans.executar(pontos)