peso_sem = float(input('Qual o peso do caminhão sem carga? '))
peso_com = float(input('Qual o peso do caminhão com carga? '))
if peso_sem > peso_com:
    print('Não tem como o peso sem carga ser maior que o peso com carga.')
else:
    carga = peso_com - peso_sem

    if carga > peso_sem * 1.20:
        print(f'O valor que deverá ser pago é de R$20.00')
    elif carga > peso_sem * 1.10:
        print(f'O valor que deverá ser pago é de R$10.00')
    else:
        print(f'Não será preciso pagar nenhum valor.')
