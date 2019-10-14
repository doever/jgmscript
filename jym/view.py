import os
import tkinter as tk
from tkinter import messagebox as mes
from tkinter import ttk
import threading
from datetime import datetime

import webbrowser

from jym.css import Css
from jym.backed import *


class JYMView():
    def __init__(self):
        self.top = tk.Tk()
        # self.top.update_idletasks()
        # self.top.overrideredirect(True) #无标题栏
        # self.top.attributes("-alpha", 0.9)  # 窗口透明度60 %
        self.top.resizable(False, False)  # 不可拉伸
        self.init_view()
        self.top.mainloop()

    def _create_tab_control(self):
        '''创建视图分离控制器'''
        self.tabControl = ttk.Notebook(self.top)
        self.tabControl.pack(expand=5, fill="both")

        self.index_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.index_tab, text='首页')

        # self.config_tab = ttk.Frame(self.tabControl)
        # self.tabControl.add(self.config_tab, text='配置坐标')

        self.about_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.about_tab, text='说明')

    def _set_title(self, _title):
        self.top.title(_title)

    def _create_menu(self):
        '''菜单相关'''
        menuBar = tk.Menu(self.top)
        self.top.config(menu=menuBar)
        # 增加主题
        # 第一个菜单
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="修改配置", command=self.listen_config_event)
        fileMenu.add_separator()
        fileMenu.add_command(label="升级链接", command=self.update_program)
        fileMenu.add_separator()
        fileMenu.add_command(label="使用说明", command=self.instructions)
        fileMenu.add_separator()
        # fileMenu.add_command(label="意见反馈", command=self.listen_feedback_event)
        # fileMenu.add_separator()
        fileMenu.add_command(label="退出程序", command=self.listen_quit_event)
        menuBar.add_cascade(label="系统", menu=fileMenu)

    def index_view(self):
        '''首页-主页面'''
        title = tk.Label(self.index_tab, text="家国梦脚本", fg=Css.Color['main_color'], font=('Comic Sans MS', 16))
        title.pack()
        tk.Label(self.index_tab, text='-----------------------------------', font=('', 10)).pack()
        self.start_button = tk.Button(self.index_tab, Css.Button['primary_btn'], text="启动", command=self.listen_start_event)
        self.start_button.place(x=46, y=210)

        # 模式选择框
        tk.Label(self.index_tab, text='选择功能').place(x=10, y=52)
        self.mode = tk.StringVar()
        self.mode.set('1')
        tk.Radiobutton(self.index_tab, variable=self.mode, value='1', text='卸货').place(x=65, y=50)
        tk.Radiobutton(self.index_tab, variable=self.mode, value='2', text='开红包').place(x=120, y=50)
        tk.Radiobutton(self.index_tab, variable=self.mode, value='3', text='开相册').place(x=180, y=50)
        # 附加功能复选框
        self.auto_money = tk.IntVar()
        self.auto_level = tk.IntVar()
        self.all_cargo = tk.IntVar()
        self.auto_money.set(0)
        self.auto_level.set(0)
        self.all_cargo.set(0)
        tk.Checkbutton(self.index_tab, text='自动收集金币', variable=self.auto_money, onvalue=1, offvalue=0).place(x=63, y=80)
        tk.Checkbutton(self.index_tab, text='自动升级建筑', variable=self.auto_level, onvalue=1, offvalue=0).place(x=63, y=110)
        tk.Checkbutton(self.index_tab, text='卸所有类型货物', variable=self.all_cargo, onvalue=1, offvalue=0).place(x=63, y=140)
        # 数量值
        tk.Label(self.index_tab, text='红包个数',).place(x=10, y=175)
        self.blue_package = tk.Entry(self.index_tab, bd=0, bg='white', width=3)
        self.purple_package = tk.Entry(self.index_tab, bd=0, bg='white', width=3)
        self.epic_package = tk.Entry(self.index_tab, bd=0, bg='white', width=3)
        tk.Label(self.index_tab, text='相册个数', ).place(x=150, y=175)
        self.photo_count = tk.Entry(self.index_tab, bd=0, bg='white', width=4)
        self.blue_package.place(x=65, y=177)
        self.purple_package.place(x=93, y=177)
        self.epic_package.place(x=121, y=177)
        self.photo_count.place(x=205, y=177)

    def config_view(self):
        '''配置页面'''
        # def get_coord():
        #     coord = {
        #         'building1': (building1x.get(), building1y.get()),
        #         'building2': (building2x.get(), building2y.get()),
        #         'building3': (building3x.get(), building3y.get()),
        #         'building4': (building4x.get(), building4y.get()),
        #         'building5': (building5x.get(), building5y.get())
        #     }
        #     return coord
        #
        # canvas_export = tk.Canvas(self.config_tab, height=240, width=240)
        # canvas_export.pack()
        # canvas_export.create_rectangle(0, 0, 240, 240, fill="white")
        #
        # title = tk.Label(self.config_tab, text="配置坐标", fg=Css.Color['main_color'], bg='white', font=('Comic Sans MS', 16))
        # title.place(x=150, y=2)
        #
        # canvas_export.create_text(40, 70, text='建筑1坐标', fill="#2f2f2f", font=Css.TEXT_FONT)
        # building1x = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building1x.place(x=80, y=60)
        # building1y = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building1y.place(x=150, y=60)
        #
        # canvas_export.create_text(40, 100, text='建筑3坐标', fill="#2f2f2f", font=Css.TEXT_FONT)
        # building2x = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building2x.place(x=80, y=90)
        # building2y = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building2y.place(x=150, y=90)
        #
        # canvas_export.create_text(40, 130, text='建筑7坐标', fill="#2f2f2f", font=Css.TEXT_FONT)
        # building3x = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building3x.place(x=80, y=120)
        # building3y = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building3y.place(x=150, y=120)
        #
        # canvas_export.create_text(40, 160, text='货物1坐标', fill="#2f2f2f", font=Css.TEXT_FONT)
        # building4x = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building4x.place(x=80, y=150)
        # building4y = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building4y.place(x=150, y=150)
        #
        # canvas_export.create_text(40, 190, text='货物2坐标', fill="#2f2f2f", font=Css.TEXT_FONT)
        # building5x = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building5x.place(x=80, y=180)
        # building5y = tk.Entry(self.config_tab, bd=2, highlightcolor=Css.Color['main_color'], width=8)
        # building5y.place(x=150, y=180)
        #
        # config_button = tk.Button(self.config_tab, Css.Button['danger_btn'], text='配置', command=None)
        # config_button.place(x=55, y=220)
        pass

    def about_view(self):
        '''说明页'''
        canvas_export = tk.Canvas(self.about_tab, height=240, width=240)
        canvas_export.pack()
        canvas_export.create_rectangle(0, 0, 240, 240, fill="#eee")
        tk.Label(self.about_tab, text="使用说明", fg=Css.Color['main_color'], font=('Comic Sans MS', 16)).place(x=15, y=10)
        tk.Label(self.about_tab, text="* 使用前请先看下使用说明",).place(x=15, y=50)
        tk.Label(self.about_tab, text="* 配置文件请放在C盘根路径").place(x=15, y=75)
        tk.Label(self.about_tab, text="* 小屏用户需要修改配置.ini文件,请将").place(x=15, y=100)
        tk.Label(self.about_tab, text="  small_simulator值修改为yes").place(x=15, y=125)

    def init_view(self):
        '''初始化视图'''
        self._set_title('家园梦自动卸货2.0')
        self._create_menu()
        self._create_tab_control()
        self.index_view()
        # self.config_view()
        self.about_view()

    # 事件区
    def get_user_input(self):
        user_input = {
            'mode': self.mode.get(),
            'auto_money': self.auto_money.get(),
            'auto_level': self.auto_level.get(),
            'all_cargo': self.all_cargo.get(),
            'blue_package': self.blue_package.get(),
            'purple_package': self.purple_package.get(),
            'epic_package': self.epic_package.get(),
            'photo_count': self.photo_count.get()
        }
        return user_input

    def listen_start_event(self):
        '''开始任务'''
        self.start_button.config(Css.Button['danger_btn'], text='暂停', command=self.listen_pause_event)
        print(f"{datetime.now()}:任务开始")
        user_input = self.get_user_input()
        global event
        event = threading.Event()
        event.clear()  # event值设置为False
        task_thread = threading.Thread(target=back_task, name='TaskThread', args=(event, user_input))
        task_thread.start()

    def listen_pause_event(self):
        '''暂停任务'''
        self.start_button.config(Css.Button['primary_btn'], text='启动', command=self.listen_start_event)
        event.set()  # event值设置为True

    def listen_quit_event(self):
        self.top.quit()
        exit()

    @staticmethod
    def listen_config_event():
        os.system("start c:/config.ini")

    @staticmethod
    def update_program():
        try:
            webbrowser.open('https://github.com/doever/jgmscript/tree/master/download')
        except:
            print('打开Url发生错误,升级下载地址为：https://github.com/doever/jgmscript/tree/master/download')

    @staticmethod
    def instructions():
        try:
            webbrowser.open('https://github.com/doever/jgmscript/blob/master/download/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md')
        except:
            print('打开Url发生错误,地址为：https://github.com/doever/jgmscript/blob/master/download/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md')

    @staticmethod
    def listen_feedback_event():
        try:
            webbrowser.open('https://github.com/doever/jgmscript/blob/master/vx.png')
        except:
            print('打开Url发生错误,地址为：https://github.com/doever/jgmscript/blob/master/vx.png')


def back_task(event, user_input):
    while 1:
        if event.isSet():
            print(f"{datetime.now()}:任务暂停")
            break
        main(user_input)
        time.sleep(1)


if __name__ == '__main__':
    t = JYMView()



