frase = input('Digite uma frase: ')
tamanho = len(frase)
for i in range (0, tamanho):
    letra = frase[i]
    print(' ' * i, letra)

#sem espaços
#for i in range (0, tamanho):
#    letra = frase[i]
#    if letra == ' ':
#        continue
#    else:
#        print(' ' * i, letra)

#jeito do professor
#branco = ' '
#for i in range (0, tamanho):
#    letra = frase[i]
#    print(branco, letra)
#    branco = branco + ' '
