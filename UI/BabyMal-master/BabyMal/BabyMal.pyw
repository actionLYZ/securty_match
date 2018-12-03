
#import MainWindow,WebWindow
#import MainWindow
from title_widget import *
from content_widget import *
import Global
import sys
import WebWindow
import os,threading,Demo
from library import *
from PyQt5 import QtWidgets,QtCore

#程序主窗口
class MainWindow(QtWidgets.QWidget):
    filepath = None
    def __init__(self):

        super(MainWindow,self).__init__()
        self.location = QtCore.QRect()

        #初始化title_widget
        self.title_widget = TitleWidget(self)
        self.title_widget.setFixedHeight(100)
        self.skin_name = str("./images/titleSkin.png")
        self.setMinimumSize(900, 600)
        self.setWindowIcon(QIcon("./images/BabyMal.ico"))
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint | Qt.FramelessWindowHint)#去掉边框
        self.location = self.geometry()
        self.is_max = False

        #初始化tab窗口
        self.stackedWidget = QtWidgets.QStackedWidget(self)
        self.content_widget = ContentWidget(self)
        self.content_widget2 = ContentWidget2(self)
        self.content_widget3 = ContentWidget3(self)
        self.content_widget4 = ContentWidget4(self)
        self.stackedWidget.addWidget(self.content_widget)
        self.stackedWidget.addWidget(self.content_widget2)
        self.stackedWidget.addWidget(self.content_widget3)
        self.stackedWidget.addWidget(self.content_widget4)
        #self.stackedWidget.raise_()
        self.stackedWidget.setCurrentIndex(0)


        #垂直布局
        self.center_layout = QVBoxLayout()
        self.center_layout.addWidget(self.stackedWidget)
        self.center_layout.setSpacing(0)
        self.center_layout.setContentsMargins(1, 0, 1, 1)

        # 垂直布局
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_widget)
        main_layout.addLayout(self.center_layout)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)
        #放背景
        self.pixmap = QPixmap()
        self.pixmap.load(self.skin_name)

    #绘制背景事件，这里主要是title_widget的背景
    def paintEvent(self, event):  # QPaintEvent *

        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)
        painter.end()

        painter2 = QPainter(self)
        painter2.setPen(Qt.gray)
        painter2.drawPolyline(QPointF(0, 100), QPointF(0, self.height() - 1),
                              QPointF(self.width() - 1, self.height() - 1), QPointF(self.width() - 1, 100))
        painter2.end()

    # 最大化
    def showMax(self):
        # 修复有问题的最大化
        '''if not Global.mainWindow.isMaximized():
            Global.mainWindow.showMaximized()
        else:
            Global.mainWindow.showNormal()'''
        pass

    # 最小化
    def showMin(self):
        Global.mainWindow.showMinimized()

    # 关闭窗口
    def showClose(self):
        Global.mainWindow.close()

    #更改到第几个tab标签
    def ChangeTabCurrentIndex(self):
        self.stackedWidget.setCurrentIndex(0)
    def ChangeTabCurrentIndex1(self):
        self.stackedWidget.setCurrentIndex(1)
    def ChangeTabCurrentIndex2(self):
        self.stackedWidget.setCurrentIndex(2)
    def ChangeTabCurrentIndex3(self):
        self.stackedWidget.setCurrentIndex(3)

    #选择程序
    def OpenUrl(self):
        getfile = QtWidgets.QFileDialog()
        self.filepath, filetype = getfile.getOpenFileNames(self,
                                                      "选择目标程序",
                                                      "C:/",
                                                      "aim program (*.exe)")
        self.content_widget.urlTextEdit.setText(self.filepath[0])

    #开始检测
    def RunAnalyzer(self):
        self.analyzerThread = AnalyzerThread(self)
        self.analyzerThread.start()
        self.stackedWidget.setCurrentIndex(1)
        QApplication.processEvents()

    #显示神经网络网站
    def OpenWeb1(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#scalars&run=.')

    def OpenWeb2(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#graphs&run=.')

    def OpenWeb3(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#distributions&run=.')

    def OpenWeb4(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#histograms&run=.')

    #显示神经网络
    def ShowGraph(self):
        Global.webWindow.show()


class AnalyzerThread (threading.Thread):

    def __init__(self, ui):
        threading.Thread.__init__(self)
        self.ui = ui

    def run(self):
        '''analyzer = Analyzer(self.ui.filepath[0])
        value, result = analyzer.dynamic_analyze()
        value *= 100
        value = round(value,2)
        message = '该程序是恶意软件的概率为：{0}%'.format(value)
        #生成报告
        Demo.DoFilter('softsnoop/Demo/api.txt')
        Global.mainWindow.content_widget4.resultLabel.setText(message)'''
        self.ui.stackedWidget.setCurrentIndex(3)


#程序入口
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # 初始化各个窗体
    mainWindow = MainWindow()
    webWindow = WebWindow.WebWindow()
    Global.SetWindow(mainWindow,webWindow)
    Global.mainWindow.show()

    sys.exit(app.exec_())