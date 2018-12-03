
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

class ContentWidget(QWidget):
	def __init__(self, parent=None):
		super(ContentWidget, self).__init__(parent)
		self.palette = QPalette()

		self.top_widget = QWidget()
		self.down_widget = QWidget()
		self.top_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")
		self.down_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")

		self.palette.setBrush(QPalette.Window, QBrush(Qt.white))	#创建画刷
		self.setPalette(self.palette)
		self.setAutoFillBackground(True)


		self.InitTopWidget()	#设置上边窗体
		self.InitDownWidget()	#设置下边窗体

		#设置主窗体
		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.top_widget)
		self.main_layout.addWidget(self.down_widget)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)


		self.setLayout(self.main_layout)
		self.translateLanguage()

		#按键映射
		self.searchButton.clicked.connect(parent.OpenUrl)
		self.startButton.clicked.connect(parent.RunAnalyzer)

	# 设置上边窗体
	def InitTopWidget(self):

		self.computerLabel = QLabel()  # 电脑的图片
		self.searchButton = QPushButton()	#搜索按钮
		self.searchButton.setCursor(Qt.PointingHandCursor)
		self.urlTextEdit = QTextEdit()
		self.urlTextEdit.setFixedSize(400,30)
		self.urlTextEdit.setStyleSheet("background-image: url()")



		self.top_widget.resize(650, 500)

		#电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/computer.png")
		self.computerLabel.setPixmap(label_pixmap)
		self.computerLabel.setFixedSize(label_pixmap.size())

		#搜索按钮属性
		pixmap = QPixmap("./images/contentWidget/power.png")
		self.searchButton.setIcon(QIcon(pixmap))
		self.searchButton.setIconSize(pixmap.size())
		self.searchButton.setFixedSize(180, 70)
		self.searchButton.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
										"QPushButton:hover{background:rgb(140, 220, 35)}")
		searchFont = QFont()  # 字体设置
		searchFont.setPointSize(16)
		self.searchButton.setFont(searchFont)


		h_layout = QHBoxLayout()  # 水平布局
		h_layout.addStretch(1)
		h_layout.addWidget(self.computerLabel, 0, Qt.AlignVCenter)  # 垂直方向居中
		h_layout.addStretch(2)
		h_layout.addWidget(self.urlTextEdit, 0, Qt.AlignVCenter)
		h_layout.addStretch(2)
		h_layout.addWidget(self.searchButton, 0, Qt.AlignRight)

		h_layout.addStretch(2)
		#h_layout.setSpacing(50)		#控件之间的间距
		h_layout.setContentsMargins(30, 20, 0, 0)	#布局距离窗体四周边缘距离


		self.top_widget.setLayout(h_layout)		#最后装入top_widget返回

	# 设置下边窗体
	def InitDownWidget(self):

		#中间部分文字的widget
		self.firstLabel = QLabel()
		self.firstLabel.setFixedSize(190,50)
		self.firstLabel.setStyleSheet("background: transparent;\n"
									 "font: 75 18pt \"Microsoft YaHei UI\";")
		#二级标题
		self.secondList = []
		for i in range(3):
			self.tempLabel = QLabel()
			self.tempLabel.setFixedSize(90,30)
			self.tempLabel.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
			self.secondList.append(self.tempLabel)
		#三级标题
		self.thirdList = []
		for i in range(3):
			self.tempLabel = QLabel()
			self.tempLabel.setFixedSize(250, 20)
			self.tempLabel.setStyleSheet("background: transparent;\n"
											"font: 10pt \"Microsoft YaHei UI\";")
			self.thirdList.append(self.tempLabel)

		#文字左侧图标
		self.leftIconLabel = QLabel()
		label_pixmap = QPixmap ("./images/contentWidget/wallIcon.png")
		self.leftIconLabel.setPixmap(label_pixmap)
		self.leftIconLabel.setFixedSize(label_pixmap.size())
		self.leftIconLabel.setStyleSheet("background-image: url()")		#防止继承父类背景
		self.leftIconLabel2 = QLabel()
		label_pixmap = QPixmap ("./images/contentWidget/monitorIcon.png")
		self.leftIconLabel2.setPixmap(label_pixmap)
		self.leftIconLabel2.setFixedSize(label_pixmap.size())
		self.leftIconLabel2.setStyleSheet("background-image: url()")
		self.leftIconLabel3 = QLabel()
		label_pixmap = QPixmap ("./images/contentWidget/reportIcon.png")
		self.leftIconLabel3.setPixmap(label_pixmap)
		self.leftIconLabel3.setFixedSize(label_pixmap.size())
		self.leftIconLabel3.setStyleSheet("background-image: url()")

		self.leftBigIconLabel = QLabel()	#最左侧大图标
		label_pixmap = QPixmap("./images/contentWidget/protectIcon.png")
		self.leftBigIconLabel.setPixmap(label_pixmap)
		self.leftBigIconLabel.setFixedSize(label_pixmap.size())
		self.leftBigIconLabel.setStyleSheet("background-image: url()")

		#右侧按钮和艺术字
		self.startButton = QPushButton()
		self.startButton.setCursor(Qt.PointingHandCursor)
		self.startButton.setFixedSize(180, 70)
		self.startButton.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
			"QPushButton:hover{background:rgb(140, 220, 35)}")
		power_font = QFont()  #= self.power_button.font()
		power_font.setPointSize(16)
		self.startButton.setFont(power_font)

		self.artLabel = QLabel()
		label_pixmap = QPixmap("./images/contentWidget/artword.png")
		self.artLabel.setPixmap(label_pixmap)
		self.artLabel.setFixedSize(label_pixmap.size())
		self.artLabel.setStyleSheet("background: transparent;")



		self.down_widget.resize(650, 500)

		#左侧图标布局
		icon_layout = QVBoxLayout()  # 垂直布局
		icon_layout.addWidget(self.leftIconLabel, 0, Qt.AlignLeft)
		icon_layout.addWidget(self.leftIconLabel2, 0, Qt.AlignLeft)
		icon_layout.addWidget(self.leftIconLabel3, 0, Qt.AlignLeft)
		icon_layout.addStretch()
		icon_layout.setSpacing(45)		#控件之间的间距
		icon_layout.setContentsMargins(0, 85, 0, 0)	#布局距离窗体四周边缘距离



		#中间文字布局
		text_layout = QVBoxLayout()	#垂直布局
		text_layout.addWidget(self.firstLabel, 0, Qt.AlignLeft)	#水平方向靠左
		text_layout.addWidget(self.secondList[0], 0, Qt.AlignLeft)
		text_layout.addWidget(self.thirdList[0], 0, Qt.AlignLeft)
		text_layout.addWidget(self.secondList[1], 0, Qt.AlignLeft)
		text_layout.addWidget(self.thirdList[1], 0, Qt.AlignLeft)
		text_layout.addWidget(self.secondList[2], 0, Qt.AlignLeft)
		text_layout.addWidget(self.thirdList[2], 0, Qt.AlignLeft)
		text_layout.addStretch()
		text_layout.setSpacing(15)		#控件之间的间距
		text_layout.setContentsMargins(0, 20, 0, 20)	#布局距离窗体四周边缘距离

		#右侧布局
		right_layout = QVBoxLayout()  # 垂直布局
		right_layout.addWidget(self.startButton, 0, Qt.AlignCenter)
		right_layout.addWidget(self.artLabel, 0, Qt.AlignCenter)
		right_layout.addStretch()
		right_layout.setSpacing(100)		#控件之间的间距
		right_layout.setContentsMargins(0, 40, 0, 0)	#布局距离窗体四周边缘距离


		#总的布局
		main_layout = QHBoxLayout()  # 水平布局
		main_layout.addStretch(1)	#空白部分比例(所有的addStretch之间的比例)
		main_layout.addWidget(self.leftBigIconLabel,0,Qt.AlignVCenter)
		main_layout.addStretch(5)
		main_layout.addLayout(icon_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(text_layout)
		main_layout.addStretch(5)
		main_layout.addLayout(right_layout)
		main_layout.addStretch(1)
		main_layout.setSpacing(15)
		main_layout.setContentsMargins(0, 0, 0, 0)


		self.down_widget.setLayout(main_layout)	#最后装入down_widget返回

	def translateLanguage(self):
		self.searchButton.setText(u"search")
		self.firstLabel.setText(u"检测未知程序")
		self.secondList[0].setText(u"隔离保护")
		self.secondList[1].setText(u"监测检测")
		self.secondList[2].setText(u"生成报告")
		self.thirdList[0].setText(u"避免计算机收到来自未知程序的伤害")
		self.thirdList[1].setText(u"检测未知程序调用的API函数")
		self.thirdList[2].setText(u"生成未知程序的测试报告")
		self.startButton.setText(u"开始检测")


	#事件过滤器(具体作用没了解)
	def eventFilter(self, obj, event):
		if(obj is QLabel):

			if(event.type() == QEvent.Paint):
				label_height_1 = self.line_label_1.height()
				label_width_1 = self.line_label_1.width()
				painter = QPainter (self.line_label_1)
				painter.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter.drawLine(label_width_1 / 2, 0, label_width_1 / 2, label_height_1)

				label_height_2 = self.line_label_2.height()
				label_width_2 = self.line_label_2.width()
				painter2 = QPainter (self.line_label_2)
				painter2.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter2.drawLine(label_width_2 / 2, 0, label_width_2 / 2, label_height_2)
				return True

		return False#self.eventFilter(obj, event)


class ContentWidget2(QWidget):
	def __init__(self, parent=None):
		super(ContentWidget2, self).__init__(parent)
		self.palette = QPalette()

		self.top_widget = QWidget()
		self.down_widget = QWidget()
		self.top_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")
		self.down_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")

		self.palette.setBrush(QPalette.Window, QBrush(Qt.white))	#创建画刷
		self.setPalette(self.palette)
		self.setAutoFillBackground(True)

		self.main_splitter = QSplitter()	#分割窗口
		self.main_splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.main_splitter.setOrientation(Qt.Vertical)	#横向排列
		self.main_splitter.setHandleWidth(1)	#设置窗口分割线
		self.main_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")

		self.InitTopWidget()	#设置上边窗体
		self.InitDownWidget()	#设置下边窗体

		#设置主窗体
		self.main_splitter.addWidget(self.top_widget)
		self.main_splitter.addWidget(self.down_widget)


		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.main_splitter)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)

		#设置按键映射
		self.rightButtonList[0].clicked.connect(parent.OpenWeb1)
		self.rightButtonList[1].clicked.connect(parent.OpenWeb2)
		self.rightButtonList[2].clicked.connect(parent.OpenWeb3)
		self.rightButtonList[3].clicked.connect(parent.OpenWeb4)

		self.setLayout(self.main_layout)
		self.translateLanguage()

	# 设置上边窗体
	def InitTopWidget(self):

		self.computerLabel = QLabel()  # 电脑的图片
		self.showButton = QPushButton()	#显示按钮
		self.showButton.setCursor(Qt.PointingHandCursor)

		#进度条
		self.progressBar = QProgressBar()
		self.progressBar.setFixedSize(500,30)
		self.progressBar.setProperty("value", 0)


		self.top_widget.resize(650, 500)

		#电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/computer.png")
		self.computerLabel.setPixmap(label_pixmap)
		self.computerLabel.setFixedSize(label_pixmap.size())

		#显示信息按钮属性
		self.showButton.setFixedSize(150, 50)
		self.showButton.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
										"QPushButton:hover{background:rgb(140, 220, 35)}")
		searchFont = QFont()  # 字体设置
		searchFont.setPointSize(16)
		self.showButton.setFont(searchFont)


		h_layout = QHBoxLayout()  # 水平布局
		h_layout.addStretch(1)
		h_layout.addWidget(self.computerLabel, 0, Qt.AlignVCenter)  # 垂直方向居中
		h_layout.addStretch(1)
		h_layout.addWidget(self.progressBar, 0, Qt.AlignVCenter)
		h_layout.addStretch(1)
		h_layout.addWidget(self.showButton, 0, Qt.AlignVCenter)
		h_layout.addStretch(6)
		#h_layout.setSpacing(50)		#控件之间的间距
		h_layout.setContentsMargins(30, 20, 0, 0)	#布局距离窗体四周边缘距离

		'''main_layout = QVBoxLayout()  # 垂直布局
		main_layout.addLayout(h_layout)
		main_layout.addWidget(self.power_button, 0, Qt.AlignCenter)  # 水平方向居中
		main_layout.addStretch()
		main_layout.setSpacing(0)
		main_layout.setContentsMargins(0, 0, 0, 0)'''

		self.top_widget.setLayout(h_layout)		#最后装入top_widget返回

	# 设置下边窗体
	def InitDownWidget(self):
		self.reportTextEdit = QPlainTextEdit()
		self.reportTextEdit.setFixedSize(500,270)
		self.reportTextEdit.setStyleSheet("background-image: url(./images/contentWidget/whitebackground.png);")

		#右侧四个按钮
		self.rightButtonList = []
		temp_button = QToolButton()
		temp_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		recovery_pixmap = QPixmap ("./images/contentWidget/scalars.png")
		temp_button.setIcon(QIcon(recovery_pixmap))
		temp_button.setIconSize(recovery_pixmap.size())
		temp_button.setFixedSize(recovery_pixmap.width() + 50, recovery_pixmap.height() + 35)
		#修复hover样式
		temp_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")
		self.rightButtonList.append(temp_button)

		temp_button = QToolButton()
		temp_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		recovery_pixmap = QPixmap ("./images/contentWidget/graphs.png")
		temp_button.setIcon(QIcon(recovery_pixmap))
		temp_button.setIconSize(recovery_pixmap.size())
		temp_button.setFixedSize(recovery_pixmap.width() + 50, recovery_pixmap.height() + 35)
		#修复hover样式
		temp_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")
		self.rightButtonList.append(temp_button)

		temp_button = QToolButton()
		temp_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		recovery_pixmap = QPixmap ("./images/contentWidget/distributions.png")
		temp_button.setIcon(QIcon(recovery_pixmap))
		temp_button.setIconSize(recovery_pixmap.size())
		temp_button.setFixedSize(recovery_pixmap.width() + 50, recovery_pixmap.height() + 35)
		#修复hover样式
		temp_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")
		self.rightButtonList.append(temp_button)

		temp_button = QToolButton()
		temp_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		recovery_pixmap = QPixmap ("./images/contentWidget/histograms.png")
		temp_button.setIcon(QIcon(recovery_pixmap))
		temp_button.setIconSize(recovery_pixmap.size())
		temp_button.setFixedSize(recovery_pixmap.width() + 50, recovery_pixmap.height() + 35)
		#修复hover样式
		temp_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")
		self.rightButtonList.append(temp_button)

		self.down_widget.resize(650, 500)

		#左侧布局（主要是为了控制距离窗体的距离）
		left_layout = QVBoxLayout()
		left_layout.addWidget(self.reportTextEdit, 0, Qt.AlignCenter)
		left_layout.setContentsMargins(40, 40, 40, 40)	#布局距离窗体四周边缘距离


		#右侧布局
		v_layout1 = QHBoxLayout()	#水平布局
		v_layout1.addWidget(self.rightButtonList[0], 0, Qt.AlignCenter)
		v_layout1.addWidget(self.rightButtonList[1], 0, Qt.AlignCenter)
		v_layout2 = QHBoxLayout()	#水平布局
		v_layout2.addWidget(self.rightButtonList[2], 0, Qt.AlignCenter)
		v_layout2.addWidget(self.rightButtonList[3], 0, Qt.AlignCenter)
		right_layout = QVBoxLayout()  # 垂直布局
		right_layout.addLayout(v_layout1)
		right_layout.addLayout(v_layout2)
		right_layout.addStretch()
		right_layout.setSpacing(30)		#控件之间的间距
		right_layout.setContentsMargins(0, 50, 40, 0)	#布局距离窗体四周边缘距离

		#总的布局
		main_layout = QHBoxLayout()  # 水平布局
		main_layout.addStretch(1)	#空白部分比例(所有的addStretch之间的比例)
		main_layout.addLayout(left_layout)
		main_layout.addStretch(2)
		main_layout.addLayout(right_layout)
		main_layout.addStretch(1)
		main_layout.setSpacing(15)
		main_layout.setContentsMargins(0, 0, 0, 0)


		self.down_widget.setLayout(main_layout)	#最后装入down_widget返回

	def translateLanguage(self):
		self.showButton.setText(u"显示信息")
		self.rightButtonList[0].setText(u"SCALARS")
		self.rightButtonList[1].setText(u"GRAPHS")
		self.rightButtonList[2].setText(u"DISTRIBUTIONS")
		self.rightButtonList[3].setText(u"HISTOGRAMS")


	#事件过滤器(具体作用没了解)
	def eventFilter(self, obj, event):
		if(obj is QLabel):

			if(event.type() == QEvent.Paint):
				label_height_1 = self.line_label_1.height()
				label_width_1 = self.line_label_1.width()
				painter = QPainter (self.line_label_1)
				painter.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter.drawLine(label_width_1 / 2, 0, label_width_1 / 2, label_height_1)

				label_height_2 = self.line_label_2.height()
				label_width_2 = self.line_label_2.width()
				painter2 = QPainter (self.line_label_2)
				painter2.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter2.drawLine(label_width_2 / 2, 0, label_width_2 / 2, label_height_2)
				return True

		return False#self.eventFilter(obj, event)


class ContentWidget3(QWidget):
	def __init__(self, parent=None):
		super(ContentWidget3, self).__init__(parent)
		self.palette = QPalette()

		self.top_widget = QWidget()
		self.down_widget = QWidget()
		self.top_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")
		self.down_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")

		self.palette.setBrush(QPalette.Window, QBrush(Qt.white))	#创建画刷
		self.setPalette(self.palette)
		self.setAutoFillBackground(True)

		self.main_splitter = QSplitter()	#分割窗口
		self.main_splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.main_splitter.setOrientation(Qt.Vertical)	#横向排列
		self.main_splitter.setHandleWidth(1)	#设置窗口分割线
		self.main_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")

		self.InitTopWidget()	#设置上边窗体
		self.InitDownWidget()	#设置下边窗体

		#设置主窗体
		self.main_splitter.addWidget(self.top_widget)
		self.main_splitter.addWidget(self.down_widget)


		self.main_layout = QVBoxLayout()
		self.main_layout.addWidget(self.main_splitter)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)


		self.setLayout(self.main_layout)
		self.translateLanguage()

	# 设置上边窗体
	def InitTopWidget(self):

		self.computerLabel = QLabel()  # 电脑的图片
		self.showButton = QPushButton()	#显示按钮
		self.showButton.setCursor(Qt.PointingHandCursor)

		#进度条
		self.progressBar = QProgressBar()
		self.progressBar.setFixedSize(500,30)
		self.progressBar.setProperty("value", 0)


		self.top_widget.resize(650, 500)

		#电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/computer.png")
		self.computerLabel.setPixmap(label_pixmap)
		self.computerLabel.setFixedSize(label_pixmap.size())

		#显示信息按钮属性
		self.showButton.setFixedSize(150, 50)
		self.showButton.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
										"QPushButton:hover{background:rgb(140, 220, 35)}")
		searchFont = QFont()  # 字体设置
		searchFont.setPointSize(16)
		self.showButton.setFont(searchFont)


		h_layout = QHBoxLayout()  # 水平布局
		h_layout.addStretch(1)
		h_layout.addWidget(self.computerLabel, 0, Qt.AlignVCenter)  # 垂直方向居中
		h_layout.addStretch(1)
		h_layout.addWidget(self.progressBar, 0, Qt.AlignVCenter)
		h_layout.addStretch(1)
		h_layout.addWidget(self.showButton, 0, Qt.AlignVCenter)
		h_layout.addStretch(6)
		#h_layout.setSpacing(50)		#控件之间的间距
		h_layout.setContentsMargins(30, 20, 0, 0)	#布局距离窗体四周边缘距离

		self.top_widget.setLayout(h_layout)		#最后装入top_widget返回

	# 设置下边窗体
	def InitDownWidget(self):
		self.reportTextEdit = QPlainTextEdit()
		self.reportTextEdit.setFixedSize(500,270)
		self.reportTextEdit.setStyleSheet("background-image: url(./images/contentWidget/whitebackground.png);")

		self.grayTextLabel = QLabel()
		self.grayTextLabel.setFixedSize(90, 30)
		self.grayTextLabel.setStyleSheet("background: transparent;\n"
									 "font: 14pt \"Microsoft YaHei UI\";")

		self.grayPictureLabel = QLabel()  # 电脑的图片
		#电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/gray.png")
		self.grayPictureLabel.setPixmap(label_pixmap)
		self.grayPictureLabel.setFixedSize(label_pixmap.size())

		self.down_widget.resize(650, 500)

		#左侧布局（主要是为了控制距离窗体的距离）
		left_layout = QVBoxLayout()
		left_layout.addWidget(self.reportTextEdit, 0, Qt.AlignCenter)
		left_layout.setContentsMargins(40, 40, 40, 40)	#布局距离窗体四周边缘距离


		#右侧布局
		right_layout = QVBoxLayout()  # 垂直布局
		right_layout.addWidget(self.grayPictureLabel, 0, Qt.AlignCenter)
		right_layout.addWidget(self.grayTextLabel, 0, Qt.AlignCenter)
		right_layout.setSpacing(10)		#控件之间的间距
		right_layout.setContentsMargins(0, 45, 20, 0)	#布局距离窗体四周边缘距离

		#总的布局
		main_layout = QHBoxLayout()  # 水平布局
		main_layout.addStretch(1)	#空白部分比例(所有的addStretch之间的比例)
		main_layout.addLayout(left_layout)
		main_layout.addStretch(5)
		main_layout.addLayout(right_layout)
		main_layout.addStretch(1)
		main_layout.setSpacing(15)
		main_layout.setContentsMargins(0, 0, 0, 0)


		self.down_widget.setLayout(main_layout)	#最后装入down_widget返回

	def translateLanguage(self):
		self.showButton.setText(u"显示信息")
		self.grayTextLabel.setText(u"灰度图像")


	#事件过滤器(具体作用没了解)
	def eventFilter(self, obj, event):
		if(obj is QLabel):

			if(event.type() == QEvent.Paint):
				label_height_1 = self.line_label_1.height()
				label_width_1 = self.line_label_1.width()
				painter = QPainter (self.line_label_1)
				painter.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter.drawLine(label_width_1 / 2, 0, label_width_1 / 2, label_height_1)

				label_height_2 = self.line_label_2.height()
				label_width_2 = self.line_label_2.width()
				painter2 = QPainter (self.line_label_2)
				painter2.setPen(QPen(QColor(220, 220, 220), 1, Qt.DashLine))
				painter2.drawLine(label_width_2 / 2, 0, label_width_2 / 2, label_height_2)
				return True

		return False#self.eventFilter(obj, event)

class ContentWidget4(QWidget):
	def __init__(self, parent=None):
		super(ContentWidget4, self).__init__(parent)
		self.palette = QPalette()	#改变控件颜色
		self.right_widget = QWidget()
		self.left_widget = QWidget()
		self.left_widget.setStyleSheet("background-image: url(./images/contentWidget/background.png)")
		self.right_widget.setStyleSheet("background-image: url(./images/contentWidget/background_right.png)")

		self.palette.setBrush(QPalette.Window, QBrush(Qt.white))	#创建画刷
		self.setPalette(self.palette)
		self.setAutoFillBackground(True)

		self.initLeft()
		self.initRight()

		self.main_layout = QHBoxLayout()
		self.main_layout.addWidget(self.left_widget)
		self.main_layout.addWidget(self.right_widget)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.main_layout)
		self.translateLanguage()


	def initLeft(self):

		self.computerLabel = QLabel()  # 电脑的图片
		self.neuralButton = QPushButton()  # 神经网络按钮
		self.neuralButton.setCursor(Qt.PointingHandCursor)

		#中间部分文字的widget
		self.resultLabel = QLabel()
		self.resultLabel.setFixedSize(250,100)
		self.resultLabel.setStyleSheet("background: transparent;\n"
									 "font: 75 13pt \"Microsoft YaHei UI\";")

		self.left_widget.resize(650, 500)

		# 电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/computer.png")
		self.computerLabel.setPixmap(label_pixmap)
		self.computerLabel.setFixedSize(label_pixmap.size())

		# 显示神经网络按钮属性
		self.neuralButton.setFixedSize(150, 50)
		self.neuralButton.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
										"QPushButton:hover{background:rgb(140, 220, 35)}")
		searchFont = QFont()  # 字体设置
		searchFont.setPointSize(16)
		self.neuralButton.setFont(searchFont)

		#显示报告文本
		self.reportTextEdit = QPlainTextEdit()
		self.reportTextEdit.setFixedSize(600,250)
		self.reportTextEdit.setStyleSheet("background-image: url(./images/contentWidget/whitebackground.png);")


		h_layout = QHBoxLayout()  # 水平布局
		h_layout.addStretch(1)
		h_layout.addWidget(self.computerLabel, 0, Qt.AlignVCenter)  # 垂直方向居中
		h_layout.addStretch(3)
		h_layout.addWidget(self.resultLabel, 0, Qt.AlignVCenter)
		h_layout.addStretch(3)
		h_layout.addWidget(self.neuralButton, 0, Qt.AlignVCenter)
		h_layout.addStretch(6)
		# h_layout.setSpacing(50)		#控件之间的间距
		h_layout.setContentsMargins(0, 20, 0, 0)  # 布局距离窗体四周边缘距离

		v_layout = QVBoxLayout()	#垂直布局
		v_layout.addLayout(h_layout)
		v_layout.addStretch(1)
		v_layout.addWidget(self.reportTextEdit)
		v_layout.addStretch(2)
		v_layout.setContentsMargins(20, 20, 20, 0)  # 布局距离窗体四周边缘距离


		self.left_widget.setLayout(v_layout)  # 最后装入top_widget返回


	def initRight(self):

		'''self.grayTextLabel = QLabel()
		self.grayTextLabel.setFixedSize(90, 30)
		self.grayTextLabel.setStyleSheet("background: transparent;\n"
										 "font: 14pt \"Microsoft YaHei UI\";")'''

		self.grayTextbutton = QPushButton()
		self.grayTextbutton.setFixedSize(240, 60)
		self.grayTextbutton.setStyleSheet("QPushButton{color:green;border-image:url(./images/contentWidget/gray_button.png)}"
			"QPushButton:hover{color:rgb(110, 190, 10)}")
		login_font = QFont()
		login_font.setBold(True)
		login_font.setPointSize(12)
		self.grayTextbutton.setFont(login_font)

		self.grayPictureLabel = QLabel()  # 电脑的图片
		# 电脑图片属性
		label_pixmap = QPixmap("./images/contentWidget/gray4.png")
		self.grayPictureLabel.setPixmap(label_pixmap)
		self.grayPictureLabel.setFixedSize(label_pixmap.size())

		self.right_widget.resize(300, 250)

		# 右侧布局
		main_layout = QVBoxLayout()  # 垂直布局
		main_layout.addWidget(self.grayTextbutton, 0, Qt.AlignRight)
		main_layout.addWidget(self.grayPictureLabel, 0, Qt.AlignCenter)
		main_layout.setSpacing(10)  # 控件之间的间距
		main_layout.setContentsMargins(10, 0, 10, 10)  # 布局距离窗体四周边缘距离

		self.right_widget.setLayout(main_layout)  # 最后装入right_widget返回




	def translateLanguage(self):

		self.resultLabel.setText(u"当前未进行检测")
		self.neuralButton.setText(u"显示神经网络")
		self.grayTextbutton.setText(u"灰度图像")



#这个是原来360的widget
class ContentWidget5(QWidget):
	def __init__(self, parent=None):
		super(ContentWidget5, self).__init__(parent)
		self.palette = QPalette()	#改变控件颜色
		self.right_splitter = QSplitter()	#分割窗口
		self.right_top_widget = QWidget()
		self.right_center_widget = QWidget()
		self.right_bottom_widget = QWidget()
		self.right_center_function_widget = QWidget()
		self.left_widget = QWidget()

		self.palette.setBrush(QPalette.Window, QBrush(Qt.white))	#创建画刷
		self.setPalette(self.palette)
		self.setAutoFillBackground(True)
		self.main_splitter = QSplitter()	#分割窗口
		self.main_splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.main_splitter.setOrientation(Qt.Horizontal)	#横向排列
		self.main_splitter.setHandleWidth(1)	#设置窗口分割线
		self.main_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")
		self.initLeft()
		self.initRight()
		self.initRightTop()
		self.initRightCenter()
		self.initRightCenterFunction()
		self.initRightBottom()
		self.right_splitter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.right_splitter.setOrientation(Qt.Vertical)
		self.right_splitter.setHandleWidth(1)
		self.right_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")
		self.right_top_widget.setFixedSize(250, 130)
		self.right_center_widget.setFixedSize(250, 90)
		self.right_bottom_widget.setFixedSize(250, 30)
		self.right_splitter.addWidget(self.right_top_widget)
		self.right_splitter.addWidget(self.right_center_widget)
		self.right_splitter.addWidget(self.right_center_function_widget)
		self.right_splitter.addWidget(self.right_bottom_widget)
		self.main_splitter.addWidget(self.left_widget)
		self.main_splitter.addWidget(self.right_splitter)

		#禁止拖动
		for i in range(self.right_splitter.count()):
			handle = QSplitterHandle(Qt.Horizontal, self.right_splitter)
			self.right_splitter.handle(i)
			handle.setEnabled(False)


		for i in range(self.main_splitter.count()):
			handle = QSplitterHandle(Qt.Horizontal, self.right_splitter)
			self.main_splitter.handle(i)
			handle.setEnabled(False)
		self.main_layout = QHBoxLayout()
		self.main_layout.addWidget(self.main_splitter)
		self.main_layout.setSpacing(0)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.setLayout(self.main_layout)
		self.translateLanguage()


	def initLeft(self):

		#self.left_widget =  QWidget()
		self.label = QLabel()	#电脑的图片
		self.suggest_label = QLabel()
		self.system_safe_label = QLabel()
		self.power_button = QPushButton()

		self.left_widget.resize(650, 500)

		label_pixmap = QPixmap ("./images/contentWidget/computer.png")
		self.label.setPixmap(label_pixmap)
		self.label.setFixedSize(label_pixmap.size())

		#设置字体
		suggest_font = QFont()  #= self.suggest_label.font()
		suggest_font.setPointSize(12)
		suggest_font.setBold(True)
		self.suggest_label.setFont(suggest_font)
		self.suggest_label.setStyleSheet("color:gray")

		system_safe_font = QFont()#  = self.system_safe_label.font()
		system_safe_font.setBold(True)
		self.system_safe_label.setFont(system_safe_font)
		self.system_safe_label.setStyleSheet("color:gray")

		pixmap = QPixmap("./images/contentWidget/power.png") #
		self.power_button.setIcon(QIcon(pixmap))
		self.power_button.setIconSize(pixmap.size())
		self.power_button.setFixedSize(180, 70)
		self.power_button.setStyleSheet("QPushButton{border-radius:5px;background:rgb(110, 190, 10);color:white}"
			"QPushButton:hover{background:rgb(140, 220, 35)}")
		power_font = QFont()  #= self.power_button.font()
		power_font.setPointSize(16)
		self.power_button.setFont(power_font)

		v_layout = QVBoxLayout()	#垂直布局
		v_layout.addWidget(self.suggest_label)
		v_layout.addWidget(self.system_safe_label)
		v_layout.addStretch()
		v_layout.setSpacing(15)		#控件之间的间距
		v_layout.setContentsMargins(0, 20, 0, 0)	#布局距离窗体四周边缘距离

		h_layout = QHBoxLayout()	#水平布局
		h_layout.addWidget(self.label, 0, Qt.AlignTop)	#垂直方向靠上
		h_layout.addLayout(v_layout)
		h_layout.addStretch()
		h_layout.setSpacing(20)
		h_layout.setContentsMargins(30, 20, 0, 0)

		main_layout = QVBoxLayout()		#垂直布局
		main_layout.addLayout(h_layout)
		main_layout.addWidget(self.power_button, 0, Qt.AlignCenter)	#水平方向居中
		main_layout.addStretch()
		main_layout.setSpacing(0)
		main_layout.setContentsMargins(0, 0, 0, 0)

		self.left_widget.setLayout(main_layout)


	def initRight(self):

		self.right_splitter = QSplitter()
		#self.right_splitter.resize(250, 500)


	def initRightTop(self):

		self.right_top_widget = QWidget()
		self.login_button = QPushButton()
		priv_label = QLabel()
		self.info_label = QLabel()
		self.privilege_label = QLabel()
		self.register_button = QPushButton()
		safe_button = QPushButton()
		tab_button = QPushButton()
		pet_button = QPushButton()
		lottery_button = QPushButton()
		cloud_five_button = QPushButton()
		caipiao_button = QPushButton()

		self.login_button.setFixedSize(240, 60)
		self.login_button.setStyleSheet("QPushButton{color:green;border-image:url(./images/contentWidget/login.png)}"
			"QPushButton:hover{color:rgb(110, 190, 10)}")
		login_font = QFont()#  = self.login_button.font()
		login_font.setBold(True)
		login_font.setPointSize(12)
		self.login_button.setFont(login_font)

		priv_label.setPixmap(QPixmap("./images/contentWidget/priv.png"))
		safe_pixmap = QPixmap ("./images/contentWidget/360")
		safe_button.setIcon(QIcon(safe_pixmap))
		safe_button.setFixedSize(safe_pixmap.size())
		tab_pixmap = QPixmap ("./images/contentWidget/tab.png")
		tab_button.setIcon(QIcon(tab_pixmap))
		tab_button.setFixedSize(tab_pixmap.size())
		pet_pixmap = QPixmap ("./images/contentWidget/pet.png")
		pet_button.setIcon(QIcon(pet_pixmap))
		pet_button.setFixedSize(tab_pixmap.size())
		lottery_pixmap = QPixmap ("./images/contentWidget/lottery.png")
		lottery_button.setIcon(QIcon(lottery_pixmap))
		lottery_button.setFixedSize(lottery_pixmap.size())
		cloud_five_pixmap = QPixmap ("./images/contentWidget/cloud_five.png")
		cloud_five_button.setIcon(QIcon(cloud_five_pixmap))
		cloud_five_button.setFixedSize(cloud_five_pixmap.size())
		caipiao_pixmap = QPixmap ("./images/contentWidget/caipiao.png")
		caipiao_button.setIcon(QIcon(caipiao_pixmap))
		caipiao_button.setFixedSize(caipiao_pixmap.size())

		self.register_button.setCursor(Qt.PointingHandCursor)
		safe_button.setCursor(Qt.PointingHandCursor)
		tab_button.setCursor(Qt.PointingHandCursor)
		pet_button.setCursor(Qt.PointingHandCursor)
		lottery_button.setCursor(Qt.PointingHandCursor)
		cloud_five_button.setCursor(Qt.PointingHandCursor)
		caipiao_button.setCursor(Qt.PointingHandCursor)

		#修复无法parses的问题：elf.register_button.setStyleSheet("color:rgb(0, 120, 230) background:transparent")
		self.register_button.setStyleSheet("color:rgb(0, 120, 230);background:transparent")
		safe_button.setStyleSheet("background:transparent")
		tab_button.setStyleSheet("background:transparent")
		pet_button.setStyleSheet("background:transparent")
		lottery_button.setStyleSheet("background:transparent")
		cloud_five_button.setStyleSheet("background:transparent")
		caipiao_button.setStyleSheet("background:transparent")

		login_layout = QHBoxLayout()
		login_layout.addWidget(self.login_button)
		login_layout.addStretch()
		login_layout.setContentsMargins(15, 0, 0, 0)

		register_layout = QHBoxLayout()
		register_layout.addStretch()
		register_layout.addWidget(priv_label)
		register_layout.addWidget(self.info_label)
		register_layout.addWidget(self.register_button)
		register_layout.addStretch()
		register_layout.setSpacing(5)
		register_layout.setContentsMargins(0, 0, 0, 0)

		privilege_layout = QHBoxLayout()
		privilege_layout.addStretch()
		privilege_layout.addWidget(self.privilege_label)
		privilege_layout.addWidget(safe_button)
		privilege_layout.addWidget(tab_button)
		privilege_layout.addWidget(pet_button)
		privilege_layout.addWidget(lottery_button)
		privilege_layout.addWidget(cloud_five_button)
		privilege_layout.addWidget(caipiao_button)
		privilege_layout.addStretch()
		privilege_layout.setSpacing(8)
		privilege_layout.setContentsMargins(0, 0, 0, 0)

		main_layout = QVBoxLayout()
		main_layout.addStretch()
		main_layout.addLayout(login_layout)
		main_layout.addLayout(register_layout)
		main_layout.addLayout(privilege_layout)
		main_layout.addStretch()
		main_layout.setSpacing(5)
		main_layout.setContentsMargins(10, 10, 10, 10)

		self.right_top_widget.setLayout(main_layout)


	def initRightCenter(self):

		self.right_center_widget = QWidget()
		self.fireproof_button = QToolButton()
		self.triggerman_button = QToolButton()
		self.net_shop_button = QToolButton()
		self.line_label_1 = QLabel()
		self.line_label_2 = QLabel()
		self.line_label_1.setFixedWidth(10)
		self.line_label_2.setFixedWidth(10)
		self.line_label_1.installEventFilter(self)
		self.line_label_2.installEventFilter(self)

		self.fireproof_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.triggerman_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.net_shop_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

		#设置图标
		fireproof_pixmap = QPixmap ("./images/contentWidget/fireproof.png")
		self.fireproof_button.setIcon(QIcon(fireproof_pixmap))
		self.fireproof_button.setIconSize(fireproof_pixmap.size())
		self.fireproof_button.setFixedSize(fireproof_pixmap.width() + 25, fireproof_pixmap.height() + 25)

		triggerman_pixmap = QPixmap ("./images/contentWidget/triggerman.png")
		self.triggerman_button.setIcon(QIcon(triggerman_pixmap))
		self.triggerman_button.setIconSize(triggerman_pixmap.size())
		self.triggerman_button.setFixedSize(triggerman_pixmap.width() + 25, triggerman_pixmap.height() + 25)

		net_shop_pixmap = QPixmap ("./images/contentWidget/net_shop.png")
		self.net_shop_button.setIcon(QIcon(net_shop_pixmap))
		self.net_shop_button.setIconSize(net_shop_pixmap.size())
		self.net_shop_button.setFixedSize(net_shop_pixmap.width() + 25, net_shop_pixmap.height() + 25)

		self.fireproof_button.setStyleSheet("background:transparent")
		self.triggerman_button.setStyleSheet("background:transparent")
		self.net_shop_button.setStyleSheet("background:transparent")

		h_layout = QHBoxLayout()
		h_layout.addWidget(self.fireproof_button)
		h_layout.addWidget(self.line_label_1)
		h_layout.addWidget(self.triggerman_button)
		h_layout.addWidget(self.line_label_2)
		h_layout.addWidget(self.net_shop_button)
		h_layout.setSpacing(0)
		h_layout.setContentsMargins(0, 0, 0, 0)

		self.right_center_widget.setLayout(h_layout)


	def initRightCenterFunction(self):

		self.right_center_function_widget = QWidget()
		self.function_label = QLabel()
		self.more_button = QPushButton()

		function_font = QFont()#  = self.function_label.font()
		function_font.setBold(True)
		self.function_label.setFont(function_font)
		self.function_label.setStyleSheet("color:green")
		self.more_button.setFixedSize(50, 25)
		self.more_button.setStyleSheet("QPushButton{color:rgb(0, 120, 230);background:transparent}")
		self.more_button.setCursor(Qt.PointingHandCursor)

		h_layout = QHBoxLayout()
		h_layout.addWidget(self.function_label)
		h_layout.addStretch()
		h_layout.addWidget(self.more_button)
		h_layout.setSpacing(0)
		h_layout.setContentsMargins(10, 5, 0, 0)

		self.recovery_button = QToolButton()
		self.recovery_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		recovery_pixmap = QPixmap ("./images/contentWidget/recovery.png")
		self.recovery_button.setIcon(QIcon(recovery_pixmap))
		self.recovery_button.setIconSize(recovery_pixmap.size())
		self.recovery_button.setFixedSize(recovery_pixmap.width() + 50, recovery_pixmap.height() + 35)
		#修复hover样式
		self.recovery_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.mobile_button = QToolButton()
		self.mobile_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		mobile_pixmap = QPixmap ("./images/contentWidget/mobile.png")
		self.mobile_button.setIcon(QIcon(mobile_pixmap))
		self.mobile_button.setIconSize(mobile_pixmap.size())
		self.mobile_button.setFixedSize(mobile_pixmap.width() + 50, mobile_pixmap.height() + 35)
		self.mobile_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.game_box_button = QToolButton()
		self.game_box_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		game_box_pixmap = QPixmap ("./images/contentWidget/game_box.png")
		self.game_box_button.setIcon(QIcon(game_box_pixmap))
		self.game_box_button.setIconSize(game_box_pixmap.size())
		self.game_box_button.setFixedSize(game_box_pixmap.width() + 50, game_box_pixmap.height() + 35)
		self.game_box_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.desktop_button = QToolButton()
		self.desktop_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		desktop_pixmap = QPixmap ("./images/contentWidget/desktop.png")
		self.desktop_button.setIcon(QIcon(desktop_pixmap))
		self.desktop_button.setIconSize(desktop_pixmap.size())
		self.desktop_button.setFixedSize(desktop_pixmap.width() + 50, desktop_pixmap.height() + 35)
		self.desktop_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.net_repair_button = QToolButton()
		self.net_repair_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		net_repair_pixmap = QPixmap ("./images/contentWidget/net_repair.png")
		self.net_repair_button.setIcon(QIcon(net_repair_pixmap))
		self.net_repair_button.setIconSize(net_repair_pixmap.size())
		self.net_repair_button.setFixedSize(net_repair_pixmap.width() + 50, net_repair_pixmap.height() + 35)
		self.net_repair_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.auto_run_button = QToolButton()
		self.auto_run_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		auto_run_pixmap = QPixmap ("./images/contentWidget/auto_run.png")
		self.auto_run_button.setIcon(QIcon(auto_run_pixmap))
		self.auto_run_button.setIconSize(auto_run_pixmap.size())
		self.auto_run_button.setFixedSize(auto_run_pixmap.width() + 50, auto_run_pixmap.height() + 35)
		self.auto_run_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.net_speed_button = QToolButton()
		self.net_speed_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		net_speed_pixmap = QPixmap ("./images/contentWidget/net_speed.png")
		self.net_speed_button.setIcon(QIcon(net_speed_pixmap))
		self.net_speed_button.setIconSize(net_speed_pixmap.size())
		self.net_speed_button.setFixedSize(net_speed_pixmap.width() + 50, net_speed_pixmap.height() + 35)
		self.net_speed_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.net_pretext_button = QToolButton()
		self.net_pretext_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		net_pretext_pixmap = QPixmap ("./images/contentWidget/net_pretext.png")
		self.net_pretext_button.setIcon(QIcon(net_pretext_pixmap))
		self.net_pretext_button.setIconSize(net_pretext_pixmap.size())
		self.net_pretext_button.setFixedSize(net_pretext_pixmap.width() + 50, net_pretext_pixmap.height() + 35)
		self.net_pretext_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		self.first_add_button = QToolButton()
		self.first_add_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		first_add_pixmap = QPixmap ("./images/contentWidget/first_add.png")
		self.first_add_button.setIcon(QIcon(first_add_pixmap))
		self.first_add_button.setIconSize(first_add_pixmap.size())
		self.first_add_button.setFixedSize(first_add_pixmap.width() + 50, first_add_pixmap.height() + 35)
		self.first_add_button.setStyleSheet("QToolButton{background:transparent}"
			"QToolButton:hover{border-radius:5px;border:1px solid rgb(210, 225, 230)}")

		grid_layout = QGridLayout()
		grid_layout.addWidget(self.recovery_button, 0, 0)
		grid_layout.addWidget(self.mobile_button, 0, 1)
		grid_layout.addWidget(self.game_box_button, 0, 2)
		grid_layout.addWidget(self.desktop_button, 1, 0)
		grid_layout.addWidget(self.net_repair_button, 1, 1)
		grid_layout.addWidget(self.auto_run_button, 1, 2)
		grid_layout.addWidget(self.net_speed_button, 3, 0)
		grid_layout.addWidget(self.net_pretext_button, 3, 1)
		grid_layout.addWidget(self.first_add_button, 3, 2)
		grid_layout.setSpacing(0)
		grid_layout.setContentsMargins(5, 0, 5, 5)

		v_layout = QVBoxLayout()
		v_layout.addLayout(h_layout)
		v_layout.addLayout(grid_layout)
		v_layout.addStretch()
		v_layout.setSpacing(10)
		v_layout.setContentsMargins(0, 0, 0, 0)

		self.right_center_function_widget.setLayout(v_layout)


	def initRightBottom(self):

		self.right_bottom_widget = QWidget()
		icon_label = QLabel()
		self.connect_label = QLabel()
		self.version_label = QLabel()
		version_button = QPushButton()

		label_pixmap = QPixmap ("./images/contentWidget/cloud.png")
		icon_label.setPixmap(label_pixmap)
		icon_label.setFixedSize(label_pixmap.size())

		pixmap = QPixmap ("./images/contentWidget/version.png")
		version_button.setIcon(QIcon(pixmap))
		version_button.setIconSize(pixmap.size())
		version_button.setFixedSize(20, 20)
		version_button.setStyleSheet("background:transparent")

		bottom_layout = QHBoxLayout()
		bottom_layout.addWidget(icon_label)
		bottom_layout.addWidget(self.connect_label)
		bottom_layout.addStretch()
		bottom_layout.addWidget(self.version_label)
		bottom_layout.addWidget(version_button)
		bottom_layout.setSpacing(5)
		bottom_layout.setContentsMargins(10, 0, 10, 0)
		self.right_bottom_widget.setLayout(bottom_layout)


	def translateLanguage(self):

		self.suggest_label.setText(u"suggest")
		self.system_safe_label.setText(u"system safe")
		self.power_button.setText(u"power")

		self.login_button.setText(u"login home")
		self.info_label.setText(u"show beautifull icon")
		self.register_button.setText(u"register")
		self.privilege_label.setText(u"privilege power")

		self.fireproof_button.setText(u"fireproof")
		self.triggerman_button.setText(u"triggerman")
		self.net_shop_button.setText(u"net shop")

		self.function_label.setText(u"function")
		self.more_button.setText(u"more")
		self.recovery_button.setText(u"recovery")
		self.mobile_button.setText(u"mobile")
		self.game_box_button.setText(u"game box")
		self.desktop_button.setText(u"desktop")
		self.net_repair_button.setText(u"net repair")
		self.auto_run_button.setText(u"auto run")
		self.net_speed_button.setText(u"net speed")
		self.net_pretext_button.setText(u"net pretext")
		self.first_add_button.setText(u"first add")

		self.connect_label.setText(u"connect success")
		self.version_label.setText(u"version")

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	content = ContentWidget()
	content.show()
	sys.exit(app.exec_())


