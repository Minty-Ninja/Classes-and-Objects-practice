#Defining a class- Always start with writing class followed by name
class person():
    name = ''
    age = 0
    city = ''
    #Defining a constructor
    def __init__(self):#self is a pointer to the person
        print("Hello World")
    def ofni(self):
        self.name=input("What is ur name")
        self.age=int(input("What is your age"))
        self.city=input("What is your city?")
    def tou(self):
        print("Your name is",self.name)
        print("Your age is",self.age)
        print("Your city is", self.city)
    
#object creation
o1 = person()
o2= person()
o1.ofni()
o1.tou()
o2.ofni()
o2.tou()
    

    