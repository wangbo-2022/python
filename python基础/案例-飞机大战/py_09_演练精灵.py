import pygame
from plane_sprites import *

# 游戏初始化
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
# pygame.display.update()

#绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))

# 更新屏幕图像
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环
while True:

    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():

        # 退出游戏
        if event.type == pygame.QUIT:

            pygame.quit()

            exit()

    # 修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)


    pygame.display.update()

pygame.quit()
