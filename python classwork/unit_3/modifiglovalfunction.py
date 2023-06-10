#Modification in global variable is made
def add_gv(a,b):
    global gv          # here gv is a gloval variable , to gv ka value har jagah 150 hi rahega , function ke andar ya bahar 
    gv=150
    print(gv)
    c=a+b+gv
    return c
    
gv=100
print(gv)
x=add_gv(10,20)
print(x)
print(gv)