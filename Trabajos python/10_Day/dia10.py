##1
count=0
while count<11:
    print(count)
    count=count+1

##2
ciclo=10
while ciclo>-1:
    print(ciclo)
    ciclo=ciclo-1

##3
ciclo2=1
while ciclo2<8:
    print("#"*ciclo2)
    ciclo2=ciclo2+1

##4
fila=8
columna=8
for i in range(fila):
    for j in range(columna):
        print("#", end=" ")
    print()

##5
num1=0
while num1<11:
    print(num1, "X", num1, "=", num1*num1)
    num1=num1+1

##6
lista=['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lista:
    print(i)

##7
num2=0
while num2<101:
    print(num2)
    num2=num2+2

##8
num3=1
while num3<100:
    print(num3)
    num3=num3+2

##ejercicios nivel 2

##1
for i in range(101):
    for j in range(100):
        i=i+j

print(i)

##2
for i in range(101):
    for j in range(100):
        if i%2==0 and j%2==0:
            i=i+j
print(i)

sum=0
for i in range(101):
    if i%2!=0:
        sum=sum+i
print(sum)

##ejercicios nivel 3

##1
from lista_de_paises import countries
land=[countries for countries in countries if "land" in countries]
print(land)
    
##2
fruitlist=['banana', 'orange', 'mango', 'lemon']
reversa=-1
for i in fruitlist:
    print(fruitlist[reversa])
    reversa=reversa-1

##3
from country_data import info_paises

# Obtener el conjunto de todos los idiomas únicos
all_languages = set()
for country in info_paises:
    all_languages.update(country.get('languages', []))  # Manejar posibles claves inexistentes

total_languages = len(all_languages)
print("Total number of languages:", total_languages)

# Contar la cantidad de países que hablan cada idioma
language_count = {}
for country in info_paises:
    for language in country.get('languages', []):
        language_count[language] = language_count.get(language, 0) + 1

# Obtener los 10 idiomas más hablados
most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]

print("\nTen most spoken languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

# Obtener los 10 países más poblados
most_populated_countries = sorted(info_paises, key=lambda x: x.get('population', 0), reverse=True)[:10]

print("\nTen most populated countries:")
for country in most_populated_countries:
    print(f"{country.get('name', 'Unknown')}: {country.get('population', 'Unknown')}")

print("revisado")