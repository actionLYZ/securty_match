
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
import Global

class MainMenu(QMenu):
	def __init__(self,parent = None):
		super(MainMenu,self).__init__()
		self.createActions()
		self.translateActions()

	def createActions(self):

		#创建菜单项
		self.action_setting =  QAction(self)
		self.action_character =  QAction(self)
		self.action_check_update =  QAction(self)
		self.action_change_company =  QAction(self)
		self.action_help_online =  QAction(self)
		self.action_platform_help =  QAction(self)
		self.action_login_home =  QAction(self)
		self.action_protect =  QAction(self)
		self.action_about_us =  QAction(self)

		self.action_about_us.setIcon(QIcon("./img/mainMenu/about.png"))
		self.action_help_online.setIcon(QIcon("./img/mainMenu/help.png"))
		self.action_check_update.setIcon(QIcon("./img/mainMenu/update.png"))
		self.action_setting.setIcon(QIcon("./img/mainMenu/setting.png"))

		#添加菜单项
		self.addAction(self.action_setting)
		self.addAction(self.action_character)
		self.addAction(self.action_check_update)
		self.addAction(self.action_change_company)
		self.addSeparator()
		self.addAction(self.action_help_online)
		self.addAction(self.action_platform_help)
		self.addAction(self.action_login_home)
		self.addAction(self.action_protect)
		self.addAction(self.action_about_us)

		#设置信号连接
		self.action_setting.triggered.connect(Global.main_widget.showSettingDialog)
		self.action_character.triggered.connect(Global.main_widget.showCharacter)
		self.action_about_us.triggered.connect(Global.main_widget.showAboutUs)

	def translateActions(self):
		self.action_setting.setText(u"setting")
		self.action_character.setText(u" character")
		self.action_check_update.setText(u"check update")
		self.action_change_company.setText(u"change company")
		self.action_help_online.setText(u"help online")
		self.action_platform_help.setText(u"platform help")
		self.action_login_home.setText(u"login home")
		self.action_protect.setText(u"protect")
		self.action_about_us.setText(u"about us")

