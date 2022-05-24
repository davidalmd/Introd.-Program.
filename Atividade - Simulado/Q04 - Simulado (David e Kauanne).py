# IFPE - Campus Belo Jardim
# Questão 04 do Simulado
# Alunos: David e Kauanne

import random
import time

km_azul = 0 
km_branco = 0 
pontos_azul = 0 
pontos_branco = 0

for c in range(1, 6):
    time.sleep(1)
    distancia_km = random.randint(300, 1000)
    print(f'A distância da {c}ª corrida será de {distancia_km}Km.')
    time.sleep(1)
    distancia_ms = distancia_km/3.6
    azul_ms = 240/3.6 
    branco_ms = 200/3.6 
    corrida_azul = 0 
    corrida_branco = 0
    km = 0 

    while True:
        km += 1

        if km_branco < 10:
            km_branco += 1
            corrida_branco += branco_ms/10
        else:
            corrida_branco += branco_ms
        
        if km_azul < 6:
            km_azul += 1
            corrida_azul += azul_ms/6
        else:
            corrida_azul += azul_ms
        
        if km == 50:
            km_branco = 0
        
        if km == 30:
            km_azul = 0
        
        if corrida_branco >= distancia_ms:
            pontos_branco += 1
            print(f'O carro branco ganhou a {c}ª corrida.\n')
            break

        if corrida_azul >= distancia_ms:
            pontos_azul += 1
            print(f'O carro azul ganhou a {c}ª corrida.\n')
            break

time.sleep(1)
print(f'O azul ganhou {pontos_azul} vezes.')
time.sleep(1)
print(f'O branco ganhou {pontos_branco} vezes.\n')

time.sleep(1)
if (pontos_branco > pontos_azul):
    print('O carro branco foi o vencedor do campeonato!')
else:
    print('O carro azul foi o vencedor do campeonato!')
