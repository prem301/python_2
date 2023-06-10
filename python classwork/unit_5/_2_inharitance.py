class A:
    def displayA(self):
        print("my ")

class B(A):
    def displayB(self):
        print("name")



obj = B()
obj.displayA()
obj.displayB()