from random import sample

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]

nome_escolhido = sample(lista, k=1)[0]  # Acessa o primeiro elemento da lista retornada por random.sample()

print(nome_escolhido)