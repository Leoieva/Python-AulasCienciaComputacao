vlr_divida = int(input())
vlr_carteira = int(input()) 
contador_mespagamento = 0

while vlr_divida > 0:
    contador_mespagamento += 1
    print("pagamento:", contador_mespagamento)                   
    print("antes =",vlr_divida)
    vlr_divida = vlr_divida - vlr_carteira
    if vlr_divida < 0:
        print("depois =",0)    
        print("-----")
    else:  
        print("depois =",vlr_divida)    
        print("-----")
    
