### Note : List = Array

list1 = ["name1", "name2", 5, 5.2]

print(list1[0])

list1.append("Wow! Such as JavaScript")

print(list1)

del list1[1]

print("Now \"name2\" deleted --> ", list1)

#Using len() for show list length
print(len(list1))

### Tuple = List but IMMUTABLE, cannot be edited (add, delete, etc.)

tuple1 = ("Hello", 1, 7.2, "World")

#Convert tuple to list
print(list(tuple1))

#Convert list to tuple
print(tuple(list1))


### Dictionary = Object in JS

dictionary1 = {
    "name":"athalla",
    "age":15,
    "admin":1
}

print(dictionary1['name'])

dictionary1["name"] = "Rizky"
del dictionary1['age']
dictionary1["status"] = "single"

print(dictionary1)

for (key,val) in dictionary1.items():
    print("key = " , key , " --- value = " , val)



# Summary

listData = [1,2,3]
setData  = {1,2,3}
tupleData = (1,2,3)
rangeData = list(range(0,100,2))
print(rangeData)