nomes = []
idade = []
for a in range(0, 6):
    name = input('Digite o nome: ')
    nomes = nomes + [name]
print(f'Lista desordenada: {nomes}')

#Bolha
trocou = True
fim = len(nomes) - 1
while fim > 0 and trocou:
    trocou = False
    for b in range(0, fim):
        if nomes[b] > nomes[b + 1]:
            trocou = True
            temp = nomes[b]
            nomes[b] = nomes[b + 1]
            nomes[b + 1] = temp
    fim = fim - 1
#Fim da bolha
print(f'Lista ondernada: {nomes}')
