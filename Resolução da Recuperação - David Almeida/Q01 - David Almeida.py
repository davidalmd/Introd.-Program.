contH = contM = mediaM = mediaH = idadeM = 0
resp = 's'

while resp == 's':
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo [m/f]: ')
    if sexo == 'm' and idade >= 18:
        mediaH += idade
        contH += 1
    
    elif sexo == 'f' and idade % 2 != 0:
        mediaM += idade
        contM += 1
    
    if idade % 2 == 0 and idade > idadeM:
        idadeM = idade
    
    resp = input('Digite s para continuar...')

print(f'A média de idade dos homens maiores de idade é {mediaH/contH}.')
print(f'A média de idade das mulheres com idade ímpar é {mediaM/contM}')
print(f'A maior idade par é {idadeM}')
