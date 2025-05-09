##1
listavacia=list()

##2
lista=list(["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete"])

print(lista)

##3
print(len(lista))

##4
listacortada=lista[::3]

##5
print(listacortada)

##6
empresas_tecnologicas = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

##7
print(empresas_tecnologicas) 

##8
print(len(empresas_tecnologicas))

##9
print(empresas_tecnologicas[0])
print(empresas_tecnologicas[3])
print(empresas_tecnologicas[6])

##10
del empresas_tecnologicas[0]
empresas_tecnologicas.insert(0, 'Twitter')
print(empresas_tecnologicas)

##11
empresas_tecnologicas.append('IBM')

##12
empresas_tecnologicas.insert(3, 'Samsung')

##13
empresas_tecnologicas[0] = empresas_tecnologicas[0].upper()
print(empresas_tecnologicas)

##14
print(str.join('#;', empresas_tecnologicas))

##15
existe = 'Facebook' in empresas_tecnologicas
print(existe)

##16
empresas_tecnologicas.sort()
print(empresas_tecnologicas)

##17
empresas_tecnologicas.reverse()
print(empresas_tecnologicas)

##18
primeras_tres_empresas = empresas_tecnologicas[0:3]
print(primeras_tres_empresas)

##19
ultimas_empresas = empresas_tecnologicas[6:9]
print(ultimas_empresas)

##20
empresa_unica = empresas_tecnologicas[4:5]
print(empresa_unica)

##21
print(empresas_tecnologicas.remove('Facebook'))

##22
print(empresas_tecnologicas.remove('IBM'))

##23
print(empresas_tecnologicas.remove('Oracle'))

##24
print(empresas_tecnologicas.remove[0:9])

##25
del(empresas_tecnologicas)

##26
tecnologias_front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
tecnologias_back_end = ['Node', 'Express', 'MongoDB']
pila_completa_tecnologica = tecnologias_front_end + tecnologias_back_end
print(pila_completa_tecnologica)

##27
copia_pila_completa = pila_completa_tecnologica.copy()
print(copia_pila_completa)

##28
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
print(edades)
del edades[0:2]
del edades[7:8]
print(edades)
edades.append(19)
edades.append(19)
edades.append(26)
print(edades)

##29
promedio_edad = sum(edades) / len(edades)
print(promedio_edad)

##30
edades.sort()
print(abs(edades[0] - promedio_edad))
print(abs(edades[8] - promedio_edad))

##31
from listapaises import countries
print(countries[int(len(countries)/2)])
primera_mitad = countries[0:96]
segunda_mitad = countries[96:192]

##32
paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
primeros_tres_paises = paises[0:3] 
resto_paises = paises[3:7]
print(primeros_tres_paises)
print(resto_paises)

print("revisado")