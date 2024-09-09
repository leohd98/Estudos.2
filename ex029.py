velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = velocidade - 80
    multa = multa * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/f \n Você deve pagar uma multa de R${multa:.2f}! \n Tenha um bom dia! Dirija com segurança!')
