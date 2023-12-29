class teacher:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def display(self):
        print("name :",self.name)
        print("regno :",self.regno)
        
t1 = teacher("Anandan",621321105006)
t2 = teacher("Abisheik",621321105003)

t1.display()
print()
t2.display()

