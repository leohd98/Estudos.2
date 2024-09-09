frase = str(input('Digite uma frase: ')).strip().lower()
contador = frase.count('a')
primeiro = frase.find('a') + 1
ultimo = frase.rfind('a') + 1

print(f'A letra "A" aparece {contador} vezes na frase.')
print(f'A primeira letra "A" apareceu na posição {primeiro}.')
print(f'A última letra "A" apareceu na posição {ultimo}')