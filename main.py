#class Animal:
    #def sound(self):
        #pass
#class Dog(Animal):
    #def sound(self):
        #return "ГАВ"
#class Cat(Animal):
    #def sound(self):
        #return "МЯУ"
#class Cow(Animal):
    #def sound(self):
        #return "МУ"

#def speak(an):
    #print(an.sound())
#a1=Dog()
#a2=Cat()
#a3=Cow()
#speak(a1)
#speak(a2)
#speak(a3)




class Avto:
    def speed(self):
        pass
class Avto1(Avto):
    def speed(self):
        return "10"
class Avto2(Avto):
    def speed(self):
        return "20"
class Avto3(Avto):
    def speed(self):
        return "30"

def printspeed(an):
    print(an.speed())
printspeed(Avto1())
printspeed(Avto2())
printspeed(Avto3())