
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("match matrix program")
        Form.resize(750, 400)

        self.btn_calculate = QtWidgets.QPushButton(Form)
        self.btn_calculate.setGeometry(QtCore.QRect(50, 275, 175, 50))
        self.btn_calculate.setObjectName("btn_calculate")

        self.txt_first = QtWidgets.QLineEdit(Form)
        self.txt_first.setGeometry(QtCore.QRect(175, 100, 500, 20))
        self.txt_first.setObjectName("txt_first")

        self.txt_second = QtWidgets.QLineEdit(Form)
        self.txt_second.setGeometry(QtCore.QRect(175, 150, 500, 20))
        self.txt_second.setObjectName("txt_second")

        self.txt_n = QtWidgets.QLineEdit(Form)
        self.txt_n.setGeometry(QtCore.QRect(175, 200, 50, 20))
        self.txt_n.setObjectName("txt_n")

        self.lbl_first = QtWidgets.QLabel(Form)
        self.lbl_first.setGeometry(QtCore.QRect(45, 100, 120, 20))
        self.lbl_first.setObjectName("lbl_first")

        self.lbl_second = QtWidgets.QLabel(Form)
        self.lbl_second.setGeometry(QtCore.QRect(45, 150, 120, 20))
        self.lbl_second.setObjectName("lbl_second")

        self.lbl_n = QtWidgets.QLabel(Form)
        self.lbl_n.setGeometry(QtCore.QRect(45, 200, 120, 20))
        self.lbl_n.setObjectName("lbl_n")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "match matrix program"))
        self.btn_calculate.setText(_translate("Form", "Calculate"))
        self.lbl_first.setText(_translate("Form", "First Sequence: "))
        self.lbl_second.setText(_translate("Form", "Second Sequence: "))
        self.lbl_n.setText(_translate("Form", "n-search value: "))
