class Cat:

    def __init__(self, new_name):
        self.name = new_name
        print("%s幸会幸会" % self.name)

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)

    def __del__(self):
        print("%s江湖再见" % self.name)

    def __str__(self):
        return "我是小猫【%s】" % self.name


Tom = Cat("tom")
# print(Tom.name)
# Tom.eat()
# Tom.drink()
print(Tom)

Jerry = Cat("jerry")
# print(Jerry.name)
# Jerry.eat()
# Jerry.drink()
print(Jerry)

del Tom
print("-"*50)

