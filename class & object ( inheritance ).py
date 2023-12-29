class dad():
    def phone(self):
        print("dads phone")
class mom():        
    def sweets(self):
        print("mom's sweets")
class son(dad,mom):        
    def laptop(self):
        print("son's laptop")

anand = son()

anand.laptop()

anand.phone()

anand.sweets()

