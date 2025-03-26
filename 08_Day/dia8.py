##1
dog={}

##2
dog={"nombre":"firulais", "color":"negro", "raza":"pastor aleman", "piernas":"3", "edad":"5 años"}
print(dog)

##3
estudiante={"first_name":"Isai",
 "last_name":"Muro González",
 "gender":"male", 
 "age":"18",
   "marital_status":"single", 
   "skills":["english", "python"],
   "country":"Mexico",
   "city":"aguascalientes",
   "adress":"catalina de ayala #130 zona centro"}
print(estudiante)

##4
print(len(estudiante))

##5
print(type(estudiante["skills"]))

##6
estudiante["skills"].extend(["cooking","basketball"])
print(estudiante["skills"])

##7
key=estudiante.keys()
print(key)

##8
values=estudiante.values()
print(values)

##9
lista_de_tuples=estudiante.items()
print(lista_de_tuples)

##10