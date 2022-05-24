frase = input('Digite uma frase: ')
tamanho = len(frase)
for i in range (0, tamanho):
    letra = frase[i]
    if letra != 'a' and letra != 'A' and letra != 'e' and letra != 'E' and letra != 'i' and letra != 'I' and letra != 'o' and letra != 'O':
        if letra != 'u' and letra != 'U':
            print(letra, end='')
