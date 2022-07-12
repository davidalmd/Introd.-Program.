nomes = ['David', 'Gabriel', 'Victor', 'Samuel', 'Ray', 'Rafa', 'Lav', 'Louise']
arquivo = open('nomes.txt', 'a')
for i in range(len(nomes)):
    arquivo.write('%s\n' %nomes[i])
arquivo.close()

trocou = True
fim = len(nomes) - 1
while fim > 0 and trocou:
    trocou = False
    for i in range(0, fim):
        if nomes[i] > nomes[i + 1]:
            trocou = True
            temp = nomes[i]
            nomes[i] = nomes[i + 1]
            nomes[i + 1] = temp
    fim = fim - 1
saida = open('nomes.txt', 'w')
for i in range(len(nomes)):
    saida.write('%s\n' %nomes[i])
saida.close()

