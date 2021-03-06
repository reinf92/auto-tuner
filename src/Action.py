import win32con
import win32api
import time

BUY_POINT = (120 << 16) | 50
SELL_POINT = (120 << 16) | 120
SELL_OK_POINT = (225 << 16) | 450
SELL_OK_POINT2 = (285 << 16) | 385
TUNE_POINT = (120 << 16)| 190
OK_POINT = (230 << 16) | 450
BOARD_POINT = (50 << 16) | 250
TUNING_POINT = (330 << 16) | 350
SHOP_POINT1 = (260 << 16) | 170
SHOP_POINT2 = (300 << 16) | 170
SHOP_POINT3 = (340 << 16) | 170
SHOP_POINT4 = (380 << 16) | 170
SHOP_POINT5 = (420 << 16) | 170
ITEM_POINTS = [(360 << 16) | 770, (360 << 16) | 850, (400 << 16) | 770, (400 << 16) | 850, (445 << 16) | 770, (445 << 16) | 850, (490 << 16) | 770, (490 << 16) | 850]


class Action:

    def __init__(self, window):
        self.window = window
        self.setDelay(window.sliderValue)
        
        if (self.window.storeLocation == 1):
            self.window.storePoint = SHOP_POINT1
        elif (self.window.storeLocation == 2):
            self.window.storePoint = SHOP_POINT2
        elif (self.window.storeLocation == 3):
            self.window.storePoint = SHOP_POINT3
        elif (self.window.storeLocation == 4):
            self.window.storePoint = SHOP_POINT4
        else:
            self.window.storePoint = SHOP_POINT5

    def setDelay(self, val):
        if (val == 1):
            self.delay = 1
        elif (val == 2):
            self.delay = 1.25
        elif (val == 3):
            self.delay = 1.5
        elif (val == 4):
            self.delay = 1.75
        elif (val == 5):
            self.delay = 2

    def buyAction(self):
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, BUY_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, BUY_POINT)
        time.sleep(0.3 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, self.window.storePoint) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, self.window.storePoint)
        time.sleep(0.3 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, OK_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, OK_POINT)
        time.sleep(0.5 * self.delay)

    def sellAction(self, index):
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, SELL_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, SELL_POINT)
        time.sleep(0.3 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, ITEM_POINTS[index]) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, ITEM_POINTS[index])
        time.sleep(0.3 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, SELL_OK_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, SELL_OK_POINT)
        time.sleep(0.5 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, SELL_OK_POINT2) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, SELL_OK_POINT2)
        time.sleep(0.3 * self.delay)

    def tuneAction(self):
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, TUNE_POINT) 
        time.sleep(0.1 * self.delay)
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, TUNE_POINT)
        time.sleep(0.3 * self.delay)

    def tuningAction(self, index):
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, ITEM_POINTS[index]) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, ITEM_POINTS[index])
        time.sleep(0.3 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, TUNING_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, TUNING_POINT)
        time.sleep(4 * self.delay)

    def boardAction(self):
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, BOARD_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, BOARD_POINT)
        time.sleep(0.1 * self.delay)

        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONDOWN, 1, BOARD_POINT) 
        win32api.SendMessage(self.window.contentHwnd, win32con.WM_LBUTTONUP, 0, BOARD_POINT)
        time.sleep(0.3 * self.delay)