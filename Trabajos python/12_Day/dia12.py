##1
import random
import string

def random_user():
    characters = string.ascii_letters + string.digits 
    user_id = str(''.join(random.choice(characters) for _ in range(6))) 
    return user_id

print(random_user()) 

##2
def random_user_id():
    try:
        char = int(input('Enter the number of characters for the user ID: '))
        user = int(input('Enter the number of user IDs to generate: '))
        for i in range(user):
            user_id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(char))
            print(user_id)
    except ValueError:
        print("Please enter valid integers for both inputs.")
random_user_id()

##3
def rgb():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return r,g,b
print(rgb())

##ejercicios nivel 2

##1
def generar_colores_hex():
    for _ in range(6):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print(color)
    print()

generar_colores_hex()

 ##2
def crear_lista_rgb():
    try:
        cantidad = int(input('¿Cuántos colores RGB quieres crear?: '))
        lista_colores = []
        for _ in range(cantidad):
            rojo = random.randint(0, 255)
            verde = random.randint(0, 255)
            azul = random.randint(0, 255)
            lista_colores.append((rojo, verde, azul))
        print(lista_colores)
    except ValueError:
        print("Debes ingresar un número entero válido.")
    print()

crear_lista_rgb()

##3
def crear_colores():
    try:
        tipo = input('¿Qué tipo de color deseas (RGB o HEX)?: ').strip().upper()
        cantidad = int(input('¿Cuántos colores quieres generar?: '))
        resultado = []

        for _ in range(cantidad):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            if tipo == 'RGB':
                resultado.append((r, g, b))
            else:
                color_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                resultado.append(color_hex)

        print(resultado)
    except ValueError:
        print("Por favor ingresa un número válido.")
    print()

crear_colores()

##ejercicios nivel 3

##1
def mezclar_elementos():
    elementos = ['Papa', 'Tomate', 'Mango', 'Leche']
    random.shuffle(elementos)
    print(elementos)
    print()
    return elementos

mezclar_elementos()

##2
def generar_numeros_unicos():
    numeros = set()
    while len(numeros) < 7:
        nuevo = random.randint(0, 9)
        if nuevo not in numeros:
            numeros.add(nuevo)
            print(nuevo, end=',')
    print("\n")

generar_numeros_unicos()


print("revisado")

