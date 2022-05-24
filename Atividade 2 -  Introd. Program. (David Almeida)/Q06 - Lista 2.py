# IFPE - Campus Belo Jardim
# Questão 06 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

import random

aposta1 = aposta2 = aposta3 = aposta4 = aposta5 = aposta6 = 0
print('-' * 18)
print('    MEGA SENA       ')
print('-' * 18)
for i in range(1, 6):
    aposta1 = random.randint(1, 60)
    aposta2 = random.randint(1, 60)
    while aposta1 == aposta2:
        aposta2 = random.randint(1, 60)
    aposta3 = random.randint(1, 60)
    while (aposta3 == aposta1) or (aposta3 == aposta2):
        aposta3 = random.randint(1, 60)
    aposta4 = random.randint(1, 60)
    while (aposta4 == aposta1) or (aposta4 == aposta2) or (aposta4 == aposta3):
        aposta4 = random.randint(1, 60)
    aposta5 = random.randint(1, 60)
    while (aposta5 == aposta1) or (aposta5 == aposta2) or (aposta5 == aposta3) or (aposta5 == aposta4):
        aposta5 = random.randint(1, 60)
    aposta6 = random.randint(1, 60)
    while (aposta6 == aposta1) or (aposta6 == aposta2) or (aposta6 == aposta3) or (aposta6 == aposta4)\
            or (aposta6 == aposta5):
        aposta6 = random.randint(1, 60)
    if aposta1 < 10:
        print(f'0{aposta1}', aposta2, aposta3, aposta4, aposta5, aposta6)
    elif aposta2 < 10:
        print(aposta1, f'0{aposta2}', aposta3, aposta4, aposta5, aposta6)
    elif aposta3 < 10:
        print(aposta1, aposta2, f'0{aposta3}', aposta4, aposta5, aposta6)
    elif aposta4 < 10:
        print(aposta1, aposta2, aposta3, f'0{aposta4}', aposta5, aposta6)
    elif aposta5 < 10:
        print(aposta1, aposta2, aposta3, aposta4, f'0{aposta5}', aposta6)
    elif aposta6 < 10:
        print(aposta1, aposta2, aposta3, aposta4, aposta5, f'0{aposta6}')
    else:
        print(aposta1, aposta2, aposta3, aposta4, aposta5, aposta6)
print('-' * 18)
