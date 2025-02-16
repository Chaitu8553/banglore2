#Inheritance pgm...
class person:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class chaitu(person):
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
        
male=chaitu()
male.flirt()
male.work()