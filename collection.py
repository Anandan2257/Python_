print()
print("------------------list------------------\n")
    
a=[1,2,3,4,5]
print(type(a))
print(a)

a.append(6)
a.append("@")
a.append(True)
print(a)

print(a[2])
print(a[0])

a.insert(0,100)
print(a)

a.insert(1,"oviya")
print(a)

a[0]="anandan"
print(a)

a.pop(8)
print(a)

a.pop()
print("remove last number : ",a)

b=[1,2,3,4,5,6]
c=[10,11,12]
b.extend(c)
print("combain b and c values : ",b)

print()
print("-------------------tuple---------------------\n")

a=(1,2,3,4,5)
print(a)
b=list(a)
print(b)


print()
print("------------------------set---------------------\n")

a={1,2,3,4,5,1}
a.add(11)
print(a)

a.remove(4)
print(a)

b={1,2,3,4}
c={'a','b'}
b.update(c)
print(b)


print()
print("----------------------dictionary-------------------\n")

a={
    "name":"anandan",
    "age":20,
    "location":"namakkal",
    "skills":["python","html","css"]
              }
print(a)
print(a["skills"])
print(a["name"])

print(a.keys())
print(a.values())

a["age"]=21
print(a["age"])

a["color"]="red"
print(a)

a.update({"age":22})
print(a)

a.pop("age")
print(a)

del a["name"]
print(a)

a.clear()
print(a)

del a





























    






























