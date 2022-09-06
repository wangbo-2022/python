import pygame

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
screen.blit(hero, (200, 600))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

i = 0
# 游戏循环
while True:
    clock.tick(60)
    print(i)
    i += 1

pygame.quit()
