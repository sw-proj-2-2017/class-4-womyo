import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):

        label1 = QLabel("Name: ", self)
        label1.move(10, 16)
        label2 = QLabel("Age: ", self)
        label2.move(170, 16)
        label3 = QLabel("Score: ", self)
        label3.move(320, 16)
        label4 = QLabel("Amount: ", self)
        label4.move(195, 46)
        label5 = QLabel("Key: ", self)
        label5.move(375, 46)
        label6 = QLabel("Result:", self)
        label6.move(10, 103)
        line1 = QLineEdit("", self)
        line1.move(50, 13)
        line2 = QLineEdit("", self)
        line2.move(200, 13)
        line3 = QLineEdit("", self)
        line3.move(360, 13)
        line4 = QLineEdit("", self)
        line4.move(250, 43)
        c = QComboBox(self)
        c.addItem("Name", self)
        c.addItem("Age", self)
        c.addItem("Score", self)
        c.move(405, 43)
        b1 = QPushButton("Add", self)
        b1.move(50, 73)
        b2 = QPushButton("Del", self)
        b2.move(135, 73)
        b3 = QPushButton("Find", self)
        b3.move(220, 73)
        b4 = QPushButton("Inc", self)
        b4.move(305, 73)
        b5 = QPushButton("show", self)
        b5.move(390, 73)
        text = QTextEdit(self)
        text.move(10, 123)
        text.resize(460, 120)

        self.setGeometry(300, 300, 480, 250)
        self.setWindowTitle('Assignment6')    
        self.show()





    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return
        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()



    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





