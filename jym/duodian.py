import time
import random
from pynput.mouse import Button, Controller
# import win32gui, win32api, win32con, time
from win32api import GetSystemMetrics
from PIL import ImageGrab
from setting import BUILDING_ACTIVE_COLOR, BUILDING_ACTIVE_COLOR2, BUILDING_COLOR


mouse = Controller()


def pil_image(x, y):
    mouse.position = (1661, 890)
    mouse.press(Button.left)
    time.sleep(0.2)

    a, b = GetSystemMetrics(0), GetSystemMetrics(1)  # Python获取屏幕分辨率
    im = ImageGrab.grab((0, 0, a, b))  # 与坐标不同，这里0，0，1，1是一个像素，而坐标是从0~1919的
    pix = im.load()

    mouse.release(Button.left)
    return pix[x, y]


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


def collect_money():
    '''收集金币'''
    buildings_crood = count_crood()['buildings']
    for building, crood in buildings_crood.items():
        mouse.position = crood
        mouse.click(Button.left, 1)
        print(f"已收集{building}金币")
        time.sleep(1)


def discharge_cargo():
    '''卸货'''
    epic_buildings_crood = count_crood()['buildings']
    epic_buildings_crood = count_crood()['epic_buildings']
    cargos_crood = count_crood()['cargos']

    for cargo, crood in cargos_crood.items():  # 遍历货箱，需优化只找史诗货物
        for i in range(4):   # 史诗货物卸两次
            for epic_build, epic_crood in epic_buildings_crood.items():  # 遍历寻找建筑，需优化点对点
                    x = epic_crood[0] - crood[0]
                    y = epic_crood[1] - crood[1]
                    mouse.position = crood
                    mouse.press(Button.left)
                    time.sleep(0.1)
                    mouse.move(x, y)
                    time.sleep(0.15)
                    mouse.click(Button.left, 1)
                    mouse.release(Button.left)
                    print(f"搬运{cargo}到{epic_build}...")


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


def set_crood():
    builds = {
        "build1": (1403, 412),
        "build2": (1535, 347),
        "build3": (1667, 282),
        "build4": (1403, 544),
        "build5": (1535, 479),
        "build6": (1667, 414),
        # "build7": (1403, 674),
        "build8": (1535, 610),
        "build9": (1667, 544)
    }
    return builds


def get_three_crood(crood):
    '''根据中点找到对角点，系数是0.65'''
    crood1 = (crood[0]+145, crood[1])
    return crood, crood1


def color_like(colorA, colorB):
    '''判断两个颜色的RGB值是否相近'''
    is_like = False
    diff = abs(colorA[0] - colorB[0]) + abs(colorA[1] - colorB[1]) + abs(colorA[2] - colorB[2])
    if abs(diff) < 10:
        is_like = True
        print(abs(diff))
    return is_like


def main():
    croods = set_crood()
    for build, crood in croods.items():
        croods_trupe = get_three_crood(crood)
        for crood in croods_trupe:
            pix = pil_image(crood[0], crood[1])
            is_like = color_like(pix, BUILDING_COLOR)
            if is_like:
                continue
            else:
                print(f"找到匹配建筑{build}")


if __name__ == '__main__':
    # main()
    restat_game()