
x = (1,) # un solo elemento debe tener coma para ser tupla

print(type(x))
print(dir(x))

x = (1, 2, 3) # las tuplas son mas rapidas de una lista

print(x)

months = ("Enero", "Febrero", "Marzo") # elementos que nunca cambian.

print(months)

y = tuple((4, 5, 6)) # constructor tuple(), utilizado para bajo nivel

print(y)

print(x[1])

del x # elimina toda la tupla
#print x

# utilizado en diccionarios
locations = {
    (35.2321, 36.2325):"Tokio",
    (27.2321, 25.2325):"New York"
}

print(locations)