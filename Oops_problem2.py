
# The question is - make calculater class and find out square, qube, Squareroot.

class calculater:
    def __init__(self, n):
        self.n=n
         
    def square(self):
            print(f"this is square: {self.n*self.n}")
    
    def qube(self):
            print(f"this is qube: {self.n*self.n*self.n}")

    def squareroot(self):
            print(f"this is squareroot: {self.n**1/2}")


cal = calculater(5)
cal.square()
cal.qube()
cal.squareroot()

# Here solved a Oops problem base con calulation basics in different mode-

class Cal_number:

    def __init__(self, d, s):
        self.d = d
        self.s = s

    def a_number(self,a,b):
        print(f"{a+b} this is combine number {self.d}")
    
    def s_number(self,a,b):
        print(f"{a-b} this is not combine number {self.s}")
    
    def p_number(self,a,b):
        print(f"{a*b} this is double numbe {self.d}")
    
    def d_number(self,a,b):
        print(f"{a/b} this is half of number {self.s}")
    

n = Cal_number("Given value", "Taken value")
n.a_number(4,5)
n.s_number(16,4)
n.p_number(5,6)
n.d_number(10,5)

         