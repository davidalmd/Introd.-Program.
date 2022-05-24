# IFPE - Campus Belo Jardim
# # Questão 08 da Atividade de Introdução a Programação
# # Aluno: David Lucas Alves de Almeida

print('~' * 47)
print('Vamos descobrir a área de uma figura geométrica')
print('~' * 47)
figura = int(input('Qual a figura geométrica que você deseja saber a área?\n'
                   '[1] Retângulo\n'
                   '[2] Triângulo\n'
                   '[3] Círculo\n'))
if figura == 1:
    a = int(input('Informe o valor da base do retângulo: '))
    b = int(input('Informe o valor da altura do retângulo: '))
    print(f'O valor da área desse retângulo é igual a {a * b}.')
elif figura == 2:
    b = int(input('Informe o valor da base do triângulo: '))
    h = int(input('Informe o valor da altura do triângulo: '))
    print(f'O valor da área desse triângulo é igual a {(b * h) / 2}.')
elif figura == 3:
    r = int(input('Informe o valor do raio do círculo: '))
    print(f'O valor da área desse círculo é igual a {3.14 * (r ** 2)}.')
else:
    print('Escolha uma das opções disponíveis de figuras geométricas!')
