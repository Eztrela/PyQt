import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
  def __init__(self,) -> None:
    super().__init__()
    self.top = 100
    self.left = 100
    self.w_width = 800
    self.w_heigth = 600
    self.title = "Primeira Janela"
    self.LoadWindow()

  def LoadWindow(self):
    self.setGeometry(self.left,self.top,self.w_width,self.w_heigth)
    self.setWindowTitle(self.title)
    self.show()

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())