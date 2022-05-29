mes_user = int(input("Em que mês estamos?\nR: "))
frete_padrao = ("O frete é de R$10,00")
frete_maio = ("Para o mês de maio temos frete gratuito")
black_friday = ("Mês da Black Friday! A cada 10 unidades, você recebe mais 2 unidades de graça!")


if mes_user >= 6 and mes_user <= 9:
    print("O produto do momento é foundue.\nValor: R$12,50 por unidade")
else:
    print("O produto do momento é sorvete.\nValor: R$7,99 unidade")

if mes_user == 2 or mes_user == 3:
    print("Olha só! Época de folia! Em comemoração ao carnaval, você tem um desconto de 5% no final da compra!")  

local_user = input("De que forma é possível te atender? (Presencial ou APP)\nR: ").lower()

if local_user == "app":
    app_user = input("Em que região você se encontra?\nR: ").lower()
    if app_user == "zona norte" or app_user == "centro":
        qtd_user = int(input("Quantidade\nR: "))
    else:
        print("Desculpe! Apenas as unidades da Zona Norte e Centro estão em funcionamento.\nAs demais estão em reforma e não será possível atender este pedido!") 
        quit()   
elif local_user == "presencial":
    qtd_user = int(input("Quantidade\nR: "))

if mes_user == 5:
    print(frete_maio)
elif mes_user != 5:
    print(frete_padrao)
elif mes_user == 11:
    print(black_friday)

if mes_user >= 6 and mes_user <= 9:
    print("Produto escolhido: Fondue")
    valor_total = qtd_user * 12.50
else:
    print("Produto escolhido: Sorvete")
    valor_total = qtd_user * 7.99

print("Quantidade:",qtd_user) 
    
if mes_user == 5:
    print("Valor Total: R$",valor_total)
    print("Você participou do: Frete Gratuito!")
elif mes_user == 2 or mes_user == 3:
    print("Valor total: R$",(valor_total - 5 / 100) + 10)
elif mes_user != 5 and mes_user != 11:
    print("Valor Total: R$",valor_total + 10)
elif mes_user == 11:
    qtd_div10 = int(qtd_user / 10)
    qtd_produtobonus = qtd_div10 * 2
    qtd_user = qtd_user + qtd_produtobonus
    if qtd_div10 > 0:
        print("Valor Total: R$",valor_total)
        print(f"Você participou da Black Friday! Por isso, você está recebendo {qtd_produtobonus} complementamente grátis")
    







    