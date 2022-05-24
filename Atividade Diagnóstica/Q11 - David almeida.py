homens = 0
for c in range(0, 2):
    print('=' * 25)
    sexo =  str(input('Qual é o seu sexo:[M/F]'))
    altura = float(input('Digite a sua altura:'))
    if c == 0:
        maior_altura = altura
        menor_altura = altura

    if sexo == 'm' :
        homens += 1
   
    if  maior_altura <=  altura:
        maior_altura = altura
    
    if menor_altura >= altura:
        menor_altura = altura
        
print('=' * 25)
print('Maior altura:{}'.format(maior_altura))
print('Menor altura:{}'.format(menor_altura))
print('O numero total de homens:{}'.format(homens))
print('=' * 25)