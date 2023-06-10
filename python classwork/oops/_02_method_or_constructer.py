class democlass:
    a = 10
    def showvalue(self):
        print(self.a)
        self.c = self.a*self.a
        print(self.c)

    def showvalue1(self):
        print("welcome")

obj = democlass()
obj.showvalue()
obj.showvalue1()

print(obj.a)