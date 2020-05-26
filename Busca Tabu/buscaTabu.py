# Busca Tabu para resolver o problema da mochila

import random

mochila = [[4,2], [5,2], [7,3], [9,4], [6,4]] # configuração da mochila
iteracao, melhor_iteracao = 0, 0 # iterações
melhor_solucao = [] # guarda a melhor solução
lista_tabu = [] # lista tabu
capacidade_maxima = 23 # capacidade máxima da mochila
bt_max = 1 # quantidade máxima de iterações sem melhora no valor da melhor solução
max_vizinhos = 5 # quantidade máxima de vizinhos

# função para obter o valor da função objetivo
def obter_avaliacao(solucao, mochila, capacidade_maxima):
	somatorio_peso, somatorio_beneficio = 0, 0

	for i in range(len(solucao)):
		somatorio_peso += solucao[i] * mochila[i][0]
		somatorio_beneficio += solucao[i] * mochila[i][1]
	avaliacao = somatorio_beneficio * (1 - max(0, somatorio_peso - capacidade_maxima))

	return avaliacao


# função para obter o peso de uma solução
def obter_peso(solucao, mochila):
	peso = 0
	for i in range(len(solucao)):
		peso += solucao[i] * mochila[i][0]
	return peso


# função para gerar os vizinhos
def gerar_vizinhos(melhor_solucao, max_vizinhos):
	vizinhos, pos = [], 0
	for i in range(max_vizinhos):
		vizinho = []
		for j in range(len(melhor_solucao)):
			if j == pos:
				if melhor_solucao[j] == 0:
					vizinho.append(1)
				else:
					vizinho.append(0)
			else:
				vizinho.append(melhor_solucao[j])
		vizinhos.append(vizinho)
		pos += 1
	return vizinhos

# função para obter o valor de avaliação de cada vizinho
def obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinhos):
	vizinhos_avaliacao = []
	for i in range(max_vizinhos):
		vizinhos_avaliacao.append(obter_avaliacao(vizinhos[i], mochila, capacidade_maxima))
	return vizinhos_avaliacao


# função para obter o bit modificado
def obter_bit_modificado(melhor_solucao, melhor_vizinho):
	for i in range(len(melhor_solucao)):
		if melhor_solucao[i] != melhor_vizinho[i]:
			return i


# função para obter o vizinho com a máxima avaliação
def obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos):
	maxima_avaliacao = max(vizinhos_avaliacao)
	pos = 0
	bit_proibido = -1

	# verifica se a lista tabu não possui elementos
	if len(lista_tabu) != 0:
		# se possuir, é porque tem bit proibido, então pega esse bit
		bit_proibido = lista_tabu[0]

	# for para obter a posição do melhor vizinho
	for i in range(len(vizinhos_avaliacao)):
		if vizinhos_avaliacao[i] == maxima_avaliacao:
			pos = i
			break

	# verifica se o vizinho é resultado de movimento proibido
	if bit_proibido != -1:

		# obtém a posição do bit que foi modificado para gerar esse vizinho
		bit_pos = obter_bit_modificado(melhor_solucao, vizinhos[pos])

		# verifica se o bit está na lista tabu
		if bit_pos == bit_proibido:

			# se cair aqui, então procura o segundo melhor vizinho
			melhor_pos = 0

			for i in range(len(vizinhos_avaliacao)):
				if i != bit_pos:
					if vizinhos_avaliacao[i] > vizinhos_avaliacao[melhor_pos]:
						melhor_pos = i

			# retorna a posição do segundo melhor vizinho
			return melhor_pos

	# retorna a posição do melhor vizinho
	return pos


# gera uma solução inicial aleatória
for i in range(len(mochila)):
	bit = random.randint(0, 1)
	melhor_solucao.append(bit)

# mostra a solução inicial e seu valor de avaliação
print('Solução inicial: {0}, Avaliação: {1}'.format(melhor_solucao,
			obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)))

# obter o peso corrente da mochila
peso_corrente = obter_peso(melhor_solucao, mochila)

# obter o valor de avaliaçãoda melhor solução
melhor_avaliacao = obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)

# gera os vizinhos
vizinhos = gerar_vizinhos(melhor_solucao, max_vizinhos)

# calcula a avaliação dos vizinhos
vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinhos)

# obtém a posição do melhor vizinho
pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)

# verifica se o melhor vizinho tem avaliação melhor do que a avaliação até o momento
if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:

	# obtém o bit que foi modificado do melhor vizinho
	bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])

	# guarda o movimento proibido
	lista_tabu.append(bit_modificado)

	# faz uma cópia da solução
	melhor_solucao = vizinhos[pos_melhor_vizinho][:]

	# incrementa a iteração onde foi achada a melhor solução até o momento
	melhor_iteracao += 1

iteracao += 1

# entar em loop
while True:

	'''
		A condição de parada é se a diferença entre a iteraco e melhor_iteracao
		for maior que bt_max. A iteracao é a iteração global (sempre é incrementada).
		melhor_iteracao é a iteração onde se achou a melhor solução (nem sempre é incrementada).
		bt_max é o máximo de iterações sem melhora no valor da melhor solução.
	'''
	if (iteracao - melhor_iteracao) > bt_max:
		break

	# gera os novos vizinhos
	vizinhos = gerar_vizinhos(melhor_solucao, max_vizinhos)[:]

	# obtém o valor de avaliação dos vizinhos
	vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinhos)[:]

	# obtém a posição do melhor vizinho
	pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)

	# verifica se o melhor vizinho tem avaliação melhor do que a melhor avaliação corrente
	if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:

		# obtém o bit que foi modificado para gerar o melhor vizinho
		bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])

		# guarda o movimento proibido
		lista_tabu[0] = bit_modificado

		# temos uma solução melhor, faz uma cópia
		melhor_solucao = vizinhos[pos_melhor_vizinho][:]

		# atualiza a melhor avaliação
		melhor_avaliacao = vizinhos_avaliacao[pos_melhor_vizinho]

		# incrementa a iteração onde foi achada a melhor soluçao
		melhor_iteracao += 1

	iteracao += 1


# mostra a solução final e sua avaliação
print('Solução final: {0}, Avaliação: {1}'.format(melhor_solucao,
			obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)))
print('Melhor iteração: {0}'.format(melhor_iteracao))
print('Iteração: {0}'.format(iteracao))