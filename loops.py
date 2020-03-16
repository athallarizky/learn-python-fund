
i = 0

while i < 5:
    print("Hello World")
    i+=1
else: print("Hello Stopped")


data = ["a","b", 5]
for datax in data: print(datax)

string = "kiky"

for letter in string: print(letter)

for numb in range(0,5): print(numb, end=" ")

print("\n How to print ")

dictionary = {
    1:{"name":"athalla","kelas":"IF-42-09"},
    2:{"name":"rizky","kelas":4}
}

for (keys,items) in dictionary.items():
    print("data ke", keys , end=" ")
    
    for (key) in items:
        print(key + " " + items[key])