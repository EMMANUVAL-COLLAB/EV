class person:
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname  = lname

    def printname(self):
        print(self.fname, self.lname)
    

p1 = person("johny", "Mcov")
p1.printname()

class student(person):
    pass

s = student("Hmaxa","Sutha")
s.printname()

