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
