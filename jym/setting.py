import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TRAIN_COLOR = ()

BUILDING_COLOR = (150, 150, 133)

BUILDING_ACTIVE_COLOR = (138, 195, 113)
BUILDING_ACTIVE_COLOR2 = (107, 206, 97)

MIN_DIFF = 10

if __name__ == '__main__':
    print(BASE_DIR)
