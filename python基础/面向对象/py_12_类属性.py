class Tool(object):

    count = 0

    @classmethod
    def show_tool_count(cls):
        print(cls.count)

    def __init__(self, name):
        self.name = name

        Tool.count += 1




tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

tool1.count = 1

print(Tool.count)
print(tool1.count)

Tool.show_tool_count()


