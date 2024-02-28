import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()

class ExibirClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Clientes cadastrados")


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


        layout = QVBoxLayout()
        layout.addWidget(tbclientes)
        self.setLayout(layout)

if __name__=="__main__":
    app = QApplication(sys.argv)
    tela = ExibirClientes()
    tela.show()
    sys.exit(app.exec_())