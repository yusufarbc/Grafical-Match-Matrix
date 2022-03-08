
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Table(object):
    def setupUi(self, Table):
        Table.setObjectName("match matrix")
        Table.resize(2000, 1000)

        self.table = QtWidgets.QTableWidget(Table)
        self.table.setGeometry(QtCore.QRect(0, 0, 2000, 1000))
        self.table.setObjectName("table")

        self.retranslateUi(Table)
        QtCore.QMetaObject.connectSlotsByName(Table)

    def retranslateUi(self, Table):
        _translate = QtCore.QCoreApplication.translate
        Table.setWindowTitle(_translate("Table", "match matrix"))
