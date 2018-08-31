import time
import datetime
import sendemail
import subprocess as sp
import sys
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)
        Dialog.setAcceptDrops(False)

        self.mdiArea = QtWidgets.QMdiArea(Dialog)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 441, 331))
        brush = QtGui.QBrush(QtGui.QColor(10, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")

        self.mdiArea.setObjectName("mdiArea")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setAcceptDrops(False)
        Dialog.setStyleSheet("background-image: url(:/newPrefix/design.jpg);")
        Dialog.setModal(False)

        
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 60, 191, 31))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("<link rel=\"stylesheet\" type=\"text/css\" href=\"bootstrap.min.css\">")
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMidLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Rust Slab Black Shadow 01")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setObjectName("label_4")
        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(150, 220, 121, 41))
        # self.pushButton.setObjectName("pushButton")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 220, 251, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        #self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 220, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 210, 231, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(130, 110, 41, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "22", "23"])
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 110, 41, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"])
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.showData)
        #self.buttonBox.rejected.connect(Dialog.reject)
        #self.buttonBox.rejected.connect(self.icon, SIGNAL("activated(QSystemTrayIcon::ActivationReason)"), self.iconClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "COMPANION"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "Today\'s Tasks"))
        self.label_2.setText(_translate("Dialog", "Time"))
        self.label_3.setText(_translate("Dialog", ":"))
        self.label_4.setText(_translate("Dialog", "COMPANION"))
        self.label_6.setText(_translate("Dialog", "E-mail"))
        self.label_5.setText(_translate("Dialog", "//email scheduler"))
        # self.pushButton.setText(_translate("Dialog", "Add Reminders"))


    def showData(self):

        conn = sqlite3.connect('mydatabase.db')

        TASK = self.textEdit.toPlainText()
        HOUR = str(self.comboBox.currentText())
        MINUTE = str(self.comboBox_2.currentText())
        # userIdd=str(self.textEdit_2.toPlainText())
        # userId = '"'+userIdd'"'
        # str(userId)
        #print(userId)
        print(TASK)
        print(HOUR)
        print(MINUTE)

        # conn = sqlite3.connect('mydatabase.db')

        # print("Opened database successfully");

        # conn.execute("INSERT INTO REMINDER VALUES ('"+TASK+"', "+HOUR+", "+MINUTE+")")

        # conn.commit()
        # print("Records created successfully");

        startTime = HOUR+" : "+MINUTE
        str(startTime)
        print("your reminder has been set to -> "+startTime)
        now = datetime.datetime.now()
        hour = str(now.hour)
        minute = str(now.minute)
        systime = hour + " : " + minute
        str(systime)
        print(systime)

        sp.Popen(["python.exe", "rem.py"])


        while (systime < startTime):
            now = datetime.datetime.now()
            hour = str(now.hour)
            minute = str(now.minute)
            systime = hour + " : " + minute
            str(systime) 
            #return(systime)

        print("Hello its "+startTime+"  you have a reminder of  "+TASK)
        #smail(TASK)
        #tredirect()  


    #def smail(message):
        # Python code to illustrate Sending mail from 
        # your Gmail account 
        import smtplib
         
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        print("sending email")
         
        # Authentication
        //enter your email id here
        s.login("", "")

        # message to be sent
        #rec = input("Enter the sender's email")
         
        # sending the mail
        //your email id and senders email id to send the mail
        s.sendmail("","",TASK)
        
        print("email send succesfully")

        # terminating the session
        s.quit()    

        conn.close()    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


