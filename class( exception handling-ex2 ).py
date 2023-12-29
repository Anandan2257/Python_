try:
    a = int(input("enter a : "))
    b = int(input("enter b : "))
    c = input("enter c : ")
    print(c/a)
except ValueError as e:
    print("ValueError",e)
except TypeError as e:
    print("TypeError",e)
except NameError as e:
    print("NameError",e)    

finally:
    print("done")
    
