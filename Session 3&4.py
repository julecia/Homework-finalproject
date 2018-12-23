#Write a program that asks for your name and prints: “Hello <name>!”
print("Hello Javier")

#Write a program that takes 2 numbers as input and prints the rounded up division result

print(4/4)

#Write a program that takes the radius of circle as input and prints the surface of the circle


from math import pi
r = float(input ("radius : "))
print ("The Area  " + str(r) + " is equal to: " + str(pi * r**2))


#create a pocket calculator
print("\nCalculator"
      "\nOperate now, when finished just type it")

while True:
    print("Your operation:")
    value = input()

    if value == "finish":
        print("Bye!")
        exit(1)
    else:
        command = eval(value)
        print("The result is ", command)

