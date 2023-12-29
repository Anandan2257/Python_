class friend_1():
    def phone(self):
        print("anandan have iphone")
class friend_2(friend_1):
    def laptop(self):
        print("abi have hp laptop")
class friend_3(friend_2):
    def waterbottle(self):
        print("saravana have waterbottle")

saravana = friend_3()
saravana.waterbottle()
saravana.laptop()

abi = friend_2()
abi.phone()
