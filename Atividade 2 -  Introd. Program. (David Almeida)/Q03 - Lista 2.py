# IFPE - Campus Belo Jardim
# Questão 03 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

import random

print('\nVamos descobrir a vibração dos novos três planetas Terra do Universo da DC\n')
planeta1, planeta2, planeta3 = 0, 0, 0

while True:
    if planeta1 == planeta2 or planeta1 == planeta3 or planeta2 == planeta3:
        planeta1 = random.randrange(1, 30)
        planeta2 = random.randrange(1, 30)
        planeta3 = random.randrange(1, 30)
    else:
        break

print(f'O Planeta Terra 1 terá vibração de {planeta1} vibro.')
print(f'O Planeta Terra 2 terá vibração de {planeta2} vibro.')
print(f'O Planeta Terra 3 terá vibração de {planeta3} vibro.')
