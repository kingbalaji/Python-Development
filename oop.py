class Dog (object):
    def __init__(self,name, age):#self=instance calling
       self.name = name
       self.age= age #reference where it belongs

    def speak(self) :
        print("this is dog:",self.name,'and i am ',self.age )

    def talk (self):
         print('Bark')

class Cat (Dog):
    def speak(self, name , age, color):
      super().__init__(name,age)
      self.color = color

    def talk(self):
         print('Hello')

tim = Dog('tim', 84, 'red') #tim=instance
tim.talk()

fred = Cat('fred', 52, 'blue')
fred.talk()