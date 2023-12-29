class student:
    def __init__(self):
        self.name = ""
        self.register_number =""
    def display(self):
        print("name of a student :",self.name)
        print("register number of a student :",self.register_number)

class1 = student()
class2 = student()

class1.name = "Anandan"
class1.register_number =621321105006

class2.name = "Abisheik"
class2.register_number =621321105003

class1.display()
print()
class2.display()

