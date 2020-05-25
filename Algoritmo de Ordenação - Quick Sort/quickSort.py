# passa a lista, o início e o fim da lista
def particiona(v, ini, fim):
    # o pivô é o elemento do início
    pivo = ini

    for i in range(ini + 1, fim + 1):
        if v[i] <= v[ini]:
            pivo += 1
            v[i], v[pivo] = v[pivo], v[i]

    v[pivo], v[ini] = v[ini], v[pivo]

    return pivo


# passa a lista, o início e o fim da lista
def quick_sort(v, ini, fim):
    '''
        Se o fim for maior que o iníco, então
        eu calculo a posição do pivô utilizando
         a função particiona
    '''
    if fim > ini:
        # separa os dados em duas partições
        pivo = particiona(v, ini, fim)

        '''
            Tendo o pivô, chama a função duas
            vezes para cada partição, a primeira
            dos elementos que estão antes do pivô
            e a segunda é a dos elementos que estão
            depois do pivô
        '''
        quick_sort(v, ini, pivo - 1)
        quick_sort(v, pivo + 1, fim)


v = [50, 20, 70, 15]
quick_sort(v, 0, len(v) - 1)
print(v)