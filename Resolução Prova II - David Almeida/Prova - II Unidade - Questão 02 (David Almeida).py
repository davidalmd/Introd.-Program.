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

palavras = ['friend', 'amico', 'prijatelj', 'Freund', 'ven', 'ystävä', 'пријaтeљ', 'Mellon', 'amigo', 'barát']

tentativas = 0
friend = 0 
amico = 0 
prijatelj = 0
Freund = 0
ven = 0
ystävä = 0
пријaтeљ = 0
Mellon = 0
amigo = 0
barát = 0
pronunciada = ''
ordemMaior = []

while pronunciada != 'Mellon':
    tentativas += 1
    pronunciada = palavras[random.randint(0, 9)]
    if pronunciada == 'friend':
        friend += 1
    elif pronunciada == 'amico':
        amico += 1
    elif pronunciada == 'prijatelj':
        prijatelj += 1
    elif pronunciada == 'Freund':
        Freund += 1
    elif pronunciada == 'ven':
        ven += 1
    elif pronunciada == 'ystävä':
        ystävä += 1
    elif pronunciada == 'пријaтeљ':
        пријaтeљ += 1
    elif pronunciada == 'Mellon':
        Mellon += 1
    elif pronunciada == 'amigo':
        amigo += 1
    else: #Nesse caso a palavra pronunciada só pode ser 'barát'
        barát += 1

ordemMaior += [friend] + [amico] + [prijatelj] + [Freund] + [ven] + [ystävä] + [пријaтeљ] + [Mellon] + [amigo] + [barát]

bolha(ordemMaior)

maiorPalavra = ordemMaior[0]

if maiorPalavra == friend:
    palavraMaior = 'friend'
elif maiorPalavra == amico:
    palavraMaior = 'amico'
elif maiorPalavra == prijatelj:
    palavraMaior = 'prijatelj'
elif maiorPalavra == Freund:
    palavraMaior = 'Freund'
elif maiorPalavra == ven:
    palavraMaior = 'ven'
elif maiorPalavra == ystävä:
    palavraMaior = 'ystävä'
elif maiorPalavra == пријaтeљ:
    palavraMaior = 'пријaтeљ'
elif maiorPalavra == Mellon:
    palavraMaior = 'Mellon'
elif maiorPalavra == amigo:
    palavraMaior = 'amigo'
else: #Nesse caso a palavra mais repetida só pode ser 'barát'
    palavraMaior = 'barát'

ultimaLetra = len(palavraMaior) - 1
palavraInvertida = ''
vogais = 0

for i in range(0, (ultimaLetra + 1)):
    indice = ultimaLetra - i
    palavraInvertida += palavraMaior[indice]

    if palavraMaior[i] == 'a' or palavraMaior[i] == 'e' or palavraMaior[i] == 'i' or palavraMaior[i] == 'o' or palavraMaior[i] == 'u':
        vogais += 1

print(f'\nForam necessárias {tentativas} tentativas para pronunciar a palavra correta.\n')
print(f'A palavra que mais se repetiu foi {palavraMaior}, e ela na ordem invertida fica {palavraInvertida}.\n')
print(f'E, por fim, {palavraMaior} possui {vogais} vogais, desconsiderando possíveis vogais com alguma acentuação.')
