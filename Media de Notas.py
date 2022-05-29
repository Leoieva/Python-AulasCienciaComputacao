N1, N2, N3, N4 = input().split(' ') 

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
   
media1 = (((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1)) / 10)

if media1 >= 5.0 and media1 <= 6.9:
    notaexame = float(input())

    print(f"Media: {media1:.1f}")

    print("Aluno em exame.")

    print("Nota do exame:",notaexame)

    mediafinal = ((media1 + notaexame) / 2)

    if mediafinal >= 5.0:
        print("Aluno aprovado.")

    if mediafinal <= 4.9:
        print("Aluno reprovado.") 

    print(f"Media final: {mediafinal:.1f}")

if media1 >= 7.0:
    print(f"Media: {media1:.1f}")
    print("Aluno aprovado.")
    
if media1 < 5.0:
    print(f"Media: {media1:.1f}")  
    print("Aluno reprovado.")
      