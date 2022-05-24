# IFPE - Campus Belo Jardim
# Questão 04 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

idade = 0
f_velha = 0
m_novo = 0
nome_velha = ''
nome_novo = ''
resp = 's'
while True:
    sexo = input('Digite o sexo [m/f]: ')
    nome = input('Digite o nome: ')
    if m_novo == 0:
        idade = int(input('Digite a idade: '))
        if sexo == 'm':
            nome_novo = nome
            m_novo = idade
    else:
        idade = int(input('Digite a idade: '))

    if sexo == 'f' and idade > f_velha:
        nome_velha = nome
        f_velha = idade

    if sexo == 'm' and idade < m_novo:
        nome_novo = nome
        m_novo = idade

    resp = input('Deseja continuar? [s/n]\n')
    if resp == 'n':
        break

if f_velha == 0:
    print('Não tivemos mulheres cadastradas no sistema.')
else:
    print(f'A mulher mais velha se chama {nome_velha}, com {f_velha} anos.')

if m_novo == 0:
    print('Não tivemos homens cadastrados no sistema.')
else:
    print(f'O homem mais novo se chama {nome_novo}, com {m_novo} anos.')
