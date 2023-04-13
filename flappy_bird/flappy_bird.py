import pygame                               #导入模块
import sys
import random

class Bird(object):                         #创建小鸟类
    """定义一个小鸟类"""                      #对类的一个描述
    def __init__(self):                     #初始化
        """定义初始化方法"""
                                            #获取小鸟的矩形坐标
        self.birdRect=pygame.Rect(65,50,50,50)
        self.birdstatus=[pygame.image.load("1.png"),
                         pygame.image.load("2.png"),
                         pygame.image.load("dead.png")]
        self.status=0                       #默认状态
        self.birdx=120                      #小鸟的x轴坐标
        self.birdy=200                      #小鸟的y轴坐标
        self.jump=False                     #用来判断小鸟是否跳跃
        self.jumpspeed=10                   #向上跳跃的速度
        self.gravity=5                      #向下自由落体的初始速度
        self.dead=False                     #用来判断小苗是否死亡

    def birdUpdate(self):                   #移动的方法
        """定义移动方法"""
        if self.jump==True:                 #也可以省略==True
            self.jumpspeed-=1               #由于向上受到空气阻力，速度减少
            self.birdy-=self.jumpspeed      #y轴坐标的变化
        else:                               #没有跳跃，则向下运动
            self.gravity +=  0.18           #重力的作用下，速度增加
            self.birdy += self.gravity      #y轴坐标增加
        self.birdRect[1]=self.birdy         #小鸟的矩形坐标y

class Pipeline(object):                     #创建一个管道类
    """定义一个管道类"""                      #对类的一个描述
    def __init__(self):                     #初始化
        """定义初始化方法"""
        self.walkx=400                      #管道的x轴坐标
                                            #下载管道的两张图片
        self.pineUp=pygame.image.load("top.png")
        self.pineDown=pygame.image.load("bottom.png")
    def updatePipeline(self):
        """水平移动"""
        self.walkx-=7                       #管道向左移动
        #当管道运动到一定位置后，即小鸟通过管道，分数加一，并且重置管道
        if self.walkx<=80:
            global score                    #全局变量
            score+=1
            self.walkx=width                #重新调整位置

def createMap():                            #用来更新地图的函数
    """定义创建地图的方法"""
    screen.blit(background,(0,0))           #用一个图片来填充背景，第二个参数数位置坐标

    #显示管道
    screen.blit(Pipeline.pineUp,(Pipeline.walkx,-50))
    screen.blit(Pipeline.pineDown,(Pipeline.walkx,420))
    Pipeline.updatePipeline()               #移动管道

    #显示小鸟
    if bird.dead:                           #如果小鸟死亡
        bird.status=2                       #小鸟变为死亡状态
    elif bird.jump:                         #发生跳跃事件
        bird.status=1

    screen.blit(bird.birdstatus[bird.status],(bird.birdx,bird.birdy))
    bird.birdUpdate()                       #移动小鸟
    #显示分数
    screen.blit(font.render("your score;"+str(score),-1,(255,255,255)),(100,50))

    # 更新更新屏幕，与pygame.display.update()方法相同，如果update后面有参数，则更新那个对象
    pygame.display.update()  # 更新整个屏幕

def checkDead():
    #判断小鸟是否死亡
    upRect=pygame.Rect(Pipeline.walkx,-50,Pipeline.pineUp.get_width(),Pipeline.pineUp.get_height())
    downRect=pygame.Rect(Pipeline.walkx,420,Pipeline.pineDown.get_width(),Pipeline.pineDown.get_height())
    #检测是否碰撞
    if upRect.colliderect(bird.birdRect)or downRect.colliderect(bird.birdRect):
        bird.dead=True

    #检测是否超出边界
    if not 0<bird.birdRect[1]<height:
        bird.dead=True
        return True                         #小鸟死亡，则返回True
    else:
        return False

def getResult():
    #获取总分
    final_text1="Game Over"
    final_text2="Your final score is ;"+str(score)
    fit_font=pygame.font.SysFont("Arial",70)
    ft1_surf=font.render(final_text1,1,(242,3,36))       #第3个参数RGB颜色值
    ft2_font=pygame.font.SysFont("Arial",50)
    ft2_surf=font.render(final_text2,1,(30,177,6))

    screen.blit(ft1_surf,[screen.get_width()/2-ft1_surf.get_width()/2,100])
    screen.blit(ft2_surf,[screen.get_width()/2-ft2_surf.get_width()/2,300])
    pygame.display.update()

if __name__=="__main__":                    #主程序入口
    """主程序"""
    pygame.init()                           #初始化pygame
    pygame.font.init()                      #初始化字体
    font=pygame.font.SysFont(None,50)       #设置默认字体和大小
    size=width,height=600,525               #屏幕的大小
    screen=pygame.display.set_mode(size)    #设置屏幕
    clock=pygame.time.Clock()               #引入时间，降低cpu的处理速度
    color=(255,255,255)                     #设置颜色

    bird=Bird()                             #实例化对象
    score=0
    Pipeline=Pipeline()
    while True:                             #创建一个死循环，使屏幕一直存在
        clock.tick(60)                      #设置CPU每秒处理（）次
        """轮询事件"""
        for event in pygame.event.get():    #所有的事件
            if event.type==pygame.QUIT:
                sys.exit()                  #退出pygame

                                            #单击鼠标，发生相关事件，使小鸟产生跳跃
        if event.type==pygame.MOUSEBUTTONDOWN and not bird.dead:
            bird.jump=True
            bird.gravity=5                  #由于发生跳跃，重力加速度变为零
            bird.jumpspeed=10               #重新调整向上的跳跃速度

        #screen.fill(color)                 #填充颜色
                                            #加载背景图片
        background=pygame.image.load("background.png")
        if checkDead():
            getResult()
        else:
            createMap()                         #调用函数

    #pygame.quit()                           #关闭pygame


