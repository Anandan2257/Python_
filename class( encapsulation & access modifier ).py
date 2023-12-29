class employee():
    def __init__(self):
        self.__company = "google"
    def display(self):
        print(self.__company)

e1 = employee()
e1.display()
print("private modifier")
print(e1.__company)
