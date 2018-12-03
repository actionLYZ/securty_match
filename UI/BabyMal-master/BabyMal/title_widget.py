from tool_button import ToolButton
from push_button import PushButton

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import Global


class TitleWidget(QWidget):
    def __init__(self, parent=None):
        super(TitleWidget, self).__init__(parent)

        self.skin_button = PushButton(self)
        self.min_button = PushButton(self)
        self.max_button = PushButton(self)
        self.close_button = PushButton(self)
        self.medal_button = QPushButton(self)
        self.button_list = []

        # 版本标题颜色设置
        self.version_title = QLabel()
        self.version_title.setStyleSheet("color:white")

        # 设置按钮的图片
        self.skin_button.loadPixmap("./images/sysButton/skin_button.png")
        self.min_button.loadPixmap("./images/sysButton/min_button.png")
        self.max_button.loadPixmap("./images/sysButton/max_button.png")
        self.close_button.loadPixmap("./images/sysButton/close_button.png")

        # 设置功勋图标
        medal_icon = QIcon("./images/contentWidget/medal.png")
        self.medal_button.setIcon(medal_icon)
        self.medal_button.setFixedSize(25, 25)
        self.medal_button.setIconSize(QSize(25, 25))
        self.medal_button.setStyleSheet("background:transparent")  # 透明显示

        #self.skin_button.clicked.connect(Global.mainWindow.showSkinWidget)
        self.min_button.clicked.connect(Global.mainWindow.showMin)
        self.max_button.clicked.connect(Global.mainWindow.showMax)
        self.close_button.clicked.connect(Global.mainWindow.showClose)


        title_layout = QHBoxLayout()
        title_layout.addWidget(self.version_title, 0, Qt.AlignVCenter)
        title_layout.addStretch()
        title_layout.addWidget(self.medal_button, 0, Qt.AlignTop)
        title_layout.addWidget(self.skin_button, 0, Qt.AlignTop)
        title_layout.addWidget(self.min_button, 0, Qt.AlignTop)
        title_layout.addWidget(self.max_button, 0, Qt.AlignTop)
        title_layout.addWidget(self.close_button, 0, Qt.AlignTop)
        title_layout.setSpacing(0)

        #设置边距
        title_layout.setContentsMargins(0, 0, 5, 0)
        self.version_title.setContentsMargins(15, 0, 0, 0)
        self.skin_button.setContentsMargins(0, 0, 10, 0)

        # string_list = QStringList

        #工具栏图标列表
        string_list = ["./images/toolWidget/ruanJian.png","./images/toolWidget/qingLi.png", \
                       "./images/toolWidget/muMa.png","./images/toolWidget/menZhen.png"]

        button_layout = QHBoxLayout()

        # 还不知道怎么用
        signal_mapper = QSignalMapper(self)
        for i in range(len(string_list)):
            self.tool_button = ToolButton(string_list[i])
            # self.tool_button.setParent()
            self.button_list.append(self.tool_button)
            # self.connect(self.tool_button, SIGNAL("clicked()"), signal_mapper, SLOT("map()"))
            # self.tool_button.clicked.connect(map)
            # self.tool_button.clicked.connect(self.map())
            # signal_mapper.setMapping(self.tool_button, QString.number(i, 10))
            signal_mapper.setMapping(self.tool_button, str(i))
            button_layout.addWidget(self.tool_button, 0, Qt.AlignBottom)


        self.button_list[0].clicked.connect(parent.ChangeTabCurrentIndex)
        self.button_list[1].clicked.connect(parent.ChangeTabCurrentIndex1)
        self.button_list[2].clicked.connect(parent.ChangeTabCurrentIndex2)
        self.button_list[3].clicked.connect(parent.ChangeTabCurrentIndex3)

        # self.connect(signal_mapper, SIGNAL("mapped()"), self, SLOT("turnPage()"))

        logo_label = QLabel()
        pixmap = QPixmap("./images/logo.png")
        logo_label.setPixmap(pixmap)
        logo_label.setFixedSize(pixmap.size())
        logo_label.setCursor(Qt.PointingHandCursor)

        button_layout.addStretch()
        button_layout.addWidget(logo_label)
        button_layout.setSpacing(8)
        button_layout.setContentsMargins(15, 0, 15, 0)

        main_layout = QVBoxLayout()
        main_layout.addLayout(title_layout)
        main_layout.addLayout(button_layout)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.translateLanguage()

        self.setLayout(main_layout)
        self.setFixedHeight(100)
        self.is_move = False

    def translateLanguage(self):

        self.version_title.setText(u"BabyMal")
        self.skin_button.setToolTip(u"change skin")
        self.min_button.setToolTip(u"minimize")
        self.max_button.setToolTip(u"maximize")
        self.close_button.setToolTip(u"close")

        self.button_list[0].setText(u"主页")
        self.button_list[1].setText(u"动态分析")
        self.button_list[2].setText(u"静态分析")
        self.button_list[3].setText(u"检测报告")


    def ChangeTabCurrentIndex(self,num):
        #parent.ChangeTabCurrentIndex(num)
        print(num)
    # 如果不用QApplication.winEvent方法，就要启动以下代码
    def mousePressEvent(self, e):
        self.press_point = e.pos()
        self.is_move = True

    #已修复无法移动的问题
    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton and self.is_move:
            parent_widget = self.parentWidget()
            if parent_widget:
                parent_point = QPoint()
                parent_point = parent_widget.pos()
                parent_point.setX(parent_point.x() + e.x() - self.press_point.x())
                parent_point.setY(parent_point.y() + e.y() - self.press_point.y())
                parent_widget.move(parent_point)

    def mouseReleaseEvent(self, event):
        if self.is_move:
            self.is_move = False


    # 双击工具栏，放大
    def mouseDoubleClickEvent(self, event):
        self.max_button.clicked.emit()

    @pyqtSlot()
    def turnPage(self, current_page):
        current_index = current_page
        for i in range(len(self.button_list)):
            self.tool_button = self.button_list[i]
            if (current_index == i):
                self.tool_button.setMousePress(True)
            else:
                self.tool_button.setMousePress(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    title = TitleWidget()
    title.show()

    app.exec_()


