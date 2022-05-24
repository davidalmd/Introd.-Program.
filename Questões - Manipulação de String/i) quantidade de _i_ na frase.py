frase = input('Digite uma frase: ')
tamanho = len(frase)
quant = 0
for i in range (0, tamanho):
    letra = frase[i]
    if letra == 'i' or letra == 'I':
        quant = quant + 1
print(f'A quantidade de letras i na frase é de {quant}.')
