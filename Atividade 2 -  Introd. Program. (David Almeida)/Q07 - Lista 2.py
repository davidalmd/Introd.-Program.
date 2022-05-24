# IFPE - Campus Belo Jardim
# Questão 07 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

passou = 0
reprovou = 0

print('Chegamos ao fim do semestre. Vamos ver quem passou e quem reprovou!')

for c in range(1, 21):
    nota = float(input(f'Qual foi a média do {c}º aluno(a)? '))
    if nota >= 7:
        print('Parabéns, aprovado!')
        passou += 1
    else:
        print('Que pena, reprovado!')
        reprovou += 1

print(f'Dos 20 alunos, {passou} alunos passaram acima da média, enquanto {reprovou} alunos foram reprovados...')
