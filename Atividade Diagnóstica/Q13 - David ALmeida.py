nome = input('Digite seu nome completo: ')
branco = cont = 0
primeiro = ultimo = ''

for i in range(len(nome)):
    letra = nome[i]
    if letra != ' ' and branco < 1:
        primeiro = primeiro + letra
    else:
        branco += 1
    
    if letra != ' ':
        cont += 1
    else:
        cont = 0
    
    if i == len(nome) - 1:
        cont2 = cont
        for c in range(cont):
            ultimo = ultimo + nome[len(nome) - cont2]
            cont2 -= 1

print(f'Primeiro nome lido: {primeiro}')
print(f'Último nome lido: {ultimo}')
