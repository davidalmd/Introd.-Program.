import random

repPORT = repMAT = mediaM = 0

for c in range (0, 20):
    nota1 = random.randint(0, 10)
    if nota1 > 7:
        nota2 = random.randint(0, 10)
        if nota2 > 8:
            nota3 = random.randint(0, 10)
            if nota3 > 8.5:
                media = (nota1 + nota2 + nota3) / 3
                if media > mediaM:
                    mediaM = media
        else:
            repMAT += 1
    else:
        repPORT += 1

print(f'Tivemos {repPORT} candidatos reprovados em português.')
print(f'Tivemos {repMAT} candidatos reprovados em matemática.')
print(f'O candidato selecionado para a vaga ficou com média {mediaM}.')
