# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboard.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if not dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1500, 1000)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 1000))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.other_fields)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(100, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(100, 0))
        self.controls_frame.setMaximumSize(QSize(100, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(40, 20, 16, 16))
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(10, 20, 16, 16))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")
        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 16, 16))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(70, 0))
        self.menu_frame.setMaximumSize(QSize(80, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(40, 40))
        self.btn_search.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_search)

        self.btn_camera = QPushButton(self.frame)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(0, 70))
        self.btn_camera.setMaximumSize(QSize(16777215, 70))
        self.btn_camera.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon2)
        self.btn_camera.setIconSize(QSize(40, 40))
        self.btn_camera.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_camera)

        self.btn_database = QPushButton(self.frame)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setMinimumSize(QSize(0, 70))
        self.btn_database.setMaximumSize(QSize(16777215, 70))
        self.btn_database.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon3)
        self.btn_database.setIconSize(QSize(45, 45))
        self.btn_database.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_database)

        self.btn_report = QPushButton(self.frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(0, 70))
        self.btn_report.setMaximumSize(QSize(16777215, 70))
        self.btn_report.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon4)
        self.btn_report.setIconSize(QSize(40, 40))
        self.btn_report.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_report)

        self.btn_help = QPushButton(self.frame)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 70))
        self.btn_help.setMaximumSize(QSize(16777215, 70))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon5)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_help)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 470))
        self.info_frame.setMaximumSize(QSize(16777215, 600))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 261, 291))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.image.setFont(font1)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 20, 201, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.firstname.setFont(font2)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(290, 70, 201, 41))
        self.middlename.setFont(font2)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 120, 201, 41))
        self.lastname.setFont(font2)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(290, 170, 201, 41))
        self.refrence.setFont(font2)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(290, 220, 201, 41))
        self.index.setFont(font2)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coledge = QLabel(self.info_frame)
        self.coledge.setObjectName(u"coledge")
        self.coledge.setGeometry(QRect(290, 270, 201, 41))
        self.coledge.setFont(font2)
        self.coledge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.coledge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.validity = QLabel(self.info_frame)
        self.validity.setObjectName(u"validity")
        self.validity.setGeometry(QRect(20, 320, 261, 41))
        self.validity.setFont(font2)
        self.validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nationality = QLabel(self.info_frame)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setGeometry(QRect(290, 320, 201, 41))
        self.nationality.setFont(font2)
        self.nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_in = QLabel(self.info_frame)
        self.last_in.setObjectName(u"last_in")
        self.last_in.setGeometry(QRect(20, 420, 231, 41))
        self.last_in.setFont(font2)
        self.last_in.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.last_in.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.year = QLabel(self.info_frame)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(20, 370, 151, 41))
        self.year.setFont(font2)
        self.year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.program = QLabel(self.info_frame)
        self.program.setObjectName(u"program")
        self.program.setGeometry(QRect(180, 370, 311, 41))
        self.program.setFont(font2)
        self.program.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.program.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_out = QLabel(self.info_frame)
        self.last_out.setObjectName(u"last_out")
        self.last_out.setGeometry(QRect(260, 420, 231, 41))
        self.last_out.setFont(font2)
        self.last_out.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.last_out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(20, 360, 471, 101))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.date_frame_2 = QFrame(self.frame_3)
        self.date_frame_2.setObjectName(u"date_frame_2")
        self.date_frame_2.setGeometry(QRect(20, 10, 471, 41))
        self.date_frame_2.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame_2.setFrameShape(QFrame.StyledPanel)
        self.date_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.date_frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.face_auth = QRadioButton(self.date_frame_2)
        self.face_auth.setObjectName(u"face_auth")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.face_auth.setFont(font4)
        self.face_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.face_auth.setIcon(icon6)
        self.face_auth.setChecked(False)

        self.horizontalLayout_13.addWidget(self.face_auth)

        self.qr_code_auth = QRadioButton(self.date_frame_2)
        self.qr_code_auth.setObjectName(u"qr_code_auth")
        self.qr_code_auth.setFont(font4)
        self.qr_code_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.qr_code_auth.setIcon(icon6)
        self.qr_code_auth.setChecked(False)

        self.horizontalLayout_13.addWidget(self.qr_code_auth)

        self.biometric_auth = QRadioButton(self.date_frame_2)
        self.biometric_auth.setObjectName(u"biometric_auth")
        self.biometric_auth.setFont(font4)
        self.biometric_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.biometric_auth.setIcon(icon6)
        self.biometric_auth.setChecked(True)

        self.horizontalLayout_13.addWidget(self.biometric_auth)

        self.camera_ip = QLineEdit(self.frame_3)
        self.camera_ip.setObjectName(u"camera_ip")
        self.camera_ip.setGeometry(QRect(30, 90, 451, 51))
        font5 = QFont()
        font5.setPointSize(10)
        self.camera_ip.setFont(font5)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_ip.setClearButtonEnabled(True)
        self.btn_connect_detect = QPushButton(self.frame_3)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(30, 150, 131, 41))
        self.btn_connect_detect.setFont(font5)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_detect.setIcon(icon7)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(40, 100, 41, 31))
        self.label_27.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(170, 150, 141, 41))
        self.btn_disconnect.setFont(font5)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon8)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(320, 150, 161, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.firstname_23 = QLabel(self.frame_3)
        self.firstname_23.setObjectName(u"firstname_23")
        self.firstname_23.setGeometry(QRect(20, 60, 471, 141))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.firstname_23.setFont(font6)
        self.firstname_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_24 = QLabel(self.frame_3)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(20, 210, 471, 141))
        self.firstname_24.setFont(font6)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_exit_cam_disconect = QPushButton(self.frame_3)
        self.btn_exit_cam_disconect.setObjectName(u"btn_exit_cam_disconect")
        self.btn_exit_cam_disconect.setGeometry(QRect(170, 300, 141, 41))
        self.btn_exit_cam_disconect.setFont(font5)
        self.btn_exit_cam_disconect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_exit_cam_disconect.setIcon(icon8)
        self.btn_exit_cam_disconect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_disconect.setFlat(True)
        self.btn_exit_cam_ip = QLineEdit(self.frame_3)
        self.btn_exit_cam_ip.setObjectName(u"btn_exit_cam_ip")
        self.btn_exit_cam_ip.setGeometry(QRect(30, 240, 451, 51))
        self.btn_exit_cam_ip.setFont(font5)
        self.btn_exit_cam_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.btn_exit_cam_ip.setClearButtonEnabled(True)
        self.exit_comboBox = QComboBox(self.frame_3)
        self.exit_comboBox.addItem("")
        self.exit_comboBox.setObjectName(u"exit_comboBox")
        self.exit_comboBox.setGeometry(QRect(320, 300, 161, 38))
        self.exit_comboBox.setMinimumSize(QSize(0, 38))
        self.exit_comboBox.setMaximumSize(QSize(16777215, 38))
        self.exit_comboBox.setFont(font5)
        self.exit_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.exit_comboBox.setFrame(False)
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(40, 250, 41, 31))
        self.label_28.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_exit_cam_connect = QPushButton(self.frame_3)
        self.btn_exit_cam_connect.setObjectName(u"btn_exit_cam_connect")
        self.btn_exit_cam_connect.setGeometry(QRect(30, 300, 131, 41))
        self.btn_exit_cam_connect.setFont(font5)
        self.btn_exit_cam_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_exit_cam_connect.setIcon(icon7)
        self.btn_exit_cam_connect.setIconSize(QSize(30, 30))
        self.btn_exit_cam_connect.setFlat(True)
        self.firstname_23.raise_()
        self.label_notification.raise_()
        self.date_frame_2.raise_()
        self.camera_ip.raise_()
        self.btn_connect_detect.raise_()
        self.label_27.raise_()
        self.btn_disconnect.raise_()
        self.comboBox.raise_()
        self.firstname_24.raise_()
        self.btn_exit_cam_disconect.raise_()
        self.btn_exit_cam_ip.raise_()
        self.exit_comboBox.raise_()
        self.label_28.raise_()
        self.btn_exit_cam_connect.raise_()

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 700))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 700))
        self.camera_frame.setMaximumSize(QSize(16777215, 700))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font1)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 3, -1, 0)
        self.entry_dilation_label = QLabel(self.frame_4)
        self.entry_dilation_label.setObjectName(u"entry_dilation_label")
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(8)
        font7.setBold(False)
        self.entry_dilation_label.setFont(font7)
        self.entry_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_dilation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_dilation_label, 1, 0, 1, 1)

        self.dilation = QSlider(self.frame_4)
        self.dilation.setObjectName(u"dilation")
        self.dilation.setMaximum(500)
        self.dilation.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.dilation, 1, 1, 1, 1)

        self.entry_erosion_label = QLabel(self.frame_4)
        self.entry_erosion_label.setObjectName(u"entry_erosion_label")
        self.entry_erosion_label.setFont(font7)
        self.entry_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_erosion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_erosion_label, 2, 0, 1, 1)

        self.erosion = QSlider(self.frame_4)
        self.erosion.setObjectName(u"erosion")
        self.erosion.setMaximum(500)
        self.erosion.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.erosion, 2, 1, 1, 1)

        self.entry_blur_label = QLabel(self.frame_4)
        self.entry_blur_label.setObjectName(u"entry_blur_label")
        self.entry_blur_label.setFont(font7)
        self.entry_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_blur_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_blur_label, 3, 0, 1, 1)

        self.blur = QSlider(self.frame_4)
        self.blur.setObjectName(u"blur")
        self.blur.setMaximum(500)
        self.blur.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.blur, 3, 1, 1, 1)

        self.entry_unimp_label = QLabel(self.frame_4)
        self.entry_unimp_label.setObjectName(u"entry_unimp_label")
        self.entry_unimp_label.setFont(font7)
        self.entry_unimp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_unimp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_unimp_label, 4, 0, 1, 1)

        self.horizontalSlider_4 = QSlider(self.frame_4)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setMaximum(500)
        self.horizontalSlider_4.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider_4, 4, 1, 1, 1)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 0, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 3, -1, 0)
        self.exit_dilation_label = QLabel(self.frame_5)
        self.exit_dilation_label.setObjectName(u"exit_dilation_label")
        self.exit_dilation_label.setFont(font7)
        self.exit_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_dilation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_dilation_label, 1, 0, 1, 1)

        self.exit_cam_dilation = QSlider(self.frame_5)
        self.exit_cam_dilation.setObjectName(u"exit_cam_dilation")
        self.exit_cam_dilation.setMaximum(500)
        self.exit_cam_dilation.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.exit_cam_dilation, 1, 1, 1, 1)

        self.exit_erosion_label = QLabel(self.frame_5)
        self.exit_erosion_label.setObjectName(u"exit_erosion_label")
        self.exit_erosion_label.setFont(font7)
        self.exit_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_erosion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_erosion_label, 2, 0, 1, 1)

        self.exit_cam_erosion = QSlider(self.frame_5)
        self.exit_cam_erosion.setObjectName(u"exit_cam_erosion")
        self.exit_cam_erosion.setMaximum(500)
        self.exit_cam_erosion.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.exit_cam_erosion, 2, 1, 1, 1)

        self.exit_blur_label = QLabel(self.frame_5)
        self.exit_blur_label.setObjectName(u"exit_blur_label")
        self.exit_blur_label.setFont(font7)
        self.exit_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_blur_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_blur_label, 3, 0, 1, 1)

        self.exit_cam_blur = QSlider(self.frame_5)
        self.exit_cam_blur.setObjectName(u"exit_cam_blur")
        self.exit_cam_blur.setMaximum(500)
        self.exit_cam_blur.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.exit_cam_blur, 3, 1, 1, 1)

        self.exit_umimpl = QLabel(self.frame_5)
        self.exit_umimpl.setObjectName(u"exit_umimpl")
        self.exit_umimpl.setFont(font7)
        self.exit_umimpl.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_umimpl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_umimpl, 4, 0, 1, 1)

        self.horizontalSlider_5 = QSlider(self.frame_5)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        self.horizontalSlider_5.setMaximum(500)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_5, 4, 1, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_frame_2 = QFrame(self.search)
        self.left_frame_2.setObjectName(u"left_frame_2")
        self.left_frame_2.setMinimumSize(QSize(500, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 400))
        self.top.setMaximumSize(QSize(600, 418))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_validity = QLabel(self.top)
        self.db_validity.setObjectName(u"db_validity")
        self.db_validity.setGeometry(QRect(20, 320, 261, 41))
        self.db_validity.setFont(font2)
        self.db_validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(290, 170, 201, 41))
        self.db_refrence.setFont(font2)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_year = QLabel(self.top)
        self.db_year.setObjectName(u"db_year")
        self.db_year.setGeometry(QRect(20, 370, 151, 41))
        self.db_year.setFont(font3)
        self.db_year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_nationality = QLabel(self.top)
        self.db_nationality.setObjectName(u"db_nationality")
        self.db_nationality.setGeometry(QRect(290, 320, 201, 41))
        self.db_nationality.setFont(font2)
        self.db_nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 20, 261, 291))
        self.db_image_data.setFont(font1)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(290, 120, 201, 41))
        self.db_lastname.setFont(font2)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(290, 70, 201, 41))
        self.db_middlename.setFont(font2)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(290, 20, 201, 41))
        self.db_firstname.setFont(font2)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_index = QLabel(self.top)
        self.db_index.setObjectName(u"db_index")
        self.db_index.setGeometry(QRect(290, 220, 201, 41))
        self.db_index.setFont(font2)
        self.db_index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_programe = QLabel(self.top)
        self.db_programe.setObjectName(u"db_programe")
        self.db_programe.setGeometry(QRect(180, 370, 311, 41))
        self.db_programe.setFont(font2)
        self.db_programe.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_programe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_college = QLabel(self.top)
        self.db_college.setObjectName(u"db_college")
        self.db_college.setGeometry(QRect(290, 270, 201, 41))
        self.db_college.setFont(font2)
        self.db_college.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_college.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.search_box = QLineEdit(self.bottom)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(30, 20, 321, 51))
        self.search_box.setFont(font5)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_box.setClearButtonEnabled(True)
        self.btn_print = QPushButton(self.bottom)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setGeometry(QRect(30, 80, 131, 41))
        self.btn_print.setFont(font5)
        self.btn_print.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print.setIcon(icon9)
        self.btn_print.setIconSize(QSize(30, 30))
        self.btn_print.setFlat(True)
        self.btn_dump_csv = QPushButton(self.bottom)
        self.btn_dump_csv.setObjectName(u"btn_dump_csv")
        self.btn_dump_csv.setGeometry(QRect(190, 80, 141, 41))
        self.btn_dump_csv.setFont(font5)
        self.btn_dump_csv.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dump_csv.setIcon(icon10)
        self.btn_dump_csv.setIconSize(QSize(30, 30))
        self.btn_dump_csv.setFlat(True)
        self.btn_reload = QPushButton(self.bottom)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setGeometry(QRect(360, 80, 121, 41))
        self.btn_reload.setFont(font5)
        self.btn_reload.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reload.setIcon(icon11)
        self.btn_reload.setIconSize(QSize(30, 30))
        self.btn_reload.setFlat(True)
        self.frame_6 = QFrame(self.bottom)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(30, 270, 451, 241))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setNavigationBarVisible(True)

        self.verticalLayout_12.addWidget(self.calendarWidget)

        self.start_date = QRadioButton(self.bottom)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(30, 240, 95, 20))
        self.start_date.setFont(font4)
        self.start_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.end_date = QRadioButton(self.bottom)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(150, 240, 95, 20))
        self.end_date.setFont(font4)
        self.end_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.label_24 = QLabel(self.bottom)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(270, 180, 31, 31))
        self.label_24.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(30, 170, 211, 51))
        self.db_start_date.setFont(font5)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_start_date.setClearButtonEnabled(True)
        self.db_end_date = QLineEdit(self.bottom)
        self.db_end_date.setObjectName(u"db_end_date")
        self.db_end_date.setGeometry(QRect(260, 170, 221, 51))
        self.db_end_date.setFont(font5)
        self.db_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_end_date.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.bottom)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(40, 180, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_29 = QLabel(self.bottom)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(20, 10, 471, 121))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(20, 150, 471, 371))
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_search_page = QPushButton(self.bottom)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(360, 20, 121, 51))
        self.btn_search_page.setFont(font5)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search_page.setIcon(icon1)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_30.raise_()
        self.label_29.raise_()
        self.search_box.raise_()
        self.btn_print.raise_()
        self.btn_dump_csv.raise_()
        self.btn_reload.raise_()
        self.frame_6.raise_()
        self.start_date.raise_()
        self.end_date.raise_()
        self.label_24.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.db_end_date.raise_()
        self.btn_search_page.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.StyledPanel)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 23):
            self.tableWidget.setRowCount(23)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(23)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_5.addWidget(self.rigth_frame)

        self.stackedWidget.addWidget(self.search)
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.horizontalLayout_6 = QHBoxLayout(self.camera)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_child = QFrame(self.camera)
        self.left_child.setObjectName(u"left_child")
        self.left_child.setMaximumSize(QSize(450, 16777215))
        self.left_child.setFrameShape(QFrame.NoFrame)
        self.left_child.setFrameShadow(QFrame.Plain)
        self.btn_cast = QPushButton(self.left_child)
        self.btn_cast.setObjectName(u"btn_cast")
        self.btn_cast.setGeometry(QRect(20, 690, 131, 41))
        self.btn_cast.setFont(font5)
        self.btn_cast.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/cast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cast.setIcon(icon12)
        self.btn_cast.setIconSize(QSize(30, 30))
        self.btn_cast.setFlat(True)
        self.btn_capture = QPushButton(self.left_child)
        self.btn_capture.setObjectName(u"btn_capture")
        self.btn_capture.setGeometry(QRect(300, 690, 141, 41))
        self.btn_capture.setFont(font5)
        self.btn_capture.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/asset/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_capture.setIcon(icon13)
        self.btn_capture.setIconSize(QSize(30, 30))
        self.btn_capture.setFlat(True)
        self.btn_cast_all = QPushButton(self.left_child)
        self.btn_cast_all.setObjectName(u"btn_cast_all")
        self.btn_cast_all.setGeometry(QRect(160, 690, 131, 41))
        self.btn_cast_all.setFont(font5)
        self.btn_cast_all.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_cast_all.setIcon(icon12)
        self.btn_cast_all.setIconSize(QSize(30, 30))
        self.btn_cast_all.setFlat(True)
        self.image_file_name = QLineEdit(self.left_child)
        self.image_file_name.setObjectName(u"image_file_name")
        self.image_file_name.setGeometry(QRect(20, 630, 201, 51))
        self.image_file_name.setFont(font5)
        self.image_file_name.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_file_name.setClearButtonEnabled(True)
        self.label_4 = QLabel(self.left_child)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 640, 31, 31))
        self.label_4.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.video_file_name = QLineEdit(self.left_child)
        self.video_file_name.setObjectName(u"video_file_name")
        self.video_file_name.setGeometry(QRect(240, 630, 201, 51))
        self.video_file_name.setFont(font5)
        self.video_file_name.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.video_file_name.setClearButtonEnabled(True)
        self.label_15 = QLabel(self.left_child)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(250, 640, 31, 31))
        self.label_15.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.btn_capture_video = QPushButton(self.left_child)
        self.btn_capture_video.setObjectName(u"btn_capture_video")
        self.btn_capture_video.setGeometry(QRect(20, 740, 131, 41))
        self.btn_capture_video.setFont(font5)
        self.btn_capture_video.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_capture_video.setIcon(icon7)
        self.btn_capture_video.setIconSize(QSize(30, 30))
        self.btn_capture_video.setFlat(True)
        self.firstname_25 = QLabel(self.left_child)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 10, 441, 141))
        self.firstname_25.setFont(font6)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_camera_one_connect = QPushButton(self.left_child)
        self.btn_camera_one_connect.setObjectName(u"btn_camera_one_connect")
        self.btn_camera_one_connect.setGeometry(QRect(20, 100, 131, 41))
        self.btn_camera_one_connect.setFont(font5)
        self.btn_camera_one_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_one_connect.setIcon(icon7)
        self.btn_camera_one_connect.setIconSize(QSize(30, 30))
        self.btn_camera_one_connect.setFlat(True)
        self.btn_camera_one_disconnect = QPushButton(self.left_child)
        self.btn_camera_one_disconnect.setObjectName(u"btn_camera_one_disconnect")
        self.btn_camera_one_disconnect.setGeometry(QRect(160, 100, 141, 41))
        self.btn_camera_one_disconnect.setFont(font5)
        self.btn_camera_one_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_one_disconnect.setIcon(icon8)
        self.btn_camera_one_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_one_disconnect.setFlat(True)
        self.camera_one_comboBox = QComboBox(self.left_child)
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.setObjectName(u"camera_one_comboBox")
        self.camera_one_comboBox.setGeometry(QRect(310, 100, 131, 38))
        self.camera_one_comboBox.setMinimumSize(QSize(0, 38))
        self.camera_one_comboBox.setMaximumSize(QSize(16777215, 38))
        self.camera_one_comboBox.setFont(font5)
        self.camera_one_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.camera_one_comboBox.setFrame(False)
        self.camera_one_id_ip = QLineEdit(self.left_child)
        self.camera_one_id_ip.setObjectName(u"camera_one_id_ip")
        self.camera_one_id_ip.setGeometry(QRect(20, 40, 421, 51))
        self.camera_one_id_ip.setFont(font5)
        self.camera_one_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_one_id_ip.setClearButtonEnabled(True)
        self.label_31 = QLabel(self.left_child)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 50, 41, 31))
        self.label_31.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_two_disconnect = QPushButton(self.left_child)
        self.btn_camera_two_disconnect.setObjectName(u"btn_camera_two_disconnect")
        self.btn_camera_two_disconnect.setGeometry(QRect(160, 250, 141, 41))
        self.btn_camera_two_disconnect.setFont(font5)
        self.btn_camera_two_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_two_disconnect.setIcon(icon8)
        self.btn_camera_two_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_two_disconnect.setFlat(True)
        self.camera_two_comboBox = QComboBox(self.left_child)
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.setObjectName(u"camera_two_comboBox")
        self.camera_two_comboBox.setGeometry(QRect(310, 250, 131, 38))
        self.camera_two_comboBox.setMinimumSize(QSize(0, 38))
        self.camera_two_comboBox.setMaximumSize(QSize(16777215, 38))
        self.camera_two_comboBox.setFont(font5)
        self.camera_two_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.camera_two_comboBox.setFrame(False)
        self.camera_two_id_ip = QLineEdit(self.left_child)
        self.camera_two_id_ip.setObjectName(u"camera_two_id_ip")
        self.camera_two_id_ip.setGeometry(QRect(20, 190, 421, 51))
        self.camera_two_id_ip.setFont(font5)
        self.camera_two_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_two_id_ip.setClearButtonEnabled(True)
        self.btn_camera_two_connect = QPushButton(self.left_child)
        self.btn_camera_two_connect.setObjectName(u"btn_camera_two_connect")
        self.btn_camera_two_connect.setGeometry(QRect(20, 250, 131, 41))
        self.btn_camera_two_connect.setFont(font5)
        self.btn_camera_two_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_two_connect.setIcon(icon7)
        self.btn_camera_two_connect.setIconSize(QSize(30, 30))
        self.btn_camera_two_connect.setFlat(True)
        self.firstname_26 = QLabel(self.left_child)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 160, 441, 141))
        self.firstname_26.setFont(font6)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_32 = QLabel(self.left_child)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(30, 200, 41, 31))
        self.label_32.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_three_disconnect = QPushButton(self.left_child)
        self.btn_camera_three_disconnect.setObjectName(u"btn_camera_three_disconnect")
        self.btn_camera_three_disconnect.setGeometry(QRect(160, 400, 141, 41))
        self.btn_camera_three_disconnect.setFont(font5)
        self.btn_camera_three_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_three_disconnect.setIcon(icon8)
        self.btn_camera_three_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_three_disconnect.setFlat(True)
        self.camera_three_comboBox = QComboBox(self.left_child)
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.setObjectName(u"camera_three_comboBox")
        self.camera_three_comboBox.setGeometry(QRect(310, 400, 131, 38))
        self.camera_three_comboBox.setMinimumSize(QSize(0, 38))
        self.camera_three_comboBox.setMaximumSize(QSize(16777215, 38))
        self.camera_three_comboBox.setFont(font5)
        self.camera_three_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.camera_three_comboBox.setFrame(False)
        self.camera_three_id_ip = QLineEdit(self.left_child)
        self.camera_three_id_ip.setObjectName(u"camera_three_id_ip")
        self.camera_three_id_ip.setGeometry(QRect(20, 340, 421, 51))
        self.camera_three_id_ip.setFont(font5)
        self.camera_three_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_three_id_ip.setClearButtonEnabled(True)
        self.btn_camera_three_connect = QPushButton(self.left_child)
        self.btn_camera_three_connect.setObjectName(u"btn_camera_three_connect")
        self.btn_camera_three_connect.setGeometry(QRect(20, 400, 131, 41))
        self.btn_camera_three_connect.setFont(font5)
        self.btn_camera_three_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_three_connect.setIcon(icon7)
        self.btn_camera_three_connect.setIconSize(QSize(30, 30))
        self.btn_camera_three_connect.setFlat(True)
        self.firstname_27 = QLabel(self.left_child)
        self.firstname_27.setObjectName(u"firstname_27")
        self.firstname_27.setGeometry(QRect(10, 310, 441, 141))
        self.firstname_27.setFont(font6)
        self.firstname_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_33 = QLabel(self.left_child)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 350, 41, 31))
        self.label_33.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_four_disconnect = QPushButton(self.left_child)
        self.btn_camera_four_disconnect.setObjectName(u"btn_camera_four_disconnect")
        self.btn_camera_four_disconnect.setGeometry(QRect(160, 550, 141, 41))
        self.btn_camera_four_disconnect.setFont(font5)
        self.btn_camera_four_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_four_disconnect.setIcon(icon8)
        self.btn_camera_four_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_four_disconnect.setFlat(True)
        self.camera_four_comboBox = QComboBox(self.left_child)
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.setObjectName(u"camera_four_comboBox")
        self.camera_four_comboBox.setGeometry(QRect(310, 550, 131, 38))
        self.camera_four_comboBox.setMinimumSize(QSize(0, 38))
        self.camera_four_comboBox.setMaximumSize(QSize(16777215, 38))
        self.camera_four_comboBox.setFont(font5)
        self.camera_four_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.camera_four_comboBox.setFrame(False)
        self.camera_four_id_ip = QLineEdit(self.left_child)
        self.camera_four_id_ip.setObjectName(u"camera_four_id_ip")
        self.camera_four_id_ip.setGeometry(QRect(20, 490, 421, 51))
        self.camera_four_id_ip.setFont(font5)
        self.camera_four_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_four_id_ip.setClearButtonEnabled(True)
        self.btn_camera_four_connect = QPushButton(self.left_child)
        self.btn_camera_four_connect.setObjectName(u"btn_camera_four_connect")
        self.btn_camera_four_connect.setGeometry(QRect(20, 550, 131, 41))
        self.btn_camera_four_connect.setFont(font5)
        self.btn_camera_four_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_four_connect.setIcon(icon7)
        self.btn_camera_four_connect.setIconSize(QSize(30, 30))
        self.btn_camera_four_connect.setFlat(True)
        self.firstname_28 = QLabel(self.left_child)
        self.firstname_28.setObjectName(u"firstname_28")
        self.firstname_28.setGeometry(QRect(10, 460, 441, 141))
        self.firstname_28.setFont(font6)
        self.firstname_28.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_34 = QLabel(self.left_child)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 500, 41, 31))
        self.label_34.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.firstname_29 = QLabel(self.left_child)
        self.firstname_29.setObjectName(u"firstname_29")
        self.firstname_29.setGeometry(QRect(10, 620, 441, 171))
        self.firstname_29.setFont(font6)
        self.firstname_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.notification = QLabel(self.left_child)
        self.notification.setObjectName(u"notification")
        self.notification.setGeometry(QRect(10, 810, 441, 131))
        self.notification.setFont(font3)
        self.notification.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.notification.setAlignment(Qt.AlignCenter)
        self.camera_four_comboBox_2 = QComboBox(self.left_child)
        self.camera_four_comboBox_2.addItem("")
        self.camera_four_comboBox_2.addItem("")
        self.camera_four_comboBox_2.addItem("")
        self.camera_four_comboBox_2.addItem("")
        self.camera_four_comboBox_2.setObjectName(u"camera_four_comboBox_2")
        self.camera_four_comboBox_2.setGeometry(QRect(300, 740, 141, 38))
        self.camera_four_comboBox_2.setMinimumSize(QSize(0, 38))
        self.camera_four_comboBox_2.setMaximumSize(QSize(16777215, 38))
        self.camera_four_comboBox_2.setFont(font5)
        self.camera_four_comboBox_2.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.camera_four_comboBox_2.setFrame(False)
        self.btn_capture_video_2 = QPushButton(self.left_child)
        self.btn_capture_video_2.setObjectName(u"btn_capture_video_2")
        self.btn_capture_video_2.setGeometry(QRect(160, 740, 131, 41))
        self.btn_capture_video_2.setFont(font5)
        self.btn_capture_video_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_capture_video_2.setIcon(icon8)
        self.btn_capture_video_2.setIconSize(QSize(30, 30))
        self.btn_capture_video_2.setFlat(True)
        self.firstname_29.raise_()
        self.firstname_28.raise_()
        self.firstname_27.raise_()
        self.firstname_26.raise_()
        self.btn_cast.raise_()
        self.btn_capture.raise_()
        self.btn_cast_all.raise_()
        self.image_file_name.raise_()
        self.label_4.raise_()
        self.video_file_name.raise_()
        self.label_15.raise_()
        self.btn_capture_video.raise_()
        self.firstname_25.raise_()
        self.btn_camera_one_connect.raise_()
        self.btn_camera_one_disconnect.raise_()
        self.camera_one_comboBox.raise_()
        self.camera_one_id_ip.raise_()
        self.label_31.raise_()
        self.btn_camera_two_disconnect.raise_()
        self.camera_two_comboBox.raise_()
        self.camera_two_id_ip.raise_()
        self.btn_camera_two_connect.raise_()
        self.label_32.raise_()
        self.btn_camera_three_disconnect.raise_()
        self.camera_three_comboBox.raise_()
        self.camera_three_id_ip.raise_()
        self.btn_camera_three_connect.raise_()
        self.label_33.raise_()
        self.btn_camera_four_disconnect.raise_()
        self.camera_four_comboBox.raise_()
        self.camera_four_id_ip.raise_()
        self.btn_camera_four_connect.raise_()
        self.label_34.raise_()
        self.notification.raise_()
        self.camera_four_comboBox_2.raise_()
        self.btn_capture_video_2.raise_()

        self.horizontalLayout_6.addWidget(self.left_child)

        self.rignt_child = QFrame(self.camera)
        self.rignt_child.setObjectName(u"rignt_child")
        self.rignt_child.setFrameShape(QFrame.NoFrame)
        self.rignt_child.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.rignt_child)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.camera_down = QFrame(self.rignt_child)
        self.camera_down.setObjectName(u"camera_down")
        self.camera_down.setFrameShape(QFrame.StyledPanel)
        self.camera_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.camera_down)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.camera_1 = QLabel(self.camera_down)
        self.camera_1.setObjectName(u"camera_1")
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(20)
        font8.setBold(True)
        self.camera_1.setFont(font8)
        self.camera_1.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_1)

        self.camera_2 = QLabel(self.camera_down)
        self.camera_2.setObjectName(u"camera_2")
        self.camera_2.setFont(font8)
        self.camera_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_2)


        self.verticalLayout_10.addWidget(self.camera_down)

        self.camera_top = QFrame(self.rignt_child)
        self.camera_top.setObjectName(u"camera_top")
        self.camera_top.setFrameShape(QFrame.StyledPanel)
        self.camera_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.camera_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.camera_3 = QLabel(self.camera_top)
        self.camera_3.setObjectName(u"camera_3")
        self.camera_3.setFont(font8)
        self.camera_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_3)

        self.camera_4 = QLabel(self.camera_top)
        self.camera_4.setObjectName(u"camera_4")
        self.camera_4.setFont(font8)
        self.camera_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_4)


        self.verticalLayout_10.addWidget(self.camera_top)


        self.horizontalLayout_6.addWidget(self.rignt_child)

        self.stackedWidget.addWidget(self.camera)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.horizontalLayout_14 = QHBoxLayout(self.database)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.left_fram_reg = QFrame(self.database)
        self.left_fram_reg.setObjectName(u"left_fram_reg")
        self.left_fram_reg.setMinimumSize(QSize(600, 0))
        self.left_fram_reg.setMaximumSize(QSize(500, 16777215))
        self.left_fram_reg.setFrameShape(QFrame.NoFrame)
        self.left_fram_reg.setFrameShadow(QFrame.Raised)
        self.reg_image = QLabel(self.left_fram_reg)
        self.reg_image.setObjectName(u"reg_image")
        self.reg_image.setGeometry(QRect(40, 130, 291, 291))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(14)
        font9.setBold(True)
        self.reg_image.setFont(font9)
        self.reg_image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image.setAlignment(Qt.AlignCenter)
        self.reg_firstname = QLineEdit(self.left_fram_reg)
        self.reg_firstname.setObjectName(u"reg_firstname")
        self.reg_firstname.setGeometry(QRect(340, 130, 231, 51))
        self.reg_firstname.setFont(font5)
        self.reg_firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_firstname.setClearButtonEnabled(True)
        self.reg_image_2 = QLabel(self.left_fram_reg)
        self.reg_image_2.setObjectName(u"reg_image_2")
        self.reg_image_2.setGeometry(QRect(20, 110, 571, 511))
        self.reg_image_2.setFont(font9)
        self.reg_image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_2.setAlignment(Qt.AlignCenter)
        self.reg_middlename = QLineEdit(self.left_fram_reg)
        self.reg_middlename.setObjectName(u"reg_middlename")
        self.reg_middlename.setGeometry(QRect(340, 190, 231, 51))
        self.reg_middlename.setFont(font5)
        self.reg_middlename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_middlename.setClearButtonEnabled(True)
        self.reg_lastname = QLineEdit(self.left_fram_reg)
        self.reg_lastname.setObjectName(u"reg_lastname")
        self.reg_lastname.setGeometry(QRect(340, 250, 231, 51))
        self.reg_lastname.setFont(font5)
        self.reg_lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_lastname.setClearButtonEnabled(True)
        self.reg_index = QLineEdit(self.left_fram_reg)
        self.reg_index.setObjectName(u"reg_index")
        self.reg_index.setGeometry(QRect(340, 370, 231, 51))
        self.reg_index.setFont(font5)
        self.reg_index.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_index.setClearButtonEnabled(True)
        self.reg_college = QLineEdit(self.left_fram_reg)
        self.reg_college.setObjectName(u"reg_college")
        self.reg_college.setGeometry(QRect(340, 430, 231, 51))
        self.reg_college.setFont(font5)
        self.reg_college.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_college.setClearButtonEnabled(True)
        self.reg_student_ref = QLineEdit(self.left_fram_reg)
        self.reg_student_ref.setObjectName(u"reg_student_ref")
        self.reg_student_ref.setGeometry(QRect(340, 310, 231, 51))
        self.reg_student_ref.setFont(font5)
        self.reg_student_ref.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_student_ref.setClearButtonEnabled(True)
        self.reg_nationality = QLineEdit(self.left_fram_reg)
        self.reg_nationality.setObjectName(u"reg_nationality")
        self.reg_nationality.setGeometry(QRect(40, 430, 291, 51))
        self.reg_nationality.setFont(font5)
        self.reg_nationality.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_nationality.setClearButtonEnabled(True)
        self.reg_start_date = QLineEdit(self.left_fram_reg)
        self.reg_start_date.setObjectName(u"reg_start_date")
        self.reg_start_date.setGeometry(QRect(40, 490, 271, 51))
        self.reg_start_date.setFont(font5)
        self.reg_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_start_date.setClearButtonEnabled(True)
        self.reg_end_date = QLineEdit(self.left_fram_reg)
        self.reg_end_date.setObjectName(u"reg_end_date")
        self.reg_end_date.setGeometry(QRect(320, 490, 251, 51))
        self.reg_end_date.setFont(font5)
        self.reg_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_end_date.setClearButtonEnabled(True)
        self.label_35 = QLabel(self.left_fram_reg)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(50, 500, 31, 31))
        self.label_35.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_36 = QLabel(self.left_fram_reg)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(330, 500, 31, 31))
        self.label_36.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.reg_programs = QComboBox(self.left_fram_reg)
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.setObjectName(u"reg_programs")
        self.reg_programs.setGeometry(QRect(320, 550, 251, 50))
        self.reg_programs.setMinimumSize(QSize(0, 50))
        self.reg_programs.setMaximumSize(QSize(16777215, 50))
        self.reg_programs.setFont(font5)
        self.reg_programs.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_programs.setFrame(False)
        self.btn_search_reg = QPushButton(self.left_fram_reg)
        self.btn_search_reg.setObjectName(u"btn_search_reg")
        self.btn_search_reg.setGeometry(QRect(450, 30, 121, 51))
        self.btn_search_reg.setFont(font5)
        self.btn_search_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search_reg.setIcon(icon1)
        self.btn_search_reg.setIconSize(QSize(30, 30))
        self.btn_search_reg.setFlat(True)
        self.label_37 = QLabel(self.left_fram_reg)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(20, 10, 571, 91))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_reg = QLineEdit(self.left_fram_reg)
        self.search_reg.setObjectName(u"search_reg")
        self.search_reg.setGeometry(QRect(40, 30, 401, 51))
        self.search_reg.setFont(font5)
        self.search_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_reg.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.left_fram_reg)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(20, 680, 571, 61))
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_register = QPushButton(self.left_fram_reg)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(30, 690, 131, 41))
        self.btn_register.setFont(font5)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_register.setIcon(icon3)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.btn_update = QPushButton(self.left_fram_reg)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(170, 690, 131, 41))
        self.btn_update.setFont(font5)
        self.btn_update.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/asset/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon14)
        self.btn_update.setIconSize(QSize(30, 30))
        self.btn_update.setFlat(True)
        self.btn_remove = QPushButton(self.left_fram_reg)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(310, 690, 131, 41))
        self.btn_remove.setFont(font5)
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/asset/user-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon15)
        self.btn_remove.setIconSize(QSize(30, 30))
        self.btn_remove.setFlat(True)
        self.date_frame_3 = QFrame(self.left_fram_reg)
        self.date_frame_3.setObjectName(u"date_frame_3")
        self.date_frame_3.setGeometry(QRect(20, 630, 571, 41))
        self.date_frame_3.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame_3.setFrameShape(QFrame.StyledPanel)
        self.date_frame_3.setFrameShadow(QFrame.Raised)
        self.reg_face_auth = QRadioButton(self.date_frame_3)
        self.reg_face_auth.setObjectName(u"reg_face_auth")
        self.reg_face_auth.setGeometry(QRect(9, 9, 191, 23))
        self.reg_face_auth.setFont(font4)
        self.reg_face_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_face_auth.setIcon(icon6)
        self.reg_face_auth.setChecked(False)
        self.reg_qr_auth = QRadioButton(self.date_frame_3)
        self.reg_qr_auth.setObjectName(u"reg_qr_auth")
        self.reg_qr_auth.setGeometry(QRect(206, 9, 114, 23))
        self.reg_qr_auth.setFont(font4)
        self.reg_qr_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_qr_auth.setIcon(icon6)
        self.reg_qr_auth.setChecked(False)
        self.reg_biometric_auth = QRadioButton(self.date_frame_3)
        self.reg_biometric_auth.setObjectName(u"reg_biometric_auth")
        self.reg_biometric_auth.setGeometry(QRect(330, 9, 121, 23))
        self.reg_biometric_auth.setFont(font4)
        self.reg_biometric_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_biometric_auth.setIcon(icon6)
        self.reg_biometric_auth.setChecked(False)
        self.reg_both = QRadioButton(self.date_frame_3)
        self.reg_both.setObjectName(u"reg_both")
        self.reg_both.setGeometry(QRect(460, 10, 101, 23))
        self.reg_both.setFont(font4)
        self.reg_both.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_both.setIcon(icon6)
        self.reg_both.setChecked(True)
        self.btn_clear = QPushButton(self.left_fram_reg)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(450, 690, 131, 41))
        self.btn_clear.setFont(font5)
        self.btn_clear.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon16)
        self.btn_clear.setIconSize(QSize(30, 30))
        self.btn_clear.setFlat(True)
        self.label_39 = QLabel(self.left_fram_reg)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(20, 750, 571, 91))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.image_file_reg = QLineEdit(self.left_fram_reg)
        self.image_file_reg.setObjectName(u"image_file_reg")
        self.image_file_reg.setGeometry(QRect(40, 780, 401, 51))
        self.image_file_reg.setFont(font5)
        self.image_file_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_file_reg.setClearButtonEnabled(True)
        self.btn_browse_reg = QPushButton(self.left_fram_reg)
        self.btn_browse_reg.setObjectName(u"btn_browse_reg")
        self.btn_browse_reg.setGeometry(QRect(450, 780, 121, 51))
        self.btn_browse_reg.setFont(font5)
        self.btn_browse_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse_reg.setIcon(icon17)
        self.btn_browse_reg.setIconSize(QSize(30, 30))
        self.btn_browse_reg.setFlat(True)
        self.reg_notification_label = QLabel(self.left_fram_reg)
        self.reg_notification_label.setObjectName(u"reg_notification_label")
        self.reg_notification_label.setGeometry(QRect(20, 850, 571, 91))
        self.reg_notification_label.setFont(font3)
        self.reg_notification_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.reg_notification_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.reg_college_2 = QComboBox(self.left_fram_reg)
        self.reg_college_2.addItem("")
        self.reg_college_2.addItem("")
        self.reg_college_2.addItem("")
        self.reg_college_2.setObjectName(u"reg_college_2")
        self.reg_college_2.setGeometry(QRect(40, 550, 271, 50))
        self.reg_college_2.setMinimumSize(QSize(0, 50))
        self.reg_college_2.setMaximumSize(QSize(16777215, 50))
        self.reg_college_2.setFont(font5)
        self.reg_college_2.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_college_2.setFrame(False)
        self.label_37.raise_()
        self.search_reg.raise_()
        self.reg_image_2.raise_()
        self.reg_image.raise_()
        self.reg_firstname.raise_()
        self.reg_middlename.raise_()
        self.reg_lastname.raise_()
        self.reg_index.raise_()
        self.reg_college.raise_()
        self.reg_student_ref.raise_()
        self.reg_nationality.raise_()
        self.reg_start_date.raise_()
        self.reg_end_date.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.reg_programs.raise_()
        self.btn_search_reg.raise_()
        self.label_38.raise_()
        self.btn_register.raise_()
        self.btn_update.raise_()
        self.btn_remove.raise_()
        self.date_frame_3.raise_()
        self.btn_clear.raise_()
        self.label_39.raise_()
        self.image_file_reg.raise_()
        self.btn_browse_reg.raise_()
        self.reg_notification_label.raise_()
        self.reg_college_2.raise_()

        self.horizontalLayout_14.addWidget(self.left_fram_reg)

        self.right_frame_reg = QFrame(self.database)
        self.right_frame_reg.setObjectName(u"right_frame_reg")
        self.right_frame_reg.setFrameShape(QFrame.NoFrame)
        self.right_frame_reg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.right_frame_reg)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 9, 0)
        self.frame_13 = QFrame(self.right_frame_reg)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.reg_camera_view = QLabel(self.frame_13)
        self.reg_camera_view.setObjectName(u"reg_camera_view")
        self.reg_camera_view.setFont(font9)
        self.reg_camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_camera_view.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.reg_camera_view)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, -1, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.firstname_31 = QLabel(self.frame_18)
        self.firstname_31.setObjectName(u"firstname_31")
        self.firstname_31.setGeometry(QRect(0, 0, 391, 141))
        self.firstname_31.setFont(font6)
        self.firstname_31.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.camera_ip_reg = QLineEdit(self.frame_18)
        self.camera_ip_reg.setObjectName(u"camera_ip_reg")
        self.camera_ip_reg.setGeometry(QRect(10, 20, 371, 51))
        self.camera_ip_reg.setFont(font5)
        self.camera_ip_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_ip_reg.setClearButtonEnabled(True)
        self.label_41 = QLabel(self.frame_18)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(20, 30, 41, 31))
        self.label_41.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_reg = QPushButton(self.frame_18)
        self.btn_camera_reg.setObjectName(u"btn_camera_reg")
        self.btn_camera_reg.setGeometry(QRect(10, 80, 111, 41))
        self.btn_camera_reg.setFont(font5)
        self.btn_camera_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_reg.setIcon(icon7)
        self.btn_camera_reg.setIconSize(QSize(30, 30))
        self.btn_camera_reg.setFlat(True)
        self.btn_cam_dis_reg = QPushButton(self.frame_18)
        self.btn_cam_dis_reg.setObjectName(u"btn_cam_dis_reg")
        self.btn_cam_dis_reg.setGeometry(QRect(130, 80, 131, 41))
        self.btn_cam_dis_reg.setFont(font5)
        self.btn_cam_dis_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_cam_dis_reg.setIcon(icon8)
        self.btn_cam_dis_reg.setIconSize(QSize(30, 30))
        self.btn_cam_dis_reg.setFlat(True)
        self.comboBox_reg = QComboBox(self.frame_18)
        self.comboBox_reg.addItem("")
        self.comboBox_reg.setObjectName(u"comboBox_reg")
        self.comboBox_reg.setGeometry(QRect(270, 80, 111, 38))
        self.comboBox_reg.setMinimumSize(QSize(0, 38))
        self.comboBox_reg.setMaximumSize(QSize(16777215, 38))
        self.comboBox_reg.setFont(font5)
        self.comboBox_reg.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox_reg.setFrame(False)

        self.verticalLayout_19.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 300))
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 60, 391, 241))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.calendarWidget_reg = QCalendarWidget(self.frame_20)
        self.calendarWidget_reg.setObjectName(u"calendarWidget_reg")
        self.calendarWidget_reg.setNavigationBarVisible(True)

        self.verticalLayout_20.addWidget(self.calendarWidget_reg)

        self.end_date_reg = QRadioButton(self.frame_19)
        self.end_date_reg.setObjectName(u"end_date_reg")
        self.end_date_reg.setGeometry(QRect(130, 10, 95, 20))
        self.end_date_reg.setFont(font4)
        self.end_date_reg.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.start_date_reg = QRadioButton(self.frame_19)
        self.start_date_reg.setObjectName(u"start_date_reg")
        self.start_date_reg.setGeometry(QRect(10, 10, 95, 20))
        self.start_date_reg.setFont(font4)
        self.start_date_reg.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.label_42 = QLabel(self.frame_19)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 0, 391, 41))
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_42.raise_()
        self.frame_20.raise_()
        self.end_date_reg.raise_()
        self.start_date_reg.raise_()

        self.verticalLayout_19.addWidget(self.frame_19)


        self.horizontalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_17)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.reg_show_biometric_data = QLabel(self.frame_21)
        self.reg_show_biometric_data.setObjectName(u"reg_show_biometric_data")
        self.reg_show_biometric_data.setGeometry(QRect(10, 10, 201, 211))
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(10)
        font10.setBold(True)
        self.reg_show_biometric_data.setFont(font10)
        self.reg_show_biometric_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_show_biometric_data.setAlignment(Qt.AlignCenter)
        self.reg_image_5 = QLabel(self.frame_21)
        self.reg_image_5.setObjectName(u"reg_image_5")
        self.reg_image_5.setGeometry(QRect(220, 10, 171, 211))
        self.reg_image_5.setFont(font10)
        self.reg_image_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_22)


        self.horizontalLayout_15.addWidget(self.frame_17)

        self.frame_17.raise_()
        self.frame_16.raise_()

        self.verticalLayout_18.addWidget(self.frame_15)


        self.verticalLayout_17.addWidget(self.frame_13)


        self.horizontalLayout_14.addWidget(self.right_frame_reg)

        self.stackedWidget.addWidget(self.database)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.gridLayout_3 = QGridLayout(self.report)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(6, 0, 6, 0)
        self.frame_10 = QFrame(self.report)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 9)
        self.label_17 = QLabel(self.frame_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 35))
        self.label_17.setMaximumSize(QSize(16777215, 35))
        self.label_17.setFont(font10)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_17)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 2px solid rgb(255,255,255);\n"
"}")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_11)


        self.gridLayout_3.addWidget(self.frame_10, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.report)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 35))
        self.label_16.setMaximumSize(QSize(16777215, 35))
        self.label_16.setFont(font10)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_16)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 2px solid rgb(255,255,255);\n"
"}")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_9)


        self.gridLayout_3.addWidget(self.frame_8, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.report)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 35))
        self.label_2.setMaximumSize(QSize(16777215, 35))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_2)

        self.pie_data = QFrame(self.frame_7)
        self.pie_data.setObjectName(u"pie_data")
        self.pie_data.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"	border: 2px solid rgb(255,255,255);\n"
"}")
        self.pie_data.setFrameShape(QFrame.StyledPanel)
        self.pie_data.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.pie_data)


        self.gridLayout_3.addWidget(self.frame_7, 0, 0, 1, 1)

        self.user_frame = QFrame(self.report)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setStyleSheet(u"")
        self.user_frame.setFrameShape(QFrame.NoFrame)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.user_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(0, 220, 411, 241))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.calendarWidget_report = QCalendarWidget(self.frame_12)
        self.calendarWidget_report.setObjectName(u"calendarWidget_report")
        self.calendarWidget_report.setNavigationBarVisible(True)

        self.verticalLayout_16.addWidget(self.calendarWidget_report)

        self.file_name = QLineEdit(self.user_frame)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(480, 30, 211, 51))
        self.file_name.setFont(font5)
        self.file_name.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.file_name.setClearButtonEnabled(True)
        self.label_20 = QLabel(self.user_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(490, 40, 31, 31))
        self.label_20.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.report_end_date = QLineEdit(self.user_frame)
        self.report_end_date.setObjectName(u"report_end_date")
        self.report_end_date.setGeometry(QRect(240, 30, 211, 51))
        self.report_end_date.setFont(font5)
        self.report_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.report_end_date.setClearButtonEnabled(True)
        self.label_21 = QLabel(self.user_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(250, 40, 31, 31))
        self.label_21.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_22 = QLabel(self.user_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 40, 31, 31))
        self.label_22.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.report_start_date = QLineEdit(self.user_frame)
        self.report_start_date.setObjectName(u"report_start_date")
        self.report_start_date.setGeometry(QRect(10, 30, 201, 51))
        self.report_start_date.setFont(font5)
        self.report_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.report_start_date.setClearButtonEnabled(True)
        self.label_23 = QLabel(self.user_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(20, 40, 31, 31))
        self.label_23.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.date_frame = QFrame(self.user_frame)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setGeometry(QRect(10, 90, 211, 43))
        self.date_frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.date_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.start_date_3 = QRadioButton(self.date_frame)
        self.start_date_3.setObjectName(u"start_date_3")
        self.start_date_3.setFont(font4)
        self.start_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.start_date_3.setChecked(True)

        self.horizontalLayout_11.addWidget(self.start_date_3)

        self.end_date_3 = QRadioButton(self.date_frame)
        self.end_date_3.setObjectName(u"end_date_3")
        self.end_date_3.setFont(font4)
        self.end_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.end_date_3)

        self.frame_14 = QFrame(self.user_frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(230, 90, 461, 43))
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.start_date_4 = QRadioButton(self.frame_14)
        self.start_date_4.setObjectName(u"start_date_4")
        self.start_date_4.setFont(font4)
        self.start_date_4.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.start_date_4.setChecked(True)

        self.horizontalLayout_12.addWidget(self.start_date_4)

        self.start_date_5 = QRadioButton(self.frame_14)
        self.start_date_5.setObjectName(u"start_date_5")
        self.start_date_5.setFont(font4)
        self.start_date_5.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.start_date_5)

        self.start_date_6 = QRadioButton(self.frame_14)
        self.start_date_6.setObjectName(u"start_date_6")
        self.start_date_6.setFont(font4)
        self.start_date_6.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.start_date_6)

        self.start_date_7 = QRadioButton(self.frame_14)
        self.start_date_7.setObjectName(u"start_date_7")
        self.start_date_7.setFont(font4)
        self.start_date_7.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.start_date_7)

        self.btn_save = QPushButton(self.user_frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(150, 150, 121, 41))
        self.btn_save.setFont(font5)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon18)
        self.btn_save.setIconSize(QSize(30, 30))
        self.btn_save.setFlat(True)
        self.btn_load = QPushButton(self.user_frame)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(10, 150, 121, 41))
        self.btn_load.setFont(font5)
        self.btn_load.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_load.setIcon(icon19)
        self.btn_load.setIconSize(QSize(30, 30))
        self.btn_load.setFlat(True)
        self.label_19 = QLabel(self.user_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(420, 220, 281, 241))
        self.label_19.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.btn_refresh = QPushButton(self.user_frame)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(290, 150, 121, 41))
        self.btn_refresh.setFont(font5)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_refresh.setIcon(icon11)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.btn_clear_area = QPushButton(self.user_frame)
        self.btn_clear_area.setObjectName(u"btn_clear_area")
        self.btn_clear_area.setGeometry(QRect(430, 150, 121, 41))
        self.btn_clear_area.setFont(font5)
        self.btn_clear_area.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_clear_area.setIcon(icon11)
        self.btn_clear_area.setIconSize(QSize(30, 30))
        self.btn_clear_area.setFlat(True)
        self.btn_reload_11 = QPushButton(self.user_frame)
        self.btn_reload_11.setObjectName(u"btn_reload_11")
        self.btn_reload_11.setGeometry(QRect(570, 150, 121, 41))
        self.btn_reload_11.setFont(font5)
        self.btn_reload_11.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_reload_11.setIcon(icon11)
        self.btn_reload_11.setIconSize(QSize(30, 30))
        self.btn_reload_11.setFlat(True)
        self.firstname_30 = QLabel(self.user_frame)
        self.firstname_30.setObjectName(u"firstname_30")
        self.firstname_30.setGeometry(QRect(0, 20, 701, 191))
        self.firstname_30.setFont(font6)
        self.firstname_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_30.raise_()
        self.frame_12.raise_()
        self.file_name.raise_()
        self.label_20.raise_()
        self.report_end_date.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.report_start_date.raise_()
        self.label_23.raise_()
        self.date_frame.raise_()
        self.frame_14.raise_()
        self.btn_save.raise_()
        self.btn_load.raise_()
        self.label_19.raise_()
        self.btn_refresh.raise_()
        self.btn_clear_area.raise_()
        self.btn_reload_11.raise_()

        self.gridLayout_3.addWidget(self.user_frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.report)
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_7 = QLabel(self.settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 300, 251, 141))
        font11 = QFont()
        font11.setPointSize(20)
        self.label_7.setFont(font11)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)


        self.verticalLayout.addWidget(self.drop_shadow_layout)

        dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText("")
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_search.setText("")
        self.btn_camera.setText("")
        self.btn_database.setText("")
        self.btn_report.setText("")
        self.btn_help.setText("")
        self.image.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Student No", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.coledge.setText(QCoreApplication.translate("dashboard", u"Coledge", None))
        self.validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.last_in.setText(QCoreApplication.translate("dashboard", u"Last In", None))
        self.year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.program.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.last_out.setText(QCoreApplication.translate("dashboard", u"Last Out", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.face_auth.setText(QCoreApplication.translate("dashboard", u"Face Authentication", None))
        self.qr_code_auth.setText(QCoreApplication.translate("dashboard", u"QR Code", None))
        self.biometric_auth.setText(QCoreApplication.translate("dashboard", u"Biometric ", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.label_27.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Entry camera", None))
        self.firstname_24.setText(QCoreApplication.translate("dashboard", u"Exit camera", None))
        self.btn_exit_cam_disconect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.btn_exit_cam_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.exit_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.label_28.setText("")
        self.btn_exit_cam_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.camera_view.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.entry_dilation_label.setText(QCoreApplication.translate("dashboard", u"Dilation", None))
#if QT_CONFIG(tooltip)
        self.dilation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.entry_erosion_label.setText(QCoreApplication.translate("dashboard", u"Erosion", None))
        self.entry_blur_label.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.entry_unimp_label.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Entry camera image processing enhancement", None))
        self.exit_dilation_label.setText(QCoreApplication.translate("dashboard", u"Dilation", None))
#if QT_CONFIG(tooltip)
        self.exit_cam_dilation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.exit_erosion_label.setText(QCoreApplication.translate("dashboard", u"Erosion", None))
        self.exit_blur_label.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.exit_umimpl.setText(QCoreApplication.translate("dashboard", u"Blur", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Exit camera image processing enhancement", None))
        self.db_validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.db_refrence.setText(QCoreApplication.translate("dashboard", u"Student No", None))
        self.db_year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.db_nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.db_image_data.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.db_lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.db_programe.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.db_college.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_print.setText(QCoreApplication.translate("dashboard", u"Print", None))
        self.btn_dump_csv.setText(QCoreApplication.translate("dashboard", u"PDF", None))
        self.btn_reload.setText("")
        self.start_date.setText(QCoreApplication.translate("dashboard", u"Start Date", None))
        self.end_date.setText(QCoreApplication.translate("dashboard", u"End Date", None))
        self.label_24.setText("")
        self.db_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.db_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_25.setText("")
        self.label_29.setText("")
        self.label_30.setText("")
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Student No", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Last In", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Last Out ", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Time In", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Time Out", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dashboard", u"Duration", None));
        self.btn_cast.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.btn_capture.setText(QCoreApplication.translate("dashboard", u"Capture", None))
        self.btn_cast_all.setText(QCoreApplication.translate("dashboard", u"Cast all", None))
        self.image_file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"Image file name?", None))
        self.label_4.setText("")
        self.video_file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"Video file name?", None))
        self.label_15.setText("")
        self.btn_capture_video.setText(QCoreApplication.translate("dashboard", u"Capture", None))
        self.firstname_25.setText(QCoreApplication.translate("dashboard", u"Camera one", None))
        self.btn_camera_one_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_camera_one_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_one_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.camera_one_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.label_31.setText("")
        self.btn_camera_two_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_two_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.camera_two_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_two_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_26.setText(QCoreApplication.translate("dashboard", u"Camera two", None))
        self.label_32.setText("")
        self.btn_camera_three_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_three_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.camera_three_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_three_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_27.setText(QCoreApplication.translate("dashboard", u"Camera three", None))
        self.label_33.setText("")
        self.btn_camera_four_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_four_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.camera_four_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_four_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_28.setText(QCoreApplication.translate("dashboard", u"Camera four", None))
        self.label_34.setText("")
        self.firstname_29.setText("")
        self.notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.camera_four_comboBox_2.setItemText(0, QCoreApplication.translate("dashboard", u"1", None))
        self.camera_four_comboBox_2.setItemText(1, QCoreApplication.translate("dashboard", u"2", None))
        self.camera_four_comboBox_2.setItemText(2, QCoreApplication.translate("dashboard", u"3", None))
        self.camera_four_comboBox_2.setItemText(3, QCoreApplication.translate("dashboard", u"4", None))

        self.btn_capture_video_2.setText(QCoreApplication.translate("dashboard", u"Close all", None))
        self.camera_1.setText(QCoreApplication.translate("dashboard", u"Camera_1", None))
        self.camera_2.setText(QCoreApplication.translate("dashboard", u"Camera_2", None))
        self.camera_3.setText(QCoreApplication.translate("dashboard", u"Camera_3", None))
        self.camera_4.setText(QCoreApplication.translate("dashboard", u"Camera_4", None))
        self.reg_image.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.reg_firstname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.reg_image_2.setText("")
        self.reg_middlename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.reg_lastname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reg_index.setPlaceholderText(QCoreApplication.translate("dashboard", u"Index", None))
        self.reg_college.setPlaceholderText(QCoreApplication.translate("dashboard", u"College", None))
        self.reg_student_ref.setPlaceholderText(QCoreApplication.translate("dashboard", u"Student No.", None))
        self.reg_nationality.setPlaceholderText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.reg_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date", None))
        self.reg_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date", None))
        self.label_35.setText("")
        self.label_36.setText("")
        self.reg_programs.setItemText(0, QCoreApplication.translate("dashboard", u"BSc. Computer Science", None))
        self.reg_programs.setItemText(1, QCoreApplication.translate("dashboard", u"BSc. Mathematics", None))
        self.reg_programs.setItemText(2, QCoreApplication.translate("dashboard", u"BSc. Chemistry", None))
        self.reg_programs.setItemText(3, QCoreApplication.translate("dashboard", u"BSc. Biology Science", None))

        self.btn_search_reg.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_37.setText("")
        self.search_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.label_38.setText("")
        self.btn_register.setText(QCoreApplication.translate("dashboard", u"Register", None))
        self.btn_update.setText(QCoreApplication.translate("dashboard", u"Update", None))
        self.btn_remove.setText(QCoreApplication.translate("dashboard", u"Remove", None))
        self.reg_face_auth.setText(QCoreApplication.translate("dashboard", u"Face Authentication", None))
        self.reg_qr_auth.setText(QCoreApplication.translate("dashboard", u"QR Code", None))
        self.reg_biometric_auth.setText(QCoreApplication.translate("dashboard", u"Biometric ", None))
        self.reg_both.setText(QCoreApplication.translate("dashboard", u"Both", None))
        self.btn_clear.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.label_39.setText(QCoreApplication.translate("dashboard", u"Image file", None))
        self.image_file_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.btn_browse_reg.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.reg_notification_label.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.reg_college_2.setItemText(0, QCoreApplication.translate("dashboard", u"CoS", None))
        self.reg_college_2.setItemText(1, QCoreApplication.translate("dashboard", u"CoE", None))
        self.reg_college_2.setItemText(2, QCoreApplication.translate("dashboard", u"HESSA", None))

        self.reg_camera_view.setText(QCoreApplication.translate("dashboard", u"Camera", None))
        self.firstname_31.setText("")
        self.camera_ip_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.label_41.setText("")
        self.btn_camera_reg.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_cam_dis_reg.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.comboBox_reg.setItemText(0, QCoreApplication.translate("dashboard", u"New Item", None))

        self.end_date_reg.setText(QCoreApplication.translate("dashboard", u"End Date", None))
        self.start_date_reg.setText(QCoreApplication.translate("dashboard", u"Start Date", None))
        self.label_42.setText("")
        self.reg_show_biometric_data.setText(QCoreApplication.translate("dashboard", u"QR/Biometric", None))
        self.reg_image_5.setText(QCoreApplication.translate("dashboard", u"QR/Biometric", None))
        self.label_17.setText(QCoreApplication.translate("dashboard", u"Line graph", None))
        self.label_16.setText(QCoreApplication.translate("dashboard", u"Bar chart", None))
        self.label_2.setText(QCoreApplication.translate("dashboard", u"Pie Chart", None))
        self.file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.label_20.setText("")
        self.report_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_21.setText("")
        self.label_22.setText("")
        self.report_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.label_23.setText("")
        self.start_date_3.setText(QCoreApplication.translate("dashboard", u"Start Date", None))
        self.end_date_3.setText(QCoreApplication.translate("dashboard", u"End Date", None))
        self.start_date_4.setText(QCoreApplication.translate("dashboard", u"Pie chart", None))
        self.start_date_5.setText(QCoreApplication.translate("dashboard", u"Bar chart", None))
        self.start_date_6.setText(QCoreApplication.translate("dashboard", u"Line graph", None))
        self.start_date_7.setText(QCoreApplication.translate("dashboard", u"All types", None))
        self.btn_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.btn_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.label_19.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Reload", None))
        self.btn_clear_area.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.btn_reload_11.setText(QCoreApplication.translate("dashboard", u"Reload", None))
        self.firstname_30.setText("")
        self.label_7.setText(QCoreApplication.translate("dashboard", u"Settings", None))
    # retranslateUi

