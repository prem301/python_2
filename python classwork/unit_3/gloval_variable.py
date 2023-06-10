'''x = 10        # global variable 

def my_function():
    y = 5    # local valriable 
    print(y)

my_function()
print(x)      # x global variable hai to yaha per print hoga 
#print(y)    #   this will cause an error because y is a local variable and is not accessible outside of the function'''




x = 10
def my_function():
    global y        # now y become global variable so we can use y outside the function also 
    y = 5      
    print(y)

my_function()
print(x)      # x global variable hai to yaha per print hoga 
print(y)    # aur y bhi gloval variable ban chucka hai to yaha y print hoga 

