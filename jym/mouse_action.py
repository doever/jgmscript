import win32gui, win32api, win32con
from win32api import GetSystemMetrics
import time


def mouse_move(dist):
    '''
    鼠标移动
    :param  dist:坐标元组(x, y)
    '''
    win32api.SetCursorPos(dist)
    # win32api.GetCursorPos()


def mouse_drag(src, dist):
    '''鼠标拖动'''
    mouse_move(src)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.2)
    mouse_move(dist)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.2)


def mouse_lclick():
    '''鼠标左键单击'''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(0.1)   # 20191010 鼠标也需要一个反应的时间
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_lpress():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def mouse_lrelease():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


if __name__ == '__main__':
    # mouse_drag((1665, 862), (1612, 566))
    for i in range(50):
        for j in range(20):
            if j == 21:
                print(j)
                break
        else:
            continue
        break