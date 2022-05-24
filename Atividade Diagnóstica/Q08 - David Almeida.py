numerador = 1
denominador = 2

for c in range(1, 31):
    if c == 30:
        print(f'{numerador}/{denominador}')
    else:
        print(f'{numerador}/{denominador} + ', end='')
    
    numerador += 1
    denominador += 2

    