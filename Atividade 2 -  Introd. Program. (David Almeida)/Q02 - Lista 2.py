# IFPE - Campus Belo Jardim
# Questão 02 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

base = int(input('Digite a base da nossa potência: '))
exp = int(input('Digite o expoente da nossa potência: '))

if exp == 0:
    print(f'O resultado da potência é 1.')
elif exp == 1:
    print(f'O resultado da potência é {base}.')
elif exp == -1:
    print(f'O resultado da potência é 1/{base} ou {1/base}.')
else:
    valor = base
    for c in range(2, abs(exp) + 1):
        valor = valor * base

    if (exp < 0) and (exp != -1):
        print(f'O resultado da potência é 1/{valor} ou {1/valor}')
    else:
        print(f'O resultado da potência é {valor}.')
