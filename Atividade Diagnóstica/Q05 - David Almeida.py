n = int(input('Digite um número: '))

if (n % 2 == 0) and (n % 3 == 0):
    print(f'{n} é múltiplo de 2 e 3 ao mesmo tempo.')
else:
    print(f'{n} NÃO é múltiplo de 2 e 3 ao mesmo tempo. ')
