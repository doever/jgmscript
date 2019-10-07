import time
import random
from pynput.mouse import Button, Controller
# import win32gui, win32api, win32con, time
from win32api import GetSystemMetrics
from PIL import ImageGrab


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


def mouse_move(src, dist):
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


def count_coord(coord):
    '''计算坐标'''
    builds = {
        '石油': (1461, 372),
        '造纸': (1593, 322),
        '企鹅': (1753, 249),
        '商贸': (1468, 519),
        '媒体': (1611, 463),
        '名食': (1736, 402),
        '花园': (1481, 651),
        '小型': (1606, 584),
        '复兴': (1740, 518)
    }
    cargo_coords = {
        'cargo1': (1667, 890),
        'cargo2': (1752, 851),
        'cargo3': (1827, 808)
    }

    cargo_colors = {
        "商贸": (240, 134, 141),
        "石油": (60, 54, 64),
        "名食": (249, 93, 53),
        "复兴": (115, 38, 43),
        "小型": (220, 146, 86),
        "企鹅": (0, 0, 0),
        "媒体": (182, 108, 3),
        "花园": (176, 227, 227),
        "造纸": (145, 91, 47)
    }

    for k, v in cargo_coords.items():
        print(k, pil_image(v[0], v[1]))
        for build, color in cargo_colors.items():
            # 如果货物的颜色能匹配上
            if color_like(color, pil_image(v[0], v[1])):
                # cargo_coords[k]:货物坐标  build[build]:建筑坐标
                print(cargo_coords[k], builds[build])
                mouse_move(cargo_coords[k], builds[build])
                print(f"移动{k}到{build}")
            else:
                pass

    return 1


def is_train_come(coord):
    '''判断火车是否来了'''
    pass


def main():
    mouse = Controller()


if __name__ == '__main__':
    count_coord(1)

    # mouse_move((1667, 890), (1461, 372))
