frase = input('Digite uma frase: ')
tamanho = len(frase)
quant = 0
for i in range (0, tamanho):
    letra = frase[i]
    if letra != ' ':
        if letra != 'a' and letra != 'A' and letra != 'e' and letra != 'E' and letra != 'i' and letra != 'I' and letra != 'o' and letra != 'O':
            if letra != 'u' and letra != 'U':
                quant = quant + 1
print(f'A quantidade de consoantes na frase é de {quant}.')
