class Student:

    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight

    def __str__(self):
        return "大家好，我是【%s】，我的体重是【%.2f】" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步，跑步能锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s是个吃货，吃饱了再减肥" % self.name)
        self.weight += 1.0

xiaoming = Student("小明", 75.0)

xiaoming.eat()
xiaoming.run()

print(xiaoming)
