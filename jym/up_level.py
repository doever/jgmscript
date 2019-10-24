from jym.mouse_action import *
from jym.config import *


def up_level(times):
    '''建筑升级'''
    left, top, right, bottom = find_window(Window_name)
    crood = (left+273, top+728)
    mouse_move(crood)
    for i in range(times):
        mouse_lclick()
        time.sleep(0.1)


if __name__ == '__main__':
    up_level(300)
