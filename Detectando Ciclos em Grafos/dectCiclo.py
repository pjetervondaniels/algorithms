class Grafo:

    def __init__(self, V):
        self.V = V
        self.lista = [[] for i in range(V)]

    def add_aresta(self, orig, dest):
        self.lista[orig].append(dest)

    def dfs(self, v):

        pilha, pilha_rec = [], []
        visitados = [False for i in range(self.V)]
        pilha_rec = [False for i in range(self.V)]

        while True:

            achou_vizinho = False

            if not visitados[v]:
                pilha.append(v)
                visitados[v] = pilha_rec[v] = True

            aux_adj = None

            for adj in self.lista[v]:

                aux_adj = adj

                # se o vizinho está na pilha, é porque existe ciclo
                if pilha_rec[adj]:
                    return True
                elif not visitados[adj]:
                    # se não está na pilha e não foi visitado, indica que achou
                    achou_vizinho = True
                    break

            if not achou_vizinho:

                # marca que saiu da pilha
                pilha_rec[pilha[-1]] = False

                # remove da pilha
                pilha.pop()

                if len(pilha) == 0:
                    break

                v = pilha[-1]
            else:
                v = adj

        return False

    def tem_ciclo(self):

        for i in range(self.V):
            if self.dfs(i):
                return True
        return False


g = Grafo(3)
g.add_aresta(0, 1)
g.add_aresta(1, 2)
g.add_aresta(2, 0)
print(g.tem_ciclo())