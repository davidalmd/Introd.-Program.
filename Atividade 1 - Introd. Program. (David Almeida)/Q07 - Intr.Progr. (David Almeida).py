# IFPE - Campus Belo Jardim
# Questão 07 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Com os valores informados é possível formar um triângulo.')
    if a == b == c:
        print('Esse triângulo seria equilátero.')
    elif a != b != c:
        print('Esse triângulo seria escaleno.')
    else:
        print('Esse triângulo seria isósceles.')
else:
    print('Com os valores informados, não é possível que se forme um triângulo.')
