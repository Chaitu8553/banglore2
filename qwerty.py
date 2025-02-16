#Inheritance pgm...
//class person:
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
male.work()//
##Program (PythonPandasEx2.py)
#Program to demo Pandas series using Series() method
'''
import pandas as pd;
x=[10,20,30,40,50]
y=pd.Series(x)
print(y)
print(y[0]);
print(y[1]);
print(y[2]);
print(y[3]);
print(y[4]);
'''
# pandass accessing with our own labels....
import pandas as pd;
x=[10,20,30,40,50]
y=pd.Series(x,index=["a","b","c","d","e"])
print(y)
print(y["a"]);
print(y["b"]);
print(y["c"]);
print(y["d"]);
print(y["e"]);
