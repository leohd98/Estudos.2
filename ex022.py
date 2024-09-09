nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')

maiusculo = nome.upper()
print(f'Seu nome em maiúsculas é {maiusculo}')
minusculo = nome.lower()
print(f'Seu nome em minúsculas é {minusculo}')
semespaco = nome.replace(" ", "")
numero_de_letras = len(semespaco)
print(f'Seu nome tem ao todo {numero_de_letras} letras')
primeira_palavra = nome.split()[0]
numero_de_letras_1p = len(primeira_palavra)
print(f'Seu primeiro nome é {primeira_palavra} e ele tem {numero_de_letras_1p} letras')
