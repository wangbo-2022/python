class A:

    def __init__(self):

        self.num1 = 10
        self.__num2 = 290

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test2(self):
        print("公有方法 %d %d" % (self.num1, self.__num2))
        self.__test()


class B(A):

    def demo(self):

        print(self.num1)
        # print(self.__num2)
        self.test2()
        # self.__test()


b = B()

b.demo()
