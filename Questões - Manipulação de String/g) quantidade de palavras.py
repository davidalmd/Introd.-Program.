frase = input('Digite uma frase: ')
tamanho = len(frase)
branco = 1
for i in range (0, tamanho):
    letra = frase[i]
    if letra == ' ':
        branco = branco + 1
print(f'O número de palavras dessa frase é igual a {branco}.')
