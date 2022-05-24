def fatorial(A):
    resultado = 1
    print(f'{A}! = ', end='')
    for c in range(A, 0, -1):
        resultado *= c
        if c == 1:
            print(f'{c} = ', end='')
        else:
            print(f'{c} x ', end='')
    print(resultado)

import random

for i in range(0, 4):
    valor = random.randint(1, 10)
    fatorial(valor)

