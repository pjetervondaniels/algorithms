# Resolvendo o problema dos cromossomos usando a lógica do caixeiro viajante

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
            else:
                if custo_circuito < melhor_custo:
                    melhor_circuito = circuito[:]
                    melhor_custo = custo_circuito

            return (melhor_circuito, melhor_custo)

        for i in range(iteracoes):
            melhor_circuito, melhor_custo = gerar_circuito(melhor_circuito, melhor_custo)

        print('Melhor circuito: %s\nCusto: %d' % (str(melhor_circuito), melhor_custo))

    def pcv_genetico(self, tam_pop, geracoes, tam_torneio, prob_cruz, prob_mut):

        pop = []  # população

        def gerar_individuo():
            vertices = [i for i in range(1, self.n)]
            individuo = [0]
            while len(vertices) > 0:
                e = random.choice(vertices)
                vertices.remove(e)
                individuo.append(e)
            return individuo

        # função de fitness
        def obter_custo(individuo):
            custo = 0
            for i in range(self.n - 1):
                custo += self.custos[(individuo[i], individuo[i + 1])]
            custo += self.custos[(individuo[-1], individuo[0])]
            return custo

        # gerando a população inicial
        for i in range(tam_pop):
            pop.append(gerar_individuo())

        # a cada geração
        for i in range(geracoes):

            # seleção por torneio
            for j in range(tam_torneio):

                if random.random() <= prob_cruz:

                    pai1, pai2 = None, None

                    # selecionando os indivíduos
                    while True:
                        pai1 = random.randint(0, tam_pop - 1)
                        pai2 = random.randint(0, tam_pop - 1)
                        if pai1 != pai2:
                            break

                    gen1_validos = [i for i in range(self.n)]
                    gen2_validos = gen1_validos[:]
                    filho1, filho2 = [], []

                    # cruzamento de um ponto
                    while True:

                        # selecionando um ponto
                        ponto = random.randint(0, self.n - 1)

                        # não seleciona as extremidades
                        if ponto != 0 and ponto != (self.n - 1):

                            for p in range(ponto):

                                if pop[pai1][p] not in filho1:
                                    filho1.append(pop[pai1][p])
                                    gen1_validos.remove(pop[pai1][p])
                                else:
                                    e = random.choice(gen1_validos)
                                    filho1.append(e)
                                    gen1_validos.remove(e)

                                if pop[pai2][p] not in filho2:
                                    filho2.append(pop[pai2][p])
                                    gen2_validos.remove(pop[pai2][p])
                                else:
                                    e = random.choice(gen2_validos)
                                    filho2.append(e)
                                    gen2_validos.remove(e)

                            for p in range(ponto, self.n):

                                if pop[pai2][p] not in filho1:
                                    filho1.append(pop[pai2][p])
                                    gen1_validos.remove(pop[pai2][p])
                                else:
                                    e = random.choice(gen1_validos)
                                    filho1.append(e)
                                    gen1_validos.remove(e)

                                if pop[pai1][p] not in filho2:
                                    filho2.append(pop[pai1][p])
                                    gen2_validos.remove(pop[pai1][p])
                                else:
                                    e = random.choice(gen2_validos)
                                    filho2.append(e)
                                    gen2_validos.remove(e)

                            break

                    # aplica o operador de mutação
                    if random.random() <= prob_mut:
                        gene1, gene2 = None, None
                        while True:
                            gene1 = random.randint(0, self.n - 1)
                            gene2 = random.randint(0, self.n - 1)
                            if gene1 != gene2:
                                filho1[gene1], filho1[gene2] = filho1[gene2], filho1[gene1]
                                filho2[gene1], filho2[gene2] = filho2[gene2], filho2[gene1]
                                break

                    # obtém o fitness dos pais e dos filhos
                    fitness_pai1 = obter_custo(pop[pai1])
                    fitness_pai2 = obter_custo(pop[pai2])
                    fitness_filho1 = obter_custo(filho1)
                    fitness_filho2 = obter_custo(filho2)

                    if fitness_filho1 < fitness_pai1 or fitness_filho1 < fitness_pai2:
                        if fitness_filho1 < fitness_pai1:
                            pop.pop(pai1)
                        else:
                            pop.pop(pai2)
                        pop.append(filho1)
                    elif fitness_filho2 < fitness_pai1 or fitness_filho2 < fitness_pai2:
                        if fitness_filho2 < fitness_pai1:
                            pop.pop(pai1)
                        else:
                            pop.pop(pai2)
                        pop.append(filho2)

        # obtém o melhor indivíduo da população
        melhor_individuo = pop[0][:]
        for ind in range(1, tam_pop):
            if obter_custo(pop[ind]) < obter_custo(melhor_individuo):
                melhor_individuo = pop[ind][:]

        print('Melhor indivíduo: %s\nCusto: %d' % (str(melhor_individuo), obter_custo(melhor_individuo)))


grafo = GeradorGrafo(50)
grafo.gerar_grafo()
print('Random')
grafo.pcv_random(1000)
print('\nAlgoritmo Genético')
grafo.pcv_genetico(tam_pop=2000, geracoes=1000, tam_torneio=1, prob_cruz=0.7, prob_mut=0.1)