nominados = ["Alba", "Antoni", "Aroa", "Dani"]

nominados[0] = nominados[0] + " Editado"
nominados[0] += " Editado"

print(nominados)

for nominado in nominados:
    print()

if "Alan" in nominados:
    print("Congratulations!")