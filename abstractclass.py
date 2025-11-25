#ovverride in inheritance
'''from abc import ABC,abstractclassmethod
class MediaPlayer(ABC):
    def playAudio(self):
        print("Can play Audio")
    @abstractclassmethod
    def playVideo(self):
        pass
class SoundRecorder(MediaPlayer):
    def playVideo(self):
        print("I can't play video")
class VLCPlayer(MediaPlayer):
    def playVideo(self):
        print("I can play video")
sr=SoundRecorder()
sr.playAudio()
sr.playVideo()
vlc=VLCPlayer()
vlc.playAudio()
vlc.playVideo()
from abc import ABC,abstractclassmethod
class Bird:
    def speak(self):
        print("I can speak")
    @abstractclassmethod
    def fly(self):
        pass
class Parrot(Bird):
    def fly(self):
        print("i can fly")
class Penguin(Bird):
    def fly(self):
        print("I can't fly")
b=Bird()
b.speak()
b.fly()
p=Penguin()
p.speak()
p.fly()
    '''
from abc import ABC,abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def printArea(self):
        pass
    @abstractclassmethod
    def printPerimeter(self):
        pass
class triangle(Shape):
    def printArea(self,b,h):
        print("Area of triangle:",0.5*b*h)
    def printPerimeter(self,a,b,c):
        print("Perimeter of triangle:",a+b+c)
class Circle(Shape):
    def printArea(self,r):
        print("Area of Circle:",3.14*r*r)
    def printPerimeter(self,r):
        print("Perimeter of Circle:",2*3.14*r)
class Square(Shape):
    def printArea(self,a):
        print("Area of Square:",a*a)
    def printPerimeter(self,a):
        print("Perimeter of Square:",4*a)
t=triangle()
t.printArea(5,6)
t.printPerimeter(3,4,5)
c=Circle()  
c.printArea(7)
c.printPerimeter(7)
s=Square()
s.printArea(4)
s.printPerimeter(4)