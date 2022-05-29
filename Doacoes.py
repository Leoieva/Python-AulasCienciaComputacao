unit_doado = 0
total_doado = 0
conversao = 0

while True:
    unit_doado = float(input())
    if unit_doado == -1.0:
        break
    total_doado = total_doado + unit_doado
    conversao = total_doado * 2.50
print(f"VC$ {total_doado:.2f}")
print(f"R$ {conversao:.2f}")


