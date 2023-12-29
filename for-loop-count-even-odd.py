count1 = 0
count2 = 0
for i in range(1,11):
    if(i%2==0):
        count1=count1+1
    elif(i%2!=0):
        count2=count2+1
print("Even = ",count1)
print("odd = ",count2)
