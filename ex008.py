distancia = float(input('Uma distância em metros: '))
print(f'A medida de {distancia}m corresponde a')
km = distancia * 0.001
print(f'{km}km')
hm = distancia * 0.01
print(f'{hm}hm')
dam = distancia * 0.1
print(f'{dam:.1f}dam') #
dm = distancia * 10
print(f'{dm:.0f}dm') #
cm = distancia * 100
print(f'{cm:.0f}cm') #
mm = distancia * 1000
print(f'{mm:.0f}mm') #
