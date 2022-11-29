import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Window(QMainWindow):
  def __init__(self,) -> None:
    super().__init__()
    self.top = 100
    self.left = 100
    self.w_width = 800
    self.w_heigth = 600
    self.title = "Primeira Janela"

    btn1 = QPushButton('Button 1',self)
    btn1.move(150,150)
    btn1.resize(150,80)
    btn1.setStyleSheet('QPushButton {background-color:#0FB328};font:bold;font-size:20px')
    btn1.clicked.connect(self.btn1_click)

    btn2 = QPushButton('Button 2',self)
    btn2.move(350,150)
    btn2.resize(150,80)
    btn2.setStyleSheet('QPushButton {background-color:red};font:bold;font-size:20px')
    btn2.clicked.connect(self.btn2_click)

    self.label_1 = QLabel(self)
    self.label_1.setText("Aperte algum botão")
    self.label_1.move(50,50)
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"blue"}')
    self.label_1.resize(400,40)

    self.LoadWindow()

  def LoadWindow(self):
    self.setGeometry(self.left,self.top,self.w_width,self.w_heigth)
    self.setWindowTitle(self.title)
    self.show()
  
  def btn1_click(self):
    self.label_1.setText('O botao 1 foi clicado')
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"green"}')


  def btn2_click(self):
    self.label_1.setText('O botao 2 foi clicado')
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"red"}')

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())