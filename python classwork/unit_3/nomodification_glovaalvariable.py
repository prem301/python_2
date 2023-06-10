#No modification in global variable id made
def add_gv(a,b):
    c=a+b+gv
    print("in function value of gv is =",gv)
    print("The addition is :",c)
    
gv=100                # gloval variable , function ke bahar ya andar har jagah gv ka value 100 hi rahega 
print("The initial value of gv =", gv)
add_gv(10,20)
print("After function value of gv =",gv)



















