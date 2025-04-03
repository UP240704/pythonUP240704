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
fruits = ['banana', 'orange', 'mango', 'lemon']
print("name a fruit")
fruta=input()
fruta=fruta.strip()
fruta=fruta.lower()

if fruta in fruits:print('That fruit already exist in the list')
else: 
    fruits.append(fruta)
    print(fruits)

##Ejerecicios nivel 3

##1
person={
    'first_name': 'Julio',
    'last_name': 'Jule',
    'age': 33,
    'country': 'Guatemala',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210' } }
##1
if "skills" in person: print("python")
else: print("no skills set found")

##3
if "Python" in person["skills"]: print("la persona sabe python")
else: print("la persona no sabe python")

##4
if 'skills' in person:
    skills = person['skills']
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
        print('He is a backend developer')
    elif set(['React', 'Node', 'MongoDB']).issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print("unknwontitle")

##5
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married")
else:
    print(f"{person['first_name']} {person['last_name']} does not meet the criteria")


print("revisado")