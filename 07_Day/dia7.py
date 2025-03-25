##1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))

##2
it_companies.add("twitter")
print(it_companies)

##3
it_companies.update(["torres corzo","asus","intel"])
print(it_companies)

##4
it_companies.remove("Microsoft")
print(it_companies)

##5


##Ejercicios nivel2
##1
union=A.union(B)
print(union)

##2
interseccion=A.intersection(B)
print(interseccion)

##3
print(A.issubset(B))

##4
print(A.isdisjoint(B))

##5
print(A.union(B))
print(B.union(A))

##6
print(A.symmetric_difference(B))

##7
del(A)
del(B)

##Ejerecicios nivel 3

##1
edad=