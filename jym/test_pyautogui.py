import pyautogui


def click(img):
    x, y = pyautogui.locateCenterOnScreen(img+'.PNG', grayscale=False)
    pyautogui.click(x, y)


if __name__ == '__main__':
    pyautogui.PAUSE = 2
    click("c")