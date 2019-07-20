class Base:
    def test(self):
        print("base...")

class A(Base):
    def test(self):
        print("A")

class B(Base):
    def test(self):
        print("B")

class C(B,A):
    pass

c = C()
c.test()

print(C.__mro__)
