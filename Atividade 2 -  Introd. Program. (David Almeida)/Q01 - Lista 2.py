# IFPE - Campus Belo Jardim
# Questão 01 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

import random
corredores = []
maior = 0
empate = False

for c in range(0, 6):
    corredores.append(random.randint(1, 12))
    if c == 0:
        maior = corredores[c]
    elif maior == corredores[c]:
        empate = True
    elif maior < corredores[c]:
        maior = corredores[c]
        empate = False

print(f'As velocidades atingidas pelos corredores foram:\n'
      f'Jesse Quick -> {corredores[0]} flash(s) ou {corredores[0] * 300000} Km/s\n'
      f'Barry Allen -> {corredores[1]} flash(s) ou {corredores[1] * 300000} Km/s\n'
      f'Wally West -> {corredores[2]} flash(s) ou {corredores[2] * 300000} Km/s\n'
      f'Dr. Wells -> {corredores[3]} flash(s) ou {corredores[3] * 300000} Km/s\n'
      f'Jay Garrick -> {corredores[4]} flash(s) ou {corredores[4] * 300000} Km/s\n'
      f'Max Mercury -> {corredores[5]} flash(s) ou {corredores[5] * 300000} Km/s\n')

if empate:
    print(f'Tivemos um empate!')
elif maior == corredores[0]:
    print(f'O vencedor da corrida foi Jesse Quick!')
elif maior == corredores[1]:
    print(f'O vencedor da corrida foi Barry Allen!')
elif maior == corredores[2]:
    print(f'O vencedor da corrida foi Wally West!')
elif maior == corredores[3]:
    print(f'O vencedor da corrida foi Dr. Wells!')
elif maior == corredores[4]:
    print(f'O vencedor da corrida foi Jay Garrick!')
elif maior == corredores[5]:
    print(f'O vencedor da corrida foi Max Mercury!')
