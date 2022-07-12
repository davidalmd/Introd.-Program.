import random

def bolha(lista):
    trocou = True
    fim = len(lista) - 1
    while fim > 0 and trocou:
        trocou = False
        for i in range(0, fim):
            if lista[i] < lista[i + 1]:
                trocou = True
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
        fim = fim - 1

parImpar = int(input('Defina a ordem do par ou impar:\n'
                '[1] Darkseid par e Fênix Negra ímpar\n'
                '[2] Darkseid ímpar e Fênix Negra par\n'))

darkseidParImpar = random.randint(0, 10) #Considerando que eles jogarão com as mãos, tendo 10 dedos disponíveis para "jogar"
fenixParImpar = random.randint(0, 10) #Considerando que eles jogarão com as mãos, tendo 10 dedos disponíveis para "jogar"

print(f'\nDarkseid colocou {darkseidParImpar} dedos e a Fênix Negra colocou {fenixParImpar} dedos, totalizando {darkseidParImpar + fenixParImpar}.')

if parImpar == 1:
    if (darkseidParImpar + fenixParImpar) % 2 == 0:
        print('O resultado é par, Darkseid ganhou e tem vantagem no empate.\n')
        defensor = 'darkseid'
    else:
        print('O resultado é ímpar, Fênix Negra ganhou e tem vantagem no empate.\n')
        defensor = 'fenix'

else: #Considerando que o usuário não vai errar e vai digitar 2
    if (darkseidParImpar + fenixParImpar) % 2 == 0:
        print('O resultado é par, Fênix Negra ganhou e tem vantagem no empate.\n')
        defensor = 'fenix'
    else:
        print('O resultado é ímpar, Darkseid ganhou e tem vantagem no empate.\n')
        defensor = 'darkseid'

darkseidDados = []
fenixDados = []

for i in range(0, 6):
    if i < 3:
        darkseidDados += [random.randint(1, 6)]
    else:
        fenixDados += [random.randint(1, 6)]

bolha(darkseidDados)
bolha(fenixDados)

print(f'Darkseid jogou os 3 dados e tirou {darkseidDados}.')
print(f'Fênix Negra jogou os 3 dados e tirou {fenixDados}.')

darkseidPontos = 0
fenixPontos = 0

for c in range(0, 3):
    if darkseidDados[c] > fenixDados[c]:
        darkseidPontos += 1
    elif fenixDados[c] > darkseidDados[c]:
        fenixPontos += 1
    else:
        if defensor == 'darkseid':
            darkseidPontos += 1
        else: #Nesse caso defensor seria igual a 'fenix'
            fenixPontos += 1

print(f'\nNa comparação dos dados, Darkseid marcou {darkseidPontos} pontos e Fênix Negra marcou {fenixPontos} pontos.')

if darkseidPontos > fenixPontos:
    print('Darkseid venceu o combate e será o dominador da terra!')
else:
    print('Fênix Negra venceu o combate e será a dominadora da terra!')
