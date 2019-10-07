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

# border=2
# 高度差130
# 宽度差130

# 1403,412
# 1535,347
# 1667,282

# 1403,544
# 1535,479
# 1667,414

# 1403,674
# 1535,610
# 1667,544


# 1661,890
# 1740,856
# 1824,814

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
    main()