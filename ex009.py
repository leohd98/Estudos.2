while True:
    try:
        numero = int(input('Digite um número para ver sua tabuada: '))
        valor = 1
        break
    except ValueError:
        print('Valor inválido. Por favor, digite apenas números inteiros.')

print('-' * 10)

while valor <= 10:
    print(f'{numero} x {valor} = {numero * valor}')
    valor += 1

print('-' * 10)
