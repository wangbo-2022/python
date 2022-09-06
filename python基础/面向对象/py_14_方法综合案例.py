class Game(object):

    top_score = 0

    def __init__(self,name):
        self.player_name = name

    @staticmethod
    def show_help():
        print("帮助")

    @classmethod
    def show_top_score(cls):
        print("最高分是%d" % cls.top_score)


    def star_game(self):
        print("%s开始游戏啦..." % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("小明")
game.star_game()
