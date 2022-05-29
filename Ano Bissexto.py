ano_inicio = int(input())
ano_termino = int(input())
contador_bissexto = 0
for cada_ano in range(ano_inicio,ano_termino+1):
    if ((cada_ano % 4 == 0) and not(cada_ano % 100 == 0) or (cada_ano % 400 == 0)):
        print(cada_ano)
        contador_bissexto += 1
    continue
print("bissextos:", contador_bissexto)  