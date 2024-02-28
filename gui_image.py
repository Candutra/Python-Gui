import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap 




class GuiImage(QWidget):
    def __init__(self):
        super().__init__()

        labelTexto = QLabel("Texto")
        labelImagem = QLabel("")
        labelImagem.setPixmap(QPixmap("eva.jpg"))

        layout = QHBoxLayout()
        layout.addWidget(labelTexto)
        layout.addWidget(labelImagem)

        self.setGeometry(100,100,600,400)

        self.setWindowTitle("Imagem em Label")

        self.setLayout(layout)


app = QApplication(sys.argv)
tela = GuiImage()
tela.show()
app.exec_()