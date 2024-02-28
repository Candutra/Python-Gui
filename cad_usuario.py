import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

db = client.loga_db

class CadUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,100,600,250)
        self.setWindowTitle("Cadastro de Usuario")  


        labelNomeUsuario = QLabel("Nome Usuario")
        self.editusuario = QLineEdit()

        labelSenha = QLabel("Senha:")
        self.editsenha = QLineEdit()

        labelNivel = QLabel("Nivel:")
        self.editnivel = QLineEdit()


        psbCadastro = QPushButton("Efetuar Cadastro")
        

        self.labelMsg = QLabel("Aguardando informações")

        layout = QVBoxLayout()
        layout.addWidget(labelNomeUsuario)
        layout.addWidget(self.editusuario)

        layout.addWidget(labelSenha)
        layout.addWidget(self.editsenha)

        layout.addWidget(labelNivel)
        layout.addWidget(self.editnivel)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.cadCli)

        layout.addWidget(self.labelMsg)
        self.setLayout(layout)
    
    def cadCli(self):
        usuario_id = db["usuario"].insert_one({"nomeusuario":self.editusuario.text(),"senha":self.editsenha.text(),"nivel":self.editnivel.text()}).inserted_id
        self.labelMsg.setText("Usuario Cadastrado")
        QTimer.singleShot(3000, lambda: self.labelMsg.setText("Aguardando informações"))

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadUsuario()
    tela.show()
    sys.exit(app.exec_())