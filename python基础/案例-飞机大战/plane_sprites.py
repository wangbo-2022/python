import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率常量
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):

        # 调用父类的初始化方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        self.rect.y += self.speed


class Backgroud(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 调用父类方法
        super().__init__("./images/background.png")
        # 判断是不是交替图像
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法
        super().update()

        # 判断是否移出屏幕
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法
        super().__init__("./images/enemy1.png")
        # 随机速度
        self.speed = random.randint(1, 3)
        # 随机水平位置
        self.rect.x = random.randint(0, (SCREEN_RECT.width - self.rect.width))
        # 垂直位置
        self.rect.bottom = 0

    def update(self):
        # 调用父类方法
        super().update()
        # 判断是否飞出屏幕
        if self.rect.y > SCREEN_RECT.height:
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 调用父类方法
        super().__init__("./images/me1.png", 0)
        # 指定初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):

        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            # 创建精灵子弹
            bullet = Bullet()
            # 调整子弹位置
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - 20 * i
            # 添加子弹
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 调用父类方法
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法
        super().update()
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

