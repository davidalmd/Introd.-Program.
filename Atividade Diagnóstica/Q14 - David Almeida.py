resp = '1'
idade_velho = mediaM = cont = 0
homem_novo = homem_velho = ''
idade_novo = 9999999

while resp == '1':
    nome = input('Digite o nome: ')
    sexo = input('Digite o sexo [m/f]: ')
    idade = int(input('Digite a idade: '))

    if sexo == 'f' and idade >= 18:
        mediaM += idade
        cont += 1

    if sexo == 'm':
        if idade > idade_velho:
            idade_velho = idade
            homem_velho = nome
        
        if idade < idade_novo:
            idade_novo = idade
            homem_novo = nome
    
    resp = input('Digite 1 para continuar...\n')

print(f'A média de idade das mulheres maiores de idade é de {(mediaM/cont):.2f}.')
print(f'O homem mais novo se chama {homem_novo}, com {idade_novo} anos.')
print(f'O homem mais velho se chama {homem_velho}, com {idade_velho} anos.')
