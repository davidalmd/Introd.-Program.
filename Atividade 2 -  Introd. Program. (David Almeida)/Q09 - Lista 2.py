# IFPE - Campus Belo Jardim
# Questão 09 da Atividade de Introdução a Programação
# Aluno: David Lucas Alves de Almeida

metal = driver = crash = warped = tekken = cortex = finalVIII = gran2 = finalVII = gran1 = 0

for c in range(1, 36):
    jogo = int(input('\nEscolha seu jogo preferido:\n'
                     '[1] Metal Gear Solid\n'
                     '[2] Driver\n'
                     '[3] Crash Bandicoot\n'
                     '[4] Warped\n'
                     '[5] Tekken 3\n'
                     '[6] Cortex Strikes Back\n'
                     '[7] Final Fantasy VIII\n'
                     '[8] Gran Turismo 2\n'
                     '[9] Final Fantasy VII\n'
                     '[10] Gran Turismo\n'))
    if jogo == 1:
        metal += 1
    elif jogo == 2:
        driver += 1
    elif jogo == 3:
        crash += 1
    elif jogo == 4:
        warped += 1
    elif jogo == 5:
        tekken += 1
    elif jogo == 6:
        cortex += 1
    elif jogo == 7:
        finalVIII += 1
    elif jogo == 8:
        gran2 += 1
    elif jogo == 9:
        finalVII += 1
    elif jogo == 10:
        gran1 += 1
    else:
        print('Você digitou uma opção inválida!\n')

if metal > driver and metal > crash and metal > warped and metal > tekken and metal > cortex and metal > finalVIII and \
        metal > gran2 and metal > finalVII and metal > gran1:
    print('Metal Gear Solid foi escolhido como o jogo preferido da turma!')
elif driver > metal and driver > crash and driver > warped and driver > tekken and driver > cortex and driver > finalVIII\
        and driver > gran2 and driver > finalVII and driver > gran1:
    print('Driver foi escolhido como o jogo preferido da turma!')
elif crash > metal and crash > driver and crash > warped and crash > tekken and crash > cortex and crash > finalVIII and \
        crash > gran2 and crash > finalVII and crash > gran1:
    print('Crash Bandicoot foi escolhido como o jogo preferido da turma!')
elif warped > metal and warped > driver and warped > crash and warped > tekken and warped > cortex and warped > finalVIII\
        and warped > gran2 and warped > finalVII and warped > gran1:
    print('Warped foi escolhido como o jogo preferido da turma!')
elif tekken > metal and tekken > driver and tekken > crash and tekken > warped and tekken > cortex and tekken > finalVIII\
        and tekken > gran2 and tekken > finalVII and tekken > gran1:
    print('Tekken 3 foi escolhido como o jogo preferido da turma!')
elif cortex > metal and cortex > driver and cortex > crash and cortex > warped and cortex > tekken and cortex > finalVIII\
        and cortex > gran2 and cortex > finalVII and cortex > gran1:
    print('Cortex Strikes Back foi escolhido como o jogo preferido da turma!')
elif finalVIII > metal and finalVIII > driver and finalVIII > crash and finalVIII > warped and finalVIII > tekken\
        and finalVIII > cortex and finalVIII > gran2 and finalVIII > finalVII and finalVIII > gran1:
    print('Final Fantasy VIII foi escolhido como o jogo preferido da turma!')
elif gran2 > metal and gran2 > driver and gran2 > crash and gran2 > warped and gran2 > tekken\
        and gran2 > cortex and gran2 > finalVIII and gran2 > finalVII and gran2 > gran1:
    print('Gran Turismo 2 foi escolhido como o jogo preferido da turma!')
elif finalVII > metal and finalVII > driver and finalVII > crash and finalVII > warped and finalVII > tekken\
        and finalVII > cortex and finalVII > finalVIII and finalVII > gran2 and finalVII > gran1:
    print('Final Fantasy VII foi escolhido como o jogo preferido da turma!')
elif gran1 > metal and gran1 > driver and gran1 > crash and gran1 > warped and gran1 > tekken\
        and gran1 > cortex and gran1 > finalVIII and gran1 > gran2 and gran1 > finalVII:
    print('Gran Turismo foi escolhido como o jogo preferido da turma!')
else:
    print('Tivemos um empate entre os jogos!')
