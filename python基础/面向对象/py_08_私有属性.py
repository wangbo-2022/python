class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print(("%s的年龄是%d") % (self.name, self.__age))


xiaofang = Women("小芳")

# print(xiaofang.__age)
# xiaofang.__secret()

print(xiaofang._Women__age)
xiaofang._Women__secret()
