import random

maior = 0
menor = 11
aprovados = 0
recuperação = 0
reprovados = 0
media = 0

for c in range(1, 41):
    nota = random.randint(0, 10)
    media += nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
        #freq = float(input('Qual a frequência (%) deste aluno? '))# Forma manual
        freq = random.randint(0, 100)
    if nota >= 7 and freq >= 70:
        aprovados += 1
    elif nota < 4 or freq < 70:
        reprovados += 1
    else:
        recuperação += 1

print(f'Tivemos {aprovados} alunos aprovados na turma.')
print(f'Tivemos {reprovados} alunos reprovados na turma.')
print(f'Tivemos {recuperação} alunos em recuperação na turma.')
print(f'A maior nota da sala foi {maior}.')
print(f'A menor nota da sala foi {menor}.')
print(f'A média da turma foi {media / 40}.')
