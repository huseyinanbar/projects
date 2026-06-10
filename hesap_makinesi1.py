print("welcome Miss ...")
x = int(input("press '0' for enter the calculator: "))

while x == 0:
    operation = int(input("press '1' for addition\npress '2' for subtraction\npress '3' for multiplication\npress '4' for division\npress '5' for exit: "))
    if operation == 1:
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        print("sum of two numbers",a + b)
        a = 0
        b = 0
    elif operation == 2:
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        print("difference of two numbers",a - b)
        a = 0
        b = 0
    elif operation == 3:
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        print("multiplication of two numbers",a * b)
        a = 0
        b = 0
    elif operation == 4:
        a = int(input("enter the first number: "))
        b = int(input("enter the second number: "))
        print("quotient of two numbers",a / b)
        a = 0
        b = 0
    elif operation == 5:
        print("see you for next projects ")
        print("We will work on projects about you soon <3<3<3")
        break
