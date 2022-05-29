lista = input(' ').split(' ')
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

trian_retan = (A * C)/2
circulo_raio = (3.14159 * C ** 2)
trapezio = ((A + B) * C)/2
quadrado = (B ** 2)
retangulo = (A * B)

print (f'TRIANGULO: {trian_retan:.3f}')
print (f'CIRCULO: {circulo_raio:.3f}')
print (f'TRAPEZIO: {trapezio:.3f}')
print (f'QUADRADO: {quadrado:.3f}')
print (f'RETANGULO: {retangulo:.3f}')
