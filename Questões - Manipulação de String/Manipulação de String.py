frase = input('Digite uma frase: ')
tamanho = len(frase)

opcao = int(input('Qual resposta você deseja receber?\n'
'[1] Frase na vertical\n'
'[2] Frase na diagonal\n'
'[3] Frase na ordem inversa\n'
'[4] Frase na diagonal invertida\n'
'[5] Frase sem vogal\n'
'[6] Frase com vogal em maiúsculo\n'
'[7] A quantidade de palavras presentes na frase\n'
'[8] Ler duas palavras, se a primeira estiver na frase, a segunda substitui essa palavra da frase\n'
'[9] Informe quantas vezes a letra i apareceu na frase\n'
'[10] Informe quantas consoantes estão presentes na frase\n'))

if opcao == 1:
    for i in range (0, tamanho):
        letra = frase[i]
        print(letra)

elif opcao == 2:
    for i in range (0, tamanho):
        letra = frase[i]
        print(' ' * i, letra)

elif opcao == 3:
    temp = tamanho - 1
    for i in range (0, tamanho):
        letra = frase[temp]
        print(letra, end='')
        temp = temp - 1

elif opcao == 4:
    for i in range (0, tamanho):
        tamanho = tamanho - 1
        letra = frase[tamanho]
        print(' ' * tamanho, letra)

elif opcao == 5:
    for i in range (0, tamanho):
        letra = frase[i]
        if letra != 'a' and letra != 'A' and letra != 'e' and letra != 'E' and letra != 'i' and letra != 'I' and letra != 'o' and letra != 'O':
            if letra != 'u' and letra != 'U':
                print(letra, end='')

elif opcao == 6:
    for i in range (0, tamanho):
        letra = frase[i]
        if letra == 'a':
            letra = 'A'
        elif letra == 'e':
            letra = 'E'
        elif letra == 'i':
            letra = 'I'
        elif letra == 'o':
            letra = 'O'
        elif letra == 'u':
            letra = 'U'
        print(letra, end='')

elif opcao == 7:
    branco = 1
    for i in range (0, tamanho):
        letra = frase[i]
        if letra == ' ':
            branco = branco + 1
    print(f'O número de palavras dessa frase é igual a {branco}.')

elif opcao == 8:
    palavra1 = input('Digite a primeira palavra para pesquisar na frase: ')
    palavra2 = input('Digite a segunda palavra que substituirá: ')
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

elif opcao == 9:
    quant = 0
    for i in range (0, tamanho):
        letra = frase[i]
        if letra == 'i' or letra == 'I':
            quant = quant + 1
    print(f'A quantidade de letras i na frase é de {quant}.')

elif opcao == 10:
    quant = 0
    for i in range (0, tamanho):
        letra = frase[i]
        if letra != ' ':
            if letra != 'a' and letra != 'A' and letra != 'e' and letra != 'E' and letra != 'i' and letra != 'I' and letra != 'o' and letra != 'O':
                if letra != 'u' and letra != 'U':
                    quant = quant + 1
    print(f'A quantidade de consoantes na frase é de {quant}.')

else:
    print('Você escolheu uma opção inválida...')
