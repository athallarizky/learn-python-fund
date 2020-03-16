name = input("Input your name = " )

print("Hello, " + name)

angka1 = input("Angka 1 = ")
angka2 = input("Angka 2 = ")

print(int(angka1) + int(angka2))

#How to print in line is using end=''
print("test",end='')
print("haha")

# To show boolean value in Int variable you should convert to str() first
# It caused by security risk
print(str(angka1).isdigit())