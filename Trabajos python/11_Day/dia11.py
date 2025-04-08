##1
def add_two_numbers(numero,numero2):
    res=numero+numero2
    return res
print(add_two_numbers(5,7))

##2
def area_of_circle(radio):
    from math import pi
    area= pi*radio*radio
    return area
print(area_of_circle(9))

##3
def sum_total(*args):
    total=0
    for i in args:
        total=total + i
    return total
print (sum_total(1,2,3,4,5))
    
##4
def temperatura(C):
    F=(C*9/5)+32
    return F
print (temperatura(70))


##5
def check_season(mes):
    if mes in["enero","febrero","diciembre"]:
        return "invierno"
    elif mes in["marzo", "abril","mayo"]:
        return "primavera"
    elif mes in["junio","julio","agosto"]:
        return "verano"
    elif mes in["sepriembre", "octubre","nomviembre"]:
        return "otoño"
    else: print("no es un mes")
print(check_season("enero"))

##6
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    return slope
print (calculate_slope(7,8,10,15))

##7
def solve_quadratic_eqn(a,b,c):
    x1=(-b+((b**2)-4*a*c)**0.5)/(2*a)
    x2=(-b-((b**2)-4*a*c)**0.5)/(2*a)
    return x1,x2
print (solve_quadratic_eqn(10,20,30))

##8
def print_list(lista):
    for i in lista:
        print(i)
print_list(["jamom","atun","pescao"])

##9
def reverse_list(lista):
    return lista[::-1]
print(reverse_list(["jamom","atun","pescao"]))

##10
def capitalize_list(lista):
    return [i.upper() for i in lista]
print (capitalize_list(['Potato', 'Tomato', 'Mango', 'Milk']))

##11
def add_item(food_staff,FOOD):
    food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
    food_staff.append(FOOD)
    return food_staff
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Pasta'))

##12
def remove_item(food_stuff,FOOD):
    food_stuff=['Potato', 'Tomato', 'Mango', 'Milk']
    food_stuff.remove(FOOD)
    return food_stuff
print (remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Tomato'))

##13
def sum_num(numero):
    for i in range(numero+1):
        for j in range(numero):
            i=i+j
    return i
print(sum_num(55))

##14
def sum_of_odds(numero):
    for i in range(numero+1):
        for j in range(numero):
            if i%2==0 and j%2==0:
                i=i+j
    return i
print(sum_of_odds(88))

##15
def sum_of_even(numero):
    total = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_even(1080))

##Ejercicios nivel 2

##1
def factorial(f):
    numb=1
    for i in range(1,f+1):
        numb=i*numb
    return numb
print (factorial(9))

##2
def is_empty(lista):
    if len(lista) == 0:
        return True
print (is_empty([]))

##3
def calculate_mean(num):
    total_median=0
    for i in num:
        total_median=total_median+i
        prom=total_median/len(num)
    return prom
print (calculate_mean([1,4,6,7,3,6,7,7]))

def calculate_median(num):
    median=num[int(len(num)/2)]
    return median
print (calculate_median([3,2,4,8,5,5,9,7]))

def calculate_mode(num):
    from collections import Counter
    calculate_mode=Counter(num)
    return calculate_mode.most_common(1)
print(calculate_mode([3,2,4,8,5,5,11,7]))

def calculate_range(num):
    num.sort()
    range1=num[0]
    range2=num[int(len(num)-1)]
    j=range(range1, range2)
    return j
print(calculate_range([8,4,48,1,5,9,5,9]))

def calculate_variance(num):
    var = sum(num) / len(num)
    var1 = sum((i - var) ** 2 for i in num) / len(num)
    return var1
print(calculate_variance([6,4,7,8,3,5,7,4]))

def calculate_std(num):
    var = sum(num) / len(num)
    var1= sum((i - var) ** 2 for i in num) / len(num)
    std=var1**0.5
    return std
print(calculate_std([8,5,7,8,34,4,6]))

##ejercicios nivel 3

##1
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if (num%i)==0:
            print(num,'no es primo')
        else:
            print(num,'es primo')
    return ''
print(is_prime(8))

##2
def unique(lista):
    return len(set(lista))==len(lista)
print(unique(["manzana","manzana","manzana"]))

##3
def same(lista):
    list = iter(lista)
    tipo = type(next(list))
    if all((type(x) is tipo) for x in list): 
        print(True)
    else:
        print(False)
    return ''
print(same([1,2,3,4,'manzana']))

##4
def is_valid_python_variable(var: str) -> bool:

    if not var.isidentifier():
        return False
    
    return True
print(is_valid_python_variable('for'))

##5
from countrydata import infopaises

from collections import Counter

def obtener_idiomas_mas_hablados(paises, cantidad=10):
    contador_idiomas = Counter()
    for pais in paises:
        contador_idiomas.update(pais["languages"])
    return contador_idiomas.most_common(cantidad)

def obtener_paises_mas_poblados(paises, cantidad=10):
    paises_ordenados = sorted(paises, key=lambda pais: pais["population"], reverse=True)
    return paises_ordenados[:cantidad]

print("Idiomas más hablados:")
for idioma, veces in obtener_idiomas_mas_hablados(infopaises, 10):
    print(f"{idioma}: en {veces} países")

print("\nPaises con mayor población:")
for pais in obtener_paises_mas_poblados(infopaises, 10):
    print(f"{pais['name']}: {pais['population']}")

print("revisado")