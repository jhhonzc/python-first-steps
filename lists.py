
demo_list = [1, "lista", 10.2, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

# Constructor list()

numbers_list = list((1, 2, 3, 4))
print(numbers_list)
print(type(numbers_list))

rango = list(range(1, 10))
print(rango)
print(type(rango))

print(dir(colors))
print(len(colors))

print(colors[2])
print(colors[-2])

print("green" in colors)
print("black" in colors)

print(colors)
colors[1] = "black"
print(colors)

colors.append("violet") # Agrega solo un elemento
print(colors)

colors.extend(["brown", "yellow"]) # Agrega varios elementos de lista
print(colors)

colors.extend(("gray", "white")) # Agrega varios elementos de tupla
print(colors)

colors.insert(1, "orange") # Agrega/modifica un elemento en posición especifica
print(colors)

colors.insert(len(colors), "other") # Agrega/modifica elemento en la ultima posición
print(colors)

colors.pop() # Elimina el ultimo valor agregado a la listaprint(colors)
print(colors)

colors.remove("violet") # elimina un elemento especifico por referencia
print(colors)

colors.pop(2) # elimina un elemento especifico por indice
print(colors)

colors.clear() # elimina todos los elementos de la lista
print(colors)

colors.extend(["red", "yellow", "blue", "red"]) # Agrega varios elementos de lista
print(colors)

colors.sort() # ordena los elementos 
print(colors)

colors.sort(reverse=True) # ordena los elementos de forma inversa
print(colors)

print(colors.index("red")) # retorna el indice del elemento

print(colors.count("red")) # retorna la cantidad de elemento concreto

