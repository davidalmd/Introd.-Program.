n = int(input('Digite um número inteiro: '))
rang = n
fatorial = 1

for c in range (0, rang):
    if c == 0:
        print(n,'! = ', n, end='')
    elif c == rang - 1:
        print(' x', n, '= ', end='')
    else:
        print(' x', n, end='')
    fatorial *= n
    n -= 1
print(fatorial)
