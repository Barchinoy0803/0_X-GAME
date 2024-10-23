from PyQt5.QtWidgets import *
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(649,450,200,500)
        self.setStyleSheet("font-size:90px")
        self.setWindowTitle("GAME🎲")
        self.gridLayout = QGridLayout()
       
        
        self.list = ["", "", "", "", "", "", "", "", ""]
        self.buttons = []
        self.value = "x"
        
        self.resetButton = QPushButton("Reset")
        self.resetButton.setStyleSheet("background:green; color:white; font-weight:500; font-size:50px")
        self.resetButton.clicked.connect(self.clickReset)
        self.resetButton.hide()


        for i in range(3):
            for j in range(3):
                btn = QPushButton()
                self.buttons.append(btn)
                btn.clicked.connect(self.clickButton)

                btn.setFixedSize(150,150)
                btn.setStyleSheet("background:lightblue; color: white; border-radius:25px; font-size: 90px")
                self.gridLayout.addWidget(btn,i,j)
          
        self.gridLayout.addWidget(self.resetButton, 4, 2) 
        self.setLayout(self.gridLayout)

        self.count = 0

    def clickButton(self):
        button = self.sender()
        self.value = "x" if self.value == "o" else "o"
        button.setText(self.value)
        self.count += 1
        button.setEnabled(False)
        flag = 0
        for i in range(self.gridLayout.rowCount()):
           for j in range(self.gridLayout.columnCount()):
                item = self.gridLayout.itemAtPosition(i, j)
                if item and item.widget() == button:
                   self.list[flag] = self.value
                flag += 1
        self.checkWinner()           


    def checkWinner(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Congratulations🎉🎉🎉")
        msg.setStyleSheet("font-size:25px")
        msg.setFixedSize(100,60)
        if self.list[0] == 'x' and self.list[1] == 'x' and self.list[2] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[3] == 'x' and self.list[4] == 'x' and self.list[5] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[6] == 'x' and self.list[7] == 'x' and self.list[8] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[0] == 'x' and self.list[3] == 'x' and self.list[6] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[1] == 'x' and self.list[4] == 'x' and self.list[7] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[2] == 'x' and self.list[5] == 'x' and self.list[8] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[0] == 'x' and self.list[4] == 'x' and self.list[8] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)   
        if self.list[2] == 'x' and self.list[4] == 'x' and self.list[6] == 'x':
            msg.setText("X tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.list[0] == 'o' and self.list[1] == 'o' and self.list[2] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)    
        if self.list[3] == 'o' and self.list[4] == 'o' and self.list[5] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)  
        if self.list[6] == 'o' and self.list[7] == 'o' and self.list[8] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.list[0] == 'o' and self.list[3] == 'o' and self.list[6] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)            
        if self.list[1] == 'o' and self.list[4] == 'o' and self.list[7] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.list[2] == 'o' and self.list[5] == 'o' and self.list[8] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.list[0] == 'o' and self.list[4] == 'o' and self.list[8] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.list[2] == 'o' and self.list[4] == 'o' and self.list[6] == 'o':
            msg.setText("O tomon yutdi🎉🎉🎉")
            msg.exec_()
            self.changeStatusButton(False)
        if self.count == 9:
            self.edit.setText("Durrang !!!")
            msg.setText("DURRANG🤝🤝🤝🎉")
            msg.exec_()
            self.changeStatusButton(False)

    def changeStatusButton(self, status):
       if status == False:
           self.resetButton.show()
       for button in self.buttons:
           button.setEnabled(status)

    def clickReset(self):
        for button in self.buttons:
            button.setText("")
        self.list = ["", "", "", "", "", "", "", "", ""]
        self.value = "x"       
        self.changeStatusButton(True)
        self.resetButton.hide()
        self.count = 0           
            
             
               







        














app = QApplication([])
win = MyWindow()
win.show()
app.exec_()