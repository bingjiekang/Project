import sys  #结束游戏
from time import sleep  #暂停游戏
 
import pygame
 
 
class Over:
    """控制游戏结束的类"""
    def __init__(self, screen): #游戏主界面
        self.is_over = False
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # 踩到炸弹
        self.msg = 'GAME OVER'
        #渲染文字'GAME OVER'到游戏主界面上
        self.font = pygame.font.SysFont(None, 48)
        self.image = self.font.render(self.msg, True, (255, 0, 0), (254,254,254))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center  #将文字放在界面中心

        # 排出所有炸弹
        self.msg2 = 'GAME WIN'
        #渲染文字'GAME WIN'到游戏主界面上
        self.image2 = self.font.render(self.msg2, True, (0, 255, 0), (254,254,254))
        self.rect2 = self.image2.get_rect()
        self.rect2.center = self.screen_rect.center #放在界面中心


    def show(self):  #遇见炸弹，游戏结束，结束前将玩家遇到的炸弹标记为红色方块,其他炸弹标记为粉红,并在结束前绘制出来
        self.screen.blit(self.image, self.rect)
        pygame.display.update()
        sleep(3)
        sys.exit()

    def show2(self): #全部排出
        self.screen.blit(self.image2, self.rect2)
        pygame.display.update()
        sleep(3)
        sys.exit()