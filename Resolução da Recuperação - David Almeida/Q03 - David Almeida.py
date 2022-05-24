altura = float(input('Digite sua altura (m): '))
sexo = input('Digite seu sexo [m/f]: ')

if sexo == 'f':
    peso = (62.1 * altura) - 44.7
    print(f'O peso ideal dessa pessoa é de {peso}Kg.')

elif sexo == 'm':
    peso = (72.2 * altura) - 58
    print(f'O peso ideal dessa pessoa é de {peso}Kg.')

else:
    print('Você digitou uma opção inválida.')
