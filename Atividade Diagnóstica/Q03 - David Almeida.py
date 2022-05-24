import random

escolha = int(input('Você quer:\n'
                    '[1] Escolher a profissão sorteada\n'
                    '[2] Gerar aleatoriamente uma profissão sorteada\n'))

if escolha == 2:
    profissão = random.randint(1,7)
    if profissão == 1:
        salario = 50
        print('Médico')
    elif profissão == 2:
        salario = 24
        print('Jornalista')
    elif profissão == 3:
        salario = 50
        print('Advogado')
    elif profissão == 4:
        salario = 24
        print('Professor')
    elif profissão == 5:
        salario = 30
        print('Físico')
    elif profissão == 6:
        salario = 12
        print('Comerciante')
    elif profissão == 7:
        salario = 16
        print('Estudante')

elif escolha == 1:
    profissão = int(input('\nQual a profissão do jogador?\n'
                          '[1] Médico\n'
                          '[2] Jornalista\n'
                          '[3] Advogado\n'
                          '[4] Professor\n'
                          '[5] Físico\n'
                          '[6] Comerciante\n'
                          '[7] Estudante\n'))

if profissão == 1 or profissão == 3:
    salario = 50
elif profissão == 2 or profissão == 4:
    salario = 24
elif profissão == 5:
    salario = 30
elif profissão == 6:
    salario = 12
elif profissão == 7:
    salario = 16
else:
    print('Escolha inválida.')

caminho = input('Qual o caminho que o jogador escolheu? [A/B]')
if caminho == 'a' or caminho == 'A':
    montante = (20 * salario) + (10 * (salario / 2))
elif caminho == 'b' or caminho == 'B':
    montante = (20 * salario) + (5 * (salario / 2))

print(f'No fim do jogo, esse jogador acumulou um montante de R${montante:.2f}')
