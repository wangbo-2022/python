import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载图像数据
bg = pygame.image.load("./images/background.png")
# 绘制图像
screen.blit(bg, (0, 0))
# 更新屏幕
pygame.display.update()

while True:
    pass

pygame.quit()
