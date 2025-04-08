# ## SyntaxError
# ##print('hello world; Comilla no cerrada
print('hello world')

# ## NameError
# ##print(age); La variable 'age' no ha sido definida
age = 25
print(age)

# ## IndexError
# ##numeros = [1, 2, 3, 4, 5]
# ##print(numeros[5]); El índice 5 está fuera del rango de la lista
numeros = [1, 2, 3, 4, 5]
print(numeros[4])

# ## ModuleNotFoundError
# ##import math1; La librería 'math1' no existe
import math
print(math.sqrt(16))

# ## AttributeError
# ##math.pi; No se puede acceder a 'pi' sin importar correctamente la librería 'math'
import math
print(math.pi)

# ## KeyError
# ##usuarios = {'name':'Asab', 'age':250, 'country':'Finland'}
# ##print(usuarios['nme']); No existe la clave 'nme' en el diccionario
usuarios = {'name':'Asab', 'age':250, 'country':'Finland'}
print(usuarios['name'])
print(usuarios['country'])

# ## TypeError
# ##4+'3'; No se puede sumar un número con un string
print(4 + float('3'))

# ## ImportError
# ## from math import power; 'power' no es una función importable de la librería 'math'
from math import pow
print(pow(2, 3))

# ## ValueError
# ##int('12a'); El valor '12a' no puede ser convertido a un entero
print("           ")
print(int('12'))

# ## ZeroDivisionError
# ##print(1/0); No se puede dividir entre cero
print(1/2)

print("revisado")