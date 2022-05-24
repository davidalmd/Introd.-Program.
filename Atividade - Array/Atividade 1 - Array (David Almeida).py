nomeIdade = []
idadeNome = []
resp = '1'

while resp == '1':
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    if idade < 10:
        idade = str(idade)
        idade = '0' + idade
    else:
        idade = str(idade) 
    nomeIdade = nomeIdade + [nome + '-' + idade]
    idadeNome = idadeNome + [idade + '-' + nome]
    resp = input('Digite 1 para continuar...')

#Bolha para nomeIdade
trocou = True
fim = len(nomeIdade) - 1
while fim > 0 and trocou:
    trocou = False
    for b in range(0, fim):
        if nomeIdade[b] > nomeIdade[b + 1]:
            trocou = True
            temp = nomeIdade[b]
            nomeIdade[b] = nomeIdade[b + 1]
            nomeIdade[b + 1] = temp
    fim = fim - 1
#Fim da bolha para nomeIdade

#Bolha para idadeNome
trocou = True
fim = len(idadeNome) - 1
while fim > 0 and trocou:
    trocou = False
    for b in range(0, fim):
        if idadeNome[b] > idadeNome[b + 1]:
            trocou = True
            temp = idadeNome[b]
            idadeNome[b] = idadeNome[b + 1]
            idadeNome[b + 1] = temp
    fim = fim - 1
#Fim da bolha para idadeNome

print('\n\nLista ordenada por nome:')
print('--------------------------------')
for c in range(len(nomeIdade)):
    print(f'{nomeIdade[c]}')

print('\n\nLista ordenada por idade:')
print('--------------------------------')
for d in range(len(idadeNome)):
    print(f'{idadeNome[d]}')
