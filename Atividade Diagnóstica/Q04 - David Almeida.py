import random

# Considerando que o senhor esquelético da questão é o esqueleto, vilão do He-man, logo uma pessoa com poderes especiais
# A força dele variará entre 40 e 70
esqueleto = random.randint(40,70)
print(f'A força do esqueleto é de {esqueleto}')

# Considerando que o senhor corcunda é uma pessoa normal com possíveis fraquezas
# A força dele variará entre 10 e 15 de força
corcunda = random.randint(10,15)
print(f'A força do senhor corcunda é de {corcunda}')

# Considerando que o homem de um braço só é uma pessoa normal  com possíveis fraquezas
# A força dele variará entre 15 e 18 de força
aparelho = random.randint(10,15)
print(f'A força do homem de um braço só é de {aparelho}')

# Considerando que a mulher de maiô roxo é a maligna, personagem de He-man, logo uma pessoa com poderes especiais
# A força dela variará entre 40 e 70
maligna = random.randint(40,70)
print(f'A força da maligna é de {maligna}')

# Como o importante é que a força puxando a porta seja maior que 120F, não consideraremos a força dos dois que estão
# tentando segurar ela, pois se for maior que 120F ela abrirá

força = esqueleto + corcunda + aparelho + maligna

if força > 120:
    print(f'A força total foi de {força} e eles conseguiram abrir a porta.')
else:
    print(f'A força total foi de {força} e eles NÃO conseguiram abrir a porta.')
