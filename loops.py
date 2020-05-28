foods = ['apples', 'bread', 'cheese', 'milk', 'graves']

print("\nwitout for:")

print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])

print("\nfor:")

for food in foods: 
    print(food)

print("\nfor with if:")

for food in foods: 
    if food == "cheese":
        print("you have to buy " + food)
    else:
        print(food)

print("\nfor with if and break:")

for food in foods: 
    if food == "cheese":
        print("you have to buy " + food)
        break # rompe o detiene el ciclo.
    else:
        print(food)

print("\nfor with if and continue:")

for food in foods: 
    if food == "cheese":
        continue # salta y continua el ciclo.
    else:
        print(food)

print("\nfor with range:")

for number in range(1, 8): 
    print(number)
    

print("\nfor with string:")

for letter in "Hello": 
    print(letter)

print("\nwhile")

count = 4

while count <= 10:
    print(count)
    #count = count + 1
    count += 1    

