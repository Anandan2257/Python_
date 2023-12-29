a=[]
print("enter a 10 number : ")
for i in range(10):
    num=int(input("enter a num "+str(i+1)+" : "))
    a.append(num)        
print(a)
sum=0
for i in a:
    sum=sum+i
print("sum of 10 numbers : ",sum)
print("average of 10 numbers : ",sum/10)
