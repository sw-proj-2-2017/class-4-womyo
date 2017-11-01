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

        label1 = QLabel("Name:")
        label2 = QLabel("Age:")
        label3 = QLabel("Score:")
        label4 = QLabel("Amount:")
        label5 = QLabel("Key:")
        self.result = QLabel("Result:")

        line1 = QLineEdit()
        line2 = QLineEdit()
        line3 = QLineEdit()
        line4 = QLineEdit()
        self.resultEdit = QTextEdit()

        self.c = QComboBox(self)
        self.c.addItem("Name")
        self.c.addItem("Age")
        self.c.addItem("Score")
        self.c.activated[str].connect(self.onActivated)

        b1 = QPushButton("Add")
        b2 = QPushButton("Del")
        b3 = QPushButton("Find")
        b4 = QPushButton("Inc")
        b5 = QPushButton("show")

        line1.textChanged[str].connect(self.onNameChanged)
        line2.textChanged[str].connect(self.onAgeChanged)
        line3.textChanged[str].connect(self.onScoreChanged)
        line4.textChanged[str].connect(self.onAmountChanged)

        b1.clicked.connect(self.AddClicked)
        b2.clicked.connect(self.DelClicked)
        b3.clicked.connect(self.FindClicked)
        b4.clicked.connect(self.IncClicked)
        b5.clicked.connect(self.showScoreDB)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(label1)
        hbox1.addWidget(line1)
        hbox1.addWidget(label2)
        hbox1.addWidget(line2)
        hbox1.addWidget(label3)
        hbox1.addWidget(line3)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(label4)
        hbox2.addWidget(line4)
        hbox2.addWidget(label5)
        hbox2.addWidget(self.c)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(b1)
        hbox3.addWidget(b2)
        hbox3.addWidget(b3)
        hbox3.addWidget(b4)
        hbox3.addWidget(b5)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        self.setLayout(vbox)
        self.show()

        self.setGeometry(300, 300, 480, 250)
        self.setWindowTitle('Assignment6')    
        self.str = ""


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
        keyname = self.c.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                self.str += attr + "=" + str(p[attr]) + '\t'
            self.str += "\n"
        self.resultEdit.setText(self.str)
        self.str = ""
        pass
    def onNameChanged(self, text):
        self.name = text

    def onAgeChanged(self, text):
        self.age = text
    def onScoreChanged(self, text):
        self.score = text
    def onAmountChanged(self, text):
        self.amount = text
    def AddClicked(self):
        record = {'Name': self.name, 'Age': int(self.age), 'Score': int(self.score)}
        self.scoredb += [record]
        self.showScoreDB()
    def DelClicked(self):
        copyscoredb = self.scoredb[:]
        for p in copyscoredb:
            if p['Name'] == self.name:
                self.scoredb.remove(p)
        self.showScoreDB()
    def FindClicked(self):
        for p in self.scoredb:
            if p['Name'] == self.name:
                self.str += "Age=" + str(p['Age']) + "\tName=" + str(p['Name']) + "\t\tScore=" + str(p['Score'])
                self.str += "\n"
        self.resultEdit.setText(self.str)
        self.str = ""
    def IncClicked(self):
        for p in self.scoredb:
            if p['Name'] == self.name:
                p['Score'] += int(self.amount)
        self.showScoreDB()
    def onActivated(self, text):
        self.keyname = text
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





