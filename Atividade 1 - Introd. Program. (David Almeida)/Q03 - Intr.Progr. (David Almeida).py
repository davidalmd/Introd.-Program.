# IFPE - Campus Belo Jardim
# Questão 03 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

print('O Batman precisa chegar em Gotham City, qual dos carros da locadora DC Comics ele escolherá?')
carro = int(input('[1] Morcego Preto | [2] Vampiro Voador'))

if carro == 1:
    custo = ((295 / 16) * 0.75) + 300
    print('Com o carro "Morcego Preto", o Sr. Wayne gastou R$', custo, 'na viagem de Metrópolis para Gotham City.')

if carro == 2:
    custo = ((295 / 11) * 0.75) + 500
    print('Com o carro "Vampiro Voador", o Sr. Wayne gastou R$', custo, 'na viagem de Metrópolis para Gotham City.')
