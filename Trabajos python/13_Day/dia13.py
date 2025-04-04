# 1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
filtrados = [n for n in numeros if n <= 0]
print(filtrados)

# 2
estructuras = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
valores = [x for grupo in estructuras for lista in grupo for x in lista]
print(valores)

# 3
potencias = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(potencias)

# 4
paises_info = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
mayusculas = [[pais.upper(), pais[:3].upper(), ciudad.upper()] 
              for grupo in paises_info for pais, ciudad in grupo]
print(mayusculas)

# 5
mayusculas_simple = [[pais.upper(), ciudad.upper()] 
                     for grupo in paises_info for pais, ciudad in grupo]
diccionarios = [{'country': pais, 'capital': ciudad} 
                for grupo in paises_info for pais, ciudad in grupo]
print(diccionarios)

# 6
personas = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for fila in personas for nombre, apellido in fila]
print(nombres_completos)

# 7
pendiente = (lambda x1, y1, x2, y2: (x2 - x1) / (y2 - y1))(3, 4, 5, 7)
print(pendiente)
