def calcular_propina(total_cuenta):
    propina1 = total_cuenta * 0.18
    total1 = total_cuenta + propina1

    propina2 = total_cuenta * 0.20
    total2 = total_cuenta + propina2

    propina3 = total_cuenta * 0.25
    total3 = total_cuenta + propina3

    return propina1, total1, propina2, total2, propina3, total3

total_cuenta = float(input("Ingresar el total de la cuenta: $"))
propina1, total1, propina2, total2, propina3, total3 = calcular_propina(total_cuenta)

print(f"Con la propina del 18% es de ${propina1:.2f}, en total sería ${total2:.2f}.")
print(f"Con la propina del 20% es de ${propina2:.2f}, en total sería ${total2:.2f}.")
print(f"Con la propina del 25% es de ${propina3:.2f}, en total sería ${total3:.2f}.")