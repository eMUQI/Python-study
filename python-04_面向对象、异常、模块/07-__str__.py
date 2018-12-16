class Human:
    
    def __init__(self,s,n):             #类似构造函数
        print("crteating...")
        self.sex = s
        self.name = n
    def __str__(self):
        return "i am %s, i am a %s"%(self.name,self.sex)
    def print1(self):               #必须有“self”?
        print("i am a human !")
    def print2(self):
        if(self.sex=='man'):
            print("i am a man !")
        if(self.sex=="woman"):
            print("i am a woman !")

A = Human("man","jack")
#A.sex = "man"

A.print1()
A.print2()
print(A)


B = Human("woman","jason")
#B.sex = "woman"

B.print1()
B.print2()
print(B)
