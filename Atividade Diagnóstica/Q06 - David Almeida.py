invalidos = 0
n1 = int(input('Digite um número: '))
if n1 < 0 or n1 > 60:
    print('Esse número seria inválido.')
    invalidos += 1

n2 = int(input('Digite um número: '))
if n2 < 0 or n2 > 60 or n2 == n1:
    print('Esse número seria inválido.')
    invalidos += 1

n3 = int(input('Digite um número: '))
if n3 < 0 or n3 > 60 or n3 == n1 or n3 == n2:
    print('Esse número seria inválido.')
    invalidos += 1

n4 = int(input('Digite um número: '))
if n4 < 0 or n4 > 60 or n4 == n1 or n4 == n2 or n4 == n3:
    print('Esse número seria inválido.')
    invalidos += 1

n5 = int(input('Digite um número: '))
if n5 < 0 or n5 > 60 or n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
    print('Esse número seria inválido.')
    invalidos += 1

n6 = int(input('Digite um número: '))
if n6 < 0 or n6 > 60 or n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
    print('Esse número seria inválido.')
    invalidos += 1

print(f'A sequência da mega-sena seria: {n1}|{n2}|{n3}|{n4}|{n5}|{n6}')
print(f'Temos um total de {invalidos} números inválidos.')
