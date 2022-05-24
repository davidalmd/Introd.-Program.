# IFPE - Campus Belo Jardim
# Questão 10 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

sinal = 1
soma = 0
print('\nSomatório = ', end='')

for c in range(1, 51):
    if sinal == 1 or sinal == 2:
        soma -= c
        sinal += 1
        print(' - ', c, end='')
    elif sinal == 3:
        soma += c
        sinal += 1
        print(' + ', c, end='')
    else:
        soma += c
        sinal = 1
        print(' + ', c, end='')

print(f'\n\nSomatório = {soma}')
