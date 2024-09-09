dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

valordias = 60 * dias
valorkm = 0.15 * km
total = valordias + valorkm

print(f'O total a pagar é de R${total:.2f}')