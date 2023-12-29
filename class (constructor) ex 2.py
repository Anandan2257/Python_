class laptop:
    def __init__(self):
        self.price=0
        self.ram=""
        self.processor=""
    def display(self):
        print("ram :",self.ram)
        print("processor :",self.processor)

hp=laptop()
dell=laptop()

hp.price=60000
hp.ram="8gb"
hp.processor="i5"

dell.price=90000
dell.ram="16gb"
dell.processor="i7"

hp.display()
dell.display()

print()

print("empty class making")

class anand:
    pass
