valor = 0
resp = 1
while resp == 1:
    ingresso = int(input('Qual o tipo do ingresso?\n'
    '[1] Inteira\n'
    '[2] Meia\n'))

    if ingresso == 1:
        valor += 30
    elif ingresso == 2:
        valor += 15
    else:
        print('Você digitou uma opção de ingresso inválida.')
    resp = int(input('Você deseja...\n'
    '[1] Continuar\n'
    '[2] Encerrar o expediente\n'))

print(f'O valor total acumulado da venda de ingressos neste dia foi de R${valor:.2f}')
