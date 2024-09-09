s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 > s2 and s1 > s3:
    maior = s1
elif s2 > s1 and s2 > s3:
    maior = s2
else:
    maior = s3

if maior == s1:
    if s1 > s2 + s3:
        print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
    else:
        print('Os segmentos acima PODEM FORMAR triângulo.')
elif maior == s2:
    if s2 > s1 + s3:
        print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
    else:
        print('Os segmentos acima PODEM FORMAR triângulo.')
else:
    if s3 > s1 + s2:
        print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
    else:
        print('Os segmentos acima PODEM FORMAR triângulo.')