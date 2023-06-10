class democlass:
    def __init__(self):
        print("welcome")     # constructer wo hota hai jisko call nahi karna padta , object banate hi wo autometic call ho jata hai 
    def showval(self,a,b):
       print(a + b)
        
    

obj = democlass()
obj.showval(10,20)