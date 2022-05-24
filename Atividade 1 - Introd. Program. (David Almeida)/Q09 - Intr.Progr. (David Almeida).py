# IFPE - Campus Belo Jardim
# Questão 09 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

print('~' * 33)
print('Vamos descobrir o estado da água')
print('~' * 33)

temp = float(input('Informe a temperatura da água: '))
if temp < 0:
    print('A água está no seu estado sólido.')
elif temp > 100:
    print('A água está no seu estado gasoso.')
else:
    print('A água está no seu estado líquido.')
