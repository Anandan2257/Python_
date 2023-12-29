print("compile time error")
print("logical error")
print("runtime error")
print()
print("these are the errors and how to handling the error using exception handling")
print()

try:
    a=int(input("enter a :"))
    b=int(input("enter b :"))
    print(a+b)
except Exception:
    print("something error to assign a correct value")
