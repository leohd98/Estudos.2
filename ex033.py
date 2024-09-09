v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

if v1 < v2 and v1 < v3:
    menor = v1
elif v2 < v1 and v2 < v3: 
    menor = v2
else:
    menor = v3

if v1 > v2 and v1 > v3:
    maior = v1
elif v2 > v1 and v2 > v3: 
    maior = v2
else:
    maior = v3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')