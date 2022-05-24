import random

consumo = random.randint(300, 700)
custo = consumo * 10

investimento = int(input('Quanto foi investido em termelétricas no mês? (%)\n'))
#Se o investimento for menor que 15%, bandeira vermelha - patamar 2. Se for menor 
#30% e maior ou igual a 15%, bandeira vermelha - patamar 1. Se for entre 30% e 
#70%, bandeira amarela. Se for maior que 70%, bandeira verde.

if investimento < 15:
    adicional = 5 * (consumo//100)
    bandeira = 'Vermelha - Patamar 2'

elif investimento < 30 and investimento >= 15:
    adicional = 3 * (consumo//100)
    bandeira = 'Vermelha - Patamar 1'

elif investimento < 70 and investimento >= 30:
    adicional = 1 * (consumo//100)
    bandeira = 'Amarela'

else:
    adicional = 0
    bandeira = 'Verde'

print(f'O consumo mensal foi de {consumo}kW/h, custando R${custo:.2f}.')
print(f'A bandeira tarifária estava na cor {bandeira}, tendo assim um acréscimo de R${adicional:.2f} na conta.')
print(f'Logo, o preço total da conta de energia desse mês foi de R${custo + adicional:.2f}.')
