nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
primeiro = nome[0]
ultimo  = nome[-1]
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro}')
print(f'Seu ultimo nome é {ultimo}')
