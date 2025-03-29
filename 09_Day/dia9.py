##1
print("ingresa tu edad")
edad=int(input())
if edad > 17:
     print("puedes aprender a conducir")
else:
     print("no puedes conducir te faltan", 18-edad)

##2
print("Ingresa tu edad")
myage = 18
yourage = int(input())
if yourage > myage:
    print("Eres", yourage - myage, "años más viejo que yo")

elif yourage < myage:
    print("Eres", myage - yourage, "años más chico que yo")

else:
    print("Tenemos la misma edad")

##3
print("ingresa un num")
n1=int(input())
print("ingresa un num")
n2=int(input())
if n1 < n2:
    print(n2, " es mayor a ", n1)
elif n1 > n2:
     print(n2, " es menor a ", n1)
else:
     print(n2, " es igual a ", n1)

##Ejercicios nivel 2

##1
print("ingresa tu calificación")
calificación=int(input())
if 80<calificación<100: print("tu nota es A")
elif 70<calificación<89: print("tu nota es B")
elif 60<calificación<69: print("tu nota es C")
elif 50<calificación<59: print("tu nota es D")
elif 0<calificación<49: print("tu nota es F")
else: print("la calificacion ingresada no es valida")

##2
print("ingresa el mes del año")
mes= input()
mes=mes.strip() #para evitar que un espacio antes del texto afecte la funcionalidad del codigo
mes=mes.lower() #para que no afecte siesta escrito en mayusculas o minisculas
if mes in["septiembre", "octubre", "noviembre"]: print("la estacion es otoño")
elif mes in["diciembre", "enero", "febrero"]: print("la estacion es invierno")
elif mes in["marzo", "abril", "mayo"]: print("la estacion es primavera")
elif mes in["junio","julio", "agosto"]: print("la estacion es verano")
else: print("el texto ingresado no corresponde con un mes")

##3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210' } }




