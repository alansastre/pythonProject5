# Ejemplo JavaScript
# if(50 > 10){
#
# }

check1 = 50 > 10
check2 = 20 < 100
check3 = 50 >= 50

# Estructura if
if check1 or check2:
    print("Verdadero")
    print("Verdadero2")

if check1 or (check2 and check3):
    print("Verdadero")
    print("Verdadero2")

if 5 < 10 < 20:
    print("Verdadero")

# Estructura if-else
if check1:
    print("Verdadero")
else:
    print("Falso")

# Estructura elif

if check1 or check2:
    print("Verdadero")
elif check3:
    print("Verdadero2")

# Estructura if-elif-else


if check1 or check2:
    print("Verdadero")
elif check3:
    print("Verdadero2")
else:
    print("Esto se ejecuta si no se cumple ninguna condición")

check4 = 4 > 9
# Equivalente a switch
if check1:
    print("")
elif check2:
    print("")
elif check3:
    print("")
elif check4:
    print("")
else:
    print("else")

# OPCIONAL
# if en una línea

if check1: print('Hola')

# if else en una línea:
num1 = 40
num2 = 10
print("Verdadero") if num1 > num2 else print("Falso")

# Anidadas

if check1:
    if num1 > num2:
        print('Hello')
        if num2 > num1:
            print('')
    if num2 < num1:
        print('')

if check1:
    pass

print('Prueba pass')

print('Hola soy Evaristo')