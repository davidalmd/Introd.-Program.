homens = 0
media = 0
cont = 0

for c in range(0, 5):
    print('=' * 25)
    sexo =  str(input('Qual é o seu sexo:[m/f] '))
    altura = float(input('Digite a sua altura (m): '))
    if c == 0:
        maior_altura = altura
        menor_altura = altura

    if sexo == 'm' :
        homens += 1
    
    if sexo=='f':
        media += altura
        cont += 1
   
    if  maior_altura <=  altura:
        maior_altura = altura
    
    if menor_altura >= altura:
        menor_altura = altura
        
print('=' * 25)
print('Maior altura:{}'.format(maior_altura))
print('Menor altura:{}'.format(menor_altura))
print('O numero total de homens:{}'.format(homens))
print(f'A média de altura das mulheres é de {media/cont}')
print('=' * 25)
