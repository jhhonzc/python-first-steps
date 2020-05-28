
colors = {"red", "blue", "green"} # conjunto de datos que no tienen un indice ni orden.

print(colors)
print(type(colors))
print("red" in colors) # valida si el elemento existe en el set

colors.add("violet") # agrega un elemento en cualquier ubicacion ya que no tienen indice
print(colors)

colors.remove("blue") # elimina un elemento especifico 
print(colors)

colors.clear() # elimina todos los valores del set
print(colors)

del colors # elimina el set completo