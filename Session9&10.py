import random


def a():
    total = 0
    for x in range(0, 10):
        num = random.random()
        print(num)
        total += num
    print("The sum is equal to", total)


def b(number, odd=True):
    check = number % 2 != 0
    if odd and check is True:
        print(number, "is odd")
    elif odd and check is False:
        print(number, "is even")
    elif not odd and check is True:
        print("Checking for even but is odd")
    else:
        print(number, "is even")


def c():
    iterations = random.randint(0, 100)
    lst = []
    for x in range(0, iterations):
        number = [random.randint(0, 9)]
        lst.extend(number)
    print("Random list is: ", lst)
    return lst


def d():
    lst = c()
    lst.sort()
    print("Largest value is", lst[len(lst)-1])


def e():
    lst = c()
    lst.sort()
    print("Sorted list is: ", lst)


def f():
    lst = c()
    maximum = 0
    for a in range(0, len(lst)-1):
        if lst[a] > maximum:
            maximum = lst[a]
    print("Largest value is", maximum)


while True:
    command = input("Enter the function (a,b,c,d,e,f): ")
    if command == "EXIT":
        break
    else:
        try:
            eval(command)
        except:
            print("Please, type a valid letter")