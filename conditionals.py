x = 30

if x < 30:
    print("x is less than 30")
else:
    print("x is greater than 30")

if x == 30:
    print("x is 30")

color = "blue"

if color == "red":
    print("the color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("is any color")

name = "John"
lastname = "Carter"

if name == "John":
    if lastname == "Carter":
        print("You are John Carter")
    else:
        print("You are not John Carter")
else: 
    print("You are not John")

# logical operators

x,y = 3,30

if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten")

if x > 2 or x <= 20: 
    print("x is greater than two and less than or equal to twenty")

if (not(x == y)):
    print("x is not equal y")
