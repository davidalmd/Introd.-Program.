preço = 0
valor = float(input('Qual o valor da compra? '))
pagamento = int(input('[1] À vista\n'
                                     '[2] Em 30 dias\n'
                                     '[3] Em 60 dias\n'))

if pagamento == 1:
    desconto = (5/100) * valor
    preço = valor - desconto
    print(f'O valor a ser pago será R${preço}')

elif pagamento == 2:
    preço = valor
    print(f'O valor a ser pago será R${preço}')

elif pagamento == 3:
    preço = 1.15 * valor
    print(f'O valor a ser pago será R${preço}')

else:
    print('Você digitou uma opção inválida.')
