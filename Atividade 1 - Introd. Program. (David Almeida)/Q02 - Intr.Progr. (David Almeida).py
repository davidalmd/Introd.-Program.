# IFPE - Campus Belo Jardim
# Questão 02 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

altura = float(input('Digite a sua altura em metros: '))
sexo = input('Qual o seu sexo? [f/m]\n')

if sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'O seu peso ideal é de {peso_ideal:.1f}Kg.')

if sexo == 'm':
    peso_ideal = (72.2 * altura) - 58
    print(f'O seu peso ideal é de {peso_ideal:.1f}Kg.')
