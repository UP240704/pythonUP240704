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






