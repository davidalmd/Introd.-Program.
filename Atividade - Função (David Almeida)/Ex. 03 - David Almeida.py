def bolha(lista):
    trocou = True
    fim = len(lista) - 1
    while fim > 0 and trocou:
        trocou = False
        for c in range(0, fim):
            if lista[c] > lista[c + 1]:
                trocou = True
                temp = lista[c]
                lista[c] = lista[c + 1]
                lista[c + 1] = temp
        fim = fim - 1

def megasena(palpites):
    for i in range(1, palpites+1):
        lista = []

        n1 = random.randint(1, 60)
        n2 = random.randint(1, 60)

        while n1 == n2:
            n2 = random.randint(1, 60)
        n3 = random.randint(1, 60)
        while n3 == n1 or n3 == n2:
            n3 = random.randint(1, 60)
        n4 = random.randint(1, 60)
        while n4 == n1 or n4 == n2 or n4 == n3:
            n4 = random.randint(1, 60)
        n5 = random.randint(1, 60)
        while n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
            n5 = random.randint(1, 60)
        n6 = random.randint(1, 60)
        while n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
            n6 = random.randint(1, 60)

        lista = lista + [n1] + [n2] + [n3] + [n4] + [n5] + [n6]

        bolha(lista)

        print(f'Palpite {i}: ', end='')
        for c in range(0, len(lista)):
            if lista[c] < 10:
                print(f'0{lista[c]}', end=' | ')
            else:
                print(f'{lista[c]}', end=' | ')
        print()

import random

n = int(input('Digite um número inteiro que gerará essa quantidade de palpites: '))
megasena(n)
