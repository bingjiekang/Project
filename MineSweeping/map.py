from random import randint
import pygame
from gameover import Over
from pygame.mixer import  *
from time import sleep
 
class Map:
    """管理游戏中出现的雷和数字"""

    def __init__(self, setting, covers, screen): #游戏参数，游戏的覆盖物，游戏界面
        pygame.mixer.init()
        self.setting = setting
        self.bg_color = self.setting.background_color
        self.screen = screen
        self.covers = covers

        #踩雷的背景音乐
        #self.boot=pygame.mixer.Sound('data/boot.wav')
        #self.boot.set_volume(0.2)

        #开始时全部初始为0，表示当前方块啥都没有,用来存放地雷和周围雷的个数
        self.maps = [[0 for _ in range(20)] for _ in range(20)]

        #状态转移数组，所有(x+moves[i][0], y+moves[i][1])表示包围坐标为(x, y)方块的另外8块方块，
        #用于随机产生地雷后更新它周围方块上的数字
        self.moves = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

        #存储当前需要被显示出来数字方块
        self.now_show = []

        #点击到地雷后结束游戏
        self.over = Over(self.screen)

        #随机生成游戏地图
        self._born_map()

    def _born_map(self):
        """随机生成地雷地图"""
        for i in range(40):
            x = randint(0, 19)
            y = randint(0, 19)
            while self.maps[x][y] != 0:
                x = randint(0, 19)
                y = randint(0, 19)
            self.maps[x][y] = 'X' #地雷用x标记
            self._connect_(x, y) #更新地雷周围的数字


    def _connect_(self, x, y):
        """更新地雷周围数字的函数"""
        for cur in self.moves:
            i = x + cur[0]
            j = y + cur[1]
            if i >= 0 and i < 20 and j >= 0 and j < 20 and self.maps[i][j] != 'X':
                self.maps[i][j] += 1

    def add(self, x, y):  #传入当前鼠标点击的位置，判断合法性，合法则将对应的方块左边传入要展示的列表中
        i = x // 25
        j = y // 25
        if i >= 0 and i < 20 and j >= 0 and j < 20:
            self.now_show.append([i, j])
            if self.maps[i][j] == 0:
                self._add_connect_(i, j)

        #如果当前点击到了地雷，将地雷标记为红色方块，并展示出来，暂停游戏3秒，自动退出游戏
        if self.maps[i][j] == 'X':
            # # 如果当前点击到了地雷，将地雷标记为红色方块，并展示出来
            # pygame.draw.rect(self.screen, (255, 0, 0), ((i * 25, j * 25), (25, 25)))
            # 点错后将其他地雷也标记出来
            for i_x in range(20):
                for j_y in range(20):
                    if self.maps[i_x][j_y] == 'X':
                        pygame.draw.rect(self.screen, (201,0,22), ((i_x * 25, j_y * 25), (25, 25)))
            # 如果当前点击到了地雷，将地雷标记为红色方块，并展示出来
            pygame.draw.rect(self.screen, (255, 0, 0), ((i * 25, j * 25), (25, 25)))
            
            #暂停游戏3秒，自动退出游戏
            self.over.show()
        
        # 如果全部排出地雷则获胜并显示
        #print(len(self.covers.covers),self.covers.istage)
        if self.covers.istage:
            for i_x in range(20):
                for j_y in range(20):
                    if self.maps[i_x][j_y] == 'X':
                        pygame.draw.rect(self.screen, (144,238,144), ((i_x * 25, j_y * 25), (25, 25)))
            self.over.show2()
        
        
        

    # 宽度搜索将(x,y)周围相连的空白方块也展示出来
    def _add_connect_(self, x, y):
        que = []
        que.append([x, y])
        while que:
            cur = que[-1]
            del (que[-1])
            for k in range(8):
                i, j = cur[0] + self.moves[k][0], cur[1] + self.moves[k][1]
                if i >= 0 and i < 20 and j >= 0 and j < 20 and self.maps[i][j] != 'X' and [i,j] not in self.now_show:
                    self.now_show.append([i, j])
                    self.covers.delete(i * 25, j * 25)
                    if self.maps[i][j]==0:
                        que.append([i, j])

    def show(self):
        """将生成的地图展现到屏幕上"""
        for cur in self.now_show:
            i = cur[0]
            j = cur[1]
            if self.maps[i][j] == 0:
                continue
            else:
                self.msg = str(self.maps[i][j])
                self.font = pygame.font.SysFont(None, 45)
                self.font_image = self.font.render(self.msg, True, (60, 0, 0),None)
                self.image_ract = self.font_image.get_rect()
                self.image_ract.x = i * 25
                self.image_ract.y = j * 25
                self.image_ract.width = 24
                self.image_ract.height = 24
                self.screen.blit(self.font_image, self.image_ract)
