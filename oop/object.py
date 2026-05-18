# class Tv:
#     def On(self):
#         print("Tv on....")

# class Fan:
#     def On ( self):
#         print("Fan on....")

# class Mixi:
#     def On (self):
#         print("Mixi on....")

# tv=Tv()
# fan=Fan()
# mixi=Mixi() 
    
# tv.On()
# fan.On()
# mixi.On()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil",12)

print(p1.name)
print(p1.age)