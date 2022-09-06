class Cat:

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


Tom = Cat()
Tom.name = "tom"
Tom.eat()
Tom.drink()
print(Tom)

jerry = Cat()
jerry.name = "Jerry"
jerry.eat()
jerry.drink()
print(jerry)


