
print("\nfunction witout arguments")

def hello():
    print("Hello world")

hello()


print("\nfunction with arguments")

def hello(name):
    print("Hello " + name)

hello("Joe")
hello("Ryan")
hello("John")

def hello(name="Person"):
    print("Hello " + name)

hello()
hello("Alice")


print("\nfunction with 2 arguments")

def add(numberOne, numberTwo):
    return numberOne + numberTwo

add(10, 30) # no print

print(add(20, 30))
print(add(45, 30))

del add

print("\nlambda function with 2 arguments")

add = lambda num1, num2: num1 + num2

print(add (20, 13))