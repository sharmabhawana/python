#Polymorphism
class Dog:
    def speak(self):
        print("Dog Barks")
class Cat:
    def speak(self):
        print("Cat meow")
def Sound(obj):
    obj.speak()
d=Dog()
Sound(d)
c=Cat()
Sound(c)