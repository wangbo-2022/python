import pygame
from plane_sprites import *

pygame.init()

score_font = pygame.font.Font("./font/ChrustyRock-ORLA.ttf", 30)
write_font = (255, 255, 255)

class PlaneGame(object):
    """主游戏类"""
    def __init__(self):

        self.score = 0
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法创建精灵，精灵组
        self.__create_sprites()
        # 设置定时器时间-创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器时间-发射子弹 0.5s
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:
            # 设置刷新率
            self.clock.tick(FRAME_PER_SEC)

            # 事件监听
            self.__event_handler()

            # 碰撞检测
            self.__check_collide()

            # 更新绘制精灵组
            self.__update_sprites()

            score_surface = score_font.render("Score: %s" % str(self.score), True, write_font)
            self.screen.blit(score_surface, (10, 5))

            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加到敌机精灵组
                self.enemy_group.add(enemy)
                self.score += 10
                print(self.score)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 子弹摧毁敌机
        flag = pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
        # if flag:
        #     self.score += 1
        # 敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断是否有敌机撞到英雄
        if len(enemies) > 0:
            # 英雄牺牲
            self.hero.kill()
            # 退出游戏
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    @staticmethod
    def __game_over():

        pygame.quit()

        exit()


if __name__ == '__main__':

    game = PlaneGame()

    game.start_game()

