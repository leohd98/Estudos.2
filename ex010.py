import requests

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    usd_brl = data["USDBRL"]
    valor_1dolar = float(usd_brl['bid'])
else:
    print("Falha na requisição:", response.status_code)

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
resultado = dinheiro / valor_1dolar

print(f'Com R${dinheiro:.2f} você pode comprar US${resultado:.2f}')
