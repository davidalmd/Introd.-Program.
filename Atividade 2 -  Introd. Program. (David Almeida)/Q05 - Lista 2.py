# IFPE - Campus Belo Jardim
# Questão 05 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

import random

lucroT = 0
lucroM = 0
lucroC = 0
lucroO = 0
nMotos = 0
nCarros = 0
nOnibus = 0

for i in range(1, 401):
    automovel = random.randint(1, 3)
    # O 1 corresponderá aos ônibus, o 2 as motos e o 3 aos carros

    if automovel == 1:
        lucroO += +20
        lucroT += 20
        nOnibus += 1
    elif automovel == 2:
        lucroM += 4
        lucroT += 4
        nMotos += 1
    else:
        lucroC += 8
        lucroT += 8
        nCarros += 1

print(f'O número de Ônibus no estacionamento é de {nOnibus}, trazendo um lucro de R${lucroO}.\n'
      f'O número de Motos no estacionamento é de {nMotos}, trazendo um lucro de R${lucroM}.\n'
      f'O número de Carros no estacionamento é de {nCarros}, trazendo um lucro de R${lucroC}.\n'
      f'Logo, o lucro total do estacionamento foi de R${lucroT}.')
