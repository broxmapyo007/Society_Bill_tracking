################################################################################
## Created by: Adesh Dangi
## bsc cs sem 5
################################################################################
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as sct
import os, sys, webbrowser
from datetime import date

dir_path = os.path.dirname(os.path.realpath(__file__))
print("File path : ", dir_path)
os.chdir(dir_path)

import_test = False
print("import check for progress : ")
import sqlite3

try:
    import PyQt5, os, sys, sqlite3, Pmw

    try:
        from tkinter.ttk import *
        from PyQt5.QtCore import QDate
        from PyQt5 import QtCore, QtGui, QtWidgets
        from PyQt5.QtCore import *

        # (QCoreApplication,QPropertyAnimation, QDate, QDateTime,QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl,Qt, QEvent)
        from PyQt5.QtGui import *

        # (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QRadialGradient)
        from PyQt5.QtWidgets import *
        from PyQt5.QtCore import *
        from PyQt5.QtGui import *

        import_test = True
    except:
        print("update modules")
    print("import test result : ", import_test)
except ModuleNotFoundError as err:
    import_test = False
    print("import error", err)

if not import_test:
    print("import_test_op result : ", import_test)
    window_err = Tk()
    window_err.title("import Error ")
    window_err.geometry("300x300+300+100")
    window_err.config(bg="white")
    window_err.resizable(0, 0)
    test_db = False

    def check_db():
        """Main database file check"""
        file_db = os.getcwd()
        print(file_db)
        return test_db

    check_db()
    try:
        groupBox1 = Pmw.Group(window_err, tag_text="check for modules to be install")
        groupBox1.place(x=0, y=0, height=300, width=300)
        module_list = """Module not installed\nTo Start using program\n\nModule list to be installed :\n1. PyQt5\n2. PySide2\n \n\nsteps to install from cmd:\n1. pip install PyQt5\n2. pip install PySide2
        """
    except:
        module_list = """Check for modules to be install\n\nModule not installed\nTo Start using program\n\nModule list to be installed :\n1. PyQt5\n2. PySide2\n3. os\n4. sys\n\nsteps to install from cmd:\n1. pip install PyQt5\n2. pip install PySide2
        """
    print("require modules :", module_list)
    txt = tkinter.Text(window_err, height=17, width=35)
    txt.insert("end", module_list)
    txt.configure(state="disable")
    txt.place(x=10, y=20)
    window_err.mainloop()
else:
    print("closed module import_test window")
############################################################
def demo_data_db(db):
    con = sqlite3.connect(db)
    cur = con.cursor()
    # try:
    def push(query, value):
        for sql in value:
            print("\n\nquery : ", query, " with value : ", sql)
            cur.execute(query, sql)

    v1 = [
        (
            "soa_admin",
            "admin",
            "admin",
            "admin0",
            "9637944866",
            "admin@admin.com",
            "adminbhk",
            "0",
            "BLLadmin",
            "BLL0",
            "0",
            "admin-wing",
        ),
        (
            "soa_a101",
            "Risi",
            "singh",
            "101",
            "9637944866",
            "a@b.com	",
            "1bhk",
            "1",
            "400",
            "BLL101a",
            "970",
            "A-wing",
        ),
        (
            "res_b102",
            "munna",
            "pandey",
            "102",
            "9632587410",
            "b@c.com",
            "2bhk",
            "0",
            "550",
            "BLL102b",
            "1070",
            "B-wing",
        ),
        (
            "res_b103",
            "pranit",
            "kula",
            "103",
            "1234567890",
            "d@a.com",
            "1bhk",
            "3",
            "400",
            "BLL103b",
            "970",
            "B-wing",
        ),
        (
            "res_a104",
            "raj",
            "dilla",
            "104",
            "2135468790",
            "e@w.com	",
            "1bhk",
            "2",
            "400",
            "BLL104a",
            "970",
            "A-wing",
        ),
    ]
    sql1 = "insert into Society_info_mem values(?,?,?,?,?,?,?,?,?,?,?,?)"
    push(sql1, v1)

    v2 = [
        (
            "Sinok galaxy",
            "120",
            "vasai,thane",
            "BLL_with_roomno",
            "5-day",
            "not yet",
            "a,b,c",
            "4",
        )
    ]
    sql2 = "insert into Society_Basic_info values(?,?,?,?,?,?,?,?)"
    push(sql2, v2)

    v3 = [
        (
            "soa_admin",
            "Adesh",
            "admin",
            "admin",
            "0",
            "admin@admin.com",
            "9637944866",
            "admin_is@adesh",
        ),
        (
            "soa_a101",
            "risi singh",
            "a1",
            "a1",
            "2",
            "a@b.com",
            "9637944866",
            "Risi@singh_is_king",
        ),
    ]
    sql3 = "insert into Login_admin_tb values(?,?,?,?,?,?,?,?)"
    push(sql3, v3)

    v4 = [
        ("250", "250", "100", "50", "120", "50", "50", "50", "970", "2020-06-01", "100")
    ]
    sql4 = "insert into Default_charges values(?,?,?,?,?,?,?,?,?,?,?)"
    push(sql4, v4)

    v5 = [
        (
            "BLL101a",
            "A/101",
            "June_2020",
            "Bill_101_June_2020",
            "2020-06-20",
            "unpaid",
            "96637944866",
            "2020-06-10",
            "0",
            "970",
            "cash",
        ),
        (
            "BLL102b",
            "B/102",
            "June_2020",
            "Bill_102_June_2020",
            "2020-06-20",
            "paid",
            "7972797319",
            "2020-06-10",
            "100",
            "1070",
            "cash",
        ),
        (
            "BLL103b",
            "B/103",
            "June_2020",
            "Bill_103_June_2020",
            "2020-06-20",
            "unpaid",
            "9637944866",
            "2020-06-10",
            "100",
            "1070",
            "cash",
        ),
        (
            "BLL104a",
            "A/104",
            "June_2020",
            "Bill_104_June_2020",
            "2020-06-20",
            "paid",
            "9637944866",
            "2020-06-10",
            "0",
            "970",
            "cheque",
        ),
    ]
    sql5 = "insert into All_Bill_info values(?,?,?,?,?,?,?,?,?,?,?)"
    push(sql5, v5)

    # except:
    print("\nDemo Data Loading Problem...\n\n")
    con.commit()
    con.close()


############################################################
class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(598, 389)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Splash_frame = QFrame(self.centralwidget)
        self.Splash_frame.setObjectName("Splash_frame")
        font = QFont()
        font.setFamily("Segoe UI")
        self.Splash_frame.setFont(font)
        self.Splash_frame.setStyleSheet(
            "QFrame{\n"
            "      background-color: rgb(56, 58, 89);	\n"
            "      color: rgb(220, 220, 220);\n"
            "	  border-radius: 10px;\n"
            "      height: 300px;\n"
            "      width: 300px;\n"
            "}"
        )
        self.Splash_frame.setFrameShape(QFrame.StyledPanel)
        self.Splash_frame.setFrameShadow(QFrame.Raised)
        self.Splash_title = QLabel(self.Splash_frame)
        self.Splash_title.setObjectName("Splash_title")
        self.Splash_title.setGeometry(0, 20, 581, 71)
        self.Splash_progressbar = QProgressBar(self.Splash_frame)
        self.Splash_progressbar.setObjectName("Splash_progressbar")
        self.Splash_progressbar.setGeometry(9, 261, 561, 21)
        self.Splash_progressbar.setStyleSheet(
            "QProgressBar {\n"
            "	\n"
            " background-color:darkblue;\n"
            "	color: rgba(255, 234, 65, 255);\n"
            "	border-style: none;\n"
            "	border-radius: 10px;\n"
            "	text-align: center;\n"
            "}\n"
            "QProgressBar::chunk{\n"
            "	border-radius: 10px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.699, y1:0.79, x2:1, y2:1, stop:0.113636 rgba(146, 21, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "\n"
            "}"
        )
        self.Splash_progressbar.setValue(24)
        self.Splash_loadtxt = QLabel(self.Splash_frame)
        self.Splash_loadtxt.setObjectName("Splash_loadtxt")
        self.Splash_loadtxt.setGeometry(0, 220, 211, 23)
        self.Splash_loadtxt.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.Splash_loadtxt.setStyleSheet("Splash_loadtxt{font-style:bold;}")
        self.Splash_discription = QLabel(self.Splash_frame)
        self.Splash_discription.setObjectName("Splash_discription")
        self.Splash_discription.setGeometry(30, 110, 551, 101)
        self.Splash_credit = QLabel(self.Splash_frame)
        self.Splash_credit.setObjectName("Splash_credit")
        self.Splash_credit.setGeometry(420, 310, 140, 36)
        self.brox_logo_label = QLabel(self.Splash_frame)
        self.brox_logo_label.setObjectName("brox_logo_label")
        self.brox_logo_label.setGeometry(QRect(10, 20, 71, 61))
        self.brox_logo_label.setStyleSheet(
            "QLabel{\n"
            "	border-image: url(image/icons/adeshlogo.PNG);\n"
            "	border:10px solid blue;\n"
            "	border-radius:30px  20px;\n"
            "}"
        )

        self.verticalLayout.addWidget(self.Splash_frame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

    # setupUi
    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(
            QCoreApplication.translate("SplashScreen", "SplashScreen", None)
        )
        self.Splash_title.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p align="center"><span style=" font-size:20pt; font-weight:600; color:#d23cfc;">SOCIETY MAINTENANCE</span></p><p align="center"><span style=" font-size:20pt; font-weight:600; color:#d23cfc;">BILL MANGEMENT</span></p></body></html>',
                None,
            )
        )
        self.Splash_loadtxt.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px;"><span style=" font-size:14pt; font-weight:600; font-style:italic; color:#ffffff;">Loading . . .</span></p></body></html>',
                None,
            )
        )
        self.Splash_discription.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; font-style:italic; color:#6272a4;">       # Manage All Society Members :</span></p>\n'
                '<p style=" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; font-style:italic; color:#6272a4;">1.) Release BiLL And  Share on WhatsApp</span></p>\n'
                '<p style=" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; font-style:italic; color:#6272a4;">2.)'
                " Keep Track Of  Unpaid And Late Payments</span></p>\n"
                '<p style=" margin-top:10px; margin-bottom:10px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:600; font-style:italic; color:#6272a4;">3.) Maintenance BiLL And ALL Members Details .</span></p></body></html>',
                None,
            )
        )
        self.Splash_credit.setText(
            QCoreApplication.translate(
                "SplashScreen",
                '<html><head/><body><p><span style=" font-weight:600; color:#ffffff;">Created by :</span><span style=" font-size:7pt; font-weight:600; text-decoration: underline; color:#e2f512;"> Adesh Dangi</span></p><p><span style=" font-size:7pt; font-weight:600; text-decoration: underline; color:#af39de;">(c) B.Sc C.S - 04</span></p></body></html>',
                None,
            )
        )
        # retranslateUi


#############################################################
# main WINDOW ui
class Ui_Society_MainWindow(object):  # cmplt
    def setupUi(self, Society_MainWindow):
        if not Society_MainWindow.objectName():
            Society_MainWindow.setObjectName("Society_MainWindow")
        Society_MainWindow.setWindowModality(Qt.ApplicationModal)
        Society_MainWindow.resize(800, 550)
        Society_MainWindow.setMinimumSize(QtCore.QSize(800, 550))
        Society_MainWindow.setMouseTracking(True)
        Society_MainWindow.setTabletTracking(True)
        icon = QIcon()
        icon.addFile(
            "image/images/building904.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        Society_MainWindow.setWindowIcon(icon)
        Society_MainWindow.setWindowOpacity(1)
        Society_MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(Society_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Society_BILLMaintenance = QStackedWidget(self.centralwidget)
        self.Society_BILLMaintenance.setObjectName("Society_BILLMaintenance")
        self.Login_Page = QWidget()
        self.Login_Page.setObjectName("Login_Page")
        self.Login_Page_css = (
            "QWidget#Login_Page{\n" "background-color: rgb(48, 48, 48);\n" "\n" "}"
        )
        self.Login_Page.setStyleSheet(self.Login_Page_css)
        self.horizontalLayout = QHBoxLayout(self.Login_Page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Login_Page_left = QFrame(self.Login_Page)
        self.Login_Page_left.setObjectName("Login_Page_left")
        self.Login_Page_left.setMaximumSize(QtCore.QSize(85, 16777215))
        self.Login_Page_left.setStyleSheet(
            "QFrame#Login_Page_left{\n"
            "  \n"
            "	background-color: rgb(33, 33, 33);\n"
            "\n"
            "}"
        )
        self.Login_Page_left.setFrameShape(QFrame.NoFrame)
        self.Login_Page_left.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.Login_Page_left)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.Login_User_box = QFrame(self.Login_Page_left)
        self.Login_User_box.setObjectName("Login_User_box")
        self.Login_User_box.setMaximumSize(QtCore.QSize(100, 133))
        self.Login_User_box.setFrameShape(QFrame.StyledPanel)
        self.Login_User_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Login_User_box)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 2, 1, 1)
        self.user_img1 = QLabel(self.Login_User_box)
        self.user_img1.setObjectName("user_img1")
        self.user_img1.setAutoFillBackground(False)
        self.user_img1.setStyleSheet(
            "QLabel#user_img1{	\n"
            "	image: url(image/icons/avatar.png);\n"
            "    background-color:rgb(202, 202, 202);\n"
            "    border :2px solid rgb(49, 181, 34);\n"
            "	background-position: center;\n"
            "}\n"
            "#user_img1:hover {\n"
            "border: 1px solid rgb(255, 225, 0);\n"
            "\n"
            "}\n"
            ""
        )
        self.verticalLayout_4.addWidget(self.user_img1)
        self.user_txt1 = QLabel(self.Login_User_box)
        self.user_txt1.setObjectName("user_txt1")
        self.verticalLayout_4.addWidget(self.user_txt1)
        self.verticalLayout_2.addWidget(self.Login_User_box)

        self.Login_control_box = QFrame(self.Login_Page_left)
        self.Login_control_box.setObjectName("Login_control_box")
        self.Login_control_box.setLayoutDirection(Qt.LeftToRight)
        self.Login_control_box.setFrameShape(QFrame.StyledPanel)
        self.Login_control_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Login_control_box)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.Login_btn = QPushButton(self.Login_control_box)
        self.Login_btn.setObjectName("Login_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login_btn.sizePolicy().hasHeightForWidth())
        self.Login_btn.setSizePolicy(sizePolicy)
        self.Login_btn.setMinimumSize(QSize(0, 40))
        self.Login_btn.setMaximumSize(QSize(16777215, 50))
        self.Login_btn.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255); \n"
            "	background-color: rgb(35, 35, 35);\n"
            "    font-size:10pt; font-weight:600;\n"
            "    color:rgb(255, 220, 24);\n"
            '    align="center";\n'
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "     color:rgb(15, 15, 15);\n"
            "}"
        )
        self.verticalLayout_5.addWidget(self.Login_btn)
        self.Forgot_pswdbtn = QPushButton(self.Login_control_box)
        self.Forgot_pswdbtn.setObjectName("Forgot_pswdbtn")
        self.Forgot_pswdbtn.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 255, 255); \n"
            "	background-color: rgb(35, 35, 35);\n"
            "    font-size:10pt; font-weight:600;\n"
            "    color:rgb(255, 220, 24);\n"
            '    align="center";\n'
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(85, 170, 255);\n"
            "     color:rgb(15, 15, 15);\n"
            "}"
        )
        self.verticalLayout_5.addWidget(self.Forgot_pswdbtn)
        self.Exit_btn = QPushButton(self.Login_control_box)
        self.Exit_btn.setObjectName("Exit_btn")
        sizePolicy.setHeightForWidth(self.Exit_btn.sizePolicy().hasHeightForWidth())
        self.Exit_btn.setSizePolicy(sizePolicy)
        self.Exit_btn.setMaximumSize(QSize(16777215, 40))
        self.Exit_btn.setStyleSheet(
            "QPushButton {\n"
            "	color: rgb(255, 0, 0);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    font-size:10pt; font-weight:600;\n"
            '    align="center";\n'
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(255, 229, 178);\n"
            "     color:rgb(15, 15, 15);\n"
            "}\n"
            ""
        )
        self.verticalLayout_5.addWidget(self.Exit_btn)
        self.Ctrl_frame = QWidget(self.Login_control_box)
        self.Ctrl_frame.setObjectName("Ctrl_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(13)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Ctrl_frame.sizePolicy().hasHeightForWidth())
        self.Ctrl_frame.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.Ctrl_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.addWidget(self.Ctrl_frame)
        self.verticalLayout_2.addWidget(self.Login_control_box)
        self.horizontalLayout.addWidget(self.Login_Page_left)
        self.Login_Page_right = QFrame(self.Login_Page)
        self.Login_Page_right.setObjectName("Login_Page_right")
        self.Login_Page_right.setStyleSheet(
            "QFrame#Login_Page_right{ \n" "background-color: rgb(90, 90, 90);\n" "}"
        )
        self.Login_Page_right.setFrameShape(QFrame.NoFrame)
        self.Login_Page_right.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.Login_Page_right)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Error_box = QFrame(self.Login_Page_right)
        self.Error_box.setObjectName("Error_box")
        self.Error_box.setMinimumSize(QtCore.QSize(0, 40))
        self.Error_box.setMaximumSize(QtCore.QSize(16777214, 40))
        self.Error_box.setFrameShape(QFrame.NoFrame)
        self.Error_box.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.Error_box)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 6, 9, 0)
        self.Error_Label = QLabel(self.Error_box)
        self.Error_Label.setObjectName("Error_Label")
        self.Error_Label.setStyleSheet(
            "QLabel{\n"
            "    color: rgb(35, 35, 35);\n"
            "	background-color: rgb(239, 62, 27);\n"
            "    border-radius : 10px 10px;\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.Error_Label)
        self.Error_Close_btn = QPushButton(self.Error_box)
        self.Error_Close_btn.setObjectName("Error_Close_btn")
        self.Error_Close_btn.setMaximumSize(QtCore.QSize(20, 30))
        self.Error_Close_btn.setStyleSheet(
            "QPushButton {\n"
            "	border-radius: 8px;	\n"
            "	/*background-image: url(image/icons/cil-x.png);*/\n"
            "	font-weight: bold;\n"
            "	background-position: center;	\n"
            "	background-color: rgb(60, 60, 60);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(39, 39, 39);\n"
            "	color:  rgb(255, 0, 4);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "	background-color:rgb(255, 0, 4);\n"
            "	color:rgb(0, 0, 0);\n"
            "}"
        )
        self.horizontalLayout_2.addWidget(self.Error_Close_btn)
        self.verticalLayout_3.addWidget(self.Error_box)
        self.Login_stackedWidget = QStackedWidget(self.Login_Page_right)
        self.Login_stackedWidget.setObjectName("Login_stackedWidget")
        self.Forgot_pg = QWidget()
        self.Forgot_pg.setObjectName("Forgot_pg")
        self.verticalLayout_9 = QVBoxLayout(self.Forgot_pg)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_2 = QGroupBox(self.Forgot_pg)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setStyleSheet(
            "QGroupBox{\n"
            "	\n"
            "	border-radius: 10px;\n"
            "\n"
            "	background-color: rgb(67, 67, 67);\n"
            '	font: 75 14pt "Segoe Print";\n'
            "	text-decoration: underline;\n"
            "\n"
            "	color:rgb(255, 141, 26);\n"
            "\n"
            "}"
        )
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setChecked(False)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.Forgot_msg_pg = QFrame(self.groupBox_2)
        self.Forgot_msg_pg.setObjectName("Forgot_msg_pg")
        self.Forgot_msg_pg.setFrameShape(QFrame.NoFrame)
        self.Forgot_msg_pg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Forgot_msg_pg)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.forgot_usermail_lineEdit = QLineEdit(self.Forgot_msg_pg)
        self.forgot_usermail_lineEdit.setObjectName("forgot_usermail_lineEdit")
        self.forgot_usermail_lineEdit.setMinimumSize(QtCore.QSize(285, 35))
        self.forgot_usermail_lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.forgot_usermail_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "\n"
            "\n"
            "\n"
            "background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  font-size: 18px;\n"
            "  color:white;\n"
            "  font-weight: bold;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(255, 207, 0);	\n"
            "	color: rgb(200, 200, 200);\n"
            "}"
        )
        self.forgot_usermail_lineEdit.setMaxLength(30)
        self.verticalLayout_12.addWidget(self.forgot_usermail_lineEdit)
        self.Forgot_whatsapp_lineEdit = QLineEdit(self.Forgot_msg_pg)
        self.Forgot_whatsapp_lineEdit.setObjectName("Forgot_whatsapp_lineEdit")
        self.Forgot_whatsapp_lineEdit.setMinimumSize(QtCore.QSize(165, 30))
        self.Forgot_whatsapp_lineEdit.setMaximumSize(QtCore.QSize(165, 35))
        self.Forgot_whatsapp_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "\n"
            "\n"
            "\n"
            "background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  font-size: 18px;\n"
            "  color:white;\n"
            "  font-weight: bold;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));	\n"
            "	color: rgb(200, 200, 200);\n"
            "}"
        )
        self.Forgot_whatsapp_lineEdit.setMaxLength(10)
        self.Forgot_whatsapp_lineEdit.setInputMethodHints(Qt.ImhDigitsOnly)
        self.verticalLayout_12.addWidget(self.Forgot_whatsapp_lineEdit)
        self.comboBox = QComboBox(self.Forgot_msg_pg)
        self.comboBox.addItem("What is your question?")
        self.comboBox.addItem("first gate notice board ?")
        self.comboBox.addItem("society total floors (a-z)?")
        self.comboBox.addItem("admin bill number?")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setMinimumSize(QtCore.QSize(0, 31))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox{\n" "	\n" "}\n" "")
        self.comboBox.setCurrentText("What is your question?")
        self.comboBox.setInsertPolicy(QComboBox.NoInsert)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.setFrame(False)
        self.verticalLayout_12.addWidget(self.comboBox)
        self.Forgot_ans_lineEdit = QLineEdit(self.Forgot_msg_pg)
        self.Forgot_ans_lineEdit.setObjectName("Forgot_ans_lineEdit")
        self.Forgot_ans_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.Forgot_ans_lineEdit.setMaximumSize(QtCore.QSize(16777215, 35))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.Forgot_ans_lineEdit.setFont(font1)
        self.Forgot_ans_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  color:white;\n"
            "  font-weight: bold;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(23, 255, 255);	\n"
            "	color: rgb(200, 200, 200);\n"
            "}"
        )
        self.Forgot_ans_lineEdit.setMaxLength(20)
        self.verticalLayout_12.addWidget(self.Forgot_ans_lineEdit)
        self.Forgot_confirm_Button = QPushButton(self.Forgot_msg_pg)
        self.Forgot_confirm_Button.setObjectName("Forgot_confirm_Button")
        self.Forgot_confirm_Button.setMinimumSize(QtCore.QSize(0, 30))
        font2 = QFont()
        font2.setFamily("Shonar Bangla")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.Forgot_confirm_Button.setFont(font2)
        self.Forgot_confirm_Button.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: rgb(255, 130, 20);\n"
            "	border: 2px solid rgb(116, 116, 116);\n"
            "	border-radius: 20px;\n"
            "\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color:rgb(255, 239, 12);\n"
            "	border: 2px solid rgb(1,1,1);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	color:orange;\n"
            "    \n"
            "	background-color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}"
        )
        self.verticalLayout_12.addWidget(self.Forgot_confirm_Button)
        self.verticalLayout_11.addWidget(self.Forgot_msg_pg)
        self.Password_show_lb = QLabel(self.groupBox_2)
        self.Password_show_lb.setObjectName("Password_show_lb")
        self.Password_show_lb.setMinimumSize(QtCore.QSize(0, 40))
        self.Password_show_lb.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalLayout_11.addWidget(self.Password_show_lb)
        self.verticalLayout_9.addWidget(self.groupBox_2)
        self.Login_stackedWidget.addWidget(self.Forgot_pg)
        self.Login_form_pg = QWidget()
        self.Login_form_pg.setObjectName("Login_form_pg")
        self.verticalLayout_6 = QVBoxLayout(self.Login_form_pg)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QGroupBox(self.Login_form_pg)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QtCore.QSize(245, 361))
        self.groupBox.setStyleSheet(
            "QGroupBox{\n"
            "	\n"
            "	border-radius: 10px;\n"
            "    font-size: 15px;\n"
            "    text-align: center;font-family:Dyuthi;\n"
            "	font-weight: bold;\n"
            "   \n"
            "\n"
            "	background-color: rgb(67, 67, 67);\n"
            "	\n"
            "	\n"
            '	font: 75 14pt "Segoe Print";\n'
            "	text-decoration: underline;\n"
            "\n"
            "	color: rgb(255, 230, 41);\n"
            "\n"
            "}"
        )
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Login_title = QLabel(self.groupBox)
        self.Login_title.setObjectName("Login_title")
        self.Login_title.setMinimumSize(QtCore.QSize(0, 0))
        font3 = QFont()
        font3.setFamily("Segoe Print")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        self.Login_title.setFont(font3)
        self.Login_title.setStyleSheet(
            "QLabel{\n" "	\n" "	background-color: transparent;	\n" "\n" "}"
        )
        self.Login_title.setWordWrap(True)
        self.verticalLayout_7.addWidget(self.Login_title)
        self.Credentials = QFrame(self.groupBox)
        self.Credentials.setObjectName("Credentials")
        self.Credentials.setStyleSheet(
            "background-color: rgb(67, 67, 67);\n" "background-color:none;"
        )
        self.Credentials.setFrameShape(QFrame.NoFrame)
        self.Credentials.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Credentials)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Login_user_name = QLineEdit(self.Credentials)
        self.Login_user_name.setObjectName("Login_user_name")
        font4 = QFont()
        font4.setFamily("MS Shell Dlg 2")
        font4.setBold(True)
        font4.setWeight(75)
        self.Login_user_name.setFont(font4)
        self.Login_user_name.setStyleSheet(
            "QLineEdit {\n"
            "	\n"
            "\n"
            "	padding: 15px;\n"
            "\n"
            "background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  font-size: 18px;\n"
            "  color:rgb(255, 255, 255);\n"
            "  font-weight: bold;\n"
            "  \n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "	color: rgb(0, 170, 255);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(255, 207, 0);	\n"
            "	color: rgb(17, 251, 255);\n"
            "   \n"
            "}"
        )
        self.Login_user_name.setMaxLength(10)
        self.Login_user_name.setEchoMode(QLineEdit.Normal)
        self.Login_user_name.setPlaceholderText("UserName")

        self.verticalLayout_8.addWidget(self.Login_user_name)

        self.Login_user_password = QLineEdit(self.Credentials)
        self.Login_user_password.setObjectName("Login_user_password")
        self.Login_user_password.setStyleSheet(
            "QLineEdit {\n"
            "	background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  font-size: 18px;\n"
            "  \n"
            "	color: rgb(255, 255, 255);\n"
            "padding: 15px;\n"
            "  font-weight: bold;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(255, 207, 0);	\n"
            "	color: rgb(8, 251, 255);\n"
            "}"
        )
        self.Login_user_password.setInputMethodHints(
            Qt.ImhHiddenText
            | Qt.ImhNoAutoUppercase
            | Qt.ImhNoPredictiveText
            | Qt.ImhSensitiveData
        )
        self.Login_user_password.setMaxLength(10)
        self.Login_user_password.setFrame(True)
        self.Login_user_password.setEchoMode(QLineEdit.Password)
        self.Login_user_password.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_8.addWidget(self.Login_user_password)
        self.eye_pushButton = QPushButton(self.Credentials)
        self.eye_pushButton.setObjectName("eye_pushButton")
        self.eye_pushButton.setMaximumSize(QSize(30, 25))
        self.eye_pushButton.setStyleSheet(
            "QPushButton{background-color: white;\n"
            "border:2px solid none;\n"
            "border-radius:10px 10px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	border:2px solid grey;}"
        )
        self.iconclose = QIcon()
        self.iconclose.addFile(
            "image/icons/eyeclose.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.iconopen = QIcon()
        self.iconopen.addFile(
            "image/icons/eyeopen.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.eye_pushButton.setIcon(self.iconclose)
        self.eye_pushButton.setIconSize(QSize(21, 20))

        self.verticalLayout_8.addWidget(self.eye_pushButton)

        self.Login_admin_btn = QPushButton(self.Credentials)
        self.Login_admin_btn.setObjectName("Login_admin_btn")
        self.Login_admin_btn.setMaximumSize(QSize(225, 45))
        self.Login_admin_btn.setSizeIncrement(QSize(0, 0))
        self.Login_admin_btn.setBaseSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily("Segoe Script")
        font5.setPointSize(14)
        self.Login_admin_btn.setFont(font5)
        self.Login_admin_btn.setAutoFillBackground(False)
        self.Login_admin_btn.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: rgb(50, 50, 50);\n"
            "	border: 2px solid rgb(60, 60, 60);\n"
            "	border-radius: 20px;\n"
            "\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color: rgb(65, 194, 194);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color:rgb(32, 199, 20);\n"
            "	border: 2px solid rgb(255, 165, 24);	\n"
            "	color: rgb(35, 35, 35);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile("image\icons/bloquear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Login_admin_btn.setIcon(icon1)

        self.verticalLayout_8.addWidget(self.Login_admin_btn)

        self.verticalLayout_7.addWidget(self.Credentials)

        self.verticalLayout_6.addWidget(self.groupBox)

        self.Login_stackedWidget.addWidget(self.Login_form_pg)

        self.verticalLayout_3.addWidget(self.Login_stackedWidget)

        self.horizontalLayout.addWidget(self.Login_Page_right)

        self.Society_BILLMaintenance.addWidget(self.Login_Page)

        self.Society_Page = QWidget()
        self.Society_Page.setObjectName("Society_Page")
        self.Society_Page.setStyleSheet(
            "QWidget#Society_Page{\n" "background-color: rgb(0, 0, 0);\n" "}"
        )
        self.verticalLayout_13 = QVBoxLayout(self.Society_Page)
        self.verticalLayout_13.setSpacing(1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.S_frame_bg = QFrame(self.Society_Page)
        self.S_frame_bg.setObjectName("S_frame_bg")
        self.S_frame_bg.setStyleSheet(
            "QFrame{\n" "background-color: rgb(43, 43, 43);\n" "\n" "}"
        )
        self.S_frame_bg.setFrameShape(QFrame.NoFrame)
        self.S_frame_bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.S_frame_bg)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.S_frame_Left = QFrame(self.S_frame_bg)
        self.S_frame_Left.setObjectName("S_frame_Left")
        self.S_frame_Left.setMinimumSize(QtCore.QSize(80, 0))
        self.S_frame_Left.setMaximumSize(QtCore.QSize(80, 16777215))
        self.S_frame_Left.setFrameShape(QFrame.NoFrame)
        self.S_frame_Left.setFrameShadow(QFrame.Sunken)
        self.S_frame_Left.setLineWidth(1)
        self.verticalLayout_14 = QVBoxLayout(self.S_frame_Left)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.S__L1 = QFrame(self.S_frame_Left)
        self.S__L1.setObjectName("S__L1")
        self.S__L1.setMinimumSize(QtCore.QSize(0, 340))
        font6 = QFont()
        font6.setFamily("Segoe UI")
        font6.setPointSize(12)
        font6.setItalic(True)
        self.S__L1.setFont(font6)
        self.S__L1.setFrameShape(QFrame.NoFrame)
        self.S__L1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.S__L1)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.Sr_User_info = QFrame(self.S__L1)
        self.Sr_User_info.setObjectName("Sr_User_info")
        self.Sr_User_info.setMinimumSize(QtCore.QSize(80, 100))
        self.Sr_User_info.setMaximumSize(QtCore.QSize(100, 140))
        self.Sr_User_info.setFrameShape(QFrame.StyledPanel)
        self.Sr_User_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.Sr_User_info)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(1, 2, 1, 1)
        self.user_img2 = QLabel(self.Sr_User_info)
        self.user_img2.setObjectName("user_img2")
        self.user_img2.setAutoFillBackground(False)
        self.user_img2.setStyleSheet(
            "QLabel{	\n"
            "	\n"
            "	\n"
            "	image: url(image/icons/avatar.png);\n"
            "    background-color:rgb(202, 202, 202);\n"
            "    border :2px solid rgb(49, 181, 34);\n"
            "	background-position: center;\n"
            "}QLabel:hover {\n"
            "border: 1px solid rgb(255, 225, 0);\n"
            "\n"
            "}\n"
            ""
        )

        self.verticalLayout_17.addWidget(self.user_img2)

        self.user_txt2 = QLabel(self.Sr_User_info)
        self.user_txt2.setObjectName("user_txt2")

        self.verticalLayout_17.addWidget(self.user_txt2)

        self.verticalLayout_15.addWidget(self.Sr_User_info)

        self.SL1_home_btn = QPushButton(self.S__L1)
        self.SL1_home_btn.setObjectName("SL1_home_btn")
        self.SL1_home_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL1_home_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.SL1_home_btn.setFont(font7)
        self.SL1_home_btn.setStyleSheet(
            "QPushButton {\n"
            "	\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    \n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0,0,0);\n"
            "	color: rgb(88, 195, 0);\n"
            "\n"
            "}"
        )
        icon2 = QIcon()
        icon2.addFile("image/icons/home.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
        self.SL1_home_btn.setIcon(icon2)
        self.SL1_home_btn.setIconSize(QtCore.QSize(95, 60))

        self.verticalLayout_15.addWidget(self.SL1_home_btn)

        self.SL1_Upaidbill_btn = QPushButton(self.S__L1)
        self.SL1_Upaidbill_btn.setObjectName("SL1_Upaidbill_btn")
        self.SL1_Upaidbill_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL1_Upaidbill_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font8 = QFont()
        font8.setFamily("Segoe UI")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.SL1_Upaidbill_btn.setFont(font8)
        self.SL1_Upaidbill_btn.setStyleSheet(
            "QPushButton {\n"
            "	\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    \n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(88, 195, 0);\n"
            "\n"
            "}"
        )

        self.verticalLayout_15.addWidget(self.SL1_Upaidbill_btn)

        self.SL1_dcharges_btn = QPushButton(self.S__L1)
        self.SL1_dcharges_btn.setObjectName("SL1_dcharges_btn")
        self.SL1_dcharges_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL1_dcharges_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SL1_dcharges_btn.setFont(font8)
        self.SL1_dcharges_btn.setStyleSheet(
            "QPushButton {\n"
            "	\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    \n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(88, 195, 0);\n"
            "\n"
            "}"
        )

        self.verticalLayout_15.addWidget(self.SL1_dcharges_btn)

        self.SL1_pdfbills_btn = QPushButton(self.S__L1)
        self.SL1_pdfbills_btn.setObjectName("SL1_pdfbills_btn")
        self.SL1_pdfbills_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL1_pdfbills_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SL1_pdfbills_btn.setFont(font8)
        self.SL1_pdfbills_btn.setStyleSheet(
            "QPushButton {\n"
            "	\n"
            "	color: rgb(255, 255, 255);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    \n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(88, 195, 0);\n"
            "\n"
            "}"
        )
        icon3 = QIcon()
        icon3.addFile(
            "image/icons/pdf_logo.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SL1_pdfbills_btn.setIcon(icon3)
        self.SL1_pdfbills_btn.setIconSize(QtCore.QSize(35, 40))

        self.verticalLayout_15.addWidget(self.SL1_pdfbills_btn)

        self.adjusting_frame = QFrame(self.S__L1)
        self.adjusting_frame.setObjectName("adjusting_frame")
        self.adjusting_frame.setMinimumSize(QtCore.QSize(0, 20))
        self.adjusting_frame.setFrameShape(QFrame.NoFrame)
        self.adjusting_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.adjusting_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.wall_art = QLabel(self.adjusting_frame)
        self.wall_art.setObjectName("wall_art")
        self.wall_art.setStyleSheet("border-image: url(image/images/Wall_art.png);")

        self.verticalLayout_21.addWidget(self.wall_art)

        self.verticalLayout_15.addWidget(self.adjusting_frame)

        self.verticalLayout_14.addWidget(self.S__L1)

        self.S_L2 = QFrame(self.S_frame_Left)
        self.S_L2.setObjectName("S_L2")
        self.S_L2.setMinimumSize(QtCore.QSize(0, 200))
        self.S_L2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.S_L2.setFrameShape(QFrame.NoFrame)
        self.S_L2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.S_L2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 5, 0, 0)
        self.SL2_whatsapp_btn = QPushButton(self.S_L2)
        self.SL2_whatsapp_btn.setObjectName("SL2_whatsapp_btn")
        self.SL2_whatsapp_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL2_whatsapp_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font9 = QFont()
        font9.setFamily("Segoe Print")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.SL2_whatsapp_btn.setFont(font9)
        self.SL2_whatsapp_btn.setStyleSheet(
            "QPushButton {\n"
            "	color:rgb(4, 194, 58);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    \n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "	\n"
            "    \n"
            "	color:rgb(103, 255, 2);\n"
            "    \n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(26, 255, 0)\n"
            "\n"
            "}"
        )
        self.SL2_whatsapp_btn.setIconSize(QtCore.QSize(52, 50))

        self.verticalLayout_18.addWidget(self.SL2_whatsapp_btn)

        self.SL2_Report_btn = QPushButton(self.S_L2)
        self.SL2_Report_btn.setObjectName("SL2_Report_btn")
        self.SL2_Report_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL2_Report_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SL2_Report_btn.setFont(font8)
        self.SL2_Report_btn.setStyleSheet(
            "QPushButton{\n"
            "     color: rgb(255, 255, 255);\n"
            "     \n"
            "	background-color: rgb(35, 35, 35);\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "	background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 0, 4);\n"
            "\n"
            "}"
        )

        self.verticalLayout_18.addWidget(self.SL2_Report_btn)

        self.SL2_Setting_btn = QPushButton(self.S_L2)
        self.SL2_Setting_btn.setObjectName("SL2_Setting_btn")
        self.SL2_Setting_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.SL2_Setting_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font10 = QFont()
        font10.setFamily("Segoe UI")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.SL2_Setting_btn.setFont(font10)
        self.SL2_Setting_btn.setStyleSheet(
            "QPushButton{\n"
            "     color: rgb(255, 255, 255);\n"
            "     \n"
            "	background-color: rgb(35, 35, 35);\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "	background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 0, 4);\n"
            "\n"
            "}"
        )
        icon4 = QIcon()
        icon4.addFile(
            "image\icons/setting.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SL2_Setting_btn.setIcon(icon4)
        self.SL2_Setting_btn.setIconSize(QtCore.QSize(30, 30))

        self.verticalLayout_18.addWidget(self.SL2_Setting_btn)

        self.SL2_logout_btn = QPushButton(self.S_L2)
        self.SL2_logout_btn.setObjectName("SL2_logout_btn")
        self.SL2_logout_btn.setFont(font10)
        self.SL2_logout_btn.setStyleSheet(
            "QPushButton{\n"
            "     color: rgb(255, 255, 255);\n"
            "     \n"
            "	background-color: rgb(35, 35, 35);\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "background-color:qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));}\n"
            "\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0,0,0);\n"
            "	color: rgb(7, 11, 255);\n"
            "\n"
            "}"
        )
        icon5 = QIcon()
        icon5.addFile("image\icons/logout.png", QtCore.QSize(), QIcon.Normal, QIcon.Off)
        self.SL2_logout_btn.setIcon(icon5)
        self.SL2_logout_btn.setIconSize(QtCore.QSize(45, 45))

        self.verticalLayout_18.addWidget(self.SL2_logout_btn)

        self.verticalLayout_14.addWidget(self.S_L2)

        self.horizontalLayout_3.addWidget(self.S_frame_Left)

        self.S_frame_right = QFrame(self.S_frame_bg)
        self.S_frame_right.setObjectName("S_frame_right")
        self.S_frame_right.setFrameShape(QFrame.NoFrame)
        self.S_frame_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.S_frame_right)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.S_R1 = QFrame(self.S_frame_right)
        self.S_R1.setObjectName("S_R1")
        self.S_R1.setMinimumSize(QtCore.QSize(0, 50))
        self.S_R1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.S_R1.setFrameShape(QFrame.Box)
        self.S_R1.setFrameShadow(QFrame.Plain)
        self.S_R1.setLineWidth(1)
        self.horizontalLayout_4 = QHBoxLayout(self.S_R1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.SR1_Title = QFrame(self.S_R1)
        self.SR1_Title.setObjectName("SR1_Title")
        self.SR1_Title.setFrameShape(QFrame.NoFrame)
        self.SR1_Title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.SR1_Title)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(10, 0, 0, 0)
        self.Title_txt = QLabel(self.SR1_Title)
        self.Title_txt.setObjectName("Title_txt")
        font11 = QFont()
        font11.setFamily("Segoe UI")
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setWeight(75)
        self.Title_txt.setFont(font11)
        self.Title_txt.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_20.addWidget(self.Title_txt)

        self.horizontalLayout_4.addWidget(self.SR1_Title)

        self.SR1_Date = QFrame(self.S_R1)
        self.SR1_Date.setObjectName("SR1_Date")
        self.SR1_Date.setFrameShape(QFrame.NoFrame)
        self.SR1_Date.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.SR1_Date)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_adj = QWidget(self.SR1_Date)
        self.widget_adj.setObjectName("widget_adj")

        self.horizontalLayout_5.addWidget(self.widget_adj)

        self.Date_lbl = QLabel(self.SR1_Date)
        self.Date_lbl.setObjectName("Date_lbl")

        self.horizontalLayout_5.addWidget(self.Date_lbl)

        self.Todays_date_dateEdit = QDateEdit(self.SR1_Date)
        self.Todays_date_dateEdit.setObjectName("Todays_date_dateEdit")
        self.Todays_date_dateEdit.setMinimumSize(QtCore.QSize(120, 30))
        self.Todays_date_dateEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(False)
        font12.setWeight(50)
        self.Todays_date_dateEdit.setFont(font12)
        self.Todays_date_dateEdit.setAutoFillBackground(False)
        self.Todays_date_dateEdit.setStyleSheet(
            "QDateEdit{\n"
            "     \n"
            "	color: rgb(255, 170, 0);\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid rgb(0, 255, 0);\n"
            "   border-radius:10px;\n"
            "}\n"
            "\n"
            "QDateEdit:hover{\n"
            "     \n"
            "	background-color: rgb(0, 0, 0);\n"
            "    font-weight:bold;\n"
            "}"
        )
        self.Todays_date_dateEdit.setInputMethodHints(Qt.ImhDate | Qt.ImhPreferNumbers)
        self.Todays_date_dateEdit.setWrapping(True)
        self.Todays_date_dateEdit.setReadOnly(False)
        self.Todays_date_dateEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.Todays_date_dateEdit.setCalendarPopup(True)

        self.horizontalLayout_5.addWidget(self.Todays_date_dateEdit)

        self.horizontalLayout_4.addWidget(self.SR1_Date)

        self.verticalLayout_19.addWidget(self.S_R1)

        self.S_R2 = QFrame(self.S_frame_right)
        self.S_R2.setObjectName("S_R2")
        self.S_R2.setFrameShape(QFrame.StyledPanel)
        self.S_R2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.S_R2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.SR_stackedWidget = QStackedWidget(self.S_R2)
        self.SR_stackedWidget.setObjectName("SR_stackedWidget")
        self.SR2_home_p1 = QWidget()
        self.SR2_home_p1.setObjectName("SR2_home_p1")
        self.SR2_home_p1.setMouseTracking(True)
        self.verticalLayout_23 = QVBoxLayout(self.SR2_home_p1)
        self.verticalLayout_23.setSpacing(2)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.SR2_cntrl = QFrame(self.SR2_home_p1)
        self.SR2_cntrl.setObjectName("SR2_cntrl")
        self.SR2_cntrl.setFrameShape(QFrame.NoFrame)
        self.SR2_cntrl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.SR2_cntrl)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.NewMonth_fr1 = QFrame(self.SR2_cntrl)
        self.NewMonth_fr1.setObjectName("NewMonth_fr1")
        self.NewMonth_fr1.setFrameShape(QFrame.StyledPanel)
        self.NewMonth_fr1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.NewMonth_fr1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.NewMonth_lb = QLabel(self.NewMonth_fr1)
        self.NewMonth_lb.setObjectName("NewMonth_lb")
        self.NewMonth_lb.setMinimumSize(QtCore.QSize(0, 0))
        self.NewMonth_lb.setMaximumSize(QtCore.QSize(16777215, 100))
        self.NewMonth_lb.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
        self.NewMonth_lb.setWordWrap(True)
        self.NewMonth_lb.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.NewMonth_lb)

        self.NewMonth_btn = QPushButton(self.NewMonth_fr1)
        self.NewMonth_btn.setObjectName("NewMonth_btn")
        self.NewMonth_btn.setMaximumSize(QtCore.QSize(175, 75))
        font13 = QFont()
        font13.setFamily("Segoe Print")
        font13.setPointSize(16)
        font13.setBold(True)
        font13.setWeight(75)
        self.NewMonth_btn.setFont(font13)
        self.NewMonth_btn.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 108, 102, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "	border: 2px solid rgb(60, 60, 60);\n"
            "	border-radius: 20px;\n"
            "   \n"
            "	color:qlineargradient(spread:pad, x1:0.960045, y1:0.727, x2:0.994318, y2:1, stop:0 rgba(13, 35, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	color:rgb(255, 170, 0);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	\n"
            "	border: 2px solid rgb(255, 165, 24);	\n"
            "	color:  qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}"
        )

        self.horizontalLayout_6.addWidget(self.NewMonth_btn)

        self.verticalLayout_16.addWidget(self.NewMonth_fr1)

        self.Billstatus_fr2 = QFrame(self.SR2_cntrl)
        self.Billstatus_fr2.setObjectName("Billstatus_fr2")
        self.Billstatus_fr2.setFrameShape(QFrame.StyledPanel)
        self.Billstatus_fr2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Billstatus_fr2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Billstatus_lb = QLabel(self.Billstatus_fr2)
        self.Billstatus_lb.setObjectName("Billstatus_lb")
        self.Billstatus_lb.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Billstatus_lb.setWordWrap(True)
        self.Billstatus_lb.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_7.addWidget(self.Billstatus_lb)

        self.Billstatus_btn = QPushButton(self.Billstatus_fr2)
        self.Billstatus_btn.setObjectName("Billstatus_btn")
        self.Billstatus_btn.setMaximumSize(QtCore.QSize(175, 75))
        self.Billstatus_btn.setFont(font13)
        self.Billstatus_btn.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 108, 102, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "	border: 2px solid rgb(60, 60, 60);\n"
            "	border-radius: 20px;\n"
            "   \n"
            "	color:qlineargradient(spread:pad, x1:0.960045, y1:0.727, x2:0.994318, y2:1, stop:0 rgba(13, 35, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	color:rgb(255, 170, 0);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	\n"
            "	border: 2px solid rgb(255, 165, 24);	\n"
            "	color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}"
        )

        self.horizontalLayout_7.addWidget(self.Billstatus_btn)

        self.verticalLayout_16.addWidget(self.Billstatus_fr2)

        self.Conwhatsapp_fr3 = QFrame(self.SR2_cntrl)
        self.Conwhatsapp_fr3.setObjectName("Conwhatsapp_fr3")
        self.Conwhatsapp_fr3.setFrameShape(QFrame.StyledPanel)
        self.Conwhatsapp_fr3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Conwhatsapp_fr3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Conwebwhatsapp_lb = QLabel(self.Conwhatsapp_fr3)
        self.Conwebwhatsapp_lb.setObjectName("Conwebwhatsapp_lb")
        self.Conwebwhatsapp_lb.setWordWrap(True)
        self.Conwebwhatsapp_lb.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_8.addWidget(self.Conwebwhatsapp_lb)

        self.Conwebwhatsapp_btn = QPushButton(self.Conwhatsapp_fr3)
        self.Conwebwhatsapp_btn.setObjectName("Conwebwhatsapp_btn")
        self.Conwebwhatsapp_btn.setMaximumSize(QtCore.QSize(175, 75))
        self.Conwebwhatsapp_btn.setFont(font13)
        self.Conwebwhatsapp_btn.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 108, 102, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "	border: 2px solid rgb(60, 60, 60);\n"
            "	border-radius: 20px;\n"
            "   \n"
            "	color:qlineargradient(spread:pad, x1:0.960045, y1:0.727, x2:0.994318, y2:1, stop:0 rgba(13, 35, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	color:rgb(255, 170, 0);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	\n"
            "	border: 2px solid rgb(255, 165, 24);	\n"
            "	color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}"
        )

        self.horizontalLayout_8.addWidget(self.Conwebwhatsapp_btn)

        self.verticalLayout_16.addWidget(self.Conwhatsapp_fr3)

        self.Info_fr4 = QFrame(self.SR2_cntrl)
        self.Info_fr4.setObjectName("Info_fr4")
        self.Info_fr4.setFrameShape(QFrame.StyledPanel)
        self.Info_fr4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Info_fr4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.updatinfo_lb = QLabel(self.Info_fr4)
        self.updatinfo_lb.setObjectName("updatinfo_lb")
        self.updatinfo_lb.setWordWrap(True)
        self.updatinfo_lb.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_9.addWidget(self.updatinfo_lb)

        self.updatinfo_btn = QPushButton(self.Info_fr4)
        self.updatinfo_btn.setObjectName("updatinfo_btn")
        self.updatinfo_btn.setMaximumSize(QtCore.QSize(175, 75))
        self.updatinfo_btn.setFont(font13)
        self.updatinfo_btn.setStyleSheet(
            "QPushButton {	\n"
            "	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(128, 108, 102, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "	border: 2px solid rgb(60, 60, 60);\n"
            "	border-radius: 20px;\n"
            "   \n"
            "	color:qlineargradient(spread:pad, x1:0.960045, y1:0.727, x2:0.994318, y2:1, stop:0 rgba(13, 35, 104, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton:hover {	\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	\n"
            "	\n"
            "	border: 2px solid rgb(70, 70, 70);\n"
            "	color:rgb(255, 168, 17);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	\n"
            "	\n"
            "	border: 2px solid rgb(255, 165, 24);	\n"
            "	color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}"
        )

        self.horizontalLayout_9.addWidget(self.updatinfo_btn)

        self.verticalLayout_16.addWidget(self.Info_fr4)

        self.verticalLayout_23.addWidget(self.SR2_cntrl)

        self.SR_stackedWidget.addWidget(self.SR2_home_p1)
        self.SR2_billrelease_p2 = QWidget()
        self.SR2_billrelease_p2.setObjectName("SR2_billrelease_p2")
        self.verticalLayout_24 = QVBoxLayout(self.SR2_billrelease_p2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.SR2_bg_frame = QFrame(self.SR2_billrelease_p2)
        self.SR2_bg_frame.setObjectName("SR2_bg_frame")
        self.SR2_bg_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_bg_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.SR2_bg_frame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.SR2_top_frame = QFrame(self.SR2_bg_frame)
        self.SR2_top_frame.setObjectName("SR2_top_frame")
        self.SR2_top_frame.setMinimumSize(QtCore.QSize(0, 380))
        self.SR2_top_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_top_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.SR2_top_frame)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.SR2_top1_lbl_frame = QFrame(self.SR2_top_frame)
        self.SR2_top1_lbl_frame.setObjectName("SR2_top1_lbl_frame")
        self.SR2_top1_lbl_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.SR2_top1_lbl_frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.SR2_top1_lbl_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_top1_lbl_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.SR2_top1_lbl_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 5, 0)
        self.SR2_subtitle_frame = QFrame(self.SR2_top1_lbl_frame)
        self.SR2_subtitle_frame.setObjectName("SR2_subtitle_frame")
        self.SR2_subtitle_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_subtitle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.SR2_subtitle_frame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.Resident_subtitle_lbl = QLabel(self.SR2_subtitle_frame)
        self.Resident_subtitle_lbl.setObjectName("Resident_subtitle_lbl")
        self.Resident_subtitle_lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_19.addWidget(self.Resident_subtitle_lbl)

        self.horizontalLayout_18.addWidget(self.SR2_subtitle_frame)

        self.New_month_datecheck_lbl = QLabel(self.SR2_top1_lbl_frame)
        self.New_month_datecheck_lbl.setObjectName("New_month_datecheck_lbl")
        self.New_month_datecheck_lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_18.addWidget(self.New_month_datecheck_lbl)

        self.verticalLayout_27.addWidget(self.SR2_top1_lbl_frame)

        self.SR2_tableholder_frame = QFrame(self.SR2_top_frame)
        self.SR2_tableholder_frame.setObjectName("SR2_tableholder_frame")
        self.SR2_tableholder_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_tableholder_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.SR2_tableholder_frame)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.SR2_cntrl_table_frame = QFrame(self.SR2_tableholder_frame)
        self.SR2_cntrl_table_frame.setObjectName("SR2_cntrl_table_frame")
        self.SR2_cntrl_table_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.SR2_cntrl_table_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_cntrl_table_frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_12 = QHBoxLayout(self.SR2_cntrl_table_frame)
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 0, 0)
        self.SR2_searchbox_frame_5 = QFrame(self.SR2_cntrl_table_frame)
        self.SR2_searchbox_frame_5.setObjectName("SR2_searchbox_frame_5")
        self.SR2_searchbox_frame_5.setMaximumSize(QtCore.QSize(325, 16777215))
        self.SR2_searchbox_frame_5.setFrameShape(QFrame.NoFrame)
        self.SR2_searchbox_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.SR2_searchbox_frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.SR2_searchbox_lineEdit = QLineEdit(self.SR2_searchbox_frame_5)
        self.SR2_searchbox_lineEdit.setObjectName("SR2_searchbox_lineEdit")
        self.SR2_searchbox_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.SR2_searchbox_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "Wing or Room no.", None)
        )
        self.SR2_searchbox_lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "	color: rgb(255, 255, 0);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    border:1px solid black;\n"
            "    border-radius:10px;\n"
            "   \n"
            '	font: 75 11pt "Segoe Script";\n'
            "	\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QLineEdit:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "\n"
            "}"
        )

        self.horizontalLayout_13.addWidget(self.SR2_searchbox_lineEdit)

        self.SR2_search_btn = QPushButton(self.SR2_searchbox_frame_5)
        self.SR2_search_btn.setObjectName("SR2_search_btn")
        self.SR2_search_btn.setMinimumSize(QtCore.QSize(100, 0))
        font14 = QFont()
        font14.setFamily("Segoe Print")
        font14.setPointSize(10)
        self.SR2_search_btn.setFont(font14)
        self.SR2_search_btn.setStyleSheet(
            "QPushButton {\n"
            "	color:rgb(4, 194, 58);\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    border:1px solid black;\n"
            "    border-radius:10px;\n"
            "	\n"
            "}\n"
            "QPushButton:hover {\n"
            "	  border:1px solid rgb(4, 194, 58) ;\n"
            "    \n"
            "	color:rgb(103, 255, 2);\n"
            "    \n"
            "}\n"
            "QPushButton:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(26, 255, 0)\n"
            "\n"
            "}"
        )

        self.horizontalLayout_13.addWidget(self.SR2_search_btn)

        self.horizontalLayout_12.addWidget(self.SR2_searchbox_frame_5)

        self.adjust_center_frame_6 = QFrame(self.SR2_cntrl_table_frame)
        self.adjust_center_frame_6.setObjectName("adjust_center_frame_6")
        self.adjust_center_frame_6.setMaximumSize(QtCore.QSize(200, 16777215))
        self.adjust_center_frame_6.setFrameShape(QFrame.NoFrame)
        self.adjust_center_frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.adjust_center_frame_6)

        self.SR2_charges_frame_7 = QFrame(self.SR2_cntrl_table_frame)
        self.SR2_charges_frame_7.setObjectName("SR2_charges_frame_7")
        self.SR2_charges_frame_7.setFrameShape(QFrame.NoFrame)
        self.SR2_charges_frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.SR2_charges_frame_7)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.SR2_charges_lbl = QLabel(self.SR2_charges_frame_7)
        self.SR2_charges_lbl.setObjectName("SR2_charges_lbl")
        self.SR2_charges_lbl.setMinimumSize(QtCore.QSize(225, 0))
        font15 = QFont()
        font15.setPointSize(12)
        self.SR2_charges_lbl.setFont(font15)

        self.horizontalLayout_14.addWidget(self.SR2_charges_lbl)

        self.horizontalLayout_12.addWidget(self.SR2_charges_frame_7)

        self.verticalLayout_29.addWidget(self.SR2_cntrl_table_frame)

        self.SR2_tablevie_frame_3 = QFrame(self.SR2_tableholder_frame)
        self.SR2_tablevie_frame_3.setObjectName("SR2_tablevie_frame_3")
        self.SR2_tablevie_frame_3.setFrameShape(QFrame.NoFrame)
        self.SR2_tablevie_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.SR2_tablevie_frame_3)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.SR2_Bill_tableView = QTableView(self.SR2_tablevie_frame_3)
        self.SR2_Bill_tableView.setObjectName("SR2_Bill_tableView")
        self.SR2_Bill_tableView.setMinimumSize(QtCore.QSize(320, 0))
        self.SR2_Bill_tableView.setMaximumSize(QtCore.QSize(320, 16777215))
        self.SR2_Bill_tableView.setFrameShadow(QFrame.Raised)
        self.SR2_Bill_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SR2_Bill_tableView.setShowGrid(True)
        self.SR2_Bill_tableView.setSortingEnabled(True)

        self.horizontalLayout_11.addWidget(self.SR2_Bill_tableView)

        self.frame_3 = QFrame(self.SR2_tablevie_frame_3)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMaximumSize(QtCore.QSize(125, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.frame_3)

        self.SR2_charges_tableWidget = QTableWidget(self.SR2_tablevie_frame_3)
        if self.SR2_charges_tableWidget.columnCount() < 2:
            self.SR2_charges_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.SR2_charges_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SR2_charges_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if self.SR2_charges_tableWidget.rowCount() < 2:
            self.SR2_charges_tableWidget.setRowCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.SR2_charges_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.SR2_charges_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.SR2_charges_tableWidget.setItem(0, 0, __qtablewidgetitem4)
        self.SR2_charges_tableWidget.setObjectName("SR2_charges_tableWidget")
        self.SR2_charges_tableWidget.setMinimumSize(QtCore.QSize(225, 0))
        self.SR2_charges_tableWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.SR2_charges_tableWidget.setFrameShadow(QFrame.Raised)
        self.SR2_charges_tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.SR2_charges_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.SR2_charges_tableWidget.setProperty("showDropIndicator", False)
        self.SR2_charges_tableWidget.setDragDropOverwriteMode(False)
        self.SR2_charges_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.SR2_charges_tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.SR2_charges_tableWidget.setShowGrid(True)
        self.SR2_charges_tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.horizontalLayout_11.addWidget(self.SR2_charges_tableWidget)

        self.adjust_right_frame_8 = QFrame(self.SR2_tablevie_frame_3)
        self.adjust_right_frame_8.setObjectName("adjust_right_frame_8")
        self.adjust_right_frame_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.adjust_right_frame_8.setFrameShape(QFrame.NoFrame)
        self.adjust_right_frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.adjust_right_frame_8)

        self.verticalLayout_29.addWidget(self.SR2_tablevie_frame_3)

        self.verticalLayout_27.addWidget(self.SR2_tableholder_frame)

        self.verticalLayout_25.addWidget(self.SR2_top_frame)

        self.SR2_down1_frame = QFrame(self.SR2_bg_frame)
        self.SR2_down1_frame.setObjectName("SR2_down1_frame")
        self.SR2_down1_frame.setMinimumSize(QtCore.QSize(0, 115))
        self.SR2_down1_frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.SR2_down1_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_down1_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.SR2_down1_frame)
        self.verticalLayout_28.setSpacing(2)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.SR2_bellow_btnbox = QFrame(self.SR2_down1_frame)
        self.SR2_bellow_btnbox.setObjectName("SR2_bellow_btnbox")
        self.SR2_bellow_btnbox.setMinimumSize(QtCore.QSize(300, 0))
        self.SR2_bellow_btnbox.setFrameShape(QFrame.NoFrame)
        self.SR2_bellow_btnbox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.SR2_bellow_btnbox)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.SR2_bellow_btnbox)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(2)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.SR2_bellow_totalbill_lbl = QLabel(self.frame_2)
        self.SR2_bellow_totalbill_lbl.setObjectName("SR2_bellow_totalbill_lbl")
        self.SR2_bellow_totalbill_lbl.setMaximumSize(QtCore.QSize(75, 16777215))
        self.SR2_bellow_totalbill_lbl.setWordWrap(True)
        self.SR2_bellow_totalbill_lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_17.addWidget(self.SR2_bellow_totalbill_lbl)

        self.SR2_bellow_totalbill_value = QLabel(self.frame_2)
        self.SR2_bellow_totalbill_value.setObjectName("SR2_bellow_totalbill_value")
        self.SR2_bellow_totalbill_value.setMaximumSize(QtCore.QSize(60, 16777215))
        self.SR2_bellow_totalbill_value.setWordWrap(True)
        self.SR2_bellow_totalbill_value.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_17.addWidget(self.SR2_bellow_totalbill_value)

        self.SR2_bellow_totalresidence_lbl = QLabel(self.frame_2)
        self.SR2_bellow_totalresidence_lbl.setObjectName(
            "SR2_bellow_totalresidence_lbl"
        )
        self.SR2_bellow_totalresidence_lbl.setMaximumSize(QtCore.QSize(115, 16777215))
        self.SR2_bellow_totalresidence_lbl.setWordWrap(False)
        self.SR2_bellow_totalresidence_lbl.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_17.addWidget(self.SR2_bellow_totalresidence_lbl)

        self.SR2_bellow_totalresidence_value = QLabel(self.frame_2)
        self.SR2_bellow_totalresidence_value.setObjectName(
            "SR2_bellow_totalresidence_value"
        )
        self.SR2_bellow_totalresidence_value.setMaximumSize(QtCore.QSize(125, 16777215))
        self.SR2_bellow_totalresidence_value.setWordWrap(True)
        self.SR2_bellow_totalresidence_value.setTextInteractionFlags(
            Qt.NoTextInteraction
        )

        self.horizontalLayout_17.addWidget(self.SR2_bellow_totalresidence_value)

        self.btn_holder = QFrame(self.frame_2)
        self.btn_holder.setObjectName("btn_holder")
        self.btn_holder.setMaximumSize(QtCore.QSize(235, 16777215))
        self.btn_holder.setFrameShape(QFrame.NoFrame)
        self.btn_holder.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.btn_holder)
        self.horizontalLayout_16.setSpacing(2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.Generate_btn = QPushButton(self.btn_holder)
        self.Generate_btn.setObjectName("Generate_btn")
        font16 = QFont()
        font16.setFamily("Segoe UI")
        font16.setPointSize(11)
        font16.setBold(True)
        font16.setWeight(75)
        self.Generate_btn.setFont(font16)
        self.Generate_btn.setStyleSheet(
            "QPushButton{\n"
            "      \n"
            "	color: rgb(255, 64, 30);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "     \n"
            "	background-color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "	background-color: rgb(0, 0, 0);\n"
            "}"
        )

        self.horizontalLayout_16.addWidget(self.Generate_btn)

        self.Release_btn = QPushButton(self.btn_holder)
        self.Release_btn.setObjectName("Release_btn")
        self.Release_btn.setFont(font16)
        self.Release_btn.setStyleSheet(
            "QPushButton{\n"
            "      \n"
            "	color: rgb(0, 255, 0);\n"
            "background-color: rgb(109, 109, 109);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "     \n"
            "	background-color: qlineargradient(spread:pad, x1:0.455, y1:0.477, x2:1, y2:1, stop:0 rgba(156, 0, 181, 255), stop:1 rgba(17, 31, 147, 255));\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "	background-color: rgb(0, 0, 0);\n"
            "    font-weight:bold;\n"
            "}"
        )

        self.horizontalLayout_16.addWidget(self.Release_btn)

        self.horizontalLayout_17.addWidget(self.btn_holder)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_6)

        self.horizontalLayout_10.addWidget(self.frame_2)

        self.verticalLayout_28.addWidget(self.SR2_bellow_btnbox)

        self.SR2_Below_infobox = QFrame(self.SR2_down1_frame)
        self.SR2_Below_infobox.setObjectName("SR2_Below_infobox")
        self.SR2_Below_infobox.setFrameShape(QFrame.NoFrame)
        self.SR2_Below_infobox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.SR2_Below_infobox)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.SR2_Below_infobox)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.SR2_extra_info1 = QLabel(self.frame)
        self.SR2_extra_info1.setObjectName("SR2_extra_info1")
        self.SR2_extra_info1.setWordWrap(True)
        self.SR2_extra_info1.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_15.addWidget(self.SR2_extra_info1)

        self.SR2_extra_info2 = QLabel(self.frame)
        self.SR2_extra_info2.setObjectName("SR2_extra_info2")
        self.SR2_extra_info2.setWordWrap(True)
        self.SR2_extra_info2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_15.addWidget(self.SR2_extra_info2)

        self.verticalLayout_26.addWidget(self.frame)

        self.verticalLayout_28.addWidget(self.SR2_Below_infobox)

        self.verticalLayout_25.addWidget(self.SR2_down1_frame)

        self.verticalLayout_24.addWidget(self.SR2_bg_frame)

        self.SR_stackedWidget.addWidget(self.SR2_billrelease_p2)
        self.SR2_billstatus_pg3 = QWidget()
        self.SR2_billstatus_pg3.setObjectName("SR2_billstatus_pg3")
        self.verticalLayout_30 = QVBoxLayout(self.SR2_billstatus_pg3)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.SR2_Billstatus_bg_frame = QFrame(self.SR2_billstatus_pg3)
        self.SR2_Billstatus_bg_frame.setObjectName("SR2_Billstatus_bg_frame")
        self.SR2_Billstatus_bg_frame.setFrameShape(QFrame.NoFrame)
        self.SR2_Billstatus_bg_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.SR2_Billstatus_bg_frame)
        self.verticalLayout_31.setSpacing(1)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.SR2_toppg3 = QFrame(self.SR2_Billstatus_bg_frame)
        self.SR2_toppg3.setObjectName("SR2_toppg3")
        self.SR2_toppg3.setMinimumSize(QtCore.QSize(715, 100))
        self.SR2_toppg3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.SR2_toppg3.setFrameShape(QFrame.StyledPanel)
        self.SR2_toppg3.setFrameShadow(QFrame.Raised)
        self.SR2_top_search_lineEdit = QLineEdit(self.SR2_toppg3)
        self.SR2_top_search_lineEdit.setObjectName("SR2_top_search_lineEdit")
        self.SR2_top_search_lineEdit.setGeometry(QRect(20, 10, 141, 31))
        self.SR2_top_search_lineEdit.setFont(font12)
        self.SR2_top_search_lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    font-weight:bold;\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QLineEdit:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.SR2_top_search_lineEdit.setMaxLength(5)
        self.SR2_top_search_btn = QPushButton(self.SR2_toppg3)
        self.SR2_top_search_btn.setObjectName("SR2_top_search_btn")
        self.SR2_top_search_btn.setGeometry(QRect(170, 10, 101, 31))
        self.SR2_top_search_btn.setFont(font15)
        self.SR2_top_search_btn.setStyleSheet(
            "QPushButton{\n"
            "      \n"
            "	color:rgb(255, 85, 0);\n"
            "   border : 1px solid rgb(0, 255, 0);\n"
            "   border-radius:10px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "     \n"
            "	background-color:rgb(0,0,0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "    font-weight:bold;\n"
            "}"
        )
        self.SR2_top_update_btn = QPushButton(self.SR2_toppg3)
        self.SR2_top_update_btn.setObjectName("SR2_top_update_btn")
        self.SR2_top_update_btn.setGeometry(QRect(280, 10, 101, 31))
        font17 = QFont()
        font17.setPointSize(12)
        font17.setBold(False)
        font17.setWeight(50)
        self.SR2_top_update_btn.setFont(font17)
        self.SR2_top_update_btn.setStyleSheet(
            "QPushButton{\n"
            "      \n"
            "	color:rgb(255, 85, 0);\n"
            "   border : 1px solid rgb(0, 255, 0);\n"
            "   border-radius:10px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "     \n"
            "background-color: rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "    font-weight:bold;\n"
            "}"
        )
        self.label = QLabel(self.SR2_toppg3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(20, 60, 101, 31))
        font18 = QFont()
        font18.setPointSize(20)
        self.label.setFont(font18)
        self.SR2_top_viewtype_comboBox = QComboBox(self.SR2_toppg3)
        self.SR2_top_viewtype_comboBox.addItem("ALL")
        self.SR2_top_viewtype_comboBox.addItem("")
        self.SR2_top_viewtype_comboBox.addItem("")
        self.SR2_top_viewtype_comboBox.addItem("")
        self.SR2_top_viewtype_comboBox.addItem("")
        self.SR2_top_viewtype_comboBox.addItem("")
        self.SR2_top_viewtype_comboBox.setObjectName("SR2_top_viewtype_comboBox")
        self.SR2_top_viewtype_comboBox.setGeometry(QRect(140, 60, 121, 31))
        self.SR2_top_viewtype_comboBox.setStyleSheet(
            "QComboBox{\n"
            "\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    font-weight:bold;\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QListView{color:rgb(255, 255, 127);}\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QComboBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.label_2 = QLabel(self.SR2_toppg3)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(380, 60, 121, 31))
        self.SR2_top_month_comboBox = QComboBox(self.SR2_toppg3)
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.addItem("")
        self.SR2_top_month_comboBox.setObjectName("SR2_top_month_comboBox")
        self.SR2_top_month_comboBox.setGeometry(QRect(520, 60, 121, 31))
        self.SR2_top_month_comboBox.setStyleSheet(
            "QComboBox{\n"
            "\n"
            "	background-color: rgb(35, 35, 35);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    font-weight:bold;\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QListView{color:rgb(255, 255, 127);}\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QComboBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.SR2_refresh_pg3 = QPushButton(self.SR2_toppg3)
        self.SR2_refresh_pg3.setObjectName("SR2_refresh_pg3")
        self.SR2_refresh_pg3.setGeometry(QRect(270, 60, 91, 31))
        icon3 = QIcon()
        icon3.addFile(
            "image/icons/refresh.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SR2_refresh_pg3.setIcon(icon3)
        self.SR2_refresh_pg3.setIconSize(QtCore.QSize(16, 16))
        self.SR2_refresh_pg3.setStyleSheet(
            "QPushButton{\n"
            "      \n"
            "	color:rgb(255, 85, 0);\n"
            "   border : 1px solid rgb(0, 255, 0);\n"
            "   border-radius:10px;\n"
            "}\n"
            "QPushButton:pressed{\n"
            "     \n"
            "	background-color: rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:hover{\n"
            "     \n"
            "    font-weight:bold;\n"
            "}"
        )

        self.verticalLayout_31.addWidget(self.SR2_toppg3)

        self.SR2_midpg3 = QFrame(self.SR2_Billstatus_bg_frame)
        self.SR2_midpg3.setObjectName("SR2_midpg3")
        self.SR2_midpg3.setFrameShape(QFrame.NoFrame)
        self.SR2_midpg3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.SR2_midpg3)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.SR2_billstatus_tableWidget = QTableWidget(self.SR2_midpg3)
        self.SR2_billstatus_tableWidget.setRowCount(0)
        if self.SR2_billstatus_tableWidget.columnCount() < 7:
            self.SR2_billstatus_tableWidget.setColumnCount(7)
        font19 = QFont()
        font19.setPointSize(11)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font19)
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.SR2_billstatus_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        self.SR2_billstatus_tableWidget.setObjectName("SR2_billstatus_tableWidget")
        self.SR2_billstatus_tableWidget.setStyleSheet(
            "QTableWidget{\n"
            "\n"
            "	color: rgb(255, 85, 0);\n"
            " \n"
            "}\n"
            "\n"
            "QTableWidget:hover{\n"
            "    font-weight:bold;\n"
            "}\n"
            ""
        )
        self.SR2_billstatus_tableWidget.setFrameShape(QFrame.NoFrame)
        self.SR2_billstatus_tableWidget.setEditTriggers(
            QAbstractItemView.NoEditTriggers
        )
        self.SR2_billstatus_tableWidget.setProperty("showDropIndicator", False)
        self.SR2_billstatus_tableWidget.setDragDropOverwriteMode(False)
        self.SR2_billstatus_tableWidget.setSelectionMode(
            QAbstractItemView.SingleSelection
        )
        self.SR2_billstatus_tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.SR2_billstatus_tableWidget.setShowGrid(True)
        self.SR2_billstatus_tableWidget.setGridStyle(Qt.DotLine)
        self.SR2_billstatus_tableWidget.setSortingEnabled(True)
        self.SR2_billstatus_tableWidget.horizontalHeader().setProperty(
            "showSortIndicator", True
        )

        self.verticalLayout_32.addWidget(self.SR2_billstatus_tableWidget)

        self.verticalLayout_31.addWidget(self.SR2_midpg3)

        self.SR2_downpg3 = QFrame(self.SR2_Billstatus_bg_frame)
        self.SR2_downpg3.setObjectName("SR2_downpg3")
        self.SR2_downpg3.setMinimumSize(QtCore.QSize(0, 40))
        self.SR2_downpg3.setFrameShape(QFrame.NoFrame)
        self.SR2_downpg3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.SR2_downpg3)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 0, 1)
        self.label_3 = QLabel(self.SR2_downpg3)
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.label_3)

        self.SR2_down_ttrows = QLabel(self.SR2_downpg3)
        self.SR2_down_ttrows.setObjectName("SR2_down_ttrows")

        self.horizontalLayout_20.addWidget(self.SR2_down_ttrows)

        self.SR_down_ttresidence = QLabel(self.SR2_downpg3)
        self.SR_down_ttresidence.setObjectName("SR_down_ttresidence")

        self.horizontalLayout_20.addWidget(self.SR_down_ttresidence)

        self.SR2_down_Ttfines = QLabel(self.SR2_downpg3)
        self.SR2_down_Ttfines.setObjectName("SR2_down_Ttfines")

        self.horizontalLayout_20.addWidget(self.SR2_down_Ttfines)

        self.verticalLayout_31.addWidget(self.SR2_downpg3)

        self.verticalLayout_30.addWidget(self.SR2_Billstatus_bg_frame)

        self.SR_stackedWidget.addWidget(self.SR2_billstatus_pg3)
        self.SR2_Default_charges = QWidget()
        self.SR2_Default_charges.setObjectName("SR2_Default_charges")
        self.horizontalLayout_43 = QHBoxLayout(self.SR2_Default_charges)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.Left_view_groupBox_3 = QGroupBox(self.SR2_Default_charges)
        self.Left_view_groupBox_3.setObjectName("Left_view_groupBox_3")
        self.Left_view_groupBox_3.setMaximumSize(QSize(383, 16777215))
        font20 = QFont()
        font20.setFamily("Mongolian Baiti")
        font20.setPointSize(15)
        self.Left_view_groupBox_3.setFont(font20)
        self.Left_view_groupBox_3.setStyleSheet(
            "QGroupBox{color:rgb(255, 255, 0);\n"
            "\n"
            "background-color: rgb(33, 33, 99) ;\n"
            "\n"
            "}"
        )
        self.verticalLayout_33 = QVBoxLayout(self.Left_view_groupBox_3)
        self.verticalLayout_33.setSpacing(1)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(5, 0, 10, 0)
        self.servicel_frame1 = QFrame(self.Left_view_groupBox_3)
        self.servicel_frame1.setObjectName("servicel_frame1")
        self.servicel_frame1.setFrameShape(QFrame.StyledPanel)
        self.servicel_frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.servicel_frame1)
        self.horizontalLayout_21.setSpacing(110)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_1 = QLabel(self.servicel_frame1)
        self.label_1.setObjectName("label_1")
        self.label_1.setStyleSheet("background-color: transparent;")
        self.label_1.setWordWrap(True)

        self.horizontalLayout_21.addWidget(self.label_1)

        self.lineEdit_1 = QLineEdit(self.servicel_frame1)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_1.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEdit_1)

        self.verticalLayout_33.addWidget(self.servicel_frame1)

        self.maintenancel_frame2 = QFrame(self.Left_view_groupBox_3)
        self.maintenancel_frame2.setObjectName("maintenancel_frame2")
        self.maintenancel_frame2.setFrameShape(QFrame.StyledPanel)
        self.maintenancel_frame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.maintenancel_frame2)
        self.horizontalLayout_22.setSpacing(65)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_4 = QLabel(self.maintenancel_frame2)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("background-color: transparent;")
        self.label_4.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(self.maintenancel_frame2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_22.addWidget(self.lineEdit_2)

        self.verticalLayout_33.addWidget(self.maintenancel_frame2)

        self.waterl_frame3 = QFrame(self.Left_view_groupBox_3)
        self.waterl_frame3.setObjectName("waterl_frame3")
        self.waterl_frame3.setFrameShape(QFrame.StyledPanel)
        self.waterl_frame3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.waterl_frame3)
        self.horizontalLayout_23.setSpacing(119)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_5 = QLabel(self.waterl_frame3)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("background-color: transparent;")
        self.label_5.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(self.waterl_frame3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_23.addWidget(self.lineEdit_3)

        self.verticalLayout_33.addWidget(self.waterl_frame3)

        self.sinkingl_frame4 = QFrame(self.Left_view_groupBox_3)
        self.sinkingl_frame4.setObjectName("sinkingl_frame4")
        self.sinkingl_frame4.setFrameShape(QFrame.StyledPanel)
        self.sinkingl_frame4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.sinkingl_frame4)
        self.horizontalLayout_24.setSpacing(110)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_6 = QLabel(self.sinkingl_frame4)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("background-color: transparent;")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.sinkingl_frame4)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_24.addWidget(self.lineEdit_4)

        self.verticalLayout_33.addWidget(self.sinkingl_frame4)

        self.repairl_frame5 = QFrame(self.Left_view_groupBox_3)
        self.repairl_frame5.setObjectName("repairl_frame5")
        self.repairl_frame5.setFrameShape(QFrame.StyledPanel)
        self.repairl_frame5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.repairl_frame5)
        self.horizontalLayout_25.setSpacing(118)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_7 = QLabel(self.repairl_frame5)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("background-color: transparent;")
        self.label_7.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.label_7)

        self.lineEdit_5 = QLineEdit(self.repairl_frame5)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.lineEdit_5)

        self.verticalLayout_33.addWidget(self.repairl_frame5)

        self.festivall_frame6 = QFrame(self.Left_view_groupBox_3)
        self.festivall_frame6.setObjectName("festivall_frame6")
        self.festivall_frame6.setFrameShape(QFrame.StyledPanel)
        self.festivall_frame6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.festivall_frame6)
        self.horizontalLayout_26.setSpacing(110)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_8 = QLabel(self.festivall_frame6)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("background-color: transparent;")
        self.label_8.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.label_8)

        self.lineEdit_6 = QLineEdit(self.festivall_frame6)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_6.setReadOnly(True)

        self.horizontalLayout_26.addWidget(self.lineEdit_6)

        self.verticalLayout_33.addWidget(self.festivall_frame6)

        self.clubhousel_frame7 = QFrame(self.Left_view_groupBox_3)
        self.clubhousel_frame7.setObjectName("clubhousel_frame7")
        self.clubhousel_frame7.setFrameShape(QFrame.StyledPanel)
        self.clubhousel_frame7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.clubhousel_frame7)
        self.horizontalLayout_27.setSpacing(81)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_9 = QLabel(self.clubhousel_frame7)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("background-color: transparent;")
        self.label_9.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_9)

        self.lineEdit_7 = QLineEdit(self.clubhousel_frame7)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_7.setReadOnly(True)

        self.horizontalLayout_27.addWidget(self.lineEdit_7)

        self.verticalLayout_33.addWidget(self.clubhousel_frame7)

        self.finel_frame8 = QFrame(self.Left_view_groupBox_3)
        self.finel_frame8.setObjectName("finel_frame8")
        self.finel_frame8.setFrameShape(QFrame.StyledPanel)
        self.finel_frame8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.finel_frame8)
        self.horizontalLayout_28.setSpacing(138)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_10 = QLabel(self.finel_frame8)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("background-color: transparent;")
        self.label_10.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.finel_frame8)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_8.setReadOnly(True)

        self.horizontalLayout_28.addWidget(self.lineEdit_8)

        self.verticalLayout_33.addWidget(self.finel_frame8)

        self.parkingl_frame9 = QFrame(self.Left_view_groupBox_3)
        self.parkingl_frame9.setObjectName("parkingl_frame9")
        self.parkingl_frame9.setFrameShape(QFrame.StyledPanel)
        self.parkingl_frame9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.parkingl_frame9)
        self.horizontalLayout_29.setSpacing(110)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_11 = QLabel(self.parkingl_frame9)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("background-color: transparent;")
        self.label_11.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.label_11)

        self.lineEdit_9 = QLineEdit(self.parkingl_frame9)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_9.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.lineEdit_9)

        self.verticalLayout_33.addWidget(self.parkingl_frame9)

        self.totall_frame10 = QFrame(self.Left_view_groupBox_3)
        self.totall_frame10.setObjectName("totall_frame10")
        self.totall_frame10.setFrameShape(QFrame.StyledPanel)
        self.totall_frame10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.totall_frame10)
        self.horizontalLayout_30.setSpacing(70)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_12 = QLabel(self.totall_frame10)
        self.label_12.setObjectName("label_12")
        self.label_12.setStyleSheet("background-color: transparent;")
        self.label_12.setWordWrap(True)

        self.horizontalLayout_30.addWidget(self.label_12)

        self.lineEdit_10 = QLineEdit(self.totall_frame10)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setInputMethodHints(Qt.ImhDigitsOnly)
        self.lineEdit_10.setMaxLength(5)
        self.lineEdit_10.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.lineEdit_10)

        self.verticalLayout_33.addWidget(self.totall_frame10)

        self.Updatel_frame11 = QFrame(self.Left_view_groupBox_3)
        self.Updatel_frame11.setObjectName("Updatel_frame11")
        self.Updatel_frame11.setFrameShape(QFrame.StyledPanel)
        self.Updatel_frame11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.Updatel_frame11)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_13 = QLabel(self.Updatel_frame11)
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("background-color: transparent;")
        self.label_13.setWordWrap(True)

        self.horizontalLayout_31.addWidget(self.label_13)

        self.updatebtnpushButton_2 = QPushButton(self.Updatel_frame11)
        self.updatebtnpushButton_2.setObjectName("updatebtnpushButton_2")
        font21 = QFont()
        font21.setFamily("Segoe Print")
        font21.setPointSize(11)
        self.updatebtnpushButton_2.setFont(font21)

        self.horizontalLayout_31.addWidget(self.updatebtnpushButton_2)

        self.verticalLayout_33.addWidget(self.Updatel_frame11)

        self.horizontalLayout_43.addWidget(self.Left_view_groupBox_3)

        self.Right_update_groupBox_4 = QGroupBox(self.SR2_Default_charges)
        self.Right_update_groupBox_4.setObjectName("Right_update_groupBox_4")
        self.Right_update_groupBox_4.setMaximumSize(QSize(383, 16777215))
        self.Right_update_groupBox_4.setFont(font20)
        self.Right_update_groupBox_4.setStyleSheet(
            "QGroupBox{color:rgb(255, 255, 0);\n"
            "\n"
            "background-color: rgb(33, 33, 99) ;\n"
            "\n"
            "}"
        )
        self.verticalLayout_34 = QVBoxLayout(self.Right_update_groupBox_4)
        self.verticalLayout_34.setSpacing(1)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, 0, 10, 0)
        self.servicer_frame1 = QFrame(self.Right_update_groupBox_4)
        self.servicer_frame1.setObjectName("servicer_frame1")
        self.servicer_frame1.setFrameShape(QFrame.StyledPanel)
        self.servicer_frame1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.servicer_frame1)
        self.horizontalLayout_32.setSpacing(120)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_14 = QLabel(self.servicer_frame1)
        self.label_14.setObjectName("label_14")
        self.label_14.setStyleSheet("background-color: transparent;")
        self.label_14.setWordWrap(True)

        self.horizontalLayout_32.addWidget(self.label_14)

        self.lineEdit_31 = QLineEdit(self.servicer_frame1)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.lineEdit_31.setMaxLength(6)
        self.lineEdit_31.setReadOnly(False)
        self.horizontalLayout_32.addWidget(self.lineEdit_31)
        self.verticalLayout_34.addWidget(self.servicer_frame1)

        self.maintenancer_frame2 = QFrame(self.Right_update_groupBox_4)
        self.maintenancer_frame2.setObjectName("maintenancer_frame2")
        self.maintenancer_frame2.setFrameShape(QFrame.StyledPanel)
        self.maintenancer_frame2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.maintenancer_frame2)
        self.horizontalLayout_33.setSpacing(76)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.label_15 = QLabel(self.maintenancer_frame2)
        self.label_15.setObjectName("label_15")
        self.label_15.setStyleSheet("background-color: transparent;")
        self.label_15.setWordWrap(True)

        self.horizontalLayout_33.addWidget(self.label_15)

        self.lineEdit_32 = QLineEdit(self.maintenancer_frame2)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_32.setMaxLength(6)
        self.lineEdit_32.setReadOnly(False)

        self.horizontalLayout_33.addWidget(self.lineEdit_32)

        self.verticalLayout_34.addWidget(self.maintenancer_frame2)

        self.waterr_frame3 = QFrame(self.Right_update_groupBox_4)
        self.waterr_frame3.setObjectName("waterr_frame3")
        self.waterr_frame3.setFrameShape(QFrame.StyledPanel)
        self.waterr_frame3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.waterr_frame3)
        self.horizontalLayout_34.setSpacing(130)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.label_16 = QLabel(self.waterr_frame3)
        self.label_16.setObjectName("label_16")
        self.label_16.setStyleSheet("background-color: transparent;")
        self.label_16.setWordWrap(True)

        self.horizontalLayout_34.addWidget(self.label_16)

        self.lineEdit_33 = QLineEdit(self.waterr_frame3)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_33.setMaxLength(6)
        self.lineEdit_33.setReadOnly(False)

        self.horizontalLayout_34.addWidget(self.lineEdit_33)

        self.verticalLayout_34.addWidget(self.waterr_frame3)

        self.sinkingr_frame4 = QFrame(self.Right_update_groupBox_4)
        self.sinkingr_frame4.setObjectName("sinkingr_frame4")
        self.sinkingr_frame4.setFrameShape(QFrame.StyledPanel)
        self.sinkingr_frame4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.sinkingr_frame4)
        self.horizontalLayout_35.setSpacing(120)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.label_17 = QLabel(self.sinkingr_frame4)
        self.label_17.setObjectName("label_17")
        self.label_17.setStyleSheet("background-color: transparent;")
        self.label_17.setWordWrap(True)

        self.horizontalLayout_35.addWidget(self.label_17)

        self.lineEdit_34 = QLineEdit(self.sinkingr_frame4)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_34.setMaxLength(6)
        self.lineEdit_34.setReadOnly(False)

        self.horizontalLayout_35.addWidget(self.lineEdit_34)

        self.verticalLayout_34.addWidget(self.sinkingr_frame4)

        self.repairr_frame5 = QFrame(self.Right_update_groupBox_4)
        self.repairr_frame5.setObjectName("repairr_frame5")
        self.repairr_frame5.setFrameShape(QFrame.StyledPanel)
        self.repairr_frame5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.repairr_frame5)
        self.horizontalLayout_36.setSpacing(126)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_18 = QLabel(self.repairr_frame5)
        self.label_18.setObjectName("label_18")
        self.label_18.setStyleSheet("background-color: transparent;")
        self.label_18.setWordWrap(True)

        self.horizontalLayout_36.addWidget(self.label_18)

        self.lineEdit_35 = QLineEdit(self.repairr_frame5)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_35.setMaxLength(6)

        self.horizontalLayout_36.addWidget(self.lineEdit_35)

        self.verticalLayout_34.addWidget(self.repairr_frame5)

        self.festivalr_frame6 = QFrame(self.Right_update_groupBox_4)
        self.festivalr_frame6.setObjectName("festivalr_frame6")
        self.festivalr_frame6.setFrameShape(QFrame.StyledPanel)
        self.festivalr_frame6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.festivalr_frame6)
        self.horizontalLayout_37.setSpacing(116)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_19 = QLabel(self.festivalr_frame6)
        self.label_19.setObjectName("label_19")
        self.label_19.setStyleSheet("background-color: transparent;")
        self.label_19.setWordWrap(True)

        self.horizontalLayout_37.addWidget(self.label_19)

        self.lineEdit_36 = QLineEdit(self.festivalr_frame6)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_36.setMaxLength(6)
        self.lineEdit_36.setReadOnly(False)

        self.horizontalLayout_37.addWidget(self.lineEdit_36)

        self.verticalLayout_34.addWidget(self.festivalr_frame6)

        self.clubhouser_frame7 = QFrame(self.Right_update_groupBox_4)
        self.clubhouser_frame7.setObjectName("clubhouser_frame7")
        self.clubhouser_frame7.setFrameShape(QFrame.StyledPanel)
        self.clubhouser_frame7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.clubhouser_frame7)
        self.horizontalLayout_38.setSpacing(89)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_20 = QLabel(self.clubhouser_frame7)
        self.label_20.setObjectName("label_20")
        self.label_20.setStyleSheet("background-color: transparent;")
        self.label_20.setWordWrap(True)

        self.horizontalLayout_38.addWidget(self.label_20)

        self.lineEdit_37 = QLineEdit(self.clubhouser_frame7)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_37.setMaxLength(6)
        self.lineEdit_37.setReadOnly(False)

        self.horizontalLayout_38.addWidget(self.lineEdit_37)

        self.verticalLayout_34.addWidget(self.clubhouser_frame7)

        self.finer_frame8 = QFrame(self.Right_update_groupBox_4)
        self.finer_frame8.setObjectName("finer_frame8")
        self.finer_frame8.setFrameShape(QFrame.StyledPanel)
        self.finer_frame8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.finer_frame8)
        self.horizontalLayout_39.setSpacing(145)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_21 = QLabel(self.finer_frame8)
        self.label_21.setObjectName("label_21")
        self.label_21.setStyleSheet("background-color: transparent;")
        self.label_21.setWordWrap(True)

        self.horizontalLayout_39.addWidget(self.label_21)

        self.lineEdit_38 = QLineEdit(self.finer_frame8)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_38.setMaxLength(6)

        self.horizontalLayout_39.addWidget(self.lineEdit_38)

        self.verticalLayout_34.addWidget(self.finer_frame8)

        self.parkingr_frame9 = QFrame(self.Right_update_groupBox_4)
        self.parkingr_frame9.setObjectName("parkingr_frame9")
        self.parkingr_frame9.setFrameShape(QFrame.StyledPanel)
        self.parkingr_frame9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.parkingr_frame9)
        self.horizontalLayout_40.setSpacing(115)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_22 = QLabel(self.parkingr_frame9)
        self.label_22.setObjectName("label_22")
        self.label_22.setStyleSheet("background-color: transparent;")
        self.label_22.setWordWrap(True)

        self.horizontalLayout_40.addWidget(self.label_22)

        self.lineEdit_39 = QLineEdit(self.parkingr_frame9)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_39.setMaxLength(6)
        self.lineEdit_39.setReadOnly(False)

        self.horizontalLayout_40.addWidget(self.lineEdit_39)

        self.verticalLayout_34.addWidget(self.parkingr_frame9)

        self.totalr_frame10 = QFrame(self.Right_update_groupBox_4)
        self.totalr_frame10.setObjectName("totalr_frame10")
        self.totalr_frame10.setFrameShape(QFrame.StyledPanel)
        self.totalr_frame10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.totalr_frame10)
        self.horizontalLayout_41.setSpacing(75)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_23 = QLabel(self.totalr_frame10)
        self.label_23.setObjectName("label_23")
        self.label_23.setStyleSheet("background-color: transparent;")
        self.label_23.setWordWrap(True)

        self.horizontalLayout_41.addWidget(self.label_23)

        self.lineEdit_40 = QLineEdit(self.totalr_frame10)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_40.setMaxLength(6)
        self.lineEdit_40.setReadOnly(False)

        self.horizontalLayout_41.addWidget(self.lineEdit_40)

        self.verticalLayout_34.addWidget(self.totalr_frame10)

        self.Updater_frame11 = QFrame(self.Right_update_groupBox_4)
        self.Updater_frame11.setObjectName("Updater_frame11")
        self.Updater_frame11.setFrameShape(QFrame.StyledPanel)
        self.Updater_frame11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.Updater_frame11)
        self.horizontalLayout_42.setObjectName("horizontalLayout_42")
        self.label_24 = QLabel(self.Updater_frame11)
        self.label_24.setObjectName("label_24")
        self.label_24.setStyleSheet("background-color: transparent;")
        self.label_24.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_24)

        self.setbtpushButton_3 = QPushButton(self.Updater_frame11)
        self.setbtpushButton_3.setObjectName("setbtpushButton_3")
        self.setbtpushButton_3.setFont(font21)

        self.horizontalLayout_42.addWidget(self.setbtpushButton_3)

        self.verticalLayout_34.addWidget(self.Updater_frame11)

        self.horizontalLayout_43.addWidget(self.Right_update_groupBox_4)

        self.SR_stackedWidget.addWidget(self.SR2_Default_charges)

        self.SR2_addupdate_pg5 = QWidget()
        self.SR2_addupdate_pg5.setObjectName("SR2_addupdate_pg5")
        self.horizontalLayout_44 = QHBoxLayout(self.SR2_addupdate_pg5)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.SR2_addup_Bgframe_4 = QFrame(self.SR2_addupdate_pg5)
        self.SR2_addup_Bgframe_4.setObjectName("SR2_addup_Bgframe_4")
        self.SR2_addup_Bgframe_4.setFrameShape(QFrame.NoFrame)
        self.SR2_addup_Bgframe_4.setFrameShadow(QFrame.Raised)
        self.SR2_addup_top_frame_5 = QFrame(self.SR2_addup_Bgframe_4)
        self.SR2_addup_top_frame_5.setObjectName("SR2_addup_top_frame_5")
        self.SR2_addup_top_frame_5.setGeometry(QRect(11, 11, 671, 45))
        self.SR2_addup_top_frame_5.setFrameShape(QFrame.NoFrame)
        self.SR2_addup_top_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.SR2_addup_top_frame_5)
        self.horizontalLayout_46.setSpacing(40)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 215, 0)
        self.SR_addup_search_lineEdit = QLineEdit(self.SR2_addup_top_frame_5)
        self.SR_addup_search_lineEdit.setObjectName("SR_addup_search_lineEdit")
        self.SR_addup_search_lineEdit.setMaximumSize(QSize(260, 35))
        font22 = QFont()
        font22.setPointSize(14)
        self.SR_addup_search_lineEdit.setFont(font22)
        self.SR_addup_search_lineEdit.setStyleSheet(
            "QLineEdit{	\n"
            "	color: rgb(85, 170, 255);\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}\n"
            "\n"
            "QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.SR_addup_search_lineEdit.setMaxLength(5)

        self.horizontalLayout_46.addWidget(self.SR_addup_search_lineEdit)

        self.SR2_addup_searchpushButton = QPushButton(self.SR2_addup_top_frame_5)
        self.SR2_addup_searchpushButton.setObjectName("SR2_addup_searchpushButton")
        self.SR2_addup_searchpushButton.setMaximumSize(QSize(150, 35))
        font23 = QFont()
        font23.setPointSize(17)
        self.SR2_addup_searchpushButton.setFont(font23)
        self.SR2_addup_searchpushButton.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(85, 255, 0);\n"
            "     border:1px Solid none;\n"
            "	border-radius:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	border-color: rgb(0, 0, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "font-weight:Bold;\n"
            "	border-color: rgb(85, 255, 127);\n"
            "\n"
            "}"
        )

        self.horizontalLayout_46.addWidget(self.SR2_addup_searchpushButton)

        self.SR2_addup_man_frame_7 = QFrame(self.SR2_addup_Bgframe_4)
        self.SR2_addup_man_frame_7.setObjectName("SR2_addup_man_frame_7")
        self.SR2_addup_man_frame_7.setGeometry(QRect(10, 70, 1000, 1000000))
        self.SR2_addup_man_frame_7.setMinimumSize(QSize(1000, 1000000))
        self.SR2_addup_man_frame_7.setFrameShape(QFrame.NoFrame)
        self.SR2_addup_man_frame_7.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.SR2_addup_man_frame_7)
        self.frame_8.setObjectName("frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 681, 45))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_45.setSpacing(5)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName("label_25")

        self.horizontalLayout_45.addWidget(self.label_25)

        self.SR2_main_genratelineEdit_2 = QLineEdit(self.frame_8)
        self.SR2_main_genratelineEdit_2.setObjectName("SR2_main_genratelineEdit_2")
        self.SR2_main_genratelineEdit_2.setMaximumSize(QSize(16777215, 30))
        font24 = QFont()
        font24.setPointSize(11)
        self.SR2_main_genratelineEdit_2.setFont(font24)
        self.SR2_main_genratelineEdit_2.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.SR2_main_genratelineEdit_2.setReadOnly(True)

        self.horizontalLayout_45.addWidget(self.SR2_main_genratelineEdit_2)

        self.SR2_main_generatepushButton_5 = QPushButton(self.frame_8)
        self.SR2_main_generatepushButton_5.setObjectName(
            "SR2_main_generatepushButton_5"
        )
        self.SR2_main_generatepushButton_5.setMinimumSize(QSize(96, 35))
        self.SR2_main_generatepushButton_5.setFont(font21)
        self.SR2_main_generatepushButton_5.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(85, 255, 0);\n"
            "     border:1px Solid none;\n"
            "	border-radius:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	border-color: rgb(0, 0, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "font-weight:Bold;\n"
            "	border-color: rgb(85, 255, 127);\n"
            "\n"
            "}"
        )

        self.horizontalLayout_45.addWidget(self.SR2_main_generatepushButton_5)

        self.SR2_admin_radioButton = QRadioButton(self.frame_8)
        self.SR2_admin_radioButton.setObjectName("SR2_admin_radioButton")
        self.SR2_admin_radioButton.setMaximumSize(QSize(182, 16777215))
        font25 = QFont()
        font25.setPointSize(11)
        font25.setBold(True)
        font25.setWeight(75)
        self.SR2_admin_radioButton.setFont(font25)
        self.SR2_admin_radioButton.setStyleSheet(
            "QRadioButton{\n" "\n" "	color: rgb(85, 255, 127);\n" "}"
        )

        self.horizontalLayout_45.addWidget(self.SR2_admin_radioButton)

        self.gridLayoutWidget = QWidget(self.SR2_addup_man_frame_7)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 50, 671, 381))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.SR2_Email_lineEdit_6 = QLineEdit(self.gridLayoutWidget)
        self.SR2_Email_lineEdit_6.setObjectName("SR2_Email_lineEdit_6")
        self.SR2_Email_lineEdit_6.setMinimumSize(QSize(0, 30))
        font26 = QFont()
        font26.setPointSize(10)
        self.SR2_Email_lineEdit_6.setFont(font26)
        self.SR2_Email_lineEdit_6.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.SR2_Email_lineEdit_6.setMaxLength(20)

        self.gridLayout.addWidget(self.SR2_Email_lineEdit_6, 4, 1, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget)
        self.label_36.setObjectName("label_36")

        self.gridLayout.addWidget(self.label_36, 0, 0, 1, 1)

        self.nameLabel = QLabel(self.gridLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setFont(font18)

        self.gridLayout.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.nameLineEdit = QLineEdit(self.gridLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLineEdit.setMinimumSize(QSize(0, 30))
        self.nameLineEdit.setFont(font24)
        self.nameLineEdit.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.nameLineEdit.setMaxLength(20)

        self.gridLayout.addWidget(self.nameLineEdit, 1, 1, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName("label_34")

        self.gridLayout.addWidget(self.label_34, 6, 0, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName("label_31")

        self.gridLayout.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")

        self.gridLayout.addWidget(self.label_32, 4, 0, 1, 1)

        self.SR2_vhiclecount_spinBox = QSpinBox(self.gridLayoutWidget)
        self.SR2_vhiclecount_spinBox.setObjectName("SR2_vhiclecount_spinBox")
        self.SR2_vhiclecount_spinBox.setMinimumSize(QSize(0, 30))
        self.SR2_vhiclecount_spinBox.setFont(font26)
        self.SR2_vhiclecount_spinBox.setStyleSheet(
            "QSpinBox{\n"
            "\n"
            "	background-color: rgb(0,0,0);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	color: rgb(255, 255, 0);\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QListView{color:rgb(255, 255, 127);}\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "QSpinBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QSpinBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.SR2_vhiclecount_spinBox.setSingleStep(1)
        self.SR2_vhiclecount_spinBox.setValue(0)
        self.SR2_vhiclecount_spinBox.setPrefix("   ")
        self.gridLayout.addWidget(self.SR2_vhiclecount_spinBox, 7, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName("label_35")

        self.gridLayout.addWidget(self.label_35, 7, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName("label_33")

        self.gridLayout.addWidget(self.label_33, 5, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")

        self.gridLayout.addWidget(self.label_30, 2, 0, 1, 1)

        self.surname_lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.surname_lineEdit_4.setObjectName("surname_lineEdit_4")
        self.surname_lineEdit_4.setMinimumSize(QSize(0, 30))
        self.surname_lineEdit_4.setFont(font15)
        self.surname_lineEdit_4.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.surname_lineEdit_4.setMaxLength(20)

        self.gridLayout.addWidget(self.surname_lineEdit_4, 1, 2, 1, 1)

        self.SR2_Roomno_comboBox_2 = QLineEdit(self.gridLayoutWidget)
        self.SR2_Roomno_comboBox_2.setObjectName("SR2_Roomno_comboBox_2")
        self.SR2_Roomno_comboBox_2.setMinimumSize(QSize(0, 35))
        self.SR2_Roomno_comboBox_2.setFont(font24)
        self.SR2_Roomno_comboBox_2.setMaxLength(6)
        self.SR2_Roomno_comboBox_2.setStyleSheet(
            "QLineEdit{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "    border:1px solid white;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "QLineEdit:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QComboBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        self.SR2_Roomno_comboBox_2.setPlaceholderText("   Room no.")

        self.gridLayout.addWidget(self.SR2_Roomno_comboBox_2, 2, 1, 1, 1)

        self.Flattype_comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.Flattype_comboBox_3.addItem("")
        self.Flattype_comboBox_3.addItem("")
        self.Flattype_comboBox_3.setObjectName("Flattype_comboBox_3")
        self.Flattype_comboBox_3.setMinimumSize(QSize(0, 35))
        self.Flattype_comboBox_3.setFont(font24)
        self.Flattype_comboBox_3.setCurrentIndex(-1)
        self.Flattype_comboBox_3.setStyleSheet(
            "QComboBox{\n"
            "\n"
            "	background-color: rgb(0,0,0);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QListView{color:rgb(255, 255, 127);}\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QComboBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )

        self.gridLayout.addWidget(self.Flattype_comboBox_3, 6, 1, 1, 1)

        self.SR2_flatarea_lineEdit_7 = QLineEdit(self.gridLayoutWidget)
        self.SR2_flatarea_lineEdit_7.setObjectName("SR2_flatarea_lineEdit_7")
        self.SR2_flatarea_lineEdit_7.setMinimumSize(QSize(0, 30))
        self.SR2_flatarea_lineEdit_7.setFont(font26)
        self.SR2_flatarea_lineEdit_7.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.SR2_flatarea_lineEdit_7.setMaxLength(4)

        self.gridLayout.addWidget(self.SR2_flatarea_lineEdit_7, 5, 1, 1, 1)

        self.Sr2_Phone_lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.Sr2_Phone_lineEdit_5.setObjectName("Sr2_Phone_lineEdit_5")
        self.Sr2_Phone_lineEdit_5.setMinimumSize(QSize(0, 30))
        self.Sr2_Phone_lineEdit_5.setFont(font26)
        self.Sr2_Phone_lineEdit_5.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.Sr2_Phone_lineEdit_5.setMaxLength(10)

        self.gridLayout.addWidget(self.Sr2_Phone_lineEdit_5, 3, 1, 1, 1)

        self.SR2_autoBillid_lineEdit_9 = QLineEdit(self.gridLayoutWidget)
        self.SR2_autoBillid_lineEdit_9.setObjectName("SR2_autoBillid_lineEdit_9")
        self.SR2_autoBillid_lineEdit_9.setMinimumSize(QSize(0, 30))
        self.SR2_autoBillid_lineEdit_9.setMaximumSize(QSize(16777215, 30))
        self.SR2_autoBillid_lineEdit_9.setFont(font24)
        self.SR2_autoBillid_lineEdit_9.setStyleSheet(
            "QLineEdit{	\n"
            "	color: white;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "   border : 1px solid none;\n"
            "   border-radius:10px;\n"
            "}QLineEdit:hover{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	border-color: rgb(0, 255, 0);\n"
            "}"
        )
        self.SR2_autoBillid_lineEdit_9.setMaxLength(7)
        self.SR2_autoBillid_lineEdit_9.setReadOnly(True)

        self.gridLayout.addWidget(self.SR2_autoBillid_lineEdit_9, 0, 1, 1, 1)

        self.SR2_wing_comboBox_4 = QComboBox(self.gridLayoutWidget)
        self.SR2_wing_comboBox_4.setObjectName("SR2_wing_comboBox_4")
        self.SR2_wing_comboBox_4.setMinimumSize(QSize(0, 35))
        self.SR2_wing_comboBox_4.setFont(font24)
        self.SR2_wing_comboBox_4.setCurrentIndex(-1)
        self.SR2_wing_comboBox_4.setStyleSheet(
            "QComboBox{\n"
            "\n"
            "	background-color: rgb(0,0,0);\n"
            "    border:1px solid none;\n"
            "    border-radius:10px;\n"
            "	\n"
            "	color: rgb(255, 255, 0);\n"
            "    border-color: rgb(0, 0,0);\n"
            "	\n"
            "}\n"
            "QListView{color:rgb(255, 255, 127);}\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "QComboBox:hover {\n"
            "    border:1px solid rgb(4, 194, 58);\n"
            "	color:rgb(103, 255, 2);\n"
            "\n"
            "}\n"
            "QComboBox:pressed{\n"
            "  \n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(255, 255, 255);\n"
            "}"
        )
        # self.SR2_wing_comboBox_4.setCurrentText(u"   Wing")

        self.gridLayout.addWidget(self.SR2_wing_comboBox_4, 2, 2, 1, 1)

        self.SR2_deletemem_pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.SR2_deletemem_pushButton_4.setObjectName("SR2_deletemem_pushButton_4")
        self.SR2_deletemem_pushButton_4.setMinimumSize(QSize(130, 35))
        self.SR2_deletemem_pushButton_4.setFont(font15)
        icon6 = QIcon()
        icon6.addFile(
            "image/icons/del_mem.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SR2_deletemem_pushButton_4.setIcon(icon6)
        self.SR2_deletemem_pushButton_4.setIconSize(QtCore.QSize(25, 20))
        self.SR2_deletemem_pushButton_4.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(85, 255, 0);\n"
            "     border:1px Solid none;\n"
            "	border-radius:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	border-color: rgb(0, 0, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "font-weight:Bold;\n"
            "	border-color: rgb(85, 255, 127);\n"
            "\n"
            "}"
        )

        self.gridLayout.addWidget(self.SR2_deletemem_pushButton_4, 7, 3, 1, 1)

        self.SR2_updatemem_pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.SR2_updatemem_pushButton_2.setObjectName("SR2_updatemem_pushButton_2")
        self.SR2_updatemem_pushButton_2.setMinimumSize(QSize(130, 35))
        self.SR2_updatemem_pushButton_2.setFont(font24)
        icon5 = QIcon()
        icon5.addFile(
            "image/icons/update_logo.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SR2_updatemem_pushButton_2.setIcon(icon5)
        self.SR2_updatemem_pushButton_2.setIconSize(QtCore.QSize(25, 20))
        self.SR2_updatemem_pushButton_2.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(85, 255, 0);\n"
            "     border:1px Solid none;\n"
            "	border-radius:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	border-color: rgb(0, 0, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "font-weight:Bold;\n"
            "	border-color: rgb(85, 255, 127);\n"
            "\n"
            "}"
        )

        self.gridLayout.addWidget(self.SR2_updatemem_pushButton_2, 6, 3, 1, 1)

        self.SR2_addmem_pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.SR2_addmem_pushButton_3.setObjectName("SR2_addmem_pushButton_3")
        self.SR2_addmem_pushButton_3.setMinimumSize(QSize(130, 35))
        self.SR2_addmem_pushButton_3.setFont(font15)
        icon4 = QIcon()
        icon4.addFile(
            "image/icons/add_mem.png", QtCore.QSize(), QIcon.Normal, QIcon.Off
        )
        self.SR2_addmem_pushButton_3.setIcon(icon4)
        self.SR2_addmem_pushButton_3.setIconSize(QtCore.QSize(16, 16))
        self.SR2_addmem_pushButton_3.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(0, 0, 0);\n"
            "	color: rgb(85, 255, 0);\n"
            "     border:1px Solid none;\n"
            "	border-radius:10px;\n"
            "\n"
            "}\n"
            "QPushButton:hover{\n"
            "	\n"
            "	border-color: rgb(0, 0, 255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "font-weight:Bold;\n"
            "	border-color: rgb(85, 255, 127);\n"
            "\n"
            "}"
        )

        self.gridLayout.addWidget(self.SR2_addmem_pushButton_3, 5, 3, 1, 1)

        self.horizontalLayout_44.addWidget(self.SR2_addup_Bgframe_4)

        self.SR_stackedWidget.addWidget(self.SR2_addupdate_pg5)
        self.verticalLayout_22.addWidget(self.SR_stackedWidget)
        self.verticalLayout_19.addWidget(self.S_R2)

        self.horizontalLayout_3.addWidget(self.S_frame_right)

        self.verticalLayout_13.addWidget(self.S_frame_bg)

        self.Society_BILLMaintenance.addWidget(self.Society_Page)

        self.verticalLayout.addWidget(self.Society_BILLMaintenance)

        Society_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Society_MainWindow)

        self.Society_BILLMaintenance.setCurrentIndex(0)
        self.Login_stackedWidget.setCurrentIndex(1)
        self.SR_stackedWidget.setCurrentIndex(0)
        # home =1 ;SR2_billrelease_p2=2;SR2_billrelease_p2=3

    # setupUi
    def retranslateUi(self, Society_MainWindow):
        Society_MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "Society_MainWindow", "Society Maintenance Bill Management", None
            )
        )
        # if QT_CONFIG(whatsthis)
        # endif // QT_CONFIG(whatsthis)
        self.user_txt1.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-weight:600; color:#1ab911;">Only </span></p><p align="center"><span style=" font-weight:600; color:#1ab911;">Admin</span></p></body></html>',
                None,
            )
        )
        # if QT_CONFIG(whatsthis)
        # endif // QT_CONFIG(whatsthis)
        self.Login_btn.setText(
            QCoreApplication.translate(
                "Society_MainWindow", "Login /\n" "SignIn  ", None
            )
        )
        self.Forgot_pswdbtn.setText(
            QCoreApplication.translate(
                "Society_MainWindow", "Forgot\n" "Password", None
            )
        )
        self.Exit_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Exit", None)
        )
        self.Error_Label.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600; color:#ffffff;">Error : </span></p></body></html>',
                None,
            )
        )
        self.Error_Close_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "X", None)
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Society_MainWindow", "Reset Password", None)
        )
        self.forgot_usermail_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "* UserName / Email", None)
        )
        self.Forgot_whatsapp_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "* WhatsApp No.", None)
        )
        self.comboBox.setPlaceholderText(
            QCoreApplication.translate(
                "Society_MainWindow", "Choose Question from list", None
            )
        )
        self.Forgot_ans_lineEdit.setText("")
        self.Forgot_ans_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "* Answer", None)
        )

        self.Forgot_confirm_Button.setText(
            QCoreApplication.translate("Society_MainWindow", "Check", None)
        )
        self.Password_show_lb.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; font-weight:600; font-style:italic; color:#2f94ff;">Your password : </span></p></body></html>',
                None,
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Society_MainWindow", "Login", None)
        )
        self.Login_title.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe Print'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><img src="image\icons/bloquear.png" /><br /><span style=" font-family:\'MS Shell Dlg 2\'; font-size:26pt; font-weight:600; color:#e5ef20;">Society Maintenance Bill Managment</span></p></body></html>',
                None,
            )
        )

        self.Login_user_name.setText("")
        self.Login_user_password.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "Password", None)
        )
        self.Login_admin_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Login", None)
        )
        self.user_img2.setText("")
        self.user_txt2.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-weight:600; color:#f9f21c;">Admin :</span></p></body></html>',
                None,
            )
        )
        self.SL1_home_btn.setText("")
        self.SL1_Upaidbill_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Unpaid\n" "bills", None)
        )
        self.SL1_dcharges_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Charges", None)
        )
        self.SL1_pdfbills_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "pdfs", None)
        )
        self.wall_art.setText("")
        self.SL2_whatsapp_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Send\nWarning.", None)
        )
        self.SL2_Report_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Report", None)
        )
        self.SL2_Setting_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Setting", None)
        )
        self.SL2_logout_btn.setText("")
        self.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">Welcome admin ...</span></p></body></html>',
                None,
            )
        )
        self.Date_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:11pt; font-weight:600; color:#c8ee3e;">Today\'s Date:</span></p></body></html>',
                None,
            )
        )
        self.NewMonth_lb.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#5555ff;">New month Bill</span></p><p align="center"><span style=" font-size:9pt; color:#8c8c8c;">This module help for generating new bill every new month ,by default new month start on 1st day of each month.</span><span style=" color:#8c8c8c;">(can be change in settings)</span><span style=" font-size:9pt; color:#787878;"><br/></span></p></body></html>',
                None,
            )
        )
        self.NewMonth_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Release bill", None)
        )
        self.Billstatus_lb.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#5555ff;">Bill status</span></p><p align="center"><span style=" font-size:9pt; color:#8a8a8a;">This module help update paid bills and give view about recent bills or any specific month bill released either paid or not.</span></p></body></html>',
                None,
            )
        )
        self.Billstatus_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "View Status", None)
        )
        self.Conwebwhatsapp_lb.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#5555ff;">New month Bill</span></p><p align="center"><span style=" font-size:9pt; color:#8c8c8c;">This module help to connect and start your web whatsapp with admin whatsapp.</span></p><p align="center"><span style=" font-size:9pt; color:#8c8c8c;">(whatsap used to share bill should be active in phone also)</span></p></body></html>',
                None,
            )
        )
        self.Conwebwhatsapp_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "web-whatsapp", None)
        )
        self.updatinfo_lb.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#5555ff;">Add / Update info.</span></p><p align="center"><span style=" font-size:9pt; color:#8c8c8c;">This module help for adding or updating information about any society member or admin for this applicaton.<br/></span></p></body></html>',
                None,
            )
        )
        self.updatinfo_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Add/Update", None)
        )
        self.Resident_subtitle_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#00ff7f;">BILL Generation and Release BILL</span></p><p><span style=" font-size:10pt; font-weight:600; text-decoration: underline; color:#ffff7f;">Residence list</span></p></body></html>',
                None,
            )
        )
        self.New_month_datecheck_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="right"><span style=" font-size:11pt; font-weight:600; color:#14f82f;">New month : YES</span></p></body></html>',
                None,
            )
        )
        self.SR2_search_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "View info", None)
        )
        self.SR2_charges_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; text-decoration: underline; color:#ecff8c;">Default charges view</span></p></body></html>',
                None,
            )
        )
        ___qtablewidgetitem = self.SR2_charges_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("Society_MainWindow", "List", None)
        )
        ___qtablewidgetitem1 = self.SR2_charges_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("Society_MainWindow", "Amount", None)
        )
        ___qtablewidgetitem2 = self.SR2_charges_tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("Society_MainWindow", "1", None)
        )
        ___qtablewidgetitem3 = self.SR2_charges_tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("Society_MainWindow", "2", None)
        )

        __sortingEnabled = self.SR2_charges_tableWidget.isSortingEnabled()
        self.SR2_charges_tableWidget.setSortingEnabled(False)
        self.SR2_charges_tableWidget.setSortingEnabled(__sortingEnabled)

        self.SR2_bellow_totalbill_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#55ff00;">Totall bills :</span></p></body></html>',
                None,
            )
        )
        self.SR2_bellow_totalbill_value.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; text-decoration: underline; color:#f9d74d;">bills</span></p></body></html>',
                None,
            )
        )
        self.SR2_bellow_totalresidence_lbl.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#55ff00;">Totall Residence :</span></p></body></html>',
                None,
            )
        )
        self.SR2_bellow_totalresidence_value.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; text-decoration: underline; color:#f9d74d;">Room</span></p></body></html>',
                None,
            )
        )
        self.Generate_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Generate BiLLs", None)
        )
        self.Release_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "Release BiLLs", None)
        )
        self.SR2_extra_info1.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:9pt; color:#7a7a7a;">* Check Bill pdf count &amp; Residence count ,and internet connection before Releasing Bill</span></p></body></html>',
                None,
            )
        )
        self.SR2_extra_info2.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-weight:600; color:#a5a5a5;">* Before Release Check for Internet Connection &amp; Whatsapp With Web-Whatsapp online Status.</span></p></body></html>',
                None,
            )
        )
        self.SR2_top_search_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "  Wing/Room no", None)
        )
        self.SR2_top_search_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "search", None)
        )
        self.SR2_top_update_btn.setText(
            QCoreApplication.translate("Society_MainWindow", "update", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; color:#55ff7f;">View of :</span></p></body></html>',
                None,
            )
        )
        self.SR2_top_viewtype_comboBox.setItemText(
            1, QCoreApplication.translate("Society_MainWindow", "A Wing", None)
        )
        self.SR2_top_viewtype_comboBox.setItemText(
            2, QCoreApplication.translate("Society_MainWindow", "B Wing", None)
        )
        self.SR2_top_viewtype_comboBox.setItemText(
            3, QCoreApplication.translate("Society_MainWindow", "C Wing", None)
        )
        self.SR2_top_viewtype_comboBox.setItemText(
            4, QCoreApplication.translate("Society_MainWindow", "ALL Paid", None)
        )
        self.SR2_top_viewtype_comboBox.setItemText(
            5, QCoreApplication.translate("Society_MainWindow", "ALL UnPaid", None)
        )

        self.label_2.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:14pt; color:#55ff7f;">which month :</span></p></body></html>',
                None,
            )
        )
        self.SR2_top_month_comboBox.setItemText(
            0, QCoreApplication.translate("Society_MainWindow", "JANUARY", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            1, QCoreApplication.translate("Society_MainWindow", "FEBRUARY", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            2, QCoreApplication.translate("Society_MainWindow", "MARCH", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            3, QCoreApplication.translate("Society_MainWindow", "APRIL", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            4, QCoreApplication.translate("Society_MainWindow", "MAY", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            5, QCoreApplication.translate("Society_MainWindow", "JUNE", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            6, QCoreApplication.translate("Society_MainWindow", "JULY", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            7, QCoreApplication.translate("Society_MainWindow", "AUGUST", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            8, QCoreApplication.translate("Society_MainWindow", "SEPTEMBER", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            9, QCoreApplication.translate("Society_MainWindow", "OCTOBER", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            10, QCoreApplication.translate("Society_MainWindow", "NOVEMBER", None)
        )
        self.SR2_top_month_comboBox.setItemText(
            11, QCoreApplication.translate("Society_MainWindow", "DECEMBER", None)
        )
        self.SR2_refresh_pg3.setText(
            QCoreApplication.translate("Society_MainWindow", "Refresh", None)
        )
        ___qtablewidgetitem4 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("Society_MainWindow", "Room no.", None)
        )
        ___qtablewidgetitem5 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("Society_MainWindow", "Name", None)
        )
        ___qtablewidgetitem6 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("Society_MainWindow", "Bill id", None)
        )
        ___qtablewidgetitem7 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("Society_MainWindow", "Month", None)
        )
        ___qtablewidgetitem8 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("Society_MainWindow", "Amount", None)
        )
        ___qtablewidgetitem9 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("Society_MainWindow", "Fine", None)
        )
        ___qtablewidgetitem10 = self.SR2_billstatus_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("Society_MainWindow", "Status", None)
        )

        __sortingEnabled1 = self.SR2_billstatus_tableWidget.isSortingEnabled()
        self.SR2_billstatus_tableWidget.setSortingEnabled(False)
        self.SR2_billstatus_tableWidget.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#3fbc5c;">Information &gt;</span></p></body></html>',
                None,
            )
        )
        self.SR2_down_ttrows.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#ffaa7f;">Total Rows :111</span></p></body></html>',
                None,
            )
        )
        self.SR_down_ttresidence.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#ffaaff;">Total Residence :100</span></p></body></html>',
                None,
            )
        )
        self.SR2_down_Ttfines.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:10pt; font-weight:600; color:#55aaff;">Total fine bills:001</span></p></body></html>',
                None,
            )
        )
        self.Left_view_groupBox_3.setTitle(
            QCoreApplication.translate("Society_MainWindow", "View Charges", None)
        )
        self.label_1.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Service :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_1.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Maintenance :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Water :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Sinking :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Repair :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Festival :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_9.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Club House :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Fine :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_8.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Parking :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_9.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_12.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Total Charges (min.) :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_10.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600; color:#21ef81;">Last Updated :</span></p><p align="center"><span style=" font-size:10pt; font-weight:600; color:#21ef81;">1/6/2020</span></p></body></html>',
                None,
            )
        )
        self.updatebtnpushButton_2.setText(
            QCoreApplication.translate("Society_MainWindow", "Update Charges", None)
        )
        self.Right_update_groupBox_4.setTitle(
            QCoreApplication.translate("Society_MainWindow", "Update Charges", None)
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Service :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_31.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Maintenance :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_32.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Water :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_33.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Sinking :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_34.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Repair :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_35.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Festival :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_36.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_20.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Club House :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_37.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Fine :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_38.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_22.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Parking :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_39.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_23.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#21ef81;">Total Charges (min.) :</span></p></body></html>',
                None,
            )
        )
        self.lineEdit_40.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "      rs.", None)
        )
        self.label_24.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600; color:#060606;">Last Updated :</span></p><p align="center"><span style=" font-size:10pt; font-weight:600; color:#060606;">1/6/2020</span></p></body></html>',
                None,
            )
        )
        self.setbtpushButton_3.setText(
            QCoreApplication.translate("Society_MainWindow", "Set Charges", None)
        )
        self.SR_addup_search_lineEdit.setText("")
        self.SR_addup_search_lineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", " Wing/Room no.  ", None)
        )
        self.SR2_addup_searchpushButton.setText(
            QCoreApplication.translate("Society_MainWindow", "Search", None)
        )
        self.label_25.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">People Id  :  </span></p></body></html>',
                None,
            )
        )
        self.SR2_main_genratelineEdit_2.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "Auto Generated", None)
        )
        self.SR2_main_generatepushButton_5.setText(
            QCoreApplication.translate("Society_MainWindow", "Generate", None)
        )
        self.SR2_admin_radioButton.setText(
            QCoreApplication.translate(
                "Society_MainWindow", "If Admin Select This.", None
            )
        )
        self.SR2_Email_lineEdit_6.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "    abc@mail.com", None)
        )
        self.label_36.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p align="right"><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Bill Id :</span></p></body></html>',
                None,
            )
        )
        self.nameLabel.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Name :</span></p></body></html>',
                None,
            )
        )
        self.nameLineEdit.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "   First name", None)
        )
        self.label_34.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Flat Type :</span></p></body></html>',
                None,
            )
        )
        self.label_31.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Contact :</span></p></body></html>',
                None,
            )
        )
        self.label_32.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Email :</span></p></body></html>',
                None,
            )
        )
        self.SR2_vhiclecount_spinBox.setSuffix("")
        self.SR2_vhiclecount_spinBox.setPrefix("   ")
        self.label_35.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Vehicle Count :</span></p></body></html>',
                None,
            )
        )
        self.label_33.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Flat Area :</span></p></body></html>',
                None,
            )
        )
        self.label_30.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; font-weight:600; color:#55ff7f;">Room no. : </span></p></body></html>',
                None,
            )
        )
        self.surname_lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "   Surname", None)
        )
        self.SR2_Roomno_comboBox_2.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", " Select  Room no.", None)
        )
        self.Flattype_comboBox_3.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", " Select BHK", None)
        )
        self.Flattype_comboBox_3.setItemText(
            0, QCoreApplication.translate("Society_MainWindow", "1BHK", None)
        )
        self.Flattype_comboBox_3.setItemText(
            1, QCoreApplication.translate("Society_MainWindow", "2BHk", None)
        )
        self.SR2_flatarea_lineEdit_7.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", " Area  sq.ft", None)
        )
        self.Sr2_Phone_lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "   10 digits", None)
        )
        self.SR2_autoBillid_lineEdit_9.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "   Auto Generate", None)
        )
        self.SR2_wing_comboBox_4.setPlaceholderText(
            QCoreApplication.translate("Society_MainWindow", "  select Wing", None)
        )
        self.SR2_deletemem_pushButton_4.setText(
            QCoreApplication.translate("Society_MainWindow", "Delete record", None)
        )
        self.SR2_updatemem_pushButton_2.setText(
            QCoreApplication.translate("Society_MainWindow", "Update", None)
        )
        self.SR2_addmem_pushButton_3.setText(
            QCoreApplication.translate("Society_MainWindow", "Add member", None)
        )

    # retranslateUi


################################################################
counter = 0
db_file_name = ""


class Start_App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.ui.Splash_frame.setCursor(QCursor(Qt.WaitCursor))

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(100)
        self.shadow.setXOffset(10)
        self.shadow.setYOffset(10)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.Splash_frame.setGraphicsEffect(self.shadow)
        ## Files checking
        print("\n>>>>>>>>>>>>>>>", os.getcwd(), "\n files :", os.listdir())
        self.file_list = ("Society_BILL_Maintenance_Pdfs", "Society_Bill_Form")
        for i in self.file_list:
            if i not in os.listdir():
                os.mkdir(i)
                print("File created : ", i)
            else:
                print("File already present:", i)
        print("done files Check...\n")
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        # Change Texts
        def update_loadtxt(msg):
            self.ui.Splash_loadtxt.setText(msg)
            return self.ui.Splash_loadtxt

        QtCore.QTimer.singleShot(
            200,
            lambda: update_loadtxt(
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px;"><strong>Checking</strong> Files . . . '
            ),
        )
        QtCore.QTimer.singleShot(1000, lambda: self.DATABASE_LOAD())
        QtCore.QTimer.singleShot(
            500,
            lambda: update_loadtxt(
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px;"><strong>LOADING</strong> DATABASE. . . '
            ),
        )
        # 3000
        QtCore.QTimer.singleShot(
            700,
            lambda: update_loadtxt(
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px;"><strong>LOADING</strong> USER INTERFACE . . .'
            ),
        )

        # TIMER IN MILLISECONDS
        self.timer.start(2)

        self.show()
        # self.close()

    def progress(self):
        global counter
        # print("SplashScreen Loading",end="\ ")
        # SET VALUE TO PROGRESS BAR
        self.ui.Splash_progressbar.setValue(counter)
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 300:
            # STOP TIMER
            self.timer.stop()
            # SHOW MAIN WINDOW other window
            self.main = Main_win()
            self.main.show()
            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        counter += 1

    def DATABASE_LOAD(self):
        test_db = False

        def check_db(x):
            global test_db
            """Main database file check """
            file_db = os.listdir(dir_path)
            print("\nlist of file : ", file_db)
            if x not in file_db:
                test_db = False
            else:
                test_db = True
            print("send test_db result:", test_db)
            return test_db

        def table_create(cur, db, tb):
            print("\ncreating tb:", tb)
            try:
                sql = ""
                print("\n steps :", db_table_dict[db_file_name])
                if tb in db_table_dict[db_file_name]:
                    try:
                        if tb == "Society_Basic_info":
                            print(db, " build tb", tb)
                            sql = f"""create table {tb}(
                            Society_name STRING (100) NOT NULL,
                            Totall_rooms        INT (10),
                            Address             TEXT (200)   NOT NULL,
                            Bill_id_type        TEXT         NOT NULL,
                            New_month_from      TEXT         NOT NULL,
                            fBill_format_address TEXT,
                            total_wing           TEXT         NOT NULL,
                            total_floor          TEXT    NOT NULL)"""
                            cur.execute(sql)
                            print(tb, "created\n")
                        if tb == "Society_info_mem":
                            print(db, " build tb", tb)
                            sql = f"""create table {tb}(
                            People_id     STRING PRIMARY KEY  NOT NULL UNIQUE,
                            Fname         TEXT       NOT NULL,
                            Lname         TEXT       NOT NULL,
                            Roomno        INTEGER    NOT NULL UNIQUE,
                            Contact       INTEGER    NOT NULL,
                            Email         TEXT       NOT NULL,
                            Flat_type     TEXT       NOT NULL,
                            Vehicle_count INT (10)   NOT NULL,
                            Flatarea      FLOAT (50) NOT NULL,
                            BillID        TEXT       NOT NULL UNIQUE,
                            BillAmount    DOUBLE    NOT NULL,
                            Wing          STRING     NOT NULL) """
                            cur.execute(sql)
                            print(tb, "created\n")
                        if tb == "All_Bill_info":
                            print(db, " build tb", tb)
                            sql = f"""create table {tb}(
                            Bill_id STRING NOT NULL UNIQUE PRIMARY KEY,
                            Roomno TEXT NOT NULL,
                            Month_year TEXT   NOT NULL,
                            Pdf_name TEXT   NOT NULL,
                            Due_date   DATE   NOT NULL,
                            Payment_status  TEXT   NOT NULL DEFAULT Unpaid,
                            Send_to TEXT   NOT NULL,
                            Date_of_release DATE   NOT NULL,
                            Fine TEXT   NOT NULL,
                            Amount DOUBLE NOT NULL,
                            Mode  TEXT)"""
                            cur.execute(sql)
                            print(tb, "created\n")
                        if tb == "Default_charges":
                            print(db, "build tb : ", tb)
                            sql = f"""create table {tb}(
                            Service       DOUBLE  NOT NULL,
                            Maintenance   DOUBLE  NOT NULL,
                            Water         DOUBLE  NOT NULL,
                            Sinking_fund  DOUBLE  NOT NULL,
                            Repair_fund      DECIMAL NOT NULL,
                            Festival_fund DOUBLE  NOT NULL,
                            Club_house    DOUBLE,
                            Parking       INTEGER NOT NULL DEFAULT (0),
                            Total_charges DOUBLE  NOT NULL,
                            Last_update   DATE    NOT NULL,
                            Fine          INTEGER       NOT NULL)"""
                            cur.execute(sql)
                            print(tb, "created\n")
                        if tb == "Login_admin_tb":
                            print(db, "build tb : ", tb)
                            sql = f"""create table {tb}(
                            Person_id    TEXT   REFERENCES Society_info_mem (People_id) UNIQUE NOT NULL,
                            Name      STRING NOT NULL,
                            UserName  TEXT   UNIQUE NOT NULL,
                            Enc_password TEXT UNIQUE NOT NULL,
                            Dec_key TEXT NOT NULL,
                            Fo_email TEXT ,
                            Fo_whatsapp TEXT,
                            Fo_answer TEXT)"""
                            cur.execute(sql)
                            print(tb, "created\n")
                        if tb == "Unpaid_dailyview":
                            print(db, " View for evey month ", tb)
                            sql = f"""Create View {tb}  (Roomno,Payment_status,Mode,Fine) as select Roomno,Payment_status,Mode,Fine from All_Bill_info;"""
                            cur.execute(sql)
                    except sqlite3.OperationalError as err:
                        print("sql error :", err)
                else:
                    raise Exception
            except sqlite3.OperationalError as err:
                print("\n Error:table or database not correct ...", err)
            except:
                print("\n Error not from database...")

        def check_db_tables(x, t):
            tb_test = False
            print(x, "checking ....table ", t)
            con_tb1 = sqlite3.connect(x)
            cur = con_tb1.cursor()
            tb_view = []

            def see_tb(cur):
                sql = "select name from sqlite_master where type='table';"
                tb = cur.execute(sql)
                temp = tb.fetchall()
                for i in temp:
                    print("table :", i)
                    tb_view.append(i)
                return temp

            def see_view(cur):
                sql = "select name from sqlite_master where type='view';"
                view = cur.execute(sql)
                temp = view.fetchall()
                for i in temp:
                    print("view :", i)
                    tb_view.append(i)
                return temp

            tables_in_dbtb = see_tb(cur)
            view_in_dbtb = see_view(cur)
            print(
                "\ntables already in db ",
                tables_in_dbtb,
                "\>count :",
                len(tables_in_dbtb),
            )
            print("\nview already in db ", view_in_dbtb, "\>count :", len(view_in_dbtb))
            for i in t:
                print("\n\ntake table :", i, "::", tb_view, i in tb_view)
                if i not in [i[0] for i in tb_view]:
                    print("need to build table", i, [j[0] for j in tb_view], "\n")
                    table_create(cur, x, i)
                else:
                    print("already present : ", i)
            print("\nall tables in db now : ", see_tb(cur))
            con_tb1.commit()
            con_tb1.close()

        db_table_dict = {
            "Society_main.db": [
                "Society_info_mem",
                "Login_admin_tb",
                "Society_Basic_info",
                "All_Bill_info",
                "Default_charges",
                "Unpaid_dailyview",
            ]
        }

        for i in db_table_dict.keys():
            print("items:", i)
            global db_file_name
            db_file_name = i
        print("file for db : ", db_file_name)

        def go_for_newdb():
            self.timer.start(1)
            self.show()
            self.Win_db.destroy()
            print("create new db ")
            con_maindb = sqlite3.connect(db_file_name)
            print(os.listdir())
            cur = con_maindb.cursor()
            for i in db_table_dict[db_file_name]:
                print("new db creating tables", i)
                table_create(cur, db_file_name, i)
            con_maindb.commit()
            con_maindb.close()
            print("load data ", self.cb_val.get())
            if self.cb_val.get():
                print("loading demo data confirm.. ")
                demo_data_db(db_file_name)
            else:
                print(self.cb_val.get(), "no demo data . . . ")

        if not check_db(db_file_name):
            Checking_db = check_db(db_file_name)
            if not Checking_db:
                self.timer.stop()
                self.hide()
                self.Win_db = Tk()
                self.Win_db.geometry("300x220+300+100")
                groupBox1 = Pmw.Group(self.Win_db, tag_text="DATABASE Problem ")
                groupBox1.place(x=0, y=0, height=500, width=500)
                msg = "No database Founded :\nDo you want to create DATABASE and default tables... Or close this and get correct database"
                txt = tkinter.Text(self.Win_db, height=10, width=35)
                txt.insert("end", msg)
                txt.configure(state="disable")
                txt.place(x=10, y=20)
                self.cb_val = IntVar(value=1)
                cb = Checkbutton(
                    self.Win_db, text="load demo data", variable=self.cb_val
                )
                cb.place(x=10, y=190)
                print("demo data process:", self.cb_val.get())
                nxtbtn = Button(self.Win_db, text="yes", width=10, command=go_for_newdb)
                nxtbtn.place(x=160, y=190)
                self.Win_db.mainloop()

            else:
                self.timer.start(1)
        else:
            print(
                "\ndatabase exist check for tables...",
                db_file_name,
                db_table_dict[db_file_name],
            )
            check_db_tables(db_file_name, db_table_dict[db_file_name])


#################################################################
class Main_win(QMainWindow):
    global db_file_name

    def login_Page_operation(self):
        self.ui.eye_pushButton.setIcon(self.ui.iconclose)
        self.temp_op = "open"
        self.admin_cred = []
        self.admin_name = ""
        # self.login_dbcolumn=[i[0] for i in self.cur.description]
        # print("\n cur description :",self.login_dbcolumn)
        for i in self.login_dbdata:
            temp1 = []
            print("all data from Login_admin_tb is \n", i)
            for j in range(len(i)):
                if j in (2, 3):
                    temp1.append(i[j])
            self.admin_cred.append(temp1)
        print("\n\nLogin step start to checkFields")
        textUser = ""
        textPassword = ""
        ###
        User_cred = ""  # StringVar()
        Password_cred = ""  # StringVar()

        # FUNCTIONS to show error box
        def showMessage(message):
            self.ui.Error_box.show()
            msg = f"""<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Error : {message}</span></p></body></html>"""
            self.ui.Error_Label.setText(
                QCoreApplication.translate("Society_MainWindow", (msg), None)
            )
            print(message)

        def login_fail(msg):
            self.ui.Error_box.hide()
            print("login fail", msg)
            showMessage(msg)

        def login_done(admin_name):
            self.ui.eye_pushButton.setIcon(self.ui.iconclose)
            self.temp_op = "open"
            self.ui.Login_user_name.setText("")
            self.ui.Login_user_password.setText("")
            self.ui.Error_box.hide()
            print("hide UserName,pass")
            temp3_adminname = f"""<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#f9f21c;\">Now :<br>{admin_name}</span></p></body></html>"""
            self.ui.user_txt2.setText(
                QCoreApplication.translate("Society_MainWindow", temp3_adminname, None)
            )
            self.logout_done = False

        def login_check(user, password):
            self.ui.Error_box.hide()
            print("login check")
            ###check password with db
            def check_with_db(x, y):
                for i in self.admin_cred:
                    print(
                        x,
                        y,
                        " check_with_db cred db : ",
                        i,
                    )
                    if i == [x, y]:
                        for k in self.login_dbdata:
                            print(k)
                            if x and y in k:
                                print("admin is :", k[1])
                                self.admin_name = k[1]
                        return True
                return False

            # trial Login Success
            if check_with_db(user, password):
                print("login done ")
                self.ui.Society_BILLMaintenance.setCurrentIndex(1)
                login_done(self.admin_name)
            else:
                text = "Login Credentials username and password not correct ! "
                login_fail(text)

        # check Qline edit for username and password
        style_error = (
            "QLineEdit {\n"
            "	\n"
            "\n"
            "	padding: 15px;\n"
            "\n"
            "background: transparent;\n"
            "  border: 1px solid rgb(255, 3, 7);\n"
            "  font-size: 18px;\n"
            "  color:rgb(255, 255, 255);\n"
            "  font-weight: bold;\n"
            "  \n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "	color: rgb(0, 170, 255);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(255, 207, 0);	\n"
            "	color: rgb(17, 251, 255);\n"
            "   \n"
            "}"
        )
        style_normal = (
            "QLineEdit {\n"
            "	background: transparent;\n"
            "  border: none;\n"
            "  border-bottom: 1px solid white;\n"
            "  font-size: 18px;\n"
            "  \n"
            "	color: rgb(255, 255, 255);\n"
            "padding: 15px;\n"
            "  font-weight: bold;\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(55, 55, 55);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(255, 207, 0);	\n"
            "	color: rgb(8, 251, 255);\n"
            "}"
        )
        if not (self.ui.Login_user_name.text()):
            textUser = " UserName can`t Empty. "
            self.ui.Login_user_name.setStyleSheet(style_error)
        else:
            textUser = ""
            self.ui.Login_user_name.setStyleSheet(style_normal)
        if not (self.ui.Login_user_password.text()):
            textPassword = " Password can`t Empty. "
            self.ui.Login_user_password.setStyleSheet(style_error)
        else:
            textPassword = ""
            self.ui.Login_user_password.setStyleSheet(style_normal)
        if textUser + textPassword != "":
            errormsg = textUser + "\t" + textPassword
            showMessage(errormsg)
        else:
            User_cred = self.ui.Login_user_name.text()
            Password_cred = self.ui.Login_user_password.text()
            login_check(User_cred, Password_cred)
            print(
                "username : ",
                User_cred,
                "\t password : ",
                Password_cred,
                "  checked ...",
            )

    def Forgot_pg_operation(self):
        self.ui.Error_box.hide()
        print("\n\nwe are on forgot page process...")
        fusermail = self.ui.forgot_usermail_lineEdit.text()
        fwhatsapp = self.ui.Forgot_whatsapp_lineEdit.text()
        flistno = self.ui.comboBox.currentIndex()
        fanswer = self.ui.Forgot_ans_lineEdit.text()
        print("details enterd : ", fusermail, fwhatsapp, flistno, fanswer)

        def showerror(message):
            self.ui.Error_box.show()
            msg = f"""<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Error : {message}</span></p></body></html>"""
            self.ui.Error_Label.setText(
                QCoreApplication.translate("Society_MainWindow", (msg), None)
            )
            print(message)

        def c_digit(x):
            for i in x:
                if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
                    continue
                else:
                    return False
            return True

        if (len(fwhatsapp) < 10 or c_digit(fwhatsapp)) or (
            (fusermail or fwhatsapp or fanswer) == "" or flistno < 0
        ):
            print("not allowed only digits")
            self.ui.Forgot_whatsapp_lineEdit.setText("")
            fwhatsapp = ""
            showerror(
                "All Fields are necessary to br filled now some are empty !<br>Whatsapp no.,No Alphabat and 10 digit must"
            )
        else:
            self.ui.Error_box.hide()
            # check details conditions
            self.forgot_dbdata = []
            for i in self.login_dbdata:
                temp2 = []
                for j in range(len(i)):
                    if j in (3, 5, 6, 7):
                        temp2.append(i[j])
                self.forgot_dbdata.append(temp2)
            print("we need db data :", self.forgot_dbdata)

            def forgot_check(c3):
                temp2_0 = []
                tempwith_email = []
                for i in self.forgot_dbdata:
                    temp2_0.append(i[0])
                    tp = []
                    for k in range(len(i)):
                        if k != 0:
                            tp.append(i[k])
                    tempwith_email.append(tp)
                print("\n we check for email and other :", tempwith_email, "\n\n")
                tempwith_user = []
                for i in temp2_0:
                    tp1 = []
                    tp1.append(i)
                    # print("fr admin tp1:",tp1,i)
                    for j in self.forgot_dbdata:
                        # print(">>>>",j,i)
                        if i in j:
                            for k in range(len(j)):
                                # print(">>>>",j[k])
                                if k > 1:
                                    tp1.append(j[k])
                    tempwith_user.append(tp1)
                    print("\nother : ", tempwith_user)
                print("\n we check for user and other :", tempwith_user)

                def ret(c3, x, msg):
                    for i in x:
                        if c3 == i:
                            print("\n\n", ":  msg ", msg, c3, "==", i, c3 == i)
                            point = 0
                            for j in range(len(self.forgot_dbdata)):
                                ind = j
                                for k in c3:
                                    print(
                                        "checking to give password :",
                                        k,
                                        self.forgot_dbdata[ind],
                                        point,
                                    )
                                    if k in self.forgot_dbdata[ind]:
                                        point += 1
                                    if point == 3:
                                        print(
                                            "set forgot password :",
                                            self.forgot_dbdata[ind],
                                        )
                                        ps = f""" "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:  rgb(255, 170, 0);\">Your password :</span><span style=\" font-size:11pt; font-weight:600; color: rgb(0, 255, 0);\">   {self.forgot_dbdata[ind][0]} <br>    Memorize it.</span></p></body></html>" """
                                        self.ui.Password_show_lb.setText(
                                            QCoreApplication.translate(
                                                "Society_MainWindow", ps, None
                                            )
                                        )
                                else:
                                    point = 0

                            return True
                    return False

                temp5 = False
                for i in range(len([tempwith_email, tempwith_user])):
                    if i == 0:
                        temp5 = ret(c3, tempwith_email, "got email")
                    if i == 1:
                        temp5 = ret(c3, tempwith_user, "got user name")
                    print(temp5, " for forgotten and view password")
                    if temp5:
                        print("correct")
                        return temp5
                return False

            c3 = [fusermail, fwhatsapp, fanswer]
            if forgot_check(c3):
                self.ui.Error_box.hide()
                QtCore.QTimer.singleShot(
                    1000, lambda: self.ui.Password_show_lb.setVisible(True)
                )

                def reset_forgot_pg():
                    print("seen:", self.ui.Password_show_lb.isVisible())
                    QtCore.QTimer.singleShot(
                        10, lambda: self.ui.Password_show_lb.setVisible(False)
                    )
                    if self.ui.Password_show_lb.isVisible():
                        self.ui.forgot_usermail_lineEdit.setText("")
                        self.ui.Forgot_whatsapp_lineEdit.setText("")
                        self.ui.comboBox.setCurrentIndex(-1)
                        self.ui.Forgot_ans_lineEdit.setText("")

                QtCore.QTimer.singleShot(5000, lambda: reset_forgot_pg())
            else:
                showerror("Wrong combination of answers.")
                self.ui.Password_show_lb.setVisible(False)

    ###############################################
    resized = QtCore.pyqtSignal()

    def __init__(self):
        QMainWindow.__init__(self)
        self.admins = {"username": "a1", "password": "a1"}
        self.ui = Ui_Society_MainWindow()
        self.ui.setupUi(self)
        self.now = QDate.currentDate()
        self.today_date = self.now.toString(Qt.ISODate)
        self.set_todays()
        new_month = lambda: self.check_new_month()
        self.S_datebox()
        self.set_room_wing()
        self.logout_done = True
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_home_p1)
        self.ui.Forgot_pswdbtn.clicked.connect(
            lambda: self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Forgot_pg)
        )
        self.ui.Login_btn.clicked.connect(
            lambda: self.ui.Login_stackedWidget.setCurrentWidget(self.ui.Login_form_pg)
        )
        self.ui.Exit_btn.clicked.connect(self.Close_Society_app)
        self.ui.Forgot_confirm_Button.clicked.connect(self.Forgot_pg_operation)
        self.ui.SL2_logout_btn.clicked.connect(self.SL2_logout_btn1_op)
        self.ui.SL1_dcharges_btn.clicked.connect(lambda: self.SL1_dcharges_btn1_op())
        self.ui.SL1_pdfbills_btn.clicked.connect(lambda: self.SL1_pdfbills_btn_op())
        self.ui.updatinfo_btn.clicked.connect(lambda: self.updatinfo_btn1_op())
        self.ui.Conwebwhatsapp_btn.clicked.connect(
            lambda: self.Conwebwhatsapp_btn1_op()
        )
        # hide error frame_error
        self.ui.Error_box.hide()
        self.ui.Password_show_lb.hide()
        # eye button
        self.temp_op = "open"
        self.ui.eye_pushButton.clicked.connect(lambda: self.eye_op())
        # Login button clicked then check FIELDS
        self.ui.Login_admin_btn.clicked.connect(self.login_Page_operation)
        self.ui.Error_Close_btn.clicked.connect(lambda: self.ui.Error_box.hide())
        self.ui.Todays_date_dateEdit.dateChanged.connect(self.S_datebox)
        self.ui.SL1_home_btn.clicked.connect(self.home_btnl_op)
        self.ui.NewMonth_btn.clicked.connect(self.NewMonth_btn1_op)
        self.ui.Billstatus_btn.clicked.connect(self.Billstatus_btn1_op)
        self.closeEvent = self.Mainclose  # detect close window
        self.resized.connect(
            lambda: print("resized ..", self.geometry())
        )  # ,self.x(),self.y(),self.width()))
        self.ui.SL1_Upaidbill_btn.clicked.connect(lambda: self.SL1_Upaidbill_btn1_op())
        self.ui.Release_btn.clicked.connect(lambda: self.Release_btn_op())
        self.ui.Generate_btn.clicked.connect(lambda: self.Generate_btn_op())
        ############################db data
        self.condb = sqlite3.connect(db_file_name)
        self.cur = self.condb.cursor()
        self.cur.execute("select * from Login_admin_tb;")
        self.login_dbdata = self.cur.fetchall()
        self.condb.close()
        ###########################
        self.select_view = ""
        self.search_boxd = ""
        self.updatebill_win = False
        self.ui.SR2_addup_searchpushButton.clicked.connect(lambda: self.search_pp())
        self.ui.SR2_deletemem_pushButton_4.clicked.connect(lambda: self.delete_res())
        self.ui.SL2_whatsapp_btn.clicked.connect(lambda: self.send_warning_op())
        self.ui.SL2_Report_btn.clicked.connect(lambda: self.Report_op())
        self.show()
        ###########################

    def set_room_wing(self):
        con = sqlite3.connect(db_file_name)
        cur = con.cursor()
        cur.execute(
            "select Totall_rooms,total_wing,total_floor from Society_Basic_info;"
        )
        data = cur.fetchall()
        if len(data) == 1:
            self.total_room = data[0][0]
            self.total_wing = []
            for i in data[0][1]:
                if i != ",":
                    self.total_wing.append(i)
            self.total_floor = data[0][2]
        # else:
        # QMessageBox.warning(QMessageBox(),"Error","More than 1 Society data saved...")
        print("\ntotal room/wing :", self.total_wing, self.total_room, self.total_floor)
        con.close()

        def setwing(ind, item):
            self.ui.SR2_wing_comboBox_4.addItem("")
            self.ui.SR2_wing_comboBox_4.setItemText(
                ind, QCoreApplication.translate("Society_MainWindow", item, None)
            )

        self.total_wing = sorted(self.total_wing)
        for i in range(len(self.total_wing)):
            print(i, self.total_wing[i])
            setwing(i, self.total_wing[i].upper())

    def eye_op(self):
        print("eye clicked")

        def change_icon(x):
            if x == "close":
                self.ui.eye_pushButton.setIcon(self.ui.iconclose)
                self.temp_op = "open"
                print(x, " to ", self.temp_op)
                self.ui.Login_user_password.setEchoMode(QLineEdit.Password)
            if x == "open":
                self.ui.eye_pushButton.setIcon(self.ui.iconopen)
                self.temp_op = "close"
                print(x, " to ", self.temp_op)
                self.ui.Login_user_password.setEchoMode(QLineEdit.Normal)

        change_icon(self.temp_op)

    def home_btnl_op(self):
        print("Home button clicked")
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_home_p1)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">Home</span></p></body></html>',
                None,
            )
        )
        print("logout_done :", self.logout_done)
        self.select_view = ""

    def NewMonth_btn1_op(self):
        print("New Bill released clicked")
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_billrelease_p2)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">New Month Bill Release</span></p></body></html>',
                None,
            )
        )
        #'''default charges Operation'''
        print("\n\n loading default charges . . .")
        self.ui.SR2_search_btn.clicked.connect(self.search_view_op)

        def tbill():

            return sum(
                len(file)
                for _, _, file in os.walk(
                    f"""{dir_path}/Society_BILL_Maintenance_Pdfs"""
                )
            )

        self.ui.SR2_bellow_totalbill_value.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                f'''"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#f9d74d;\"> {tbill()} </span></p></body></html>"''',
                None,
            )
        )
        self.default_charge_tb_op()
        self.SR2_Bill_tableView_op()

    def search_view_op(self):
        self.ui.SR2_searchbox_lineEdit.setPlaceholderText("Wing or Room no.")
        print(">>>>>> for view select is : ", self.select_view)
        self.ui.SR2_Bill_tableView.clearSelection()
        self.get_status()
        go_for = str(self.select_view).casefold()
        go_for = go_for.replace("-", "/")
        self.search_boxd = go_for
        if self.select_view != "":
            print("go for : ", go_for)
            self.open_info_win(self.tbs_data, False)
        else:
            QMessageBox.warning(
                QMessageBox(), "Error", "Could not get selected ,Select row to view.."
            )

    def SR2_Bill_tableView_op(self):
        self.society_memdb = []
        try:
            # self.SR2_charges_tableWidget
            con1 = sqlite3.connect(db_file_name)
            cur1 = con1.cursor()
            # row count
            sql_row = "select * from Society_info_mem;"
            cur1.execute(sql_row)
            dc_rowdb = cur1.fetchall()
            for li in range(1, len(dc_rowdb)):
                temp8 = []
                item = dc_rowdb[li]
                # print(">>>>>>>> len : ",len(item),item)
                # print("\n > Room : ",item[3],"\n > Name : ",str(item[1])+" "+str(item[2]),"\n > Bill amount : ",item[10])
                temp8.append(str(item[11][0]) + "-" + str(item[3]))
                temp8.append(str(str(item[1]) + " " + str(item[2])))
                temp8.append(str(item[10]))
                self.society_memdb.append(temp8)
        except sqlite3.OperationalError as err:
            print("sql error : ", err)
        print("data :", self.society_memdb, len(self.society_memdb))
        con = f""""<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#f9d74d;\">{len(self.society_memdb)}</span></p></body></html>" """
        self.ui.SR2_bellow_totalresidence_value.setText(
            QCoreApplication.translate("Society_MainWindow", con, None)
        )
        room_no_ls = []
        name_ls = []
        billamt_ls = []
        for i in self.society_memdb:
            for j in range(len(i)):
                if j == 0:
                    room_no_ls.append(i[j])
                elif j == 1:
                    name_ls.append(i[j])
                elif j == 2:
                    billamt_ls.append(i[j])
                else:
                    print("unknown:", i[j])
        # print("\n >> roomlist:",room_no_ls,"\n >> name list :",name_ls,"\n >> bill amt list: ",billamt_ls)
        tb_view = ["wing-Room no.", "Name surname", "Amount"]
        # model for quick short table view
        model = QStandardItemModel(len(tb_view), 3)
        model.setHorizontalHeaderLabels(tb_view)
        # put data in view
        for row, rooms in enumerate(room_no_ls):
            # print(row,">>",rooms)
            item = QStandardItem(rooms)
            model.setItem(row, 0, item)
        for row, names in enumerate(name_ls):
            # print(row,">>",names)
            item = QStandardItem(names)
            model.setItem(row, 1, item)
        for row, amt in enumerate(billamt_ls):
            # print(row,">>",amt)
            item = QStandardItem(amt)
            model.setItem(row, 2, item)
        # filter
        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(0)
        # set search
        self.ui.SR2_searchbox_lineEdit.textChanged.connect(
            filter_proxy_model.setFilterRegExp
        )
        # tb view set module > on
        self.ui.SR2_Bill_tableView.setStyleSheet(
            "QTableView{font-size:12px;} QTableView:item{color:rgb(0,255,255); font-weight:bold;}QTableView:select{color:red;}"
        )
        self.ui.SR2_Bill_tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.SR2_Bill_tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.SR2_Bill_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.SR2_Bill_tableView.verticalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.ui.SR2_Bill_tableView.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.ui.SR2_Bill_tableView.setModel(filter_proxy_model)
        self.ui.SR2_searchbox_lineEdit.textChanged.connect(lambda: row_ds())

        def row_ds():
            self.ui.SR2_searchbox_lineEdit.setPlaceholderText("Wing or Room no.")
            self.select_view = ""
            self.ui.SR2_Bill_tableView.clearSelection()

        def see_row():
            self.select_view = ""
            selected = self.ui.SR2_Bill_tableView.selectedIndexes()[0]
            select_room = self.ui.SR2_Bill_tableView.model().data(selected)
            self.ui.SR2_searchbox_lineEdit.setPlaceholderText(select_room)
            print("||", select_room, len(str(self.select_view)), "<<<<<<")
            if select_room != "":
                self.select_view = select_room
                print(">> select view :", self.select_view)
            else:
                print("No Selection from table")

        self.ui.SR2_Bill_tableView.clicked.connect(lambda: see_row())
        # end

    def get_dcharges(self):
        try:
            # self.SR2_charges_tableWidget
            con1 = sqlite3.connect(db_file_name)
            cur1 = con1.cursor()
            # row count
            sql_row = "select count(*) from Default_charges;"
            cur1.execute(sql_row)
            dc_rowdb = cur1.fetchall()
            dc_row = dc_rowdb[0][0]
            # column count
            cur1.execute("select * from Default_charges;")
            self.sql_description_dc = [i[0] for i in cur1.description]
            dc_col = len(self.sql_description_dc)  # sql_description,#cur1.description)
            # ---------
            # print("Default_charges tb row,column: ",dc_row,dc_col)
            # self.ui.SR2_charges_tableWidget.setColumnCount()
            self.ui.SR2_charges_tableWidget.setRowCount(dc_col)
            # ---------------
            def dc_date_compare(dd):
                # print("\n date subtract")
                near_date = ""
                temp6 = {}
                # 2020-11-11    : 0123-56-89
                d1 = date(
                    int(self.today_date[0:4]),
                    int(self.today_date[5:7]),
                    int(self.today_date[8:10]),
                )
                for i in dd:
                    d2 = date(int(i[0:4]), int(i[5:7]), int(i[8:10]))
                    # print("\ndates :",d1,"-",d2)
                    del_dd = d1 - d2
                    # print("subtract: ",del_dd.days)
                    temp6[del_dd] = i
                # print("<<>>>>>",min(temp6))
                near_date = temp6[min(temp6)]
                print("near date:", near_date, ":", temp6)
                return str(near_date)

            # print("today is :",self.today_date," take last updated charges:")
            sql_date = f"select Last_update from Default_charges;"
            cur1.execute(sql_date)
            dc_dbdate = cur1.fetchall()
            dc_date = [i[0] for i in dc_dbdate]
            # print("\nall dates :",dc_date)
            updc = dc_date_compare(dc_date)
            sql_getupdc = (
                f"""select * from Default_charges where Last_update='{updc}';"""
            )
            # print(">perform :",sql_getupdc)
            cur1.execute(sql_getupdc)
            self.dc_data = cur1.fetchall()
            print("\namounts : ", self.dc_data)
            con1.close()
        except sqlite3.OperationalError as err:
            print("sql error : ", err)

    def default_charge_tb_op(self):
        self.get_dcharges()
        # load on SR2_Default_charges widget
        print("> item \t\t| value", self.dc_data)
        item1 = self.sql_description_dc
        item2 = self.dc_data[0]
        # for i in range(len(item1)):
        # print(f"""> {item1[i]}\t===>\t{item2[i]}""")
        def load_charge_item():
            col = 0
            item = self.sql_description_dc
            # print("Sql Columns :",sql_description)
            for row in range(len(item)):
                # print("\n>>>> item added:",item[row]," row :",row," col:",col)
                brush_item = QBrush(QColor(0, 85, 255, 255))
                brush_item.setStyle(Qt.SolidPattern)
                font_item = QFont()
                font_item.setFamily("Segoe UI Semibold")
                font_item.setPointSize(12)
                qtablewidgetitem_item = QTableWidgetItem()
                qtablewidgetitem_item.setText(item[row])
                qtablewidgetitem_item.setFont(font_item)
                qtablewidgetitem_item.setForeground(brush_item)
                self.ui.SR2_charges_tableWidget.setItem(row, col, qtablewidgetitem_item)
            col = 1
            item = self.dc_data[0]
            for row in range(len(item)):
                # print("\n>>>> item added:",item[row]," row :",row," col:",col)
                brush_val = QBrush(QColor(85, 255, 0, 255))
                brush_val.setStyle(Qt.SolidPattern)
                font_val = QFont()
                font_val.setPointSize(11)
                font_val.setBold(True)
                font_val.setWeight(75)
                qtablewidgetitem_val = QTableWidgetItem()
                qtablewidgetitem_val.setFont(font_val)
                qtablewidgetitem_val.setForeground(brush_val)
                qtablewidgetitem_val.setText(str(item[row]))
                self.ui.SR2_charges_tableWidget.setItem(row, col, qtablewidgetitem_val)

        load_charge_item()
        # end

    def check_new_month(self):
        print("new Bill Month")
        ###----make read only QDateEdit
        # self.ui.Todays_date_dateEdit.setReadOnly(True)
        # self.ui.Todays_date_dateEdit.setCalendarPopup(True)
        # check new month op
        con1 = sqlite3.connect(db_file_name)
        cur2 = con1.cursor()
        sql_nxtday = """select New_month_from from Society_Basic_info; """
        cur2.execute(sql_nxtday)
        nxt_day = cur2.fetchall()
        print("from every month :", nxt_day[0][0], " is start  of new month...")
        temp7 = ""
        for i in nxt_day[0]:
            for j in i:
                # print(">>",j)
                if j.isdigit():
                    temp7 += j
        self.nxt_month_day = int(temp7)
        print(
            "get check with todays: is today",
            self.nxt_month_day,
            " of date",
            self.today_date,
        )
        print(">>", self.ui.Todays_date_dateEdit.text(), ">>>", (self.nxt_month_day))

        def new_month_active():
            self.ui.New_month_datecheck_lbl.setText(
                QCoreApplication.translate(
                    "Society_MainWindow",
                    '<html><head/><body><p align="right"><span style=" font-size:11pt; font-weight:600; color:#14f82f;">New month : YES</span></p></body></html>',
                    None,
                )
            )
            self.ui.Generate_btn.show()
            self.ui.Release_btn.show()

        def new_month_deactive():
            self.ui.New_month_datecheck_lbl.setText(
                QCoreApplication.translate(
                    "Society_MainWindow",
                    '<html><head/><body><p align="right"><span style=" font-size:11pt; font-weight:600; color:red;">New month : NO </span></p></body></html>',
                    None,
                )
            )
            # self.ui.Generate_btn.hide()
            self.ui.Release_btn.hide()

            # self.ui.Release_btn.clicked.connect(lambda:self.Qerror())

        if QDate.currentDate().day() == self.nxt_month_day or int(
            str(self.ui.Todays_date_dateEdit.text()[0:2])
        ) == (self.nxt_month_day):
            print("acitve New bill")
            new_month_active()
        else:
            print("acitve New bill")
            new_month_deactive()
        print(
            "is isVisible Generate :",
            self.ui.Generate_btn.isVisible(),
            " Release :",
            self.ui.Release_btn.isVisible(),
        )
        con1.close()
        # end

    def Release_btn_op(self):
        print("Release_btn clicked")

    def Generate_btn_op(self):
        print("Generate_btn clicked")

        def warn():
            def print_btn(i):
                print("button on # WARNING: clicked::", i.text())

            print("is isVisible:", self.ui.Generate_btn.isVisible())
            if not self.ui.Release_btn.isVisible():
                print("show # WARNING: no new Month")
                # QMessageBox.warning(QMessageBox(), 'No New Month',"Not possible before new month day", "Check system data is correct if today you want to Generate and Release.")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Not possible before new month day")
                msg.setDetailedText(
                    "Check system data is correct if today you want to Generate and Release"
                )
                msg.buttonClicked.connect(print_btn)
                retval = msg.exec_()

        warn()
        print("_" * 10)
        self.pdf_file = "Society_BILL_Maintenance_Pdfs"
        print(
            "File for pdf :",
            self.pdf_file,
            " at :",
            dir_path,
            "\n file have :",
            os.listdir(dir_path),
            "\n Databse :",
            db_file_name,
        )
        print("date :", self.ui.Todays_date_dateEdit.text())
        con = sqlite3.connect(db_file_name)
        cur = con.cursor()
        sql = "select * from Society_Basic_info;"
        cur.execute(sql)
        s_data = cur.fetchall()
        s_data = s_data[0]
        print("data fetched :", s_data[0])
        con.close()
        bill_ = f"""
\t\t\tSociety Maintenance BiLL
\t{s_data[0]}
\t{s_data[2]}
        """
        print(bill_)

    def get_status(self):
        con1 = sqlite3.connect(db_file_name)
        cur1 = con1.cursor()
        cur2 = con1.cursor()
        self.tbs_data = []
        sql1 = f""" select Bill_id,Roomno,Month_year,Payment_status,Fine,Amount from All_Bill_info;"""
        sql2 = f""" select Roomno,fname,lname,Wing from Society_info_mem; """
        cur1.execute(sql1)
        cur2.execute(sql2)
        bill_data = cur1.fetchall()
        bill_name = cur2.fetchall()
        # roomno | Name | billid | month | Amount | Fine | Status .
        def rep(bd, bn):
            # print(bd[1],"<<>>",bn)
            if str(bd[1]) == str(bn[3][0]) + "/" + str(bn[0]):
                temp = []
                # print(">>>j,k :",bd,bn,end=" >|\n ")

                roomnols = str(bn[3][0] + "/" + str(bn[0]))
                temp.append(roomnols)

                fullnamels = bn[1] + " " + bn[2]
                temp.append(fullnamels)

                billidls = str(bd[0])
                temp.append(billidls)

                # st=""
                # for i in bd[2]:
                #     if i=="_":
                #         break
                #     else:
                #         st+=i
                # monthls=st
                temp.append(bd[2])

                amt = str(bd[5])
                temp.append(amt)

                finels = str(bd[4])
                temp.append(finels)

                statusls = bd[3]
                temp.append(statusls)

                # print(">temp",temp)
                self.tbs_data.append(temp)

        for i in bill_data:
            for j in bill_name:
                # print(">>>i ,j:",i,j)
                rep(i, j)
        # print("\n bill data :",bill_data," \n bill names :",bill_name)
        con1.close()
        # end

    def open_info_win(self, billdata, updview):
        data = ""
        des = ""
        self.dataup = []
        for i in billdata:
            if str(i[0]).casefold() == str(self.search_boxd).casefold():
                print("\t|\t ".join([i[2], i[3], i[6]]))
                data += " \t|\t".join([i[2], i[3], i[6]])
                data += "\n"
                des += f""" Name : {i[1]} \n Room : {i[0]}\t\tBill Amount:{i[4]}"""
                self.dataup.append(i[0])
        win_search = Tk()
        ws = win_search

        def set_win():
            w, h = 360, 450
            r, d = 300, 50
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            # root.winfo_screenwidth()-100, root.winfo_screenheight()-100
            # height x width + position right + position down
            win_search.title("Society Maintenance-Bill Management : Search Window")
            win_search.configure(background="black")
            # win_search.resizable(0,0)

        set_win()
        descri = tkinter.Text(ws, height=3, width=40)
        descri.insert("end", des)
        descri.configure(state="disable")
        descri.place(x=10, y=5)

        txt = sct.ScrolledText(ws, height=20, width=40)
        header = " Bill ID\t|\tdate\t|\tstatus\n"
        txt.insert("end", header)
        txt.insert("end", "_" * 40)
        txt.insert("end", data)
        txt.configure(state="disable")
        txt.place(x=10, y=60)
        if updview:
            Button(
                ws,
                text="update",
                width=10,
                command=(lambda: self.bill_status_search(self.dataup[0], 2)),
            ).place(x=150, y=400)
            print("\n data up passed:", self.dataup)
        Button(
            ws, text="close", width=10, command=(lambda: win_search.destroy())
        ).place(x=250, y=400)
        win_search.mainloop()
        # end

    def bill_status_search(self, billdata, wic):
        self.search_boxd = str(self.ui.SR2_top_search_lineEdit.text()).casefold()

        def check_search(x):
            # print(">>x:",x,[str(i[0]).casefold() for i in billdata])
            if x in [str(i[0]).casefold() for i in billdata]:
                # print("correct",x)
                return True
            return False

        def wic1():
            self.search_boxd = str(self.ui.SR2_top_search_lineEdit.text()).casefold()
            print("search  bill status clicked ...", billdata, "\n", self.search_boxd)
            if self.search_boxd != "" and check_search(self.search_boxd):
                self.open_info_win(billdata, True)
            else:
                print("no data to be search...")
                QMessageBox.warning(
                    QMessageBox(),
                    "Error",
                    "No Data of wing/roomno to be search or update.",
                )
            self.ui.SR2_top_search_lineEdit.setText("")

        def wic2():
            print(
                "update bill status clicked ...",
                "\n",
                self.search_boxd,
                "billdata:",
                billdata,
            )
            if self.updatebill_win == False:
                print(
                    "open update",
                )
                data_up = ""
                if self.search_boxd != "" and check_search(self.search_boxd):
                    data_up = str(self.search_boxd).casefold()
                    print("update add :", data_up)
                    self.open_updatebill_win(data_up)
                elif len(billdata) < 7 and str(type(billdata)) == "<class 'str'>":
                    data_up = str(billdata).casefold()
                    # print(type(billdata),str(type(billdata))=="<class 'str'>","\nupdate add :",data_up)
                    self.open_updatebill_win(data_up)
                else:
                    print("no data to be search...")
                    QMessageBox.warning(
                        QMessageBox(),
                        "Error",
                        "No Data of wing/roomno to be search or update.",
                    )

                self.ui.SR2_top_search_lineEdit.setText("")
            else:
                QMessageBox.warning(
                    QMessageBox(),
                    "Error",
                    "Could not open ,\nits already updating other.",
                )

        if wic == 1:
            wic1()
        if wic == 2:
            wic2()
            # end

    def open_updatebill_win(self, roomd):
        self.updatebill_win = True
        win_search = Tk()
        ws = win_search

        def on_quit():
            win_search.destroy()
            self.updatebill_win = False

        def set_win():
            w, h = 250, 300
            r, d = 300, 200
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            # root.winfo_screenwidth()-100, root.winfo_screenheight()-100
            # height x width + position right + position down
            win_search.title("Bill: Update Window")
            win_search.configure(background="black")
            win_search.resizable(0, 0)
            win_search.protocol("WM_DELETE_WINDOW", on_quit)

        set_win()
        # print("room to update : ",roomd,"\n:tbs ",self.tbs_data)
        def set_detail(r, data):
            detail = ""
            for i in data:
                # print(r,"<>",str(i[0]).casefold(),r==str(i[0]).casefold())
                if r == str(i[0]).casefold():
                    detail += f"""Name : {i[1]}   |  Room : {i[0]}"""
            print("detail:", detail)
            des = Label(
                ws, text=detail + "\n\n" + " Updating BILL Status . . .", width=35
            )
            des.place(x=20, y=20)
            # des.configure(text=detail)

        set_detail(roomd, self.tbs_data)
        self.payment_method = "Cash"
        paym = Button(win_search, text="Payment method", command=lambda: paym_win())

        def set_pm(x):

            print("set payment_method:", x, self.payment_method)
            self.payment_method = x

        def modify(event):
            print("combox select:", combx.get(), combx.get() == "Paid")
            if str(combx.get()).casefold() == str("Paid").casefold():
                paym.place(x=140, y=70)
            else:
                paym.place_forget()

        def paym_win():

            print("payset:", self.payment_method)
            win = Tk()
            w, h = 200, 200
            r, d = 200, 200
            win.geometry("%dx%d+%d+%d" % (w, h, r, d))
            win.title("Bill: Update Window")
            win.configure(background="black")
            win.resizable(0, 0)

            def put():
                set_pm("Cash")
                win.destroy()

            b1 = Button(win, text="Cash", command=(lambda: put()))
            b1.place(x=5, y=10)

            def ent():
                def usertxt(event):
                    cheq.delete(0, END)

                cheq = Entry(win, text="", width=30)
                cheq.place(x=10, y=50)
                cheq.insert(0, "Write cheque number")
                cheq.bind("<Button-1>", usertxt)

                def sett():
                    if (
                        str(cheq.get()) != "Write cheque number"
                        and str(cheq.get()).isdigit()
                    ):
                        print("cheq:", cheq.get(), self.payment_method)
                        set_pm(cheq.get())
                        win.destroy()
                    else:
                        messagebox.showerror("Error", "Wrong cheque details")

                b3 = Button(win, text="done", command=lambda: sett())
                b3.place(x=30, y=120)

            b2 = Button(win, text="Cheque", command=lambda: ent())
            b2.place(x=100, y=10)
            win.mainloop()

        combx = Combobox(ws, width=15, state="readonly")
        combx.bind("<<ComboboxSelected>>", modify)
        combx.place(x=20, y=70)
        combx["values"] = ["Paid", "Unpaid"]
        combx.set("Payment is :")

        print("payset:", self.payment_method)

        combmonth = Combobox(ws, width=15, state="readonly")
        combmonth.place(x=20, y=100)
        combmonth["values"] = [
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
        combmonth.set("month is :")
        combmonth.current()

        def usertxt(event):
            year.delete(0, END)

        sat2 = StringVar()
        year = Entry(ws, textvariable=sat2, width=10)
        year.place(x=150, y=100)
        year.insert(0, "Write year")
        year.bind("<Button-1>", usertxt)
        txt = sct.ScrolledText(ws, height=5, width=25, state="disable")
        txt.place(x=20, y=140)

        def update_sat():
            global payment_method
            if (
                combx.get() == "Payment is :"
                or combmonth.get() == "month is :"
                or (year.get() == "Write year" and len(year.get()) > 4)
            ):
                # messagebox.showerror("Error.","Not complete details enter Payment status,month,year.")
                messagebox.showwarning(
                    "Error.", "Not complete details enter Payment status,month,year."
                )
            else:
                # print(len(year.get()),year.get())
                # print("payment method:",self.payment_method)
                if len(year.get()) == 4:
                    payment = combx.get()
                    month_year = str(combmonth.get()) + "_" + str(year.get())
                    print(
                        "room :",
                        roomd,
                        payment,
                        " month_year:",
                        month_year,
                        " mode paid as:",
                        self.payment_method,
                    )
                    cp = sqlite3.connect(db_file_name)
                    cr = cp.cursor()
                    roomn = ""
                    for rm in range(len(roomd)):
                        if rm == 0:
                            roomn = str(roomd[rm]).upper()
                        else:
                            roomn += str(roomd[rm])
                    mony = ""
                    for my in range(len(month_year)):
                        if my == 0:
                            mony = str(month_year[0]).upper()
                        else:
                            mony += str(month_year[my]).lower()
                    sql = f"""update  All_Bill_info set Mode='{self.payment_method}',Payment_status='{payment}' where Roomno='{roomn}' and Month_year='{mony}';"""
                    print(sql, "\n", (self.payment_method, payment, roomd, month_year))
                    cr.execute(sql)  # ,(self.payment_method,payment,roomd,month_year))
                    cp.commit()
                    cp.close()
                    self.get_status()
                    msg = f""" Month year:{month_year} \n Payment method :{self.payment_method} \n(Cash/cheque)\n\n Payment : {payment} """
                    print(msg)
                    txt.configure(state="normal")
                    txt.delete("1.0", "end")
                    txt.insert("end", msg)
                    txt.configure(state="disable")
                else:
                    messagebox.showerror("Error.", "year something wrong.")

        Button(ws, text="confirm", width=10, command=lambda: update_sat()).place(
            x=40, y=240
        )
        Button(ws, text="cancel", width=10, command=(lambda: on_quit())).place(
            x=140, y=240
        )
        win_search.mainloop()
        # end

    def Billstatus_btn1_op(self):

        print("Bill status clicked")
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_billstatus_pg3)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">Bill Status</span></p></body></html>',
                None,
            )
        )
        ######################################################################
        self.viewof = ""
        self.monthof = ""
        print("last month :", str(self.today_date)[5:7])
        lst_month = int(str(self.today_date)[5:7]) - 2
        self.ui.SR2_top_month_comboBox.setCurrentIndex(lst_month)
        # self.ui.SR2_top_viewtype_comboBox.setCurrentIndex(0)
        self.viewof = self.ui.SR2_top_viewtype_comboBox.currentText()
        self.monthof = self.ui.SR2_top_month_comboBox.currentText()
        print(">>", self.viewof, self.monthof)
        brushls = QBrush(QColor(0, 255, 155, 255))
        brushls.setStyle(Qt.SolidPattern)
        fontls = QFont()
        fontls.setFamily("Segoe UI Semibold")
        fontls.setPointSize(11)
        self.get_status()

        self.ui.SR2_top_update_btn.clicked.connect(
            lambda: self.bill_status_search(self.tbs_data, 2)
        )
        self.ui.SR2_top_search_btn.clicked.connect(
            lambda: self.bill_status_search(self.tbs_data, 1)
        )
        print(">> tbs data : ", self.tbs_data)
        ###########
        cont = 0
        for i in self.tbs_data:
            if int(i[5]) > 0:
                cont += 1
        con = f'''"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#55aaff;\">Total fine bills:{cont}</span></p></body></html>"'''
        self.ui.SR2_down_Ttfines.setText(
            QCoreApplication.translate("Society_MainWindow", con, None)
        )
        #########
        def total_res():
            c = sqlite3.connect(db_file_name)
            cur = c.cursor()
            cur.execute("select Count(*) from Society_info_mem;")
            total_res = cur.fetchall()
            c.close()
            return total_res[0][0]

        con = f''' "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffaaff;\">Total Residence : {total_res()}</span></p></body></html>"'''
        self.ui.SR_down_ttresidence.setText(
            QCoreApplication.translate("Society_MainWindow", con, None)
        )
        #########
        self.total_row = 0

        def set_fine(x):
            cont = 0
            for i in x:
                if int(i[5]) > 0:
                    cont += 1
                if len(x) == 0:
                    cont = 0
            con = f'''"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#55aaff;\">Total fine bills:{cont}</span></p></body></html>"'''
            self.ui.SR2_down_Ttfines.setText(
                QCoreApplication.translate("Society_MainWindow", con, None)
            )

        def set_all(month):
            print("all set")
            dataall = []
            for item in self.tbs_data:
                print("row >:", item, item[3])
                st = ""
                for i in item[3]:
                    if i == "_":
                        break
                    else:
                        st += i
                mon = st
                if str(mon).casefold() == str(month).casefold():
                    if item not in dataall:
                        dataall.append(item)
            set_fine(dataall)
            # print("\n dta all :",dataall)
            self.ui.SR2_billstatus_tableWidget.setRowCount(len(dataall))
            for row_number, row_data in enumerate(dataall):
                print("row add :", row_data)
                self.total_row = row_number + 1
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

        def set_all_unpaid(month):
            print("all unpaid set")

            def UnPaid(x):
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

            all_unpaid = []
            for i in self.tbs_data:
                st = ""
                for _1 in i[3]:
                    if _1 == "_":
                        break
                    else:
                        st += _1
                mon = st
                print("unpaids:", "unpaid" in [str(k).casefold() for k in i])
                if ("unpaid" in [str(k).casefold() for k in i]) and str(
                    mon
                ).casefold() == str(month).casefold():
                    all_unpaid.append(i)
            set_fine(all_unpaid)
            for row_number, row_data in enumerate(all_unpaid):
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if str(data).casefold() == "unpaid":
                        UnPaid(row_data)

        def set_all_paid(month):
            print("all paid set")

            def Paid(x):
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

            all_paid = []
            for i in self.tbs_data:
                st = ""
                for _1 in i[3]:
                    if _1 == "_":
                        break
                    else:
                        st += _1
                mon = st
                print(">>> mon :", mon, [str(k).casefold() for k in i])
                if ("paid" in [str(k).casefold() for k in i]) and str(
                    mon
                ).casefold() == str(month).casefold():
                    print("paids:", i)
                    all_paid.append(i)
            set_fine(all_paid)
            for row_number, row_data in enumerate(all_paid):
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if data in ["paid", "Paid"]:
                        Paid(row_data)

        def set_all_Awing(month):
            print("all a wing set")

            def awing(x):
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

            all_awing = []
            for i in self.tbs_data:
                st = ""
                for _1 in i[3]:
                    if _1 == "_":
                        break
                    else:
                        st += _1
                mon = st
                print(
                    "paids:", "A/" in i[0], str(mon).casefold(), str(month).casefold()
                )
                if ("A/" in i[0]) and str(mon).casefold() == str(month).casefold():
                    all_awing.append(i)
            set_fine(all_awing)
            for row_number, row_data in enumerate(all_awing):
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                awing(row_data)

        def set_all_Bwing(month):
            print("all b wing set")

            def bwing(x):
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

            all_bwing = []
            for i in self.tbs_data:
                print("paids:", "B/" in i[0], i[0])
                st = ""
                for _1 in i[3]:
                    if _1 == "_":
                        break
                    else:
                        st += _1
                mon = st
                if ("B/" in i[0]) and str(mon).casefold() == str(month).casefold():
                    all_bwing.append(i)
            set_fine(all_bwing)
            for row_number, row_data in enumerate(all_bwing):
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                bwing(row_data)

        def set_all_Cwing(month):
            print("all b wing set")

            def cwing(x):
                for column_number, data in enumerate(row_data):
                    qtablewidgetitemls = QTableWidgetItem()
                    qtablewidgetitemls.setText(str(data))
                    qtablewidgetitemls.setFont(fontls)
                    qtablewidgetitemls.setForeground(brushls)
                    self.ui.SR2_billstatus_tableWidget.setItem(
                        row_number, column_number, qtablewidgetitemls
                    )

            all_cwing = []
            for i in self.tbs_data:
                print("paids:", "C/" in i[0], i[0])
                st = ""
                for _1 in i[3]:
                    if _1 == "_":
                        break
                    else:
                        st += _1
                mon = st
                if ("C/" in i[0]) and str(mon).casefold() == str(month).casefold():
                    all_cwing.append(i)
            set_fine(all_cwing)
            for row_number, row_data in enumerate(all_cwing):
                self.ui.SR2_billstatus_tableWidget.insertRow(row_number)
                cwing(row_data)

        set_all(self.ui.SR2_top_month_comboBox.currentText)

        def set_rowc():
            con = f""""<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffaa7f;\">Total Rows : {self.total_row}</span></p></body></html>" """
            self.ui.SR2_down_ttrows.setText(
                QCoreApplication.translate("Society_MainWindow", con, None)
            )

        set_rowc()

        def load_bill_status(viewof, month):
            print(
                "refresh clicked : empty the rows",
            )
            self.ui.SR2_billstatus_tableWidget.setRowCount(0)
            print(">>data view of :", viewof, "\n>> month : ", month)
            if viewof == "ALL":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all(month)
                print(
                    ">>>>>>>>>>>>>>>>>>>>row count : start1 :",
                    self.ui.SR2_billstatus_tableWidget.rowCount(),
                    self.total_row,
                    month,
                )
            elif viewof == "ALL Paid":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all_paid(month)
                self.total_row = self.ui.SR2_billstatus_tableWidget.rowCount()
                print(
                    ">>>>>>>>>>>>>>>>>>>>row count : start2 :",
                    self.ui.SR2_billstatus_tableWidget.rowCount(),
                    self.total_row,
                )
            elif viewof == "ALL UnPaid":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all_unpaid(month)
                self.total_row = self.ui.SR2_billstatus_tableWidget.rowCount()
                print(
                    ">>>>>>>>>>>>>>>>>>>>row count : start3 :",
                    self.ui.SR2_billstatus_tableWidget.rowCount(),
                    self.total_row,
                )
            elif viewof == "A Wing":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all_Awing(month)
                self.total_row = self.ui.SR2_billstatus_tableWidget.rowCount()
                print(">>>>>>>>>>>>>>>>>>>>row count : start3 :", self.total_row)
            elif viewof == "B Wing":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all_Bwing(month)
                self.total_row = self.ui.SR2_billstatus_tableWidget.rowCount()
                print(">>>>>>>>>>>>>>>>>>>>row count : start3 :", self.total_row)
            elif viewof == "C Wing":
                self.ui.SR2_billstatus_tableWidget.setRowCount(0)
                set_all_Cwing(month)
                self.total_row = self.ui.SR2_billstatus_tableWidget.rowCount()
                print(">>>>>>>>>>>>>>>>>>>>row count : start3 :", self.total_row)
            else:
                print("Error no proper data ...")
            set_rowc()
            # self.SR2_billstatus_tableWidget.item(0, 2)

        def set_opt():
            self.ui.SR2_billstatus_tableWidget.clearSelection()
            self.viewof = self.ui.SR2_top_viewtype_comboBox.currentText()
            self.monthof = self.ui.SR2_top_month_comboBox.currentText()
            print(">>", self.viewof, self.monthof)
            load_bill_status(self.viewof, self.monthof)

        self.ui.SR2_refresh_pg3.clicked.connect(lambda: set_opt())
        # end

    def Conwebwhatsapp_btn1_op(self):
        print("connect web whatsapp clicked")
        self.ui.SR_stackedWidget.setCurrentIndex(0)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">On Google : Connect web-WhatsApp</span></p></body></html>',
                None,
            )
        )
        # os.start("start location chrome.exe 'www.webwhatsapp.com' --kiosk")
        webbrowser.open_new_tab("https://web.whatsapp.com/")  # new=2)

    def delete_res(self):
        print("Delete request")
        self.reset_det()
        self.admall = [i[0] for i in self.fetall]
        # print(" datas have :",self.admall)
        self.del_win(self.admall)

    def del_win(self, x):
        win_search = Tk()
        ws = win_search

        def set_win():
            w, h = 360, 250
            r, d = 300, 150
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            win_search.title("Society : Delete Record ")
            win_search.configure(background="black")
            win_search.resizable(0, 0)

        set_win()

        def room1(event):
            room.delete(0, END)

        def wing1(event):
            wing.delete(0, END)

        Label(ws, text="Room no. :").place(x=10, y=20)
        Label(ws, text="Wing (A/B/C):").place(x=180, y=20)
        rm = StringVar()
        room = Entry(ws, text=rm, width=10)
        wg = StringVar()
        wing = Entry(ws, text=wg, width=10)
        room.place(x=90, y=20)
        wing.place(x=270, y=20)
        room.bind("<Button-1>", room1)
        wing.bind("<Button-1>", wing1)

        txt = sct.ScrolledText(ws, height=10, width=46, font=("", 9))
        header = " Details :\n\t\tdelete result"
        txt.insert(
            "end",
            header + "\n",
        )
        txt.insert("end", "_" * 46)
        txt.configure(state="disable")
        txt.place(x=10, y=60)

        def delete(x):
            print("x deleted", x)
            rm1 = str(room.get())
            wg1 = wing.get().casefold()
            print("room :", room.get(), "\nwing :", wing.get())
            if (
                (rm1 != "" or rm1.isdigit())
                and len(str(wg1)) != 1
                or (str(wg1).casefold() not in [chr(i) for i in range(97 + 26)])
            ):
                txt.configure(state="normal")
                txt.insert("end", "Wrond details..Failed\n")
                txt.configure(state="disable")
                messagebox.showerror(
                    "Wrong Details", "Room no. / Wing in wrong combination.."
                )
            else:
                txt.configure(state="normal")
                txt.insert("end", "\nProcess delete...\n")
                txt.configure(state="disable")
                dop = wg1 + rm1
                ch = False
                for i in x:
                    print(dop, i, dop.casefold() in i.casefold())
                    if dop.casefold() in i.casefold():
                        ch = True
                        pd = x.pop(x.index(i))
                if ch:
                    print("deleted")
                    con = sqlite3.connect(db_file_name)
                    cur = con.cursor()
                    sql = f"delete from Society_info_mem where People_id='{pd}'"  # Roomno='{rm1}' and Wing LIKe '{wg1.upper()}' ;"
                    print("sql>", sql)
                    cur.execute(sql)
                    cr = ("row delete:", cur.rowcount)
                    print(cr)
                    con.commit()
                    con.close()
                    txt.configure(state="normal")
                    txt.insert(
                        "end",
                        f"\nDeletion successful of :\nWing/room : {wg1}/{rm1}\n{cr}",
                    )
                    txt.configure(state="disable")
                else:
                    messagebox.showerror(
                        "Wrong Details", "Room no. / Wing not in records."
                    )
                    txt.configure(state="normal")
                    txt.insert(
                        "end",
                        f"\nDeletion Failed of :\nWing/room : {wg1}/{rm1} not in records. ",
                    )
                    txt.configure(state="disable")

        Button(ws, text="Delete", width=20, command=(lambda: delete(x))).place(
            x=10, y=220
        )
        Button(
            ws, text="close", width=20, command=(lambda: win_search.destroy())
        ).place(x=210, y=220)
        win_search.mainloop()

    def updatinfo_btn1_op(self):
        self.reset_det()
        print("Update information ")
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_addupdate_pg5)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">Members Details </span></p></body></html>',
                None,
            )
        )
        self.ui.SR2_main_genratelineEdit_2.setEchoMode(QLineEdit.Password)
        self.ui.SR2_addmem_pushButton_3.clicked.connect(lambda: self.add_new_mem())
        self.ids = [i[0] for i in self.fetall]
        self.ui.SR2_Email_lineEdit_6.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.ui.SR2_main_generatepushButton_5.clicked.connect(
            lambda: self.generate_op("----", "")
        )
        # end

    def setform(self, detail):
        print("update request:", detail)

        def set_aor_res(x):
            if str(x).casefold()[0:3] == "res":
                self.ui.SR2_main_genratelineEdit_2.setText(x)
                self.ui.SR2_admin_radioButton.setChecked(False)
            if str(x).casefold()[0:3] == "soa":
                self.ui.SR2_main_genratelineEdit_2.setText(x)
                self.ui.SR2_admin_radioButton.setChecked(True)

        set_aor_res(detail[0])

        def set_name(x, y):
            self.ui.nameLineEdit.setText(x)
            self.ui.surname_lineEdit_4.setText(y)

        set_name(detail[1], detail[2])

        def set_billid(id):
            self.ui.SR2_autoBillid_lineEdit_9.setText(id)

        set_billid(detail[9])

        def set_roomno(x):
            self.ui.SR2_Roomno_comboBox_2.setText(str(x))

        set_roomno(detail[3])

        def set_wing(x):
            print(x, ord(str(x[0]).casefold()) - 97)
            ind = ord(str(x[0]).casefold()) - 97
            self.ui.SR2_wing_comboBox_4.setCurrentIndex(ind)

        set_wing(detail[11])

        def set_phone(x):
            self.ui.Sr2_Phone_lineEdit_5.setText(str(x))

        set_phone(detail[4])

        def set_email(x):
            self.ui.SR2_Email_lineEdit_6.setText(str(x))

        set_email(detail[5])

        def set_flatarea(x):
            self.ui.SR2_flatarea_lineEdit_7.setMaxLength(6)
            self.ui.SR2_flatarea_lineEdit_7.setText(str(x))

        set_flatarea(detail[8])

        def set_flattype(x):
            self.ui.Flattype_comboBox_3.setCurrentIndex(int(x[0]) - 1)

        set_flattype(detail[6])

        def set_vhicle_count(x):
            self.ui.SR2_vhiclecount_spinBox.setValue(int(x))

        set_vhicle_count(detail[7])
        self.ui.SR2_updatemem_pushButton_2.clicked.connect(
            lambda: self.update_mem_info()
        )

    def update_mem_info(self):

        print("Update saving request  . . .")
        n1, n2, r3, r4, c5, em6, fa7, ft8, vc9 = (
            self.ui.nameLineEdit.text(),
            self.ui.surname_lineEdit_4.text(),
            self.ui.SR2_Roomno_comboBox_2.text(),
            self.ui.SR2_wing_comboBox_4.currentText(),
            self.ui.Sr2_Phone_lineEdit_5.text(),
            self.ui.SR2_Email_lineEdit_6.text(),
            self.ui.SR2_flatarea_lineEdit_7.text(),
            self.ui.Flattype_comboBox_3.currentText(),
            self.ui.SR2_vhiclecount_spinBox.value(),
        )
        print(
            "\n\ndata before :",
        )
        old = []
        for i in self.fetall:
            # print(">>",i)
            if (n1 and n2) in i:
                # print(">>before",i)
                old = i
        new = ["", n1, n2, r3, c5, em6, ft8, vc9, fa7, "", "", r4]
        # print("\n\n after :",new)#[n1,n2,r3,r4,c5,em6,fa7,ft8,vc9])
        def updd(old, new):
            print("new def :", new)
            for i in range(len(old)):
                print(">>>>>", old[i], "\\??", new[i])
                if new[i] == "":
                    new.pop(new.index(new[i]))
                    new.insert(i, old[i])
            new.pop(len(new) - 1)
            new.append(old[-1])
            new.insert(len(new) - 1, self.get_billamt([int(vc9), float(fa7)]))
            print("total bill amt : \nUpdated :", new)

        updd(old, new)

        con = sqlite3.connect(db_file_name)
        cur = con.cursor()
        try:
            dele = new[0]
            dlt = cur.execute(
                f"delete from Society_info_mem where People_id='{dele}'; "
            )
            print("\n row deleted:", cur.rowcount)
            con.commit()
            sql_add = (
                f""" insert into Society_info_mem values(?,?,?,?,?,?,?,?,?,?,?,?);"""
            )
            print("updated :", len("????????????"), len(new))
            cur.execute(sql_add, new)
            con.commit()

            def showmsg():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Successfully Data updated")
                msg.setWindowTitle("complete Updating")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.buttonClicked.connect(lambda: self.reset_det())
                msg.exec_()

            showmsg()
        except Exception as eer:
            print("error :", eer)
        con.close()

    def add_new_mem(self):
        print("new Members request..")
        self.billid = [i[9] for i in self.fetall]
        print("all BLL id:", self.billid)
        self.new_add = []
        n1, n2, r3, r4, c5, em6, fa7, ft8, vc9 = (
            self.ui.nameLineEdit.text(),
            self.ui.surname_lineEdit_4.text(),
            self.ui.SR2_Roomno_comboBox_2.text(),
            self.ui.SR2_wing_comboBox_4.currentText(),
            self.ui.Sr2_Phone_lineEdit_5.text(),
            self.ui.SR2_Email_lineEdit_6.text(),
            self.ui.SR2_flatarea_lineEdit_7.text(),
            self.ui.Flattype_comboBox_3.currentText(),
            self.ui.SR2_vhiclecount_spinBox.value(),
        )
        print(
            "\n data new form :",
            n1,
            n2,
            r3,
            r4,
            c5,
            em6,
            fa7,
            ft8,
            vc9,
            str(r3).isdigit(),
        )
        try:
            if (
                n1 == ""
                or n2 == ""
                or r3 == ""
                or r4 == ""
                or c5 == ""
                or em6 == ""
                or fa7 == ""
                or ft8 == ""
                or vc9 == ""
            ):
                print("Field empty error:")
                raise Exception
            else:
                if (
                    str(r3).isdigit() == False
                    or str(c5).isdigit() == False
                    or len(str(r3)) < 3
                    or str(fa7).isdigit() == False
                    or len(str(c5)) != 10
                ):
                    print("Digit error")
                    raise Exception
                else:
                    if (".com" not in em6) or ("@" not in em6) or len(str(em6)) < 10:
                        print("email error")
                        raise Exception
                    else:
                        for i in self.fetall:
                            print(
                                "check wing / room :",
                                str(str(r4) + "/" + str(r3)).casefold(),
                                str(str(i[-1][0]) + "/" + str(i[3])).casefold(),
                                str(str(r4) + "/" + str(r3)).casefold()
                                in str(str(i[-1][0]) + "/" + str(i[3])).casefold(),
                            )
                            if (
                                str(str(r4) + "/" + str(r3)).casefold()
                                in str(str(i[-1][0]) + "/" + str(i[3])).casefold()
                            ):
                                QMessageBox.warning(
                                    QMessageBox(),
                                    "Incomplete form",
                                    f'{str(str(i[-1][0])+"/"+str(i[3]))} already exist try for upate if same wing/room .',
                                )
                        else:
                            print("Form Complete")
                            pp = str(r4).casefold() + str(r3)
                            bl = str("BLL") + str(r3) + str(r4).casefold()
                            wing = str(r4).upper() + "-wing"
                            self.generate_op(pp, bl)
                            blamt = self.get_billamt([int(vc9), float(fa7)])
                            print(
                                "all data send for save :\n",
                                pp,
                                n1,
                                n2,
                                r3,
                                c5,
                                em6,
                                ft8,
                                vc9,
                                fa7,
                                bl,
                                blamt,
                                wing,
                            )
                            self.add_new_memdb(
                                [n1, n2, r3, c5, em6, ft8, vc9, fa7, bl, blamt, wing]
                            )
        except Exception as err:
            print("ALL field not filled correct", err)
            QMessageBox.warning(
                QMessageBox(),
                "Incomplete form",
                "Fill all field correct.\n Check for contact has only number\nemail as @ and .com correct\nroom no is only digits.",
            )

    def add_new_memdb(self, data):
        print("saving to db :", data)
        print("peopleid :", self.ui.SR2_main_genratelineEdit_2.text())
        if len(self.ui.SR2_main_genratelineEdit_2.text()) == 0:
            pp = str(data[10][0]).casefold() + str(data[2])
            bl = str("BLL") + str(data[2]) + str(data[-1][0]).casefold()
            self.generate_op(pp, bl)
        print(">>>>>>", self.ui.SR2_main_genratelineEdit_2.text())
        data.insert(0, str(self.ui.SR2_main_genratelineEdit_2.text()))
        print("\n\nsaved data:", data)
        con = sqlite3.connect(db_file_name)
        cur = con.cursor()
        sql_add = f""" insert into Society_info_mem values(?,?,?,?,?,?,?,?,?,?,?,?);"""
        cur.execute(sql_add, data)
        con.commit()

        def showmsg():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Successfully Data Upload")
            msg.setWindowTitle("Upload complete")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: self.reset_det())
            msg.exec_()

        showmsg()
        con.close()

    def get_billamt(self, a):
        print("Check charges and give bill amount", a)
        self.get_dcharges()
        print("Bill amounts :", self.dc_data[0])
        bilamt = 0
        dcb = self.dc_data[0]
        for i in range(len(dcb)):
            if i == 8:
                bilamt += a[0] * dcb[i]
                print("parking :", a[0], "*", dcb[i], " add :", a[0] * dcb[i], bilamt)
            elif i in (0, 1, 2) and a[1] > 400:
                bilamt += dcb[i] + 50
                print("maintenance water service added", bilamt)
            elif i < 11:
                print("other charges :", dcb[i])
                bilamt += float(dcb[i])
                break

        def showmsg():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Maintenance Bill charges added\nyour total : {bilamt}")
            msg.setWindowTitle("Bill Charges")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.buttonClicked.connect(lambda: self.reset_det())
            msg.exec_()

        showmsg()
        return bilamt

    def setids(self, pp, bll):
        print("\n\nid recevied", pp, bll)
        self.ui.SR2_main_genratelineEdit_2.setText(pp)
        self.ui.SR2_autoBillid_lineEdit_9.setText(bll)
        # end

    def generate_op(self, pp, bll):
        print("people id requested.../:", pp, bll)
        # backsr _ wing+room
        if self.ui.SR2_admin_radioButton.isChecked():
            print("New admin id needed.../:")
            id1 = "soa_" + pp
            self.setids(id1, bll)

        else:
            print("New Recidency People_id...")
            id2 = "res_" + pp
            self.setids(id2, bll)
        # end

    def showdet(self, data):
        win_search = Tk()
        ws = win_search

        def set_win():
            w, h = 360, 400
            r, d = 300, 50
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            # root.winfo_screenwidth()-100, root.winfo_screenheight()-100
            # height x width + position right + position down
            win_search.title("Society Maintenance-Bill Management : Search Window")
            win_search.configure(background="black")
            # win_search.resizable(0,0)

        set_win()
        print("setxt:", data)
        details = f"""
                Name    :  {data[1]} {data[2]}

                Room    :  {data[3]}
                wing    :  {data[11]}

                Contact :  {data[4]}
                Email   :  {data[5]}

                FLat type : {data[6]}
                flat area : {data[8]}

                vehicles : {data[7]}

                Bill id :  {data[9]}
                Bill amount :{data[10]} Rs
            """

        def settxt(d):
            txt = sct.ScrolledText(ws, height=20, width=40, font=("", 9))
            header = " Details :\n\t\tSearch result"
            txt.insert(
                "end",
                header + "\n",
            )

            txt.insert("end", "_" * 40)
            txt.insert("end", d)
            txt.configure(state="disable")
            txt.place(x=10, y=20)
            self.zoom = 9

            def zoomin():
                print("zoomin:", self.zoom)
                if self.zoom > 10:
                    txt.configure(font=("", 10))
                else:
                    self.zoom += 1
                    txt.configure(font=("", self.zoom))

            def zoomout():
                print("zoomout:", self.zoom)
                if self.zoom == 5:
                    txt.configure(font=("", 10))
                else:
                    self.zoom -= 1
                    txt.configure(font=("", self.zoom))

            Button(ws, text="zoom +", width=10, command=(lambda: zoomin())).place(
                x=10, y=360
            )
            Button(ws, text="zoom -", width=10, command=(lambda: zoomout())).place(
                x=90, y=360
            )
            Button(
                ws, text="close", width=10, command=(lambda: win_search.destroy())
            ).place(x=250, y=360)

        def update_req():
            self.setform(data)
            ws.destroy()

        Button(ws, text="update", width=10, command=(lambda: update_req())).place(
            x=170, y=360
        )
        settxt(details)
        win_search.mainloop()

    def search_pp(self):
        def validrm(rm):
            if str(rm) != "":
                if (
                    len(rm) == 5
                    and str(rm[0]).casefold() in [chr(i) for i in range(97 + 26)]
                    and str(rm[2:5]).isdigit()
                ):
                    return True
            return False

        def checkrm(rm):
            for i in self.fetall:
                rm1 = str(str(i[11])[0]).casefold() + "/" + str(i[3])
                print("comapre :", str(rm).casefold(), rm1)
                if str(rm).casefold() == rm1:
                    print("yes Founded")
                    return i
            return []

        spp = ""
        spp = self.ui.SR_addup_search_lineEdit.text()
        try:
            print("validate :", spp != "", " and ", validrm(spp))
            if spp != "" and validrm(spp):
                print("search for :", spp)
                ff = checkrm(spp)
                print("result:", ff, len(ff))
                if len(ff) < 1:
                    # print("error 1")
                    raise Exception
                else:
                    print("show information window", ff)
                    self.showdet(ff)
            else:
                # print("error 2")
                raise Exception
        except Exception as ee:
            print("Error", ee)
            QMessageBox.warning(
                QMessageBox(), "Error", "Could not Search Wrong Room and wing."
            )

    def reset_det(self):
        self.ui.SR_addup_search_lineEdit.setText("")
        self.ui.SR2_main_genratelineEdit_2.setText("")
        self.ui.SR2_autoBillid_lineEdit_9.setText("")
        self.ui.nameLineEdit.setText("")
        self.ui.surname_lineEdit_4.setText("")
        self.ui.Sr2_Phone_lineEdit_5.setText("")
        self.ui.SR2_Email_lineEdit_6.setText("")
        self.ui.SR2_flatarea_lineEdit_7.setText("")
        self.ui.SR2_Roomno_comboBox_2.setText("")
        self.ui.SR2_wing_comboBox_4.setCurrentIndex(-1)
        self.ui.Flattype_comboBox_3.setCurrentIndex(-1)
        self.ui.SR2_admin_radioButton.setChecked(False)
        self.ui.SR2_vhiclecount_spinBox.setValue(0)

        def getdd():
            con = sqlite3.connect(db_file_name)
            cur = con.cursor()
            sql = "select * from Society_info_mem;"
            cur.execute(sql)
            self.fetall = cur.fetchall()
            # print(self.fetall)
            self.admall = [i for i in self.fetall if "soa" in i[0]]
            # print("all admins:",self.admall)
            con.commit()
            con.close()

        getdd()

    def SL1_Upaidbill_btn1_op(self):
        print("unpaid list clicked")
        self.ui.SR2_top_viewtype_comboBox.setCurrentIndex(5)
        self.curr_month = QDate.currentDate().month()  # Month()
        print("current month : ", self.curr_month)
        self.ui.SR2_top_month_comboBox.setCurrentIndex(self.curr_month - 1)
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_billstatus_pg3)
        self.ui.SR2_top_viewtype_comboBox.setCurrentText("UnPaid")
        self.Billstatus_btn1_op()

    def SL1_dcharges_btn1_op(self):
        print("default charges list clicked")
        self.ui.Right_update_groupBox_4.hide()
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_Default_charges)
        self.ui.Title_txt.setText(
            QCoreApplication.translate(
                "Society_MainWindow",
                '<html><head/><body><p><span style=" text-decoration: underline; color:#00ffff;">Default Charges</span></p></body></html>',
                None,
            )
        )
        self.get_dcharges()
        print("set charges :", self.dc_data)

        def set_view_charges():
            ds = self.dc_data[0]
            """ demo formate
    1       2           3       4               5           6           7               8       9               10      11
    Service	Maintenance	Water	Sinking_fund	Repair	Festival_fund	Club_house	Parking	Total_charges	Last_update	Fine
    250	    250	        150	    50	             120	   50	          50	     50	         970	    2020-06-01	100
            """

            v1 = f"""{ds[0]} Rs"""  # servce
            self.ui.lineEdit_1.setText(
                QCoreApplication.translate("Society_MainWindow", v1, None)
            )
            self.ui.lineEdit_31.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v1, None)
            )
            self.ui.lineEdit_31.setText(str(ds[0]))

            v2 = f"""{ds[1]} Rs"""  # Maintenance
            self.ui.lineEdit_2.setText(
                QCoreApplication.translate("Society_MainWindow", v2, None)
            )
            self.ui.lineEdit_32.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v2, None)
            )
            self.ui.lineEdit_32.setText(str(ds[1]))

            v3 = f"""{ds[2]} Rs"""  # water
            self.ui.lineEdit_3.setText(
                QCoreApplication.translate("Society_MainWindow", v3, None)
            )
            self.ui.lineEdit_33.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v3, None)
            )
            self.ui.lineEdit_33.setText(str(ds[2]))

            v4 = f"""{ds[3]} Rs"""  # sinking
            self.ui.lineEdit_4.setText(
                QCoreApplication.translate("Society_MainWindow", v4, None)
            )
            self.ui.lineEdit_34.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v4, None)
            )
            self.ui.lineEdit_34.setText(str(ds[3]))

            v5 = f"""{ds[4]} Rs"""  # repair
            self.ui.lineEdit_5.setText(
                QCoreApplication.translate("Society_MainWindow", v5, None)
            )
            self.ui.lineEdit_35.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v5, None)
            )
            self.ui.lineEdit_35.setText(str(ds[4]))

            v6 = f"""{ds[5]} Rs"""  # festival
            self.ui.lineEdit_6.setText(
                QCoreApplication.translate("Society_MainWindow", v6, None)
            )
            self.ui.lineEdit_36.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v6, None)
            )
            self.ui.lineEdit_36.setText(str(ds[5]))

            v7 = f"""{ds[6]} Rs"""  # club House
            self.ui.lineEdit_7.setText(
                QCoreApplication.translate("Society_MainWindow", v7, None)
            )
            self.ui.lineEdit_37.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v7, None)
            )
            self.ui.lineEdit_37.setText(str(ds[6]))

            v8 = f"""{ds[10]} Rs"""  # fine
            self.ui.lineEdit_8.setText(
                QCoreApplication.translate("Society_MainWindow", v8, None)
            )
            self.ui.lineEdit_38.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v8, None)
            )
            self.ui.lineEdit_38.setText(str(ds[10]))

            v9 = f"""{ds[7]} Rs"""  # parking
            self.ui.lineEdit_9.setText(
                QCoreApplication.translate("Society_MainWindow", v9, None)
            )
            self.ui.lineEdit_39.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v9, None)
            )
            self.ui.lineEdit_39.setText(str(ds[7]))

            v10 = f"{ds[8]} Rs"  # Total_charges
            self.ui.lineEdit_10.setText(
                QCoreApplication.translate("Society_MainWindow", v10, None)
            )
            self.ui.lineEdit_40.setPlaceholderText(
                QCoreApplication.translate("Society_MainWindow", v10, None)
            )

            def daat(x):
                v13 = f'''"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:pink;\"> {x} </span></p></body></html>"'''
                return v13

            self.ui.label_13.setText(
                QCoreApplication.translate(
                    "Society_MainWindow", daat(f"Last update :<br>{str(ds[9])}"), None
                )
            )
            self.ui.label_24.setText(
                QCoreApplication.translate(
                    "Society_MainWindow", daat(f"today date<br>{self.today_date}"), None
                )
            )

        set_view_charges()
        # print("note place holder:",self.ui.lineEdit_31.placeholderText())
        def update_db():
            self.ui.Right_update_groupBox_4.show()
            self.td10 = self.today_date
            self.ui.lineEdit_40.setReadOnly(True)
            # self.ui.setbtpushButton_3.setText("get total")
            def total_cal():
                try:
                    try:
                        (
                            self.p1,
                            self.p2,
                            self.p3,
                            self.p4,
                            self.p5,
                            self.p6,
                            self.p7,
                            self.p8,
                            self.p10,
                        ) = (
                            self.ui.lineEdit_31.text(),
                            self.ui.lineEdit_32.text(),
                            self.ui.lineEdit_33.text(),
                            self.ui.lineEdit_34.text(),
                            self.ui.lineEdit_35.text(),
                            self.ui.lineEdit_36.text(),
                            self.ui.lineEdit_37.text(),
                            self.ui.lineEdit_39.text(),
                            self.ui.lineEdit_38.text(),
                        )
                        self.total = (
                            float(self.p1)
                            + float(self.p2)
                            + float(self.p3)
                            + float(self.p4)
                            + float(self.p5)
                            + float(self.p6)
                            + float(self.p7)
                            + float(self.p8)
                            + float(self.p10)
                        )
                    except:
                        print("error")
                        raise Exception
                except:
                    if self.p1 == "":
                        self.p1 = 0
                    if self.p2 == "":
                        self.p2 = 0
                    if self.p3 == "":
                        self.p3 = 0
                    if self.p4 == "":
                        self.p4 = 0
                    if self.p5 == "":
                        self.p5 = 0
                    if self.p6 == "":
                        self.p6 = 0
                    if self.p7 == "":
                        self.p7 = 0
                    if self.p8 == "":
                        self.p8 = 0
                    if self.p10 == "":
                        self.p10 = 0
                    try:
                        self.total = (
                            float(self.p1)
                            + float(self.p2)
                            + float(self.p3)
                            + float(self.p4)
                            + float(self.p5)
                            + float(self.p6)
                            + float(self.p7)
                            + float(self.p8)
                            + float(self.p10)
                        )
                    except:
                        QMessageBox.warning(
                            QMessageBox(), "Error", "Press Only digit \n not Characters"
                        )
                        set_view_charges()

                print(
                    "\nvalues:",
                    self.p1,
                    self.p2,
                    self.p3,
                    self.p4,
                    self.p5,
                    self.p6,
                    self.p7,
                    self.p8,
                    self.p10,
                    "\n total:",
                    self.total,
                )
                self.ui.lineEdit_40.setText(str(self.total))
                self.p9 = self.ui.lineEdit_40.text()
                print("\n new total :", self.p9)

            total_cal()
            self.ui.lineEdit_31.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_32.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_33.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_34.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_35.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_36.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_37.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_38.textChanged.connect(lambda: total_cal())
            self.ui.lineEdit_39.textChanged.connect(lambda: total_cal())

            # self.ui.lineEdit_40.textChanged.connect(lambda:total_cal())

        def up_charge():
            try:
                print(
                    "\n save this values:",
                    self.p1,
                    self.p2,
                    self.p3,
                    self.p4,
                    self.p5,
                    self.p6,
                    self.p7,
                    self.p8,
                    self.p10,
                    "\n total:",
                    self.total,
                    self.td10,
                )
                dcc = [
                    self.p1,
                    self.p2,
                    self.p3,
                    self.p4,
                    self.p5,
                    self.p6,
                    self.p7,
                    self.p8,
                    self.total,
                    self.td10,
                    self.p10,
                ]
                print(dcc)
                con = sqlite3.connect(db_file_name)
                cr = con.cursor()
                sql = "insert into Default_charges values(?,?,?,?,?,?,?,?,?,?,?);"
                # cr.execute(sql,dcc)
                con.commit()
                con.close()
                ab = QMessageBox()
                ab.setIcon(QMessageBox.Information)
                QMessageBox.about(ab, "Update charges", "successfully updated.")
            except:
                update_db()
            set_view_charges()
            self.ui.Right_update_groupBox_4.hide()

        self.ui.updatebtnpushButton_2.clicked.connect(lambda: update_db())
        self.ui.setbtpushButton_3.clicked.connect(lambda: up_charge())

    def SL2_logout_btn1_op(self):
        print("logout clicked")
        self.ui.Society_BILLMaintenance.setCurrentIndex(0)
        self.ui.SR_stackedWidget.setCurrentWidget(self.ui.SR2_home_p1)
        self.logout_done = True

    def S_datebox(self):
        self.changed_date = self.ui.Todays_date_dateEdit.text()
        print("date changed :", self.changed_date)
        new_month = self.check_new_month()

    def set_todays(self):
        print("Today date is :", self.today_date)
        self.ui.Todays_date_dateEdit.setDate(self.now)

    def SL1_pdfbills_btn_op(self):
        print("pdf file at :", dir_path)
        if "Society_BILL_Maintenance_Pdfs" in os.listdir(
            f"{dir_path}"
        ):
            os.system(f"start {dir_path}/Society_BILL_Maintenance_Pdfs/")
        else:
            os.system(f" mkdir {dir_path}/Society_BILL_Maintenance_Pdfs")
            os.system(f"start {dir_path}/Society_BILL_Maintenance_Pdfs/")

    def Report_op(self):
        win_search = Tk()
        ws = win_search

        def set_win():
            w, h = 360, 500
            r, d = 300, 150
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            win_search.title("Society : Bill Reports")
            win_search.configure(background="black")
            win_search.resizable(0, 0)

        set_win()

        Label(ws, text="Report of Month_year.:").place(x=10, y=20)

        combmonth = Combobox(ws, width=15, state="readonly")
        combmonth.place(x=150, y=20)
        combmonth["values"] = [
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
        combmonth.set("month is :")
        combmonth.current()

        def usertxt(event):
            year.delete(0, END)

        sat2 = StringVar()
        year = Entry(ws, textvariable=sat2, width=10)
        year.place(x=270, y=20)
        year.insert(0, "Write year")
        year.bind("<Button-1>", usertxt)
        txt = sct.ScrolledText(ws, height=25, width=46, font=("", 9))
        header = f"\t\tReport of Maintenance\nReport viewed on is {self.today_date}\n"
        txt.insert("end", header + "\n")
        txt.configure(state="disable")
        txt.place(x=10, y=60)
        self.fil = ""

        def refresh():
            print("year :", year.get())
            print("month :", combmonth.get())
            if combmonth.get() == "month is :" or (
                year.get() == "Write year" and len(year.get()) > 4
            ):
                messagebox.showwarning(
                    "Error.", "Not complete details enter month,year."
                )
            else:
                if len(year.get()) == 4:
                    month_year = str(combmonth.get()) + "_" + str(year.get())
                    print("month_year:", month_year)
                    self.fil = month_year
                    txt.configure(state="normal")
                    txt.insert("end", "Report of date :" + self.fil)
                    self.get_status()
                    print("total db:", self.tbs_data)
                    tlb = len(self.tbs_data)
                    tbom = 0
                    tbf = 0
                    tba, tbb, tbc = 0, 0, 0
                    ravil = False
                    for i in self.tbs_data:
                        if self.fil.casefold() in i[3].casefold():
                            tbom += 1
                            ravil = True
                        else:
                            revil = False
                        if i[5] != "0":
                            tbf += 1
                        if i[0][0] == "A":
                            tba += 1
                        if i[0][0] == "B":
                            tbb += 1
                        if i[0][0] == "C":
                            tbc += 1
                    rep = f"""\n Details of BiLLs
    Total  Bill Generated : {tlb}
    Total  Bill Of month year :|>  {self.fil}
    Generated : {tbom}
    Total  Bill got fine : {tbf} person
    Total bill Generated wing wise :
        wings    | count bills
        A wing   :   {tba}
        B wing   :   {tbb}
        C wing   :   {tbc}

                    Report End...
                    """
                    txt.configure(state="normal")
                    if ravil:
                        txt.insert("end", rep)
                    else:
                        txt.configure(state="normal")
                        txt.delete("3.0", "end")
                        messagebox.showinfo(
                            "Report", "Report data of month year search is unavilabe. "
                        )
                    txt.configure(state="disable")

        def saverep():

            print("report saved.")
            filname = f"{dir_path}" + "Report_Bill_" + self.fil + ".pdf"
            print("Report saved as :", filname)
            f = open(filname, "w+")
            repmsg = txt.get("1.0", "end")
            f.write(repmsg)
            f.close()

        Button(ws, text="Save", width=15, command=(lambda: saverep())).place(
            x=10, y=450
        )
        Button(ws, text="Load Report", width=15, command=(lambda: refresh())).place(
            x=120, y=450
        )
        Button(
            ws, text="close", width=15, command=(lambda: win_search.destroy())
        ).place(x=240, y=450)
        win_search.mainloop()
        # end

    def Close_Society_app(self):
        print("exit from software ,\n today is :", self.today_date)
        print("logout_done now closing")
        self.close()
        ### events

    def send_warning_op(self):
        print("\n today:", self.today_date, "# WARNING:  request to send : ")
        win_search = Tk()
        ws = win_search

        def set_win():
            w, h = 360, 250
            r, d = 300, 150
            win_search.geometry("%dx%d+%d+%d" % (w, h, r, d))
            win_search.title("Society Maintenance-Bill Management :Send Warnings")
            win_search.configure(background="black")
            win_search.resizable(0, 0)

        set_win()

        Label(ws, text="WhatsApp no.:").place(x=10, y=20)
        wn = StringVar()
        wpc = Entry(ws, text=wn, width=15)
        wpc.place(x=100, y=20)
        vllv = IntVar()
        vll = Checkbutton(
            ws, text="All Late Payers", variable=vllv, onvalue=1, offvalue=0
        ).place(x=200, y=20)
        txt = sct.ScrolledText(ws, height=10, width=46, font=("", 9))
        header = f" Message :\n # WARNING: today is |> {self.today_date}\nPay Your Maintenance Bill after due date fine of |> 100Rs. will be added."
        txt.insert(
            "end",
            header + "\n",
        )
        txt.place(x=10, y=60)

        def sendmsg():
            print("Send request...")
            if vllv.get():
                print("send to all late due payers")
                con = sqlite3.connect(db_file_name)
                cur = con.cursor()
                cur.execute(
                    "select Send_to from All_Bill_info where Payment_status='unpaid';"
                )
                dataup = cur.fetchall()
                con.close()
                cn = "\n"
                for i in dataup:
                    print("send warning to :", i)
                    cn += str(i) + "\n"
                messagebox.showinfo("WhatsApp", f"Warning to {cn} is sended.")
            else:
                if wpc.get().isdigit() and len(wpc.get()) == 10:
                    print("single person: ", wpc.get())
                    messagebox.showinfo(
                        "WhatsApp", f"Warning to {wpc.get()} is sended."
                    )
                else:
                    print("error phone no.")
                    QMessageBox.warning(
                        QMessageBox(),
                        "Wrong Whatsapp no.",
                        "10 digit whatsap no.,\nonly digits",
                    )
            print(txt.get("1.0", "end"))

        Button(ws, text="Send", width=20, command=(lambda: sendmsg())).place(
            x=10, y=220
        )
        Button(
            ws, text="close", width=20, command=(lambda: win_search.destroy())
        ).place(x=210, y=220)
        win_search.mainloop()

    def resizeEvent(self, event):  # resize mainwindow
        self.resized.emit()
        return super(QMainWindow, self).resizeEvent(event)

    def Mainclose(self, event):
        print("logout_done :", self.logout_done)

        def warn():
            print("show WARNING")
            msg = QMessageBox.question(
                self,
                "window close",
                "Exit without logout can crash \ndatabase Data...\n do you want to logout...",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            # retval=msg.exec_()
            if msg == QMessageBox.Yes:
                self.SL2_logout_btn1_op()
                event.accept()
                print("Mainwindow closed..")
            else:
                event.ignore()
                print("Mainwindow continue..")

        if self.logout_done == False:
            warn()


##############################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Start_App()  # SplashScreen()
    sys.exit(app.exec_())
