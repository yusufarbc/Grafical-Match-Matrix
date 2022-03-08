import sys
import random as rand
from PyQt5 import QtWidgets,QtGui #pip install PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from _window import Ui_Form
from _table import Ui_Table

class Match(QWidget):
    def __init__(self):
        super(Match, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.ui.btn_calculate.clicked.connect(self.getSequence)

    def newColor(self):
        color = (rand.randint(1, 255),rand.randint(1, 255),rand.randint(1, 255))
        return color

    def divideSequence(self,sequence,n):
        temp = n
        seqList = []
        index = 0
        length = len(sequence)
        length = length - length%n
        while(index<length):
            keymer = ""
            n = temp
            while(n>0):
                keymer = keymer + sequence[index]
                n -= 1
                index += 1
            seqList.append(keymer)
        return seqList          

    def getSequence(self):
        n = self.ui.txt_n.text()
        n = int(n)   
        first = self.divideSequence(self.ui.txt_first.text(),n)
        second = self.divideSequence(self.ui.txt_second.text(),n)
        self.createTable(first,second) 
        

    def createTable(self,first,second):
        self.table = QTableWidget()
        self.close()
        self.ui = Ui_Table()
        self.ui.setupUi(self.table)
        
        lenFirst = len(first)
        lenSecond = len(second)

        # First sequence is horizontal
        self.ui.table.setRowCount(lenSecond)
        # Second sequence is vertical
        self.ui.table.setColumnCount(lenFirst)

        self.ui.table.setHorizontalHeaderLabels(first)
        self.ui.table.setVerticalHeaderLabels(second)

        i = 0
        while(i<lenFirst):
            self.ui.table.setColumnWidth(i, 7)
            i += 1
        j = 0
        while(j<lenSecond):
            self.ui.table.setRowHeight(j, 7)
            j += 1

        # i row count
        # j column count

        diagonal = 1
        while(diagonal<(lenFirst-1)):
            i=0
            j=0
            count = 0
            color = self.newColor()
            while(i<lenSecond and (j+diagonal)<lenFirst):
                if(second[i] == first[(j+diagonal)]):
                    self.ui.table.setItem(i, (j+diagonal), QTableWidgetItem(str(count)))
                    self.ui.table.item(i, (j+diagonal)).setBackground(QtGui.QColor(int(color[0]),int(color[1]),int(color[2])))
                    count += 1
                else:
                    count = 0
                    color = self.newColor()
                i += 1
                j += 1
            diagonal += 1

        i=0
        j=0
        count = 0
        color = self.newColor()
        while(i<lenSecond and j<lenFirst):
            if(first[i] == second[j]):
                self.ui.table.setItem(i, j, QTableWidgetItem(str(count)))
                self.ui.table.item(i, j).setBackground(QtGui.QColor(int(color[0]),int(color[1]),int(color[2])))
                count += 1
            else:
                count = 0
                color = self.newColor()
            i += 1
            j += 1

        diagonal = 1
        while(diagonal<(lenSecond-1)):
            i=0
            j=0
            count = 0
            color = self.newColor()
            while((i+diagonal)<lenSecond and j<lenFirst):
                if(second[(i+diagonal)] == first[j]):
                    self.ui.table.setItem((i+diagonal), j, QTableWidgetItem(str(count)))
                    self.ui.table.item((i+diagonal), j).setBackground(QtGui.QColor(int(color[0]),int(color[1]),int(color[2])))
                    count += 1
                else:
                    count = 0
                    color = self.newColor()

                i += 1
                j += 1
            diagonal += 1

        self.table.show()
     
def app():
    app = QApplication(sys.argv)
    win = Match()
    app.exit(app.exec_())
    
app()