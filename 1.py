class Car():
    name = ''
    model=''
    year=''
    colour=''
    def __init__(self, name, model, year, colour):
        self.name=name
        self.model=model
        self.year=year
        self.colour=colour
    def info(self):
        self.name=input("What is the Name?")
        self.model=input("Model Number?")
        self.year=input("Year of Production")
        self.colour=input("What is the colour")
    def out(self):
        print("The name is",self.name)
        print("The model is",self.model)
        print("The year is",self.year)
        print("The colour is",self.colour)
    
o1 = Car('Koeniggsegg Jesko Absolut','G39E series','2023','Black')
o2=Car('Devil 16 V12', '56B2', '2019','Red')
o1.info()
o2.info()
o1.out()
o2.out()


        


