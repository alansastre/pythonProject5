print('buenas tardes')

edad = int(input("¿Cuántos años tiene? "))
if edad >= 70:
    print("¡No me lo creo! intentálo de nuevo")
print(f"Usted dice que tine {edad} años.")

#else:
    #print("Adios")
#Intentar añadir otra condición, si tiene menos de <18 años print que No estas autorizado para continuar
#Ver si poner o no el pass
def saludar(nombre):
	def saludo(dia):
		if(dia):
			mensaje = "Buenos días "
		else:
			mensaje = "Buenas tardes "
		return  mensaje+ nombre+"!!"
	return saludo

saludoAlan = saludar("Alan")
saludoLeti = saludar("Leti")

print(saludoAlan(True))
print(saludoAlan(False))
print(saludoLeti(True))
print(saludoLeti(False))

''''
print(saludoPatry(True))

a = Alan
b = Alex
c = Ariel
D = Alba
E = AntonioAndres
F = Alvaro
G = Aroa
H = Emilio
I = EvaristoJ
J = Gerardo
K = Leti
L = Mariano
M = MiguelAngel
N = Patry
O = Javi
P = Dani
Q = Mario
S = Daniel
'''