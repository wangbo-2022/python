class A:

    def test(self):
        print("A --- test 方法")

    def demo(self):
        print(("A --- demo 方法"))


class B:

    def test(self):
        print("B --- test 方法")

    def demo(self):
        print(("B --- demo 方法"))


class C(A, B):

    pass


class D(B, A):

    pass


c = C()
d = D()

c.test()
c.demo()
d.test()
d.demo()

print(C.__mro__)
print(D.__mro__)
