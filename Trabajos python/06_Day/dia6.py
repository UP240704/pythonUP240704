##1
empty_tuple=()

##2
hermanos=("abner", "diego", "abner")
hermanas=("chutiya", "josefinaaa")

##3
hermanes= hermanos+hermanas
print(hermanes)

##4
print(len(hermanes))

##5
padres=("bianca", "alfonso")
familia=hermanes+padres
print(familia)

##6
padres=familia[5:]
hermanes=familia[:5]
print(padres)
print(hermanes)

##7
frutas=("manzana", "platano", "pera")
vegetales=("apio", "col", "cebolla")
producto_animal=("carne", "queso", "leche")
alimentos=frutas+vegetales+producto_animal
print(alimentos)

##8
listaalimentos=list(alimentos)
print(listaalimentos)

##9
print(listaalimentos[4])

##10
print(listaalimentos[0:3])
print(listaalimentos[6:9])

##11
del(alimentos)

##12
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in (nordic_countries))
print("Iceland" in (nordic_countries))

print("revisado")