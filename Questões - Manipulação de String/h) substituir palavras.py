frase = input('Digite uma frase: ')
palavra1 = input('Digite a primeira palavra para pesquisar na frase: ')
palavra2 = input('Digite a segunda palavra que substituirá: ')
tamanho = len(frase)
frase_final = ''
palavra = ''
for i in range(tamanho):
    if frase[i] != ' ':
        palavra = palavra + frase[i]
    else:
        if palavra1 == palavra:
            frase_final = frase_final + ' ' + palavra2
        else:
            frase_final = frase_final + ' ' + palavra
        palavra = ''
if palavra1 == palavra:
            frase_final = frase_final + ' ' + palavra2
else:
    frase_final = frase_final + ' ' + palavra
palavra = ''

print(f'A frase original é: {frase}')
print(f'A frase final é:{frase_final}')
