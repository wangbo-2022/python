class Gun:
    def __init__(self, name):
        self.model = name
        self.counter = 0

    # def __str__(self):
    #     return "%s的弹夹有%d颗子弹" % (self.model, self.counter)

    def add_counter(self, counter):
        self.counter += counter

    def shoot(self):
        if self.counter <= 0:
            print("%s没有子弹了..." % self.model)
            return

        self.counter -= 1
        print("%s突突突【%d】..." %(self.model, self.counter))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    # def __str__(self):
    #     return "%s的%s还有%d颗子弹" % (self.name, self.gun.model, self.gun.counter)

    def fire(self):
        if self.gun is None:
            print("%s没有枪..." % self.name)
            return

        print("%s冲呀..." % self.name)
        self.gun.add_counter(50)
        self.gun.shoot()


ak47 = Gun("AK47")

xusanduo = Soldier("许三多")

xusanduo.gun = ak47

xusanduo.fire()
