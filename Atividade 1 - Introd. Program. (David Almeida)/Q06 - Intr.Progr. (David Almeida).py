# IFPE - Campus Belo Jardim
# Questão 06 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

a = int(input('Informe o primeiro valor: '))
b = int(input('Informe o segundo valor: '))
c = int(input('Informe o terceiro valor: '))

if a ** 2 == b ** 2 + c ** 2:
    print(f'{a}² = {b}² + {c}²')
    print(f'{a ** 2} = {b ** 2} + {c ** 2}')
    print(f'{a ** 2} = {b ** 2 + c ** 2}')
    print('O teorema de pitágoras é válido para os valores apresentados, logo, esse seria um triângulo retângulo!')
elif b ** 2 == a ** 2 + c ** 2:
    print(f'{b}² = {a}² + {c}²')
    print(f'{b ** 2} = {a ** 2} + {c ** 2}')
    print(f'{b ** 2} = {a ** 2 + c ** 2}')
    print('O teorema de pitágoras é válido para os valores apresentados, logo, esse seria um triângulo retângulo!')
elif c ** 2 == a ** 2 + b ** 2:
    print(f'{c}² = {a}² + {b}²')
    print(f'{c ** 2} = {a ** 2} + {b ** 2}')
    print(f'{c ** 2} = {a ** 2 + b ** 2}')
    print('O teorema de pitágoras é válido para os valores apresentados, logo, esse seria um triângulo retângulo!')
else:
    print('Os valores informados não formam um triângulo retângulo!')
