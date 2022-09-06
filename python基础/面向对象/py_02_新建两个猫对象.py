class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


Tom = Cat()
Tom.name = "tom"
print(Tom)

jerry = Cat()
print(jerry)

jerry2 = jerry
print(jerry2)


