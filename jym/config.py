import os
import configparser
from tkinter import messagebox as mes

import win32gui
import win32api


def read_config(sec, item):
    '''
    读取配置文件
    :param sec:节点名
    :param item: 配置项名
    :return:
    '''
    config_file = os.path.join("C:/", 'config.ini')
    cf = configparser.ConfigParser()
    try:
        cf.read(config_file, encoding='utf-8')
        value = cf.get(sec, item)
    except NameError as err:
        print(f"未找到配置项{sec}={item}")
        mes.showerror(f"未找到配置项{sec}={item}")
    else:
        return value


def find_window(window_name):
    '''定位模拟器的坐标'''
    try:
        hwnd = win32gui.FindWindow(None, window_name)
        crood = win32gui.GetWindowRect(hwnd)
    except:
        print("未获取窗口，请先打开模拟器，如果已经打开，请对应窗口修改配置文件")
        mes.showerror("错误提示", "未获取窗口，请先打开模拟器，如果已经打开，请对应窗口修改配置文件")
    else:
        return crood  # 1330 11 1908 1009


def large_simulator_crood(window_name, wx_login='yes'):
    '''计算大屏相对坐标'''
    left, top, right, bottom = find_window(window_name)
    buildings = {
        'building1': (left + 147, top + 397),
        'building2': (left + 276, top + 332),
        'building3': (left + 402, top + 266),
        'building4': (left + 147, top + 523),
        'building5': (left + 276, top + 460),
        'building6': (left + 402, top + 397),
        'building7': (left + 147, top + 650),
        'building8': (left + 276, top + 588),
        'building9': (left + 402, top + 523),
    }
    cargos = {
        'cargo1': (left+329, top+857),  # (1671, 881),货物1
        'cargo2': (left+410, top+821),  # (1703, 783),货物2
        'cargo3': (left+489, top+772)   # (1831, 796)货物3
    }
    cargo_tag = {
        'cargo1': (left+294, top+818),  # (1636, 842),货物标记1
        'cargo2': (left+372, top+777),  # (1714, 801),货物标记2
        'cargo3': (left+449, top+734)   # (1791, 758) 货物标记3
    }
    if wx_login.lower() == 'yes':
        login = (left+172, top+830)  # (1625, 823),  微信登录
    else:
        login = (left + 395, top + 830)  # (1625, 823), qq登录
    others = {
        "avator": (left+28, top+66),    # (1370, 90), 头像
        "logout": (left+152, top+755),  # (1494, 779), 退出登录
        "login": login,
        "train": (left+257, top+880),   # (1599, 904)
        "safe": (left+3, top+110),  # 安全点
        "store": (left+254, top+953),  # 商店
        "blue_package": (left+101, top+377),  # 蓝色红包
        "purple_package": (left+275, top+377),  # 紫色红包
        "epic_package": (left+435, top+377),  # 橙色红包
        "photo": (left+267, top+734),  # 相册
    }
    # 点偏移量
    offset = {
        'width_offset': 85,
        'height_offset': 35
    }
    return {
        "buildings": buildings,
        "cargos": cargos,
        "cargo_tags": cargo_tag,
        "others": others,
        "offset": offset
    }


def small_simulator_crood(window_name, wx_login='yes'):
    '''计算小屏相对坐标'''
    left, top, right, bottom = find_window(window_name)  # 1369, 82, 1779, 782
    buildings = {
        'building1': (left + 103, top + 282),  # (1470, 364)
        'building2': (left + 191, top + 238),  # (1560, 320)
        'building3': (left + 275, top + 195),  # (1644, 277)
        'building4': (left + 103, top + 370),  # (1472, 451)
        'building5': (left + 191, top + 327),  # (1560, 409)
        'building6': (left + 275, top + 282),  # (1646, 364)
        'building7': (left + 103, top + 456),  # (1474, 538)
        'building8': (left + 191, top + 414),  # (1557, 496)
        'building9': (left + 275, top + 370),  # (1647, 453)
    }
    cargos = {
        'cargo1': (left+229, top+603),  # (1598, 685),货物1
        'cargo2': (left+281, top+574),  # (1650, 656),货物2
        'cargo3': (left+334, top+543)   # (1703, 625)货物3
    }
    cargo_tag = {
        'cargo1': (left+200, top+572),  # (1569, 654),货物标记1
        'cargo2': (left+258, top+547),  # (1627, 629),货物标记2
        'cargo3': (left+309, top+515)   # (1677, 597) 货物标记3
    }
    if wx_login.lower() == 'yes':
        login_crood = (left+115, top+587)  # (1484, 669),  微信登录
    else:
        login_crood = (left+255, top+583)  # (1624, 665), qq登录
    others = {
        "avator": (left+27, top+65),    # (1396, 147), 头像
        "logout": (left+105, top+530),  # (1474, 612), 退出登录
        "login": login_crood,
        "train": (left+175, top+620),   # (1616, 684) 火车
        "safe": (left+3, top+95),  # (1373, 177) 安全点
        "store": (left+173, top+665),  # (1542, 747) 商店
        "blue_package": (left+73, top+271),  # (1442, 353) 蓝色红包
        "purple_package": (left+183, top+271),  # (1552, 359) 紫色红包
        "epic_package": (left+304, top+271),  # (1673, 360) 橙色红包
        "photo": (left+193, top+525),  # (1562, 607) 相册
    }
    offset = {
        'width_offset': 50,
        'height_offset': 20
    }
    return {
        "buildings": buildings,
        "cargos": cargos,
        "cargo_tags": cargo_tag,
        "others": others,
        "offset": offset
    }


Window_name = read_config("Window", "window_name")
Reboot = read_config("Reboot", "is_reboot")
Small_simulator = read_config("Window", "small_simulator")
Wx_login = read_config("Window", "wx_login")
if Small_simulator.lower() == 'yes':  # 使用小屏坐标
    Croods = small_simulator_crood(Window_name, Wx_login)
else:
    Croods = large_simulator_crood(Window_name, Wx_login)


if __name__ == '__main__':
    import time
    # for b, c in Croods['others'].items():
    #     win32api.SetCursorPos(c)
    #     time.sleep(0.5)
    win32api.SetCursorPos(Croods['others']['train'])