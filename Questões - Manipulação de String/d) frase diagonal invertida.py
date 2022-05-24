frase = input('Digite uma frase: ')
tamanho = len(frase)
for i in range (0, tamanho):
    tamanho = tamanho - 1
    letra = frase[tamanho]
    print(' ' * tamanho, letra)

#sem espaço
#for i in range (0, tamanho):
#    tamanho = tamanho - 1
#    letra = frase[tamanho]
#    if letra == ' ':
#        continue
#    else:
#        print(' ' * tamanho, letra)

#jeito do professor
#branco = ' '
#for i in range(0, tamanho):
#    branco = branco + ' '
#for i in range(0, tamanho):
#    letra = frase [i]
#    print(branco, letra)
#    branco = branco[0:tamanho - i]
