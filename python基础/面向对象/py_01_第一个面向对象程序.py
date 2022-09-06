class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


Tom = Cat()
Tom.eat()
Tom.drink()

print(Tom)

print("%x" % id(Tom))
