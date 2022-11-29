import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel,QLineEdit
from PyQt5 import QtGui

class Window(QMainWindow):
  def __init__(self,) -> None:
    super().__init__()
    self.top = 100
    self.left = 100
    self.w_width = 800
    self.w_heigth = 600
    self.title = "Primeira Janela"


    self.caixa_texto = QLineEdit(self)
    self.caixa_texto.move(25,20)
    self.caixa_texto.resize(220,40)

    btn1 = QPushButton('Button 1',self)
    btn1.move(150,150)
    btn1.resize(150,80)
    btn1.setStyleSheet('QPushButton {background-color:#0FB328};font:bold;font-size:20px')
    btn1.clicked.connect(self.btn1_click)

    btn_cx = QPushButton('Envia Texto',self)
    btn_cx.move(550,150)
    btn_cx.resize(150,80)
    btn_cx.setStyleSheet('QPushButton {background-color:"DeepSkyBlue"};font:bold;font-size:20px')
    btn_cx.clicked.connect(self.btn_cx_click)

    btn2 = QPushButton('Button 2',self)
    btn2.move(350,150)
    btn2.resize(150,80)
    btn2.setStyleSheet('QPushButton {background-color:red};font:bold;font-size:20px')
    btn2.clicked.connect(self.btn2_click)

    self.label_1 = QLabel(self)
    self.label_1.setText("Aperte algum botão")
    self.label_1.move(50,70)
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px}')
    self.label_1.resize(400,40)

    self.label_cx = QLabel(self)
    self.label_cx.setText("Digitou: ")
    self.label_cx.move(350,70)
    self.label_cx.setStyleSheet('QLabel {font:bold;font-size:25px}')
    self.label_cx.resize(400,40)

    self.carro_img = QLabel(self)
    self.carro_img.move(50,400)
    # self.carro_img.setPixmap(QtGui.QPixmap('carro1.png'))
    self.carro_img.resize(400,200)

    self.LoadWindow()

  def LoadWindow(self):
    self.setGeometry(self.left,self.top,self.w_width,self.w_heigth)
    self.setWindowTitle(self.title)
    self.show()
  
  def btn1_click(self):
    self.label_1.setText('Carro 1')
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"green"}')
    self.carro_img.setPixmap(QtGui.QPixmap('carro1.png'))


  def btn2_click(self):
    self.label_1.setText('Carro2')
    self.label_1.setStyleSheet('QLabel {font:bold;font-size:25px;color:"red"}')
    self.carro_img.setPixmap(QtGui.QPixmap('carro2.png'))


  def btn_cx_click(self):
    conteudo = self.caixa_texto.text()
    self.label_cx.setText('Digitou: ' + conteudo)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())