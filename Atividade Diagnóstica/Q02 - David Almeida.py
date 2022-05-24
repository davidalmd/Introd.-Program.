tempo = 0
teste1 = input('Chico foi caminhando descalço? [s/n]')
if teste1 == 's':
    tempo += 50
else:
    teste2 = input('Chico foi caminhando de botina? [s/n]')
    if teste2 == 's':
        tempo += 40
    else:
        teste3 = input('Chico foi montado no Teobaldo? [s/n]')
        tempo += 30

teste4 = input('Chico parou no riacho? [s/n]')
if teste4 == 's':
    tempo += 40

teste5 = input('Chico saiu sem tomar café da manhã? [s/n]')
if teste5 == 's':
    tempo += 20

teste6 = input('Chico se encontrou com Rosinha? [s/n]')
if teste6 == 's':
    trocas = int(input('Quantas "trocas de ptialina" eles realizaram? [Digite 0 para nenhuma]'))
    tempo += (10 * trocas)

teste7 = input('Chico foi surpreendido pela onça? [s/n]')
if teste7 == 's':
    tempo -= 30

print(f'Chico gastou {tempo}min (ou {(tempo / 60):.2f}h) para chegar na escola.')
