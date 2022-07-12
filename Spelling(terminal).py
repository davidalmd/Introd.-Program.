import random, os, time

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

def testeNome():
    nomeExiste = False
    for i in range(0, len(rankingNivel1)):
        if nome in rankingNivel1[i]:
            nomeExiste = True
    for i in range(0, len(rankingNivel2)):
        if nome in rankingNivel2[i]:
            nomeExiste = True
    return nomeExiste

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rankingNivel1 = []
rankingNivel2 = []

rankingClassico = open('rankingClassico.txt', 'r')
for linha in rankingClassico.readlines():
    if linha[0] in '0123456789':
        rankingNivel1 += [linha]
rankingClassico.close()

rankingProdigio = open('rankingProdigio.txt', 'r')
for linha in rankingProdigio.readlines():
    if linha[0] in '0123456789':
        rankingNivel2 += [linha]
rankingProdigio.close()

while True:
    sequencia = []
    pontos = 0
    testePontos = True
    nome = input('Digite seu username: ')
    while testeNome():
        print('Esse nome de usuário já existe...')
        nome = input('Digite seu username: ')
    nivel = input('Qual nível de dificuldade você deseja jogar?\n'
                  '[1] Nível Clássico\n'
                  '[2] Nível Prodígio\n')
    os.system('cls')
    for i in range(3, 0, -1):
        print('Jogo iniciando em...')
        print(i)
        time.sleep(1)
        os.system('cls')

    while True:
        if nivel == '1':
            sequencia += [random.choice(alfabeto)]
            os.system('cls')
            for i in range(0, len(sequencia)):     
                print('A sequência é:')
                time.sleep(0.5)  
                print(sequencia[i])
                time.sleep(0.5)
                os.system('cls')
            
            for i in range(0, len(sequencia)):
                print('Digite as letras da sequência: ')
                letra = input()
                os.system('cls')
                if sequencia[i] == letra:
                    testePontos = True
                else:
                    print('GAME OVER!')
                    testePontos = False
                    break
            
            if testePontos == True:
                pontos += 1
                continue
            else:
                break
        
        elif nivel == '2':
            sequencia += [random.choice(alfabeto)]
            os.system('cls')
            if len(sequencia) == 1:
                print('A sequência é: ')
            else:
                print('A última letra da sequência é: ')
            time.sleep(0.5)
            print(f'{sequencia[len(sequencia) - 1]}')
            time.sleep(0.5)
            os.system('cls')

            for i in range(0, len(sequencia)):
                print('Digite as letras da sequência: ')
                letra = input()
                os.system('cls')
                if sequencia[i] == letra:
                    testePontos = True
                else:
                    print('GAME OVER!')
                    testePontos = False
                    break
            
            if testePontos == True:
                pontos += 1
                continue
            else:
                break

    if pontos < 10:
        pontos = '0' + str(pontos)
    
    if nivel == '1':
        rankingNivel1 += [str(pontos) + ' - ' + nome]
    elif nivel == '2':
        rankingNivel2 += [str(pontos) + ' - ' + nome]
    
    novamente = input('Digite 1 para jogar novamente...')
    if novamente == '1':
        os.system('cls')
        continue
    else:
        os.system('cls')
        break

bolha(rankingNivel1)
bolha(rankingNivel2)

rankingClassico = open('rankingClassico.txt', 'w')
for i in range(0, len(rankingNivel1)):
    rank1 = rankingNivel1[i]
    if rank1[0] in '0123456789':
        rankingClassico.write(rank1)
        rankingClassico.write('\n')
rankingClassico.close()

rankingProdigio = open('rankingProdigio.txt', 'w')
for i in range(0, len(rankingNivel2)):
    rank2 = rankingNivel2[i]
    if rank2[0] in '0123456789':
        rankingProdigio.write(rank2)
        rankingProdigio.write('\n')
rankingProdigio.close()
