def encriptar(texto, chave):

	lista = list(texto)
	texto_criptografado = ''

	for i in lista:
		ord_c = (ord(i) - ord('A') + chave) % 26
		texto_criptografado += chr(ord_c + ord('A'))
	return texto_criptografado

def descriptografar(texto, chave):

	lista = list(texto)
	texto_descriptografado = ''

	for i in lista:
		ord_c = (ord(i) - ord('A') - chave) % 26
		texto_descriptografado += chr(ord_c + ord('A'))

	return texto_descriptografado


print(encriptar('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23))
print(descriptografar('XYZABCDEFGHIJKLMNOPQRSTUVW', 23))