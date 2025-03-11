## 1 concatenar
uno="thirty "
dos="days "
tres="of "
cuatro="python"
cinco= uno+dos+tres+cuatro
print(cinco)

## 2 concatenar
a="coding"
b=" for"
c=" all"
d= a+b+c
print(d)

## 3 
company="coding for all"

## 4
print(company)

## 5
print(len(company))

## 6 
uppercompany=company.upper()

## 7
lowercompany=company.lower()

##8
print(
company.capitalize(),
company.title(),
company.swapcase())

##9
cc1=company[7:15]
print(cc1)

##10
print(company.find("coding"))

##11
print(company.replace("coding","python"))

##12
print(company.replace("all","everyone"))

##13
print(company.split(" "))

##15
texto="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(texto.split())

##16
letra1=company[0]
print(company[0])

##17
print(company[10])

##18
pye="python for everyone"
print(pye)

##19
cfa=company
print(cfa)

##20
cindex=company.index("c")
print(cindex)

##21
cindex=company.index("f")
print(cindex)

##22
lfind="coding for all people".rfind("l")
print(lfind)

##23
cindex='You cannot end a sentence with because because because is a conjunction'.index("because")
print(cindex)

##24
cindex='You cannot end a sentence with because because because is a conjunction'.rindex("because")

##25
slicedsentence='You cannot end a sentence with because because because is a conjunction'[31:55]
print(slicedsentence)

##28
print(company.startswith("coding"))

##29
print(company.endswith("coding"))

##30
print('   Coding For All      '[3:17])

##31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

##32
lista="'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'"
listaunida=" # ".join(lista)
print(listaunida)

##33
print("I am enjoying this challenge.\nI just wonder what is next.")

##34
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

##35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

##36
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))
