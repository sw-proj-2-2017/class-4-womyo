from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)


class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        for i in range(10):
            self.digitButton[i] = Button("%d" % (i), self.buttonClicked)
        
        # . and = Buttons
        self.decButton = Button('.', self.buttonClicked)
        self.eqButton = Button('=', self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonClicked)
        self.divButton = Button('/', self.buttonClicked)
        self.addButton = Button('+', self.buttonClicked)
        self.subButton = Button('-', self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonClicked)
        self.rparButton = Button(')', self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', self.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        for i in range(10):
            if i%3 == 1 or i == 0:
                n = 0
            elif i%3 == 2:
                n = 1
            elif i%3 == 0 :
                n = 2
            numLayout.addWidget(self.digitButton[i], abs(i/3 - 3) , n)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        
        opLayout.addWidget(self.clearButton, 3, 0)
        
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
