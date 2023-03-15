import sys   #调用exit()函数来结束游戏
import pygame
from covers import Cover    #未点击方块时表面的覆盖物
from map import Map   #游戏方块里面的地图
from settings import setting  #游戏参数设置
 
 
class Game:
    """管理游戏的主程序"""

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.setting = setting()

        #创立游戏主界面
        self.screen = pygame.display.set_mode(self.setting.screen_size)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('扫雷')

        self.covers = Cover(self.setting, self.screen )  #表面覆盖物
        self.maps = Map(self.setting, self.covers, self.screen)  # 内部地图

        #背景音乐
        #pygame.mixer.music.load('data/bgmusic.wav')
        #pygame.mixer.music.play()
        #pygame.mixer.music.fadeout(3)



    def run_game(self):
        while True:
            #if not pygame.mixer.music.get_busy():
            #       pygame.mixer.music.play()
            self._event_check_()  #检测事件
            self._update_screen_()  #更新屏幕

    def _event_check_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #结束游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()  #检测到单击鼠标事件，将鼠标的位置传入
                self.covers.delete(x, y) #删除对应方块上的覆盖物
                self.maps.add(x, y)  #将该位置的覆盖物下的游戏地图加入即将要显示的队伍中

    def _update_screen_(self):
        self.screen.fill(self.setting.background_color) #填充背景颜色
        for i in range(25): #绘制方格
            pygame.draw.line(self.screen, self.setting.line_color, [0, i * 25], [500, i * 25],
                             self.setting.line_width) #横线
            pygame.draw.line(self.screen, self.setting.line_color, [i * 25, 0], [i * 25, 500],
                             self.setting.line_width) #竖线

        #self.covers.show() #将还没有被点击过的数字展现出来
        self.maps.show()   #将所有被点击过的方格下的数字展现出来
        self.covers.show() #将还没有被点击过的数字展现出来

        pygame.display.update()  #更新屏幕显示，将上面所做的工作展现在游戏界面上


if __name__ == '__main__':
    my_game = Game()
    my_game.run_game()