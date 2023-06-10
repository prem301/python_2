class democlass:
     a = 10
     
     def sum(self):  # jab bhi hum class ke andar function bana rahe ho to usme self naam ka argunment pass karna padega, aur self argunment khudme ek object ka kaam karta hai
           print(20 +30)
    


demoobject = democlass()  # jab object banana hai to yaha per () defined karna hai 
print(demoobject.a)   # yaha per object ke through class me present variable ko call kar rahe hai   
demoobject.sum()
