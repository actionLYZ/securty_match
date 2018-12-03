#该文件保存全局窗口
import main_widget
main_widget = main_widget.MainWidget

#初始化各个全局窗口
def InitWindows(m1):
    global main_widget
    main_widget = m1