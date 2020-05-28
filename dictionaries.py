products = {
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

print(type(products))
print(products)

person = {
    "first_name": "Jhhon",
    "last_name": "Zapata"
}

print(type(person))
print(dir(person))
print(person.keys())
print(person.items())

person.clear()
print(person)

# Dictionary with dictionaries.
products = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 1000}
]

print(products)
