class animal():
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class birds(animal):
    def sound(self):
        print("birds sing")
        
d1 = dog()
d1.sound()

d2 = birds()
d2.sound()
