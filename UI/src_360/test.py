
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

		'''self.main_splitter = QSplitter()	#分割窗口
		self.main_splitter.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.main_splitter.setOrientation(Qt.Vertical)	#横向排列
		self.main_splitter.setHandleWidth(1)	#设置窗口分割线
		self.main_splitter.setStyleSheet("QSplitter.handle{background:lightgray}")'''

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
		h_layout.addWidget(self.computerLabel, 0, Qt.AlignVCenter)  # 垂直方向居中
		h_layout.addWidget(self.urlTextEdit, 0, Qt.AlignVCenter)
		h_layout.addWidget(self.searchButton, 0, Qt.AlignVCenter)

		h_layout.addStretch()
		h_layout.setSpacing(50)		#控件之间的间距
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
		main_layout.addWidget(self.leftBigIconLabel)
		main_layout.addStretch(3)
		main_layout.addLayout(icon_layout)
		main_layout.addStretch(1)
		main_layout.addLayout(text_layout)
		main_layout.addStretch(3)
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