import win32con
import win32api
import time

BUY_POINT = (120 << 16) | 50
SELL_POINT = (120 << 16) | 120
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

def appendChildList(hwnd, param):
    list.append(hwnd)
    return True

class Event():

    def __init__(self, hwnd, shop):
        self.hwnd = hwnd

        if (shop == 1):
            self.SHOP_POINT = SHOP_POINT1
        elif (shop == 2):
            self.SHOP_POINT = SHOP_POINT2
        elif (shop == 3):
            self.SHOP_POINT = SHOP_POINT3
        elif (shop == 4):
            self.SHOP_POINT = SHOP_POINT4
        else:
            self.SHOP_POINT = SHOP_POINT5

    def Buy(self):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, BUY_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, BUY_POINT)
        time.sleep(0.3)

        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, self.SHOP_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, self.SHOP_POINT)
        time.sleep(0.3)

        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, OK_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, OK_POINT)
        time.sleep(0.5)

    def Sell(self, index):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, SELL_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, SELL_POINT)
        time.sleep(0.3)

        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, ITEM_POINTS[index]) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, ITEM_POINTS[index])
        time.sleep(0.3)

    def Tune(self):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, TUNE_POINT) 
        time.sleep(0.1)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, TUNE_POINT)
        time.sleep(0.3)

    def Tuning(self, index):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, ITEM_POINTS[index]) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, ITEM_POINTS[index])
        time.sleep(0.3)

        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, TUNING_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, TUNING_POINT)
        time.sleep(4)

    def Board(self):
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 1, BOARD_POINT) 
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, BOARD_POINT)
        time.sleep(0.3)

# list = []
# def appendChildList(hwnd, param):
#     list.append(hwnd)
#     return True

if __name__ == '__main__':

    obj = Click()
    time.sleep(1)
    obj.clickBuyBtn()

    # handle = win32gui.FindWindow(None, "MAKE3")
    # win32gui.EnumChildWindows(handle, appendChildList, None)
    # #btnDzBuilder = win32gui.FindWindowEx(handle, None, "WindowsForms10.Window.8.app.0.2fc056_r6_ad1", None)
    # realHandle = list[0]


    # print(win32gui.GetWindowText(handle))
    # print(win32gui.GetClassName(handle))


    # print(win32gui.GetWindowText(realHandle))
    # print(win32gui.GetClassName(realHandle))

    # x = 50
    # y = 120
    
    # lParam = (y << 16) | x
    # print(lParam)
    # time.sleep(1)

    # print(handle)
    # print(realHandle)

    # win32api.SendMessage(realHandle, win32con.WM_LBUTTONDOWN, 1, lParam) 
    # win32api.SendMessage(realHandle, win32con.WM_LBUTTONUP, 0, lParam)

    

    

