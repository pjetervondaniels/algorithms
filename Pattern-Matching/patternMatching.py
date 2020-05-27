'''
	Pattern-Macthing Algorithm - Brute-force
'''


def brute_force(texto, padrao):
    len_texto, len_padrao = len(texto), len(padrao)

    for i in range(len_texto - len_padrao + 1):

        j = 0

        while j < len_padrao and texto[i + j] == padrao[j]:
            j += 1

        if j == len_padrao:
            return i  # substring texto[i:i+j] corresponde a P

    return -1


texto = 'python é uma excelente linguagem, pois python é muito fácil de aprender!'
padrao = 'python'
print(brute_force(texto, padrao))