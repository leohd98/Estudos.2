largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
litros_tinta = 0

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')

while area >= 2:
    area = area - 2
    litros_tinta += 1

produto = area / 2
litros_tinta = litros_tinta + produto

print(f'Para pintar essa parede, você precisará de {litros_tinta}l de tinta.')




# correcao - o meu cálculo foi desnecessariamente complexo.
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')