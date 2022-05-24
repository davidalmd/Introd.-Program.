import random

lista = []

print('Gerando e mostrando 40 valores aleatórios na lista')
print('----------------------------------------------------')
for i in range(0, 40):
    n = random.randint(1, 10)
    lista = lista + [n]
for i in range(0, 40):
    print(lista[i], end=' | ')

print('\n\nGerando e mostrando os valores pares da lista')
print('----------------------------------------------------')
for i in range(0, 40):
    if lista[i] % 2 == 0:
        print(lista[i], end=' | ')

print('\n\nGerando e mostrando os valores impares da lista')
print('----------------------------------------------------')
for i in range(0, 40):
    if lista[i] % 2 != 0:
        print(lista[i], end=' | ')

#bolha
trocou = True
fim = len(lista) - 1
while fim > 0 and trocou:
    trocou = False
    for i in range(0, fim):
        if lista[i] > lista[i + 1]:
            trocou = True
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp
    fim = fim - 1
print()
print(lista)
