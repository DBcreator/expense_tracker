# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt

from PyQt5.QtWidgets import QLabel, QInputDialog, QDialog, QGridLayout, QLineEdit, QPushButton, QMessageBox, QWidget

from pie import pie
from wallet import Wallet


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listwidget = QtWidgets.QTableWidget(self.centralwidget)
        self.listwidget.setGeometry(QtCore.QRect(0, 0, 511, 541))
        self.listwidget.setObjectName("listwidget")
        self.listwidget.setColumnCount(5)
        self.listwidget.setHorizontalHeaderLabels(["id", "Price", "Category", "Date", "Comments"])
        self.listwidget.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        self.listwidget.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        self.listwidget.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        self.listwidget.horizontalHeaderItem(3).setTextAlignment(Qt.AlignRight)
        self.listwidget.horizontalHeaderItem(4).setTextAlignment(Qt.AlignRight)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 0, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(820, 50, 93, 28))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText('Statistics')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 30, 77, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(510, 0, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        # data
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(710, 0, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 0, 71, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 30, 55, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)

        # wallet name

        self.pushButton_AddWallet = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AddWallet.setGeometry(QtCore.QRect(720, 90, 71, 22))
        self.pushButton_AddWallet.setObjectName("pushButton_AddWallet")
        self.pushButton_AddWallet.setText('add')

        self.lineEdit_Value = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Value.setGeometry(QtCore.QRect(550, 90, 71, 22))
        self.lineEdit_Value.setObjectName("lineEdit_Value")

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(630, 90, 71, 22))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.label_Value = QtWidgets.QLabel(self.centralwidget)
        self.label_Value.setGeometry(QtCore.QRect(550, 120, 71, 22))
        self.label_Value.setObjectName("label_Value")
        self.label_Value.setText('Сумма')

        self.label_NameWallet = QtWidgets.QLabel(self.centralwidget)
        self.label_NameWallet.setGeometry(QtCore.QRect(630, 120, 93, 22))
        self.label_NameWallet.setObjectName("label_NameWallet")
        self.label_NameWallet.setText('Имя кошелька')
        # combo = QComboBox(self)
        self.Wallet_list = QtWidgets.QComboBox(self.centralwidget)
        self.Wallet_list.setGeometry(QtCore.QRect(820, 0, 100, 22))
        self.Wallet_list.setObjectName("Wallet_list")

        self.login = UI_LoginWindow()
        self.login.show()

        #exit
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(920,520, 71,22)
        self.pushButton_Exit.setText('Exit')

        self.stat = Statistics()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    singal = QtCore.pyqtSignal(list)


    def send_signal(self):
        self.signal.emit([self.lineEdit_password.text(), self.lineEdit_login.text()])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "категория"))
        self.label_2.setText(_translate("MainWindow", "сумма"))

    def HandleQuestion(self):
        pass

    def show_it(self, the_password):
        print(the_password)

    def Statistic(self):
        pass


class Ui_RegWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    sign_up = QtCore.pyqtSignal(bool)

    def initUI(self):
        self.setObjectName("Login")
        self.setFixedSize(400, 75)

        self.label_login = QtWidgets.QLabel(self)
        self.label_login.setGeometry(QtCore.QRect(0, 0, 71, 22))
        self.label_login.setObjectName("lineEdit_login")
        self.label_login.setText('Login')

        self.lineEdit_login = QtWidgets.QLineEdit(self)
        self.lineEdit_login.setGeometry(QtCore.QRect(0, 30, 71, 22))
        self.lineEdit_login.setObjectName("lineEdit_login")

        # password
        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setGeometry(QtCore.QRect(80, 0, 71, 22))
        self.label_password.setObjectName("lineEdit_password")
        self.label_password.setText('Password')

        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 30, 71, 22))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        # name
        self.label_Name = QtWidgets.QLabel(self)
        self.label_Name.setGeometry(QtCore.QRect(161, 0, 71, 22))
        self.label_Name.setObjectName("label_Name")
        self.label_Name.setText('Name')
        self.lineEdit_Name = QtWidgets.QLineEdit(self)
        self.lineEdit_Name.setGeometry(QtCore.QRect(161, 30, 71, 22))
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        # button
        self.pushButton_Sign_up = QtWidgets.QPushButton(self)
        self.pushButton_Sign_up.setGeometry(QtCore.QRect(250, 30, 71, 22))
        self.pushButton_Sign_up.setObjectName("pushButton_Sign_up")
        self.pushButton_Sign_up.setText('Sign up')
        self.pushButton_Sign_up.clicked.connect(self.send_password)

        self.label_passed = QtWidgets.QLabel(self)
        self.label_passed.setGeometry(QtCore.QRect(0, 55, 300, 20))
        self.label_passed.setObjectName("label_passed")

    def send_password(self):
        user = Wallet()
        if not user.init_user(login=str(self.lineEdit_login.text()), password=str(self.lineEdit_password.text()),
                              name=str(self.lineEdit_Name.text())):
            self.label_passed.setText('A user with the same name already exists')
            return None
        self.sign_up.emit(True)
        self.close()
        self.lineEdit_password.clear()
        self.lineEdit_login.clear()


class UI_LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    got = QtCore.pyqtSignal(list)

    def initUI(self):
        self.setObjectName("Login")
        self.setFixedSize(400, 75)
        # login
        self.label_login = QtWidgets.QLabel(self)
        self.label_login.setGeometry(QtCore.QRect(0, 0, 71, 22))
        self.label_login.setObjectName("lineEdit_login")
        self.label_login.setText('Login')

        self.lineEdit_login = QtWidgets.QLineEdit(self)
        self.lineEdit_login.setGeometry(QtCore.QRect(0, 30, 71, 22))
        self.lineEdit_login.setObjectName("lineEdit_login")

        # password
        self.label_password = QtWidgets.QLabel(self)
        self.label_password.setGeometry(QtCore.QRect(80, 0, 71, 22))
        self.label_password.setObjectName("lineEdit_password")
        self.label_password.setText('Password')

        self.lineEdit_password = QtWidgets.QLineEdit(self)
        self.lineEdit_password.setGeometry(QtCore.QRect(80, 30, 71, 22))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        # log in
        self.pushButton_Login = QtWidgets.QPushButton(self)
        self.pushButton_Login.setGeometry(QtCore.QRect(160, 30, 71, 22))
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.pushButton_Login.setText('Login')
        self.pushButton_Login.clicked.connect(self.send_password)

        # sign up

        self.pushButton_Sign_up = QtWidgets.QPushButton(self)
        self.pushButton_Sign_up.setGeometry(QtCore.QRect(250, 30, 71, 22))
        self.pushButton_Sign_up.setObjectName("pushButton_Sign_up")
        self.pushButton_Sign_up.setText('Sign Up')
        self.pushButton_Sign_up.clicked.connect(self.SignUp)
        # label passed

        self.label_passed = QtWidgets.QLabel(self)
        self.label_passed.setGeometry(QtCore.QRect(0, 55, 300, 20))
        self.label_passed.setObjectName("label_passed")

        self.registration = Ui_RegWindow()
        self.registration.sign_up.connect(self.Exit)


    def SignUp(self):
        self.close()
        self.registration.show()

    def Exit(self):
        self.show()

    def send_password(self):
        user = Wallet()
        if not user.sign_in(login=str(self.lineEdit_login.text()), password=str(self.lineEdit_password.text())):
            self.label_passed.setText('Error check password or login')
        self.got.emit([self.lineEdit_password.text(), self.lineEdit_login.text()])
        self.lineEdit_password.clear()
        self.lineEdit_login.clear()


class Statistics(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self,lst):
        self.setObjectName("Login")
        self.setFixedSize(700, 700)
        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(0, 0, 700, 700))
        self.photo.setScaledContents(True)
        self.photo.setObjectName('photo')
        self.user = Wallet()
        self.user.sign_in(lst[0],lst[1])
        self.user.pie()
        self.photo.setPixmap(QtGui.QPixmap("diagram.png"))
        self.show()
