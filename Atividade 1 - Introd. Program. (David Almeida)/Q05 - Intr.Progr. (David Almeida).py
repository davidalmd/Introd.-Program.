# IFPE - Campus Belo Jardim
# Questão 05 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

print('Estamos em época de eleição na Aldeia da Folha\n'
      'O poder está em suas mãos, me diga:')
naruto = int(input('Quantos votos o Naruto Uzumaki recebeu? '))
sakura = int(input('Quantos votos a Sakura Haruno recebeu? '))
shino = int(input('Quantos votos o Shino Aburame recebeu? '))
nulo = int(input('Quantos votos foram brancos/nulos? '))

if (sakura + shino + naruto) > nulo:
    if (naruto > sakura) and (naruto > shino):
        print(f'O Naruto Uzumaki, com {naruto} votos, é eleito o Sexto Hokage da Aldeia da Folha!')
    elif (sakura > naruto) and (sakura > shino):
        print(f'A Sakura Haruno, com {sakura} votos, é eleita o Sexto Hokage da Aldeia da Folha!')
    elif (shino > naruto) and (shino > sakura):
        print(f'O Shino Aburame, com {shino} votos, é eleito o Sexto Hokage da Aldeia da Folha!')
    else:
        print(f'Tivemos um empate nas eleições para o Sexto Hokage da Aldeia da Folha!')
else:
    print(f'A quantidade dos votos nos candidatos ({sakura + shino + naruto}) não foi maior que a quantidade de votos '
          f'nulos ({nulo}).')
    print('Com isso, a eleição foi invalidada!')
