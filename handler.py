import win32gui

list = []

def appendChildList(hwnd, param):
    list.append(hwnd)
    return True

class Handler():

    def __init__(self, name):
        self.warpHwnd = win32gui.FindWindow(None, name)
        win32gui.EnumChildWindows(self.warpHwnd, appendChildList, None)
        self.contentHwnd = list[0]

    def getWarpHandle(self):
        return self.warpHwnd

    def getContentHandle(self):
        return self.contentHwnd