class phone:
    chargertype ="C-type"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def display(self):
        print("Brand :",self.brand)
        print("Price :",self.price)
realme = phone("realme",20000)
realme.display()
print()
redmi = phone("redmi",21000)
redmi.display()
print()
iqoo = phone("Iqoo",22000)
iqoo.display()
