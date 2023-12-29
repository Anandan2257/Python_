class phone:
    chargertype = "C-type"
    def __init__(self):
        self.brand = ""
        self.price = ""
    def setprice(self,price):
        self.price = price
    def getprice(self):
        print(self.price)
        
    @classmethod
    def changechargertype(cls):
        cls.chargertype="B-type"
        print("charger type changed to B")
        
    @staticmethod
    def anand():
        print("these for example")

redmi = phone()
redmi.setprice(21000)
redmi.getprice()

phone.changechargertype()

redmi.anand()
        
