preco = float(input('Qual é o preço do produto? R$'))
porcento = int(input('Qual é a porcentagem? '))

desconto = preco - ((preco * porcento) / 100)

print(f'O produto que custava R${preco}, na promoção com desconto de {porcento}% vai custar R${desconto:.2f}.')

# calculo de porcentagem =  valor inicial - (valor x porcentagem / 100)