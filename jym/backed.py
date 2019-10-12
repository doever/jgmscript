import time
import random

from pynput.mouse import Button, Controller
import win32gui, win32api, win32con
from win32api import GetSystemMetrics
from PIL import ImageGrab

from jym.mouse_action import *
from jym.setting import *
from jym.config import *


mouse = Controller()


def pil_image():
    '''屏幕截图'''
    a, b = GetSystemMetrics(0), GetSystemMetrics(1)  # Python获取屏幕分辨率
    im = ImageGrab.grab((0, 0, a, b))  # 与坐标不同，这里0，0，1，1是一个像素，而坐标是从0~1919的
    pix = im.load()
    return pix


def color_like(colorA, colorB, offset):
    '''判断两个颜色的RGB值是否相近'''
    is_like = False
    diff = abs(colorA[0] - colorB[0]) + abs(colorA[1] - colorB[1]) + abs(colorA[2] - colorB[2])
    if abs(diff) < offset:
        is_like = True
    return is_like


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


def find_target_color(color, callback=lambda: None):
    '''
    找对应颜色，精确度较差
    :param color：RGB颜色元组(86,200,42)  callback:未找到颜色该做什么
    :return x,y：目标色块的坐标
    '''
    left, top, right, bottom = find_window(Window_name)
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


def find_target_building(color):
    '''找目标建筑，分割pix为九块，比较九块区域目标色值的个数，最多的或超过多少就是目标建筑'''
    buildings = Croods['buildings']
    width_offset = Croods['offset']['width_offset']
    height_offset = Croods['offset']['height_offset']
    pix = pil_image()
    for building, crood in buildings.items():
        count = 0
        for width in range(crood[0]-width_offset, crood[0]+width_offset):
            for height in range(crood[1]-height_offset, crood[1]+height_offset):
                if color_like(pix[width, height], color, 30):
                    count += 1

        if count > 5:  # 如果发现八处，那就八九不离十了  # 8似乎有点苛刻
            print(f"目标建筑是{building}")
            return Croods['buildings'][building]  # 返回建筑坐标
        else:
            print(f"***************在{building}中共找到{count}处与目标值相近******************")
            continue
    return 0, 0  # 表示未找到


def have_color(_crood, _color, _offset=15):
    '''
    此方法用于判断指定坐标点位置四周10像素内是否有一定数量的目标颜色值
    因之前的单点判断会受到坐标误差影响，改为区块判断
    :param _crood:指定的坐标点 (100, 100)
    :param _color:目标颜色 (255, 255, 255)
    :param _offset:颜色偏差值，默认15
    :return:
    '''
    pix = pil_image()
    x, y = _crood
    width_offset, height_offset = 10, 10
    count = 0
    for width in range(x-width_offset, x+width_offset):
        for height in range(y-height_offset, y+height_offset):
            if color_like(pix[width, height], _color, _offset):
                count += 1
            else:
                continue
    # print(f"共找到{count}个色块与火车目标颜色接近")
    if count > 8:  # 如果区域内有8个点颜色相近, 则认为判定成功
        return True
    return False


def train_come():
    '''判断火车是否来了'''
    return have_color(Croods['others']['train'], TRAIN_COLOR)


def have_epic(crood):
    '''判断是否是史诗货物'''
    return have_color(crood, EPIC_COLOR)


def init_mouse():
    '''初始化鼠标操作，确保不被其他弹窗影响'''
    safe = Croods['others']['safe']
    mouse_move(safe)
    for no in range(2):
        mouse_lclick()
        time.sleep(0.25)
    print("初始化鼠标完成")


def collect_money():
    '''收集金币'''
    buildings_crood = Croods['buildings']
    for building, crood in buildings_crood.items():
        mouse.position = crood
        mouse.click(Button.left, 1)

    print(f"金币收集完成...")


def reboot():
    '''重启游戏，刷新火车，提高效率'''
    others = Croods['others']
    # 点击头像
    mouse.position = others['avator']
    mouse.click(Button.left)
    # 点击退出
    time.sleep(2.5)
    mouse.position = others['logout']
    mouse.click(Button.left)

    # 重复一次，确保一定可以退出
    time.sleep(1)
    mouse.position = others['logout']
    mouse.click(Button.left)

    # 点击登录，微信登录，需改成可以选择登录方式
    mouse.position = others['login']
    time.sleep(5)
    mouse.position = others['login']
    mouse.click(Button.left)

    # 重复一次确保一定可以登录
    time.sleep(0.2)
    mouse.position = others['login']
    mouse.click(Button.left)

    init_mouse()  # 初始化鼠标


def discharge_cargo(cargo_crood, times):
    '''卸货'''
    mouse_move(cargo_crood)
    mouse_lpress()
    time.sleep(0.2)
    target_crood = find_target_building(BUILDING_ACTIVE_COLOR)
    mouse_lrelease()
    if target_crood[0] == 0:  # 未找到对应的建筑,遍历所有建筑
        print("未发现目标建筑")
    else:
        for no in range(times):
            mouse_drag(cargo_crood, target_crood)
            print(f"移动货物{cargo_crood}到建筑{target_crood}上")


def cargo(user_input):
    '''
    卸货模式:
    1.判断火车有没有来，间隔等待3s，来了进入史诗资源判断
    2.依次判断三个货箱有没有史诗，有则进入卸货（加收获金币），没有重启
    3.再次进入火车判断
    '''
    all_cargo = user_input['all_cargo']
    if train_come():
        time.sleep(3)  # 火车来的时候需要等一会才会刷新货物
        print("开始卸货")
        for cargo, crood in Croods['cargo_tags'].items():
            if all_cargo:                                                 # 选择拉所有货
                print(f"搬运货物{cargo}中")
                discharge_cargo(Croods['cargos'][cargo], 6)
            else:
                # pix = pil_image()
                if have_epic(crood):   # 如果是史诗货物
                    print(f"在{cargo}出发现史诗货物")
                    discharge_cargo(Croods['cargos'][cargo], 4)           # 按史诗卸货
                else:
                    print(f'在{cargo}未发现史诗货物')
        collect_money()                                                   # 收集金币
        init_mouse()                                                      # 初始化鼠标
        if Reboot.lower() == 'yes':
            print("游戏重启...")
            reboot()                                                      # 进入重启
            time.sleep(10)
    else:
        time.sleep(3)
        if user_input["auto_money"]:
            collect_money()                  # 20191010 等待火车的时候也需要收集下金币
        print("等待火车中...")


def open_pag(crood, count, reset_count):
    '''
    鼠标循环点击
    :param crood: 点击的坐标
    :param count: 需要开多少个
    :param reset_count: 因为红包里东西个数不同，需要重置多少次
    :return:
    '''
    if reset_count == 6:
        who = "福气红包"
    elif reset_count == 10:
        who = "多福红包"
    elif reset_count == 14:
        who = "满福红包"
    elif reset_count == 8:
        who = "相册"
    else:
        who = '道具'
    try:
        count = int(count)
    except ValueError:
        count = 0

    for i in range(count):
        mouse_move(crood)
        mouse_lclick()
        print(f"正在开第{i+1}个{who}")
        for j in range(reset_count):
            mouse_move(Croods['others']['safe'])
            mouse_lclick()
            time.sleep(0.3)


def open_red_package(user_input):
    '''开红包'''
    blue_package = user_input['blue_package']
    purple_package = user_input['purple_package']
    epic_package = user_input['epic_package']
    mouse_move(Croods['others']['store'])
    mouse_lclick()
    open_pag(Croods['others']['epic_package'], epic_package, 14)
    open_pag(Croods['others']['purple_package'], purple_package, 10)
    open_pag(Croods['others']['blue_package'], blue_package, 6)


def open_photo(user_input):
    '''开相册'''
    photo = user_input['photo_count']
    mouse_move(Croods['others']['store'])
    mouse_lclick()
    open_pag(Croods['others']['photo'], photo, 8)


def main(user_input):
    mode = user_input['mode']
    if mode == '1':
        cargo(user_input)
    elif mode == '2':
        open_red_package(user_input)
    else:
        open_photo(user_input)


if __name__ == '__main__':
    # main({'mode': '1', 'all_cargo': 1})

    # while 1:
    #     main({'mode': '1', 'all_cargo': 1})
    #     time.sleep(3)

    pass
    # cargo = Croods['cargo_tags']
    # for b, c in cargo.items():
    #     mouse_move(c)
    #     time.sleep(1)

