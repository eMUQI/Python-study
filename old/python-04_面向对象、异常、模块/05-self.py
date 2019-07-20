class Human:
    def print1(self):           #必须有“self”?
        print("i am a human !")
    def print2(self):
        if(self.sex=='man'):
            print("i am a man !")
        if(self.sex=="woman"):
            print("i am a woman !")

A = Human()
A.sex = "man"

B = Human()
B.sex = "woman"

A.print1()
A.print2()
B.print1()
B.print2()
