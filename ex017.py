from math import sqrt

cateto1 = float(input('Comprimento do cateto oposto: '))
cateto2 = float(input('Comprimento do cateto adjacente: '))

resultado = (cateto1**2) + (cateto2**2)
resultado = sqrt(resultado)

print(f'A hipotenusa vai medir {resultado:.2f}')