import pyautogui
import time, sys
import random
from win32api import GetSystemMetrics


class Run:
    def move(self):
        seconds = int(sys.argv[1])
        print(seconds)
        i = 0
        while i < seconds:
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
            x = random.randint(0, width)
            y = random.randint(0, height)
            pyautogui.moveTo(x, y, duration=1)
            time.sleep(10)
            i = i + 10
            # print(i, x, y, width, height)


if __name__ == '__main__':
    obj = Run()
    obj.move()
