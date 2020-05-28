
myStr = "Hello World"

print(myStr + " Jhhon")
print(f"Jhhon {myStr}") # Python3.x 
print("Jhhon {0}".format(myStr))
# print(dir(myStr))

print(myStr.upper()) # metodo .upper() cambia todo a MAY
print(myStr.lower()) # metodo .lower() cambia todo a MIN
print(myStr.swapcase()) # primera en min y resto en MAY
print(myStr.capitalize()) # primera en MAY y resto en min
print(myStr.replace("Hello", "bye").upper()) # .replace("old", "new") reemplaza texto, y encadenado con el metoro .upper
print(myStr.count("l")) # metodo que cuenta cuantas veces esta un caracter o cadena. 

print(myStr.startswith("He")) # Valida si empieza por... y devuelve true o false
print(myStr.endswith("rlD")) # Valida si termina en... y devuelve true o false

print(myStr.split(" ")) # Separa una cadena pon cada caracter especifico encontrado, por defecto " " espacio en blanco. y devuelve una lista con los caracteres. 
print(myStr.find("o")) # busca un caracter y devuelve el indice o posision del mismo en num entero. 

print(len(myStr)) # len() devuelve la longitud de la cadena. 
print(myStr.index("e")) # devuelve el indice del caracter. 

print(myStr.isnumeric()) # devuelve true or false. Python3.x
print(myStr.isalpha()) # devuelve true or false
print(myStr[0]) # devuelve caracter de posision especifica
print(myStr[-5]) # devuelve caracter de posision especifica

