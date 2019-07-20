class Human:
    
    def __init__(self,s):             #类似构造函数
        print("crteating...")
        self.sex = s

    def print1(self):               #必须有“self”?
        print("i am a human !")
    def print2(self):
        if(self.sex=='man'):
            print("i am a man !")
        if(self.sex=="woman"):
            print("i am a woman !")

A = Human("man")
#A.sex = "man"

A.print1()
A.print2()

B = Human("woman")
#B.sex = "woman"

B.print1()
B.print2()
