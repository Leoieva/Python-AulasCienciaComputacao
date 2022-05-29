num_inicio = int(input())
num_termino = int(input())
contador_primos = 0
for numero in range(num_inicio, num_termino + 1):
    if numero > 1:
        for primo in range(2, numero):
            if (numero % primo) == 0:
                break
        else:
            print(numero)
            contador_primos += 1        
print("primos:", contador_primos)
