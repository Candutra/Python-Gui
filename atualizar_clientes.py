import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QVBoxLayout, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()

class AtualizarClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,460,400)
        self.setWindowTitle("Clientes cadastrados")

        labelId = QLabel("ID do cliente")
        self.editId = QLineEdit()

        labelNome = QLabel("Nome Completo")
        self.editNome = QLineEdit()

        labelEmail = QLabel("E-Mail:")
        self.editEmail = QLineEdit()

        labelTelefone = QLabel("Telefone:")
        self.editTelefone = QLineEdit()


        psbCadastro = QPushButton("Cadastrar")

        layout = QVBoxLayout()

        layout.addWidget(labelId)
        layout.addWidget(self.editId)

        layout.addWidget(labelNome)
        layout.addWidget(self.editNome)

        layout.addWidget(labelEmail)
        layout.addWidget(self.editEmail)

        layout.addWidget(labelTelefone)
        layout.addWidget(self.editTelefone)

        layout.addWidget(psbCadastro)
        psbCadastro.clicked.connect(self.upCli)
        

        tbclientes = QTableWidget(self)
        tbclientes.setColumnCount(4)
        tbclientes.setRowCount(10)
        headerLine=["id","Nome","Email","Telefone"]

        tbclientes.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from Clientes")
        lintb = 0
        for linha in cursor:
            tbclientes.setItem(lintb,0,QTableWidgetItem(str(linha[0])))
            tbclientes.setItem(lintb,1,QTableWidgetItem(str(linha[1])))
            tbclientes.setItem(lintb,2,QTableWidgetItem(str(linha[2])))
            tbclientes.setItem(lintb,3,QTableWidgetItem(str(linha[3])))
            lintb+=1


        layout.addWidget(tbclientes)
        self.setLayout(layout)
    
    def upCli(self):
        if (self.editId.text()==""):
            print("Não é possivel atualizar sem o id do Cliente")

        elif(self.editNome.text()=="" and self.editEmail.text()=="" and self.editTelefone.text()==""):
            print("Não foi possivel atualizar se não houver dados")

        elif(self.editNome.text()!="" and self.editEmail.text()=="" and self.editTelefone.text()==""):
            cursor.execute("update Clientes set nome_clientes=%s where clientes_id=%s",
                           (self.editNome.text(),self.editId.text()))
            

        elif(self.editNome.text()=="" and self.editEmail.text()!="" and self.editTelefone.text()==""):
            cursor.execute("update Clientes set email=%s where clientes_id=%s",
                           (self.editEmail.text(),self.editId.text()))

        elif(self.editNome.text()=="" and self.editEmail.text()=="" and self.editTelefone.text()!=""):
            cursor.execute("update Clientes set nome_clientes=%s where clientes_id=%s",
                           (self.editTelefone.text(),self.editId.text()))
        
        else:
             cursor.execute("update Clientes set nome_clientes=%s, email=%s, telefone=%s where clientes_id=%s",
                           (self.editTelefone.text(),self.editEmail.text(),self.editTelefone.text(),self.editId.text()))
             
        cx.commit()
        print("Todas as modificações foram realizadas")


if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = AtualizarClientes()
    tela.show()
    sys.exit(app.exec_())