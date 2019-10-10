import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 判断火车是否来了的标记颜色
# TRAIN_COLOR = (70, 129, 127)
# TRAIN_COLOR = (56, 97, 101)
TRAIN_COLOR = (78, 155, 138)

BUILDING_COLOR = (150, 150, 133)
# 建筑高亮的颜色
# BUILDING_ACTIVE_COLOR = (138, 195, 113)
BUILDING_ACTIVE_COLOR = (188, 255, 113)
BUILDING_ACTIVE_COLOR2 = (107, 206, 97)

# 史诗颜色
EPIC_COLOR = (255, 193, 60)

MIN_DIFF = 10

if __name__ == '__main__':
    print(BASE_DIR)
