class a():
    def __init__(self):
        print("A")
    def display(self):
        print("class a")

class b():
    def __init__(self):
        print("B")
    def display(self):
        print("class b")

class c(a,b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("class c")
        
anand=c()

