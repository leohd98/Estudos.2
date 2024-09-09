numero = int(input('Digite um número: '))
milhar = 0
centena = 0
dezena = 0
unidade = 0
print(f'Analisando o número {numero}...')

while numero != 0:
    if numero >= 1000:
        numero = numero - 1000
        milhar += 1
    elif numero >= 100:
        numero = numero - 100
        centena += 1
    elif numero >= 10:
        numero = numero - 10
        dezena += 1
    elif numero >= 0:
        numero = numero - 1
        unidade += 1

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')