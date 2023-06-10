class sample:      #  sample is a  class
    def instance_method(self):  # method with first argument 'self' is instance method 
        print("in instance method") 
    def class_method():     # method without self parameter is class method 
        print("in class method")

s = sample()      # yaha per 's' is object that is it is a instance of a class 
s.instance_method()      # instance method is accessed using object
sample.class_method()      # class method is accessed using class name 
















