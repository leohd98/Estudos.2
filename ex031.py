distancia = int(input('Qual é a distância da sua viagem? '))
if distancia < 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
print(f'E o preço da sua passagem será de R${valor:.2f}.')