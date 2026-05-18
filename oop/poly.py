class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model= model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self,brand,model):
        self.brand =brand
        self.model = model

    def move(self):
        print("self")

class plane1:
    def __init__(self,brand,moidel):
        self.brand =brand
        self.model=moidel

    def move(self):
        print("flyl")

car1= Car("must","uganh")
boat1=Boat("ibi","dfkdfkdsl")
plane= plane1("boeing","3232")


for x in (car1,boat1,plane):
    x.move()
