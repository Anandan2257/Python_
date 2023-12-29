a = int(input("Enter a tamil mark :"))
b = int(input("Enter a english mark :"))
c = int(input("Enter a maths mark :"))
d = int(input("Enter a science mark :"))
e = int(input("Enter a social mark :"))
total = a+b+c+d+e
averge = total / 5
if(averge >= 35):
    print("you are good to go")
else:
    print("additional class is required")
