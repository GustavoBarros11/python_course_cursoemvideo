print('-='*20)
print('Analisador de Triangulos')
print('-='*20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

pode_tri = False

if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print('Os segmentos acima PODEM FORMAR triangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo!')