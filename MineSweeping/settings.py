class setting:
    """管理游戏中的参数的类"""
    def __init__(self):
        self.screen_size = (500, 500)  # 屏幕大小
        self.background_color = (255, 255, 255)  # 背景色
        self.line_width = 1  # 线条粗细
        self.line_color = (120, 120,120)  # 线条颜色
        self.block_width = 24 #每一个方格的宽度
        self.screen_color = (150, 150, 150)  # 展示界面的颜色