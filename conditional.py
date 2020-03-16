angka1 = 5
angka2 = 10

if angka1 > angka2:
    print("True")
else:
    print("False")


boolean = False 

if boolean:
    print("true")
    print("printed?")
print("yes, also printed")


money = input("Your Money = ")

# Look's, python can use parentheses () too..
if (int(money) > 100000):
    print("You can buy a new Car.")
elif int(money) > 50000:
    print("You only can buy a new Motor.")
else:
    print("You only can buy an Ice Cream.")


a = 7
b = 8

if (a > 1) & (b > 1):
    print("And condition only using one ampersand: &")

if a < 1 | b > 1:
    print("Or condition also only using one pipe: | ")


number = 1

if number == 1 : print("Number is 1")

