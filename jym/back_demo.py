import time
import random
from pynput.mouse import Button, Controller

mouse = Controller()
# building1 = (1529, 372)
# building2 = (1649, 319)
# building3 = (1747, 247)
# building4 = (1501, 497)
# building5 = (1635, 441)
# building6 = (1751, 387)
# building7 = (1509, 621)
# building8 = (1632, 566)
# building9 = (1754, 508)
# cargo1 = (1683, 839)
# cargo2 = (1753, 804)
# cargo3 = (1931, 756)
# buildings = [(1529, 372), (1649, 319), (1747, 247), (1501, 497), (1635, 441), (1751, 387), (1509, 621), (1632, 566), (1754, 508)]


# 所有货物
# building_releted1 = [(-154, -467), (-34, -520), (64, -592), (-182, -342), (-48, -398), (68, -452), (-174, -218), (-51, -273), (71, -331)]
# building_releted2 = [(-224, -432), (-104, -485), (-6, -557), (-252, -307), (-118, -363), (-2, -417), (-244, -183), (-121, -238), (1, -296)]
# building_releted3 = [(-292, -384), (-172, -437), (-74, -509), (-320, -259), (-186, -315), (-70, -369), (-312, -135), (-189, -190), (-67, -248)]
# 史诗货物
building_releted1 = [(-34, -520), (64, -592), (-48, -398), (68, -452), (-174, -218)]
building_releted2 = [(-104, -485), (-6, -557),  (-118, -363), (-2, -417), (-244, -183)]
building_releted3 = [(-172, -437), (-74, -509),  (-186, -315), (-70, -369), (-312, -135)]
cargos = [(1683, 839), (1753, 804), (1821, 756)]

map = [
        {"src": (1683, 839), "dist": building_releted1},
        {"src": (1753, 804), "dist": building_releted2},
        {"src": (1821, 756), "dist": building_releted3}
       ]


# li = []
# for i in cargos:
#     for j in buildings:
#         li.append((j[0]-i[0], j[1]-i[1]))
#     li.append("---")
# print(li)

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
    for i in range(2):
        mouse.position = src
        mouse.press(Button.left)
        time.sleep(0.3)
        mouse.move(dist[0], dist[1])
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        mouse.release(Button.left)


def run():
    '''
    鼠标到货物位置1，依次鼠标拖动到九个建筑上
    ...
    鼠标到货物位置3，依次鼠标拖动到九个建筑上
    :return:
    '''
    init_mouse()
    for i in map:
        for dist in i['dist']:
            mouse_move(i['src'], dist)
    print("完成一次卸货")


if __name__ == '__main__':
    while 1:
        run()
        time.sleep(3)
