import random

lucro = 0

for c in range (0, 5):
    print('Qual pacote de viagem é desejado? ')
    print('[1] - Casa branca (Washington)')
    print('[2] - Santuário de Fátima (Portugal)')
    escolha = int(input())
    moedaLocal = random.randint(1000, 10000)
    #Coloquei o teto do valor como 10.000 moedas locais

    if escolha == 1:
        reais = moedaLocal * 5.08
        lucro += reais
    
    if escolha == 2:
        reais = moedaLocal * 5.35
        lucro += reais

print(f'Nesses 30 dias, a agência arrecadou R${lucro:.2f}.')
