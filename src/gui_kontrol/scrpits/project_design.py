import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.terminal)
        # Works also with urxvt:
        self.process.start('urxvt',['-embed', str(int(self.winId()))])
        self.setFixedSize(540, 580)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(940, 565)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 411, 201))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color : rgb(255, 155, 0)")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 131, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color : rgb(55, 155, 0)")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 70, 131, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color : rgb(255, 0, 0)")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 200, 411, 871))
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color : rgb(48, 134, 255)")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.angularVelocity = QtWidgets.QLabel(self.widget_2)
        self.angularVelocity.setGeometry(QtCore.QRect(20, 320, 91, 17))
        self.angularVelocity.setObjectName("angularVelocity")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_2.setGeometry(QtCore.QRect(330, 240, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber.setGeometry(QtCore.QRect(330, 320, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_3.setGeometry(QtCore.QRect(330, 160, 64, 23))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.linearVelocity = QtWidgets.QLabel(self.widget_2)
        self.linearVelocity.setGeometry(QtCore.QRect(20, 240, 81, 17))
        self.linearVelocity.setObjectName("linearVelocity")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_4.setGeometry(QtCore.QRect(330, 90, 64, 23))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)        
        self.terminal = EmbTerminal(MainWindow)
        self.terminal.setGeometry(QtCore.QRect(411, 0, 500, 541))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KOL-KAR S SİMÜLASYON"))
        self.label.setText(_translate("MainWindow", "Simülasyon Hareket Kontrol"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.label_4.setText(_translate("MainWindow", "Y(m)"))
        self.label_2.setText(_translate("MainWindow", "Konum ve Hız  Bilgileri"))
        self.angularVelocity.setText(_translate("MainWindow", "Açısal(rad/s)"))
        self.linearVelocity.setText(_translate("MainWindow", "Lineer(m/s)"))
        self.label_3.setText(_translate("MainWindow", "X(m)"))
        



    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

