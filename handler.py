import win32gui

list = []

def appendChildList(hwnd, param):
    list.append(hwnd)
    return True

class Handler():

    def __init__(self):
        self.hwnd = win32gui.FindWindow(None, "MAKE3")
        win32gui.EnumChildWindows(self.hwnd, appendChildList, None)
        self.hwnd = list[0]

    def getHandle(self):
        return self.hwnd