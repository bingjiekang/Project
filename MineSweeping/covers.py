import pygame
from gameover import Over

class Cover:
    """管理游戏覆盖物的类"""
    def __init__(self, setting,screen):  #游戏参数设置和游戏主界面
        self.setting = setting
        self.screen = screen
        self.over = Over(screen)
        self.covers = []  # 存储未被点击过的方块的覆盖物的位置
        self.istage = False
        for i in range(20):
            for j in range(20):
                self.covers.append([i, j])  #刚开始时整个界面都是被覆盖的


    def delete(self, x, y):  #传入单机鼠标的位置，判断是否合法，如果是，删除当前方块
        x = x // 25
        y = y // 25
        if [x, y] in self.covers:
            self.covers.remove([x, y])
        if len(self.covers) == 40:
            self.istage = True


    def show(self):  #将所有未被点击过的方块展现出来
        for cur in self.covers:
            pygame.draw.rect(self.screen, self.setting.screen_color, ((cur[0] * 25, cur[1] * 25), (24, 24)))