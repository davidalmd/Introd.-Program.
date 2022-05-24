F = 50
print('----------')
print('F  |  C  ')
print('----------')
for c in range(50, 151):
    C = (5/9) * (F - 32)
    print(f'{F} = {C:.2f}')
    F += 1
