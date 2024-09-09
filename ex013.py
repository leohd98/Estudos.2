salario = float(input('Qual é o salário do funcionário? R$'))
porcento = int(input('Escolha a porcentagem de aumento: '))

aumento = salario + ((salario * porcento) / 100)

print(f'Um funcionário que ganhava R${salario:.2f}, com {porcento}% de aumento, passa a receber R${aumento:.2f}.')
 