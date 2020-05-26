# Busca Binária

def busca_binaria(lista, chave, ini, fim):

	if ini > fim:
		return False

	meio = (ini + fim) // 2

	if chave == lista[meio]:
		return True
	if chave < lista[meio]:
		return busca_binaria(lista, chave, ini, meio - 1)
	return busca_binaria(lista, chave, meio + 1, fim)

lista = [11, 5, 10, 20, 15, 4]
chave = 15
lista.sort()
if busca_binaria(lista, chave, 0, len(lista) - 1) == True:
	print('Encontrou')
else:
	print('Não encontrou')