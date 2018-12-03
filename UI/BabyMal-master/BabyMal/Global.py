# 定义各个窗体
import BabyMal
import WebWindow
mainWindow = BabyMal.MainWindow
webWindow = None


# 初始化窗体
def SetWindow(main,web):
    global mainWindow
    global webWindow
    mainWindow = main
    webWindow = web
