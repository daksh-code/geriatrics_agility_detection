#all of the imports
import sys
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPalette, QBrush, QColor, QFontDatabase, QFont
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from Background_Registration import *


userInfo = ' '
count = 0
displayMessage = ' '

class AnotherWindow(QWidget):
  
    def __init__(self):
        super(AnotherWindow,self).__init__()
        self.layout = QVBoxLayout()
        calculation()
        label = QLabel("Your count is {} and Performance is : {}".format(count//2,displayMessage), self)
        label.setStyleSheet("color: #CFD8DC")
        label.setStyleSheet("color: #CFD8DC")
        label.move(105,95)
        label.setFont(QFont('Grandstander Black', 29))
        self.setStyleSheet("""
        background-color: #5D6D7E;
        """)
        label.adjustSize()
        self.setWindowTitle("Chair Stand test Result")
        self.setLayout(self.layout)

    def closeEvent(self, event):
        sys.exit(app.exec_())

class MainWindow(QWidget):
  
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QVBoxLayout()
        label = QLabel("Geriatric Agility Detection", self)
        label.setStyleSheet("color: #CFD8DC")
        label.move(105,105)
        label.setFont(QFont('Grandstander Black', 29))
        self.setStyleSheet("""
        background-color: #5D6D7E;
        """)
        label.adjustSize()
        self.setWindowTitle("Chair Stand Test")
        self.setLayout(self.layout)
        self.Button1()
        self.Button2()
           
    def getuserInfo(self):
        font = QFont()
        font.setFamily("Grandstander Black")
        font.setPointSize(10)
        global userInfo
        inputDialog = QInputDialog(None)
        inputDialog.setInputMode(QInputDialog.TextInput)
        inputDialog.setWindowTitle('Enter Your Details')
        inputDialog.setLabelText("Your gender and age in format(given below)   \n eg:f24")
        inputDialog.setFont(font)
        inputDialog.setStyleSheet("""
        background-color: #5D6D7E;
        color: #17202A
        """)
        okPressed=inputDialog.exec()
        userInfo=inputDialog.textValue()
        if okPressed and userInfo != '':
            global count
            count = register_Background()
            self.popup = AnotherWindow()
            self.popup.setFixedSize(1350, 200)
            self.popup.show()
            
    def Button1(self): 
        button = QPushButton("Start", self)
        button.move(290,195)
        button.setFont(QFont("Grandstander Black",13.5))
        button.setStyleSheet("""
        background-color: #80CBC4;
        color: #FDFEFE;
        border-radius: 5px;
        left: 100px;
        """)
        button.clicked.connect(self.getuserInfo)

    def Button2(self): 
        button = QPushButton("Exit", self) 
        button.setFont(QFont("Grandstander Black",13.5))
        button.setFixedSize(100,35)
        button.move(290,245)
        button.setStyleSheet("""
        background-color: #E57373;
        color: #FDFEFE;
        border-radius: 5px;
        """)
        button.clicked.connect(self.exit) 

    def exit():
        sys.exit(app.exec_())
        
def calculation():
    gender=userInfo[0]
    print(userInfo)
    age = int(userInfo[1:3])
    lower_bound=' '
    upper_bound=' '
    male = [(14, 19), (12, 18), (12, 17), (11, 17), (10, 15), (8, 14), (7, 12)]
    female = [(12, 17), (11, 16), (10, 15), (10, 15), (9, 14), (8, 13), (4, 11)]
    #making sure that age stays between 60 and 95 so we can take the correct index
    if(age < 60):
         age = 60
    if(age > 95):
         age = 95
    #taking appropriate index 
    index = (age-60)//5
    if gender=='m':
        lower_bound = male[index][0]
        upper_bound = male[index][1]
    else:
        lower_bound = female[index][0]
        upper_bound = female[index][1]

    global displayMessage

    if(count//2 < lower_bound):
        displayMessage="Less Than Average"
    elif(count//2 > upper_bound):
        displayMessage="More Than Average"
    else:
        displayMessage="Average"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.resize(700,450)
    mw.setFixedSize(700, 450)
    mw.show()
    sys.exit(app.exec_())