import os
import configparser
from tkinter import messagebox as mes

import win32gui


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
        print("配置文件未找到")
        mes.showerror("错误提示", "未找到配置文件")
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


def count_crood(window_name):
    '''计算相对坐标'''
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
    others = {
        "avator": (left+28, top+66),    # (1370, 90), 头像
        "logout": (left+152, top+755),  # (1494, 779), 退出登录
        "login": (left+172, top+830),  # (1625, 823),  微信登录
        "login2": (left + 395, top + 820),  # (1625, 823), qq登录
        "train": (left+257, top+880),   # (1599, 904)
        "safe": (left+3, top+110),  # 安全点
        "store": (left+254, top+953),  # 商店
        "blue_package": (left+101, top+377),  # 蓝色红包
        "purple_package": (left+275, top+377),  # 紫色红包
        "epic_package": (left+435, top+377),  # 橙色红包
        "photo": (left+267, top+734),  # 相册
    }
    return {
        "buildings": buildings,
        "cargos": cargos,
        "cargo_tags": cargo_tag,
        "others": others
    }


Window_name = read_config("Window", "window_name")
Reboot = read_config("Reboot", "is_reboot")
Use_crood = read_config("Crood", "use_user_crood")
if Use_crood.lower() == 'yes':  # 使用用户自定义的坐标
    Croods = {

    }
else:
    Croods = count_crood(Window_name)


if __name__ == '__main__':
    print(Window_name)