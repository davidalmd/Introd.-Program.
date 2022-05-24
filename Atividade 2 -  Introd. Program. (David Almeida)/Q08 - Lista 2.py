# IFPE - Campus Belo Jardim
# Questão 08 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

import random
import time

pontos = 0
trapaca = False

print('Está na hora de Loki lutar pelo posto de protetor de Asgard!\n')
time.sleep(2)

print('1ª BATALHA:\n'
      'Loki × Volstagg\n'
      'Disputa de comida!\n')
time.sleep(2)
loki = 0
volstagg = 0
while loki == volstagg:
    loki = random.randint(1, 100)
    volstagg = random.randint(1, 100)
print(f'Loki comeu {loki} Kg de comida.')
time.sleep(1)
print(f'Volstagg comeu {volstagg} Kg de comida.')
time.sleep(1)
if loki > volstagg:
    print('Loki venceu Volstagg!\n')
    pontos += 1
else:
    print('Loki foi derrotado por Volstagg!\n')
    trapaca = True
time.sleep(2)

print('2ª BATALHA:\n'
      'Loki × Frandral\n'
      'Disputa de Arco e Flecha!\n')
time.sleep(2)
loki = 0
frandral = 0
for i in range(1, 11):
    loki1 = random.randint(0, 60)
    loki += loki1
    frandral1 = random.randint(0, 60)
    frandral += frandral1
print(f'No total, os lançamentos de Loki ficaram a uma distância de {loki} do alvo.\n'
      f'No total, os lançamentos de Frandral ficaram a uma distância de {frandral} do alvo.')
if loki < frandral:
    print('Loki venceu Frandral!\n')
    pontos += 1
else:
    print('Loki foi derrotado por Frandral!\n')
    trapaca = True
time.sleep(2)

print('3ª BATALHA:\n'
      'Loki × Hogun\n'
      'Disputa de Polegares!\n')
loki = 0
hogun = 0
while loki == hogun:
    loki = random.randint(1, 100)
    hogun = random.randint(1, 100)
if loki > hogun:
    print('Loki venceu Hogun!\n')
    pontos += 1
else:
    print('Loki foi derrotado por Hogun!\n')
    trapaca = True
time.sleep(2)

print('4ª BATALHA:\n'
      'Loki × Valquíria\n'
      'Números aleatórios!\n')
n1 = 0
n2 = 1
resp = 0
time.sleep(2)

while n1 != n2:
    n1 = random.randint(1, 60)
    n2 = random.randint(1, 60)
    if resp == 0 and n1 == n2:
        print('Loki derrotou Valquíria!\n')
        pontos += 1
    if resp == 1 and n1 == n2:
        print('Loki foi derrotado pela Valquíria!\n')
        trapaca = True
    if resp == 0:
        resp = 1
    else:
        resp = 0
time.sleep(2)

print('5ª BATALHA:\n'
      'Loki × Lady Sif\n'
      'Par ou Impar!\n')
loki = 0
lady = 0

for c in range(1, 4):
    # Ataque de Loki
    loki1 = random.randint(1, 60)
    lady1 = random.randint(1, 60)
    if (loki1 % 2 == 0 and lady1 % 2 != 0) or (loki1 % 2 != 0 and lady1 % 2 == 0):
        loki += 1
    # Ataque de Loki
    loki1 = random.randint(1, 60)
    lady1 = random.randint(1, 60)
    if (loki1 % 2 == 0 and lady1 % 2 != 0) or (loki1 % 2 != 0 and lady1 % 2 == 0):
        lady += 1
time.sleep(1)

if loki > lady:
    print('Loki derrotou a Lady Sif!\n')
    pontos += 1
else:
    print('Loki foi derrotado pela Lady Sif!\n')
    trapaca = True
time.sleep(2)

print('~' * 80)
if trapaca:
    print('Loki usou uma de suas trapaças para ganhar um dos desafios que ele havia perdido!')
    pontos += 1
print('~' * 80)
time.sleep(2)
print()
print('~' * 80)
if pontos >= 3:
    print('Loki conseguiu vencer pelo menos 3 dos guerreiros e será o novo protetor!')
else:
    print('Loki não conseguiu vencer pelo menos 3 dos guerreiros e NÃO será o novo protetor!')
print('~' * 80)
