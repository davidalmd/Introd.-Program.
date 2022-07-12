aprovados = []
alunos = []
notas1 = []
notas2 = []
media = []
arquivo = open("alunos.txt","r")
for linha in arquivo.readlines():
    nomes = ''
    for i in range(len(linha)):
        letra = linha[i]
        if letra != '|':
            nomes = nomes + letra
        else:
            break
    alunos = alunos + [nomes]
arquivo.close()

arquivo = open("alunos.txt","r")
for linha in arquivo.readlines():
    nota1 = ''
    nota2 = ''
    for i in range(len(linha)):
        letra = linha[i]
        if letra in '0123456789':
            nota1 = nota1 + letra
        elif letra == '.':
            nota1 = nota1 + linha[i] + linha[i + 1]
            break
    nota1 = float(nota1)
    notas1 = notas1 + [nota1]
    for i in range(len(linha)):
        letra = linha[i]
        if letra in '0123456789' and linha[i - 2] == '-':
            nota2 = nota2 + linha[i:]
    nota2 = float(nota2)
    notas2 = notas2 + [nota2]
for i in range(len(notas1)):
    media = media + [(notas1[i] + notas2[i]) / 2]

for i in range(len(alunos)):
    if media[i] >= 7:
        aprovados = aprovados + [alunos[i] + '= ' + str(media[i])]
arquivo.close()

aprovados.sort()
saida = open('aprovados.txt', 'w')
for a in range(len(aprovados)):
    saida.write('%s\n' %aprovados[a])
saida.close()
