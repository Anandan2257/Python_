class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def  add(self):
        print("Add :",self.a+self.b)
    def  sub(self):
        print("Sub :",self.a-self.b)
    def  muli(self):
        print("Muli :",self.a*self.b)
    def  div(self):
        print("Div :",self.a/self.b)

answer = calculator(a=int(input("enter a :")),b=int(input("enter b :")))
print("\nAnswer for all opertion :")
answer.add()
print()
answer.sub()
print()
answer.muli()
print()
answer.div()

