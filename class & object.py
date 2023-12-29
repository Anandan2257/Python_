class goa:
    name = ""
    drink = ""
    def party(self):
        print("enjoy a party")
    def beach(self):
        print("enjoy a beach")
Anandan = goa()
Abi = goa()

Anandan.name="Anand"
Abi.name="Abi"
Anandan.drink="yes"
Abi.drink="no"

print(Anandan.name)
print("drink :",Anandan.drink)
Anandan.party()
print()
print(Abi.name)
print("drink :",Abi.drink)
Abi.beach()

