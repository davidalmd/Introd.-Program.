n = int(input('Digite a quantidade de termos do somatório: '))

sinal = 1
numerador = 0
denominador = 0
S = 0

print('S = ', end='')

for c in range(0, n):
    numerador = numerador + 2
    denominador = numerador + 1
    if sinal >= 1 and sinal <=3:
        print(' +', numerador, '/', denominador, end='')
        sinal = sinal + 1
        S = S + (numerador/denominador)
    elif sinal >= 4 and sinal <= 6:
        print(' -', numerador, '/', denominador, end='')
        sinal = sinal + 1
        S = S - (numerador/denominador)
    else:
        print(' -', numerador, '/', denominador, end='')
        sinal = 1
        S = S - (numerador/denominador)

print(f'\nS = {S}')
