from PyQt5 import uic, QtWidgets

def funcao_principal():
  if formulario.radioButton.isChecked():
    opcao = "opcao 1 selecionada"
  elif formulario.radioButton_2.isChecked():
    opcao = "opcao 2 selecionada"
  elif formulario.radioButton_3.isChecked():
    opcao = "opcao 3 selecionada"
  elif formulario.radioButton_4.isChecked():
    opcao = "opcao 4 selecionada"
  else:
    opcao = ""
  formulario.label_2.setText(opcao)


app=QtWidgets.QApplication([])
formulario = uic.loadUi("janela.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()