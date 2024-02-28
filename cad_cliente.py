import sys
import mysql.connector as mc

con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
cursor = con.cursor()

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class CadCliente(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,100,600,250)
        self.setWindowTitle("Cadastro de Clientes")  


        labelNome = QLabel("Nome Completo")
        self.editNome = QLineEdit()

        labelEmail = QLabel("E-Mail:")
        self.editEmail = QLineEdit()

        labelTelefone = QLabel("Telefone:")
        self.editTelefone = QLineEdit()


        psbCadastro = QPushButton("Cadastrar")
        

        self.labelMsg = QLabel("!")

        layout = QVBoxLayout()
        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)

        layout.addWidget(labelEmail)
        layout.addWidget(self.editEmail)

        layout.addWidget(labelTelefone)
        layout.addWidget(self.editTelefone)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.cadCli)

        layout.addWidget(self.labelMsg)
        self.setLayout(layout)
    
    def cadCli(self):
        cursor.execute("insert into Clientes(nome_clientes,email,telefone)values(%s,%s,%s)",
                       (self.editNome.text(),self.editEmail.text(),self.editTelefone.text()))
        con.commit()
        self.labelMsg.setText("Cliente Cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = CadCliente()
    tela.show()
    sys.exit(app.exec_())