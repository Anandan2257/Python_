salary = int(input("enter a salary :"))
age = int(input("enter a age :"))
if(salary >= 20000 or age <= 25):
    loan = int(input("enter a loan amount :"))
    if(loan > 50000):
        print("maximum amount is 50000")
    else:
        print("you are eligible for loan")
else:
    print("you are not eligible")
               
