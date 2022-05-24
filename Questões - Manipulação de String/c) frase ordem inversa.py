frase = input('Digite uma frase: ')
tamanho = len(frase)
temp = tamanho - 1
for i in range (0, tamanho):
    letra = frase[temp]
    print(letra, end='')
    temp = temp - 1

#com espaço
#for i in range (0, tamanho):
#    letra = frase[temp]
#    print('', letra, end='')
#    temp = temp - 1
