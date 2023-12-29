T_count = 0
F_count = 0
for i in range(1,101):
    if(i%3==0):
        T_count = T_count +1
    elif(i%5==0):
        F_count = F_count +1
print("count of divi by 3 : ",T_count)
print("count of divi by 5 : ",F_count) 
