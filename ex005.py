while True:
    try:
        numero = int(input('Digite um número: '))
        print(f'Analisando o valor {numero}, seu antecessor é {numero - 1} e o sucessor é {numero + 1}')
        break
    except ValueError:
        print('Valor inválido. Por favor, digite apenas números inteiros.')
