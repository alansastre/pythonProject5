"""
Script de pruebas de sintaxis con python
"""
hola1()
variable1 = 5
variable2 = False
variable3 = 5.6

variable4, variable5 = 'Hola', 5  # pepe

# print(variable4)
print(variable5)
print(type(variable3))

texto1 = "hola q"
texto2 = 'adios'
texto3 = '''
        SELECT * FROM customers
        WHERE name like '%mike%'
        ORDER BY 
        LIMIT
        '''

check = texto1.startswith('h')
print(check)
longitud = len(texto1)
print(longitud)
lista = ['Alan', 'Sastre']
# print(len(lista))
nuevo_texto = texto1.replace(" ", "")
print(nuevo_texto)
print(len(nuevo_texto))

first_name = 'Alan'
last_name = 'Sastre'
print(first_name + ' ' + last_name)
welcome = 'Bienvenido/a {}'
print(welcome.format('Alan'))

# Tipos de datos
# Boolean

# Tipos numéricos
entero = 4
decimal = 4.7
complejo = 4 + 9j
print('Hola ' + str(5))

numero = None  # Declarar

division1 = 10 / 4
division2 = 10 // 4
print(division1)
print(division2)

if 5 == 5 and 9 > 8:
    print('hola')


