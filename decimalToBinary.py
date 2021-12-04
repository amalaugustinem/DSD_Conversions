number = int(input("Give Number: "))
nm = number
fromBase = int(input("Give From base: "))
toBase = int(input("Give To base: "))
emp = ""

if fromBase == 10 and toBase == 2:
    while(number):
        rem = number % 2
        number = int(number/2)
        emp += str(rem)
    print("{} is Binary conversion of {}".format(emp, nm))
else:
    print("Invalid input !!")

