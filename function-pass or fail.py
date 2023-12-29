def findpassorfail(b):
    if(b>=35 and b<=100):
        print("you are pass")
    elif(b<35):
        print("you are fail")
    else:
        print("invalid mark")
a = int(input("Enter a mark : "))
findpassorfail(a)
        
