class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")

v1=car()
v1.start()
