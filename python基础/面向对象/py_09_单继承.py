class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):

    def bark(self):
        print("汪")


class XiaoTianQuan(Dog):

    def fly(self):
        print(("我会飞"))

    def bark(self):
        print(("我会说话"))

        super().bark()
        Dog.bark(self)

        print("我们不一样")


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


xtq = XiaoTianQuan()

# xtq.eat()
# xtq.drink()
# xtq.run()
# xtq.sleep()
xtq.bark()
# xtq.fly()
# xtq.catch()
