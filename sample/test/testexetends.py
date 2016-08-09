class A():
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
    def out(self):
        print self.a,self.b,self.c
    def add(self):
        print self.a+12
class B(A):
    def __init__(self):
        self.a=1
        self.b=4
        self.c=8
    def out(self):
        print self.a,self.b,self.c

b=B()
b.out()
b.add()