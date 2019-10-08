import time
import random
from pynput.mouse import Button, Controller
import win32gui, win32api, win32con
from win32api import GetSystemMetrics
from PIL import ImageGrab

from mouse_action import *

mouse = Controller()


def pil_image(x, y):
    a, b = GetSystemMetrics(0), GetSystemMetrics(1)  # Python获取屏幕分辨率
    im = ImageGrab.grab((0, 0, a, b))  # 与坐标不同，这里0，0，1，1是一个像素，而坐标是从0~1919的
    pix = im.load()
    return pix[x, y]


def color_like(colorA, colorB):
    '''判断两个颜色的RGB值是否相近'''
    is_like = False
    diff = (colorA[0] - colorB[0]) + (colorA[1] - colorB[1]) + (colorA[2] - colorB[2])
    if abs(diff) < 25:
        is_like = True
    return is_like


def init_mouse():
    '''
    初始化操作，确保不被其他弹窗影响
    :return:
    '''
    mouse.position = (1850, 850)
    mouse.click(Button.left, 1)
    print("初始化鼠标完成")


def mouse_move_2(src, dist):
    '''
    一次鼠标操作
    :paras: src:开始位置 dist：拖动后的位置
    :return:
    '''
    x = dist[0] - src[0]
    y = dist[1] - src[1]
    for i in range(4):
        mouse.position = src
        mouse.press(Button.left)
        time.sleep(0.2)
        mouse.move(x, y)
        time.sleep(0.2)
        mouse.click(Button.left, 1)
        mouse.release(Button.left)


def count_crood():
    '''计算坐标，需要把模拟器高度设置800，置于电脑右上角'''
    a, b = GetSystemMetrics(0), GetSystemMetrics(1)
    buildings = {
        "building1": (a-348, 313),
        "building2": (a-243, 265),
        "building3": (a-131, 200),
        "building4": (a-346, 421),
        "building5": (a-241, 376),
        "building6": (a-146, 324),
        "building7": (a-345, 521),
        "building8": (a-242, 475),
        "building9": (a-141, 426)
    }
    # 史诗建筑坐标，史诗建筑要求放在2，3，5,6,8,9位置上
    epic_buildings = {
        "building2": (a - 243, 265),
        "building3": (a - 131, 200),
        "building5": (a-241, 376),
        "building6": (a-146, 324),
        "building9": (a - 141, 426)
    }
    cargos = {
        "cargo1": (a-197, 691),
        "cargo2": (a-136, 656),
        "cargo3": (a-83, 624)
    }

    others = {
        "avator": (a-432, 70),
        "logout": (a-336, 605),
        "login": (a-328, 671)
    }

    return {
        "buildings": buildings,
        "epic_buildings": epic_buildings,
        "cargos": cargos,
        "others": others
    }







def find_window():
    '''定位模拟器的坐标'''
    window_name = '雷电模拟器'
    hwnd = win32gui.FindWindow(None, window_name)
    return win32gui.GetWindowRect(hwnd)  # 1330 11 1908 1009


def count_crood2():
    '''计算相对坐标'''
    left, top, right, bottom = find_window()
    buildings = {
        'building1': (left+150, top+380),  # (1480, 390),
        'building2': (left+270, top+300),  # (1600, 310),
        'building3': (left+400, top+240),  # (1730, 250),
        'building4': (left+150, top+510),  # (1480, 510),
        'building5': (left+270, top+450),  # (1600, 450),
        'building6': (left+400, top+390),  # (1730, 390),
        'building7': (left+150, top+630),  # (1480, 630),
        'building8': (left+270, top+580),  # (1600, 580),
        'building9': (left+400, top+510)   # (1730, 510)
    }
    epic_buildings = {

    }
    cargos = {
        'cargo1': (left+329, top+857),  # (1671, 881),
        'cargo2': (left+361, top+759),  # (1703, 783),
        'cargo3': (left+489, top+772)   # (1831, 796)
    }
    cargo_tag = {
        'cargo1': (left+294, top+818),  # (1636, 842),
        'cargo2': (left+372, top+777),  # (1714, 801),
        'cargo3': (left+449, top+734)   # (1791, 758)
    }
    others = {
        "avator": (left+28, top+66),    # (1370, 90),
        "logout": (left+152, top+755),  # (1494, 779),
        "login": (left+283, top+799),  # (1625, 823),
        "train": (left+257, top+880)   # (1599, 904)
    }
    return {
        "buildings": buildings,
        "epic_buildings": epic_buildings,
        "cargos": cargos,
        "cargo_tag": cargo_tag,
        "others": others
    }


def find_target_color(color, callback=lambda: None):
    '''
    找对应颜色
    :param color：RGB颜色元组(86,200,42)  callback:未找到颜色该做什么
    :return x,y：目标色块的坐标
    '''
    left, top, right, bottom = find_window()
    im = ImageGrab.grab((left, top, right, bottom))  # 与坐标不同，这里0，0，1，1是一个像素，而坐标是从0~1919的
    width, height = im.size
    pix = im.load()
    min_diff = 10
    crood = (0, 0)

    for x in range(width):
        for y in range(height):
            # diff = abs(color[0] - pix[x, y][0]) + abs(color[1] - pix[x, y][1]) + abs(color[2] - pix[x, y][2])
            r, g, b = pix[x, y]
            r_, g_, b_ = color
            diff = abs(r-r_) + abs(g-g_) + abs(b-b_)  # RGB像素差值
            if diff <= min_diff:
                crood = (x+left+50, y+top)
                print(f"在{crood}处找到颜色{pix[x, y]}与目标颜色{color}相似)")
                break
        # 内循环未break，继续外循环的下一次
        else:
            continue
        break

    # 外循环未break,说明没找到颜色的坐标
    else:
        print("没有发现相似度小于10的颜色")
        callback()
    return crood


def collect_money():
    '''收集金币'''
    buildings_crood = count_crood()['buildings']
    for building, crood in buildings_crood.items():
        mouse.position = crood
        mouse.click(Button.left, 1)
        print(f"已收集{building}金币")
        time.sleep(1)


def restat_game():
    '''重启游戏，提示效率，刷新火车'''
    others = count_crood()['others']
    # 点击头像
    mouse.position = others['avator']
    mouse.click(Button.left)
    time.sleep(1.5)
    # 点击退出
    mouse.position = others['logout']
    mouse.click(Button.left)
    time.sleep(5)
    # 点击登录，微信登录，需改成可以选择登录方式
    mouse.position = others['login']
    mouse.click(Button.left)


def is_train_come(coord):
    '''判断火车是否来了'''
    pass


def discharge_cargo(user_input):
    '''卸货'''
    epic_buildings_crood = count_crood()['buildings']
    epic_buildings_crood = count_crood()['epic_buildings']
    cargos_crood = count_crood()['cargos']
    pass


def open_red_package(user_input):
    '''开红包'''
    print("开红包中")


def open_photo(user_input):
    '''开相册'''
    print("开相册中")


def main(user_input):
    mode = user_input['mode']
    if mode == '1':
        discharge_cargo(user_input)
    elif mode == '2':
        open_red_package(user_input)
    else:
        open_photo(user_input)


if __name__ == '__main__':
    # main({'mode': '1'})
    # 测试找色
    # print(find_target_color((154, 152, 255)))
    cargo = count_crood2()['cargos']['cargo1']
    mouse_move(cargo)
    mouse_lpress()
    time.sleep(0.5)
    target = find_target_color((138, 195, 113))
    mouse_lrelease()
    mouse_move(target)
    for i in range(2):
        mouse_drag(cargo, target)
