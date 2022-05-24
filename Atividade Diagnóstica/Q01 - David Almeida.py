print('-_' * 20)
print('Processo seletivo - Escola de Mutantes')
print('-_' * 20)
#obs.: considerei necessário uma média 6 para ser aprovado

print('\nPrimeira etapa - Prova de português')
nota1 = float(input('Qual a nota desse candidato? '))
if nota1 >= 8:
    print('Candidato avançou para a próxima etapa.')
    print()
    print('Segunda etapa - Prova de matemática')
    nota2 = float(input('Qual a nota desse candidato? '))
    if nota2 > 7:
        print('Candidato avançou para a próxima etapa.')
        print()
        print('Terceira etapa - Avaliação de poder')
        nota3 = int(input('Qual o nível de poder do candidato [0 a 10]? '))
        if nota3 == 10:
            print('Ômega.')
        else:
            tipo = input('O poder do candidato é do tipo Telepatia? [s/n]')
            if tipo == 's':
                media = (nota1 + nota2 + nota3 * 2) / (1 + 1 + 2)
            else:
                media = (nota1 + nota2 + nota3) / 3
            if media >= 6:
                print(f'O candidato foi aprovado e obteve média {media}.')
            else:
                print(f'A média do candidato foi de {media}.')
                print('O candidato foi desclassificado na terceira etapa.')

    else:
        print('Candidato foi desclassificado na segunda etapa.')
            
else:
    print('Candidato foi desclassificado na primeira etapa.')
