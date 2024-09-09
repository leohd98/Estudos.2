from random import randint
random = randint(0,5)
print('\033[36m-----=-----=-----=-----=-----=-----=-----=-----=-----=-----=-----')
print('\033[31mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[36m-----=-----=-----=-----=-----=-----=-----=-----=-----=-----=-----')
numero = int(input('\033[37mEm que número eu pensei? '))
print('PROCESSANDO...')
if numero == random:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {random} e não no {numero}!')