# IFPE - Campus Belo Jardim
# Questão 10 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 < num2:
    print(f'O menor número é {num1}')
elif num2 < num1:
    print(f'O menor número é {num2}')
else:
    print('Os dois números digitados são iguais.')
