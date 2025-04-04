# Datos de ejemplo
paises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
nombres = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ## Nivel 1
## Función map
def elevar_al_cuadrado(num):
    return num ** 2
print(list(map(elevar_al_cuadrado, numeros)))

def convertir_a_mayusculas(nombre):
    return nombre.upper()
print(list(map(convertir_a_mayusculas, nombres)))

## Función filter
def es_par(num):
    return num % 2 == 0
print(list(filter(es_par, numeros)))

def tiene_land(pais):
    return 'land' in pais.lower()
print(list(filter(tiene_land, paises)))

## Función reduce
from functools import reduce

def sumar(x, y):
    return x + y

suma_total = reduce(sumar, numeros)
print(suma_total)

## Función de orden superior
def funcion_de_orden_superior(func, arg):
    return func(arg)
print(funcion_de_orden_superior(elevar_al_cuadrado, 5))

## Closure
def funcion_exterior(x):
    def funcion_interior(y):
        return x + y
    return funcion_interior
print(funcion_exterior(5)(10))

## Decorador
def registro(func):
    def envoltorio(*args, **kwargs):
        print(f"Llamando a la función '{func.__name__}' con los argumentos {args} y {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"La función '{func.__name__}' retornó {resultado}")
        return resultado
    return envoltorio

@registro
def sumar_dos(a, b):
    return a + b

@registro
def multiplicar(a, b):
    return a * b

print(sumar_dos(5, 3))
print(multiplicar(4, 6))

## Función map
def elevar_al_cubo(num):
    return num ** 3
print(list(map(elevar_al_cubo, numeros)))

## Imprimir cada país en la lista
for pais in paises:
    print(pais)

## Imprimir cada nombre en la lista
for nombre in nombres:
    print(nombre)

## Imprimir cada número en la lista
for numero in numeros:
    print(numero)

# ## Nivel 2
## Convertir países a mayúsculas
mayusculas_paises = list(map(str.upper, paises))
print(mayusculas_paises)

## Elevar los números al cuadrado
print(list(map(elevar_al_cuadrado, numeros)))

## Convertir nombres a mayúsculas
nombres_mayusculas = list(map(str.upper, nombres))
print(nombres_mayusculas)

## Filtrar países que contienen 'land'
print(list(filter(tiene_land, paises)))

## Filtrar países con exactamente 6 caracteres
paises_six_caracteres = list(filter(lambda pais: len(pais) == 6, paises))
print(paises_six_caracteres)

## Filtrar países con 6 o más caracteres
paises_seis_o_mas = list(filter(lambda pais: len(pais) >= 6, paises))
print(paises_seis_o_mas)

## Filtrar países que empiezan con 'E'
def comienza_con_e(pais):
    return pais.startswith('E')
print(list(filter(comienza_con_e, paises)))

## Combinación de map, filter y reduce
resultado = reduce(
    lambda x, y: x + y, 
    filter(
        lambda x: x % 2 == 0,  
        map(
            lambda x: x ** 2,  
            numeros
        )
    )
)
print(resultado)

## Filtrar solo cadenas en una lista
def obtener_cadenas(lista):
    return list(filter(lambda x: isinstance(x, str), lista))

lista_mixta = [1, 'hola', 3.14, 'mundo', True, 'Python']
solo_cadenas = obtener_cadenas(lista_mixta)
print(solo_cadenas)

## Sumar todos los números con reduce
suma_total = reduce(sumar, numeros)
print(suma_total)

## Concatenar países en una oración
oracion = reduce(
    lambda acc, pais: acc + ', ' + pais if pais != paises[-1] else acc + ', y ' + pais, paises[:-1], paises[0]
) + ' son países del norte de Europa.'
print(oracion)

## Filtrar países con 'land' usando una lista importada
from lista_paises import paises_2  
paises_con_land = list(filter(lambda pais: 'land' in pais.lower(), paises_2))
print(paises_con_land)

## Contar países por letra inicial
from lista_paises import paises_2
def contar_paises_por_letra(paises):
    contador_paises = {}
    for pais in paises:
        letra_inicial = pais[0].upper()  
        if letra_inicial in contador_paises:
            contador_paises[letra_inicial] += 1
        else:
            contador_paises[letra_inicial] = 1
    return contador_paises

conteo_paises_letra = contar_paises_por_letra(paises_2)
print(conteo_paises_letra)

## Obtener los primeros diez países
from lista_paises import paises_2 
def obtener_primeros_diez(paises):
    return paises[:10] 

primeros_diez = obtener_primeros_diez(paises_2)
print(primeros_diez)

## Obtener los últimos diez países
from lista_paises import paises_2 
def obtener_ultimos_diez(paises):
    return paises[-10:]  

ultimos_diez = obtener_ultimos_diez(paises_2)
print(ultimos_diez)

# ## Nivel 3
from countrydata import infopaises 

## Ordenar países por nombre
def ordenar_paises_por_nombre(paises):
    return sorted(paises, key=lambda x: x['name'])

paises_ordenados = ordenar_paises_por_nombre(infopaises)
print("Países ordenados por nombre:")
for pais in paises_ordenados:
    print(pais['name'])

## Obtener los diez idiomas más hablados
def idiomas_mas_hablados(paises, top_n=10):
    from collections import Counter
    contador_idiomas = Counter()
    for pais in paises:
        contador_idiomas.update(pais['languages'])
    return contador_idiomas.most_common(top_n)

idiomas_top_10 = idiomas_mas_hablados(infopaises, 10)
print("\nDiez idiomas más hablados:")
for idioma, conteo in idiomas_top_10:
    print(f"{idioma}: {conteo}")

## Obtener los diez países más poblados
def paises_mas_poblados(paises, top_n=10):
    return sorted(paises, key=lambda x: x['population'], reverse=True)[:top_n]

paises_mas_poblados = paises_mas_poblados(infopaises, 10)
print("\nDiez países más poblados:")
for pais in paises_mas_poblados:
    print(f"{pais['name']}: {pais['population']}")
