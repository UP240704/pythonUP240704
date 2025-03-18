myage=18
print("mi edad es" ,myage)
myheight=1.83
print("mi altura es de", myheight)

##4 
print("")
base=int(input("Ingresa la base del tiengulo "))
altura=int(input("Ingresa la altura del triangulo "))
area=float((base * altura)/2)
print("El area del triangulo es: ", area)

##5 
print("")
side1=int(input("ingresa el primer lado: "))
side2=int(input("ingresa el segundo lado: "))
side3=int(input("ingresa el tercer lado: "))
perimetro = side1 + side2 + side3
print("El perimetro es de: ", perimetro)

##6 
print("")
largo=int(input("Ingresa el valor del largo: ")) ##Largo
ancho=int(input("Ingresa el valor del ancho: ")) ##Ancho
area1=largo * ancho
perimetero2 = 2 * (largo + ancho)
print("El perimetro es de: ", perimetero2)

##7 
print("")
radio=float(input("Ingresa la circunferencia de tu circulo: "))
pi=float(3.1416)
area2=float(pi * radio **2)
circunferencia=float(2 * pi * radio)
print("Tu area es de: ", area2)
print("Tu circunferencia es de: ", circunferencia)

##8 
print("")
print("Interaccion de la pendiente:")
m = 2 
intY = -2     
intX = intY / m 
print("La pendiente de la ecuacion es: ", m)
print("La interacción es de: ", intX) 

##9 
print("")
x1 = 2
x2 = 6
y1 = 2
y2 = 10
distance = ((x2 - x1)**2 + (y2-y1)**2)**0.5
print("La distancia entre los dos puntos es: ", distance)
slope = (y2 - y1) / (x2 - x1)
print("La pendiente es de ",slope)

##10 
print("")
Compare = m <= slope
print("La diferencia entre las pendientes es de: ", Compare)

##11 
print("")
x = int(input("Ingresa el valor de X "))
y = (x**2 + (6 * x) + 9) 
print("El valor de la variable Y es igual a ", "|", y, "|")

##12
print("")
python = str(55)
dragon = str(3)

comp = python == dragon
print(len(python))
print(len(dragon))
print("La comparación de los numeros fue: ", comp)

##13
print("")
on = ("python", "dragon")
if  "dragon" in on:
    print("on is in dragon")
if  "python" in on:
    print("on is in dragon")

##14
print("")
course = ("I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.")
if "jargon" in course:
    print("jargon is in the sentence")

##15 
print("")
py = ("the tv is off")
dra = ("the tv is off")
if "on" in py and dra:
    print("on is in the sentence")
else: 
    print("on isn´t in these sentens")

##16
print("")
print("Una prueba de longitud con la funcion len")
text = str(float("654864643215"))
len(text)
print("La longitud de la frase es de: ", len(text))

##17
print("")
par = int(input("Ingresa un numero: "))
par = (par % 2)
if par > 0:
 print("Es numero inpar")
else:
    print("Es numero par")

##18
print("")
floDiv = 7 // 3
intPi = int(2.7)
comDiv = floDiv == intPi
print("El resultado de la division es:", comDiv)

##19 
print("")
ty1 = type("10")
ty2 = type(10)
comTy = ty1 == ty2
print("Los tipos de las unidades son iguales? ", comTy)

##20 
print("")
typ1 = int(float("9.8"))
typ2 = 10
comTyp = typ1 == typ2
print("Los tipos de las unidades son iguales? ", comTyp)

##21
print("")
horas = int(input("¿Cuántas horas trabajaste: "))
tarifa = int(input("Valor de la tarifa por hora: "))
salario = horas * tarifa
print("Tu salario es de ",salario)

##22 
years = int(input("Cuantos años tienes? "))
seconds = (365 * (3600*24))
total = (years * seconds)
print("Tu tienes un total de:", total, "segundos")

##23
for i in range(1, 6):  # Genera números del 1 al 5
    print(f"{i:<7} {1:<11} {i:<11} {i**2:<11} {i**3:<11}")
#Ejemplo 23.1
for i in range(1, 6):  # Números del 1 al 5
    print(i, 1, i, i**2, i**3)
