import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout,QHBoxLayout, QStyle, QLineEdit, QTableWidget, QWidgetItem, QTableWidgetItem







class GuiDuasColunas(QWidget):

    

    def __init__(self):

        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(10,25,1600,900)
        self.setWindowTitle("Caixa da Padaria")
        self.showMaximized()

        

        

        layoutVerEs = QVBoxLayout()
        layoutVerDi = QVBoxLayout()

        layoutHor = QHBoxLayout()



        labelColEsq = QLabel()
        labelColEsq.setStyleSheet("QLabel{background-color:#401d05;}")
        labelColEsq.setFixedWidth(800)



        labelColDir = QLabel()
        labelColDir.setStyleSheet("QLabel{background-color:#e8d9ba}")
        labelColEsq.setFixedWidth(800)

        labelLogo = QLabel()
        labelLogo.setPixmap(QPixmap("Padaria-cadutra.jpg"))
        labelLogo.setScaledContents(True)

        labelCodigo = QLabel("Codigo do Produto")
        labelCodigo.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.codigoEdit = QLineEdit()
        self.codigoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")


        labelNomeProduto = QLabel("Nome do Produto")
        labelNomeProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.nomeProdutoEdit = QLineEdit()
        self.nomeProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelDescProduto = QLabel("Descrição do Produto")
        labelDescProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.descProdutoEdit = QLineEdit()
        self.descProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelQuantiProduto = QLabel("Quantidade")
        labelQuantiProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.quantiProdutoEdit = QLineEdit()
        self.quantiProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelValProduto = QLabel("Preço unitario do Produto")
        labelValProduto.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.valProdutoEdit = QLineEdit()
        self.valProdutoEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")

        labelSubTotal = QLabel("Sub Total da Compra")
        labelSubTotal.setStyleSheet("QLabel{color:white;font-size:15pt}")
        self.subTotalEdit = QLineEdit("Aperte F3 para calcular o SubTotal")
        #Desabilitando a caixa do sub total
        self.subTotalEdit.setEnabled(False)
        self.subTotalEdit.setStyleSheet("QLineEdit{padding:10px;font-size:15pt}")





        layoutVerEs.addWidget(labelLogo)
        layoutVerEs.addWidget(labelCodigo)
        layoutVerEs.addWidget(self.codigoEdit)

        layoutVerEs.addWidget(labelNomeProduto)
        layoutVerEs.addWidget(self.nomeProdutoEdit)

        layoutVerEs.addWidget(labelDescProduto)
        layoutVerEs.addWidget(self.descProdutoEdit)

        layoutVerEs.addWidget(labelQuantiProduto)
        layoutVerEs.addWidget(self.quantiProdutoEdit)

        layoutVerEs.addWidget(labelValProduto)
        layoutVerEs.addWidget(self.valProdutoEdit)

        layoutVerEs.addWidget(labelSubTotal)
        layoutVerEs.addWidget(self.subTotalEdit)

        labelColEsq.setLayout(layoutVerEs)



        #Criando a tabela de dados do lado direito
        self.tbResumo = QTableWidget(self)
        self.tbResumo.setColumnCount(5)
        self.tbResumo.setRowCount(10)

        #Criando o cabeçario
        titulos = ["Código","Nome Produto","Quantidade","Preço Unitario","Preço Total"]
        self.tbResumo.setHorizontalHeaderLabels(titulos)

        labelTotalPagar = QLabel("Total a pagar")
        labelTotalPagar.setStyleSheet("QLabel{color:black;font-size:25pt}")
        self.totalPagarEdit = QLineEdit("0,00")
        self.totalPagarEdit.setEnabled(False)
        self.totalPagarEdit.setStyleSheet("QLineEdit{padding:10px;font-size:50pt}")


        


        layoutVerDi.addWidget(self.tbResumo)
        layoutVerDi.addWidget(labelTotalPagar)
        layoutVerDi.addWidget(self.totalPagarEdit)




        labelColDir.setLayout(layoutVerDi)



        layoutHor.addWidget(labelColEsq)
        layoutHor.addWidget(labelColDir)

        self.setLayout(layoutHor)

        # Capturando a tecla que o usuario esta digitando e 
        # Chamando a função (keyPressEvent) para executar um comando quando
        # for acionada.
        self.keyPressEvent = self.keyPressEvent

    def keyPressEvent(self,e):

        if(e.key()==Qt.Key_F2):
            print('Você teclou f2')
            self.tbResumo.setItem(self.linha,0,QTableWidgetItem(str(self.codigoEdit.text())))
            self.tbResumo.setItem(self.linha,1,QTableWidgetItem(str(self.nomeProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,2,QTableWidgetItem(str(self.quantiProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,3,QTableWidgetItem(str(self.valProdutoEdit.text())))
            self.tbResumo.setItem(self.linha,4,QTableWidgetItem(str(self.subTotalEdit.text())))
            self.linha+=1
            
            self.total+=float(self.subTotalEdit.text())
            self.totalPagarEdit.setText(str(self.total))
            
            # Limpar os LineEdit
            self.codigoEdit.setText("")
            self.nomeProdutoEdit.setText("")
            self.quantiProdutoEdit.setText("")
            self.valProdutoEdit.setText("")
            self.subTotalEdit.setText("Aperte F3 para calcular o SubTotal")
            self.descProdutoEdit.setText("")
        
        elif(e.key() == Qt.Key_F3):
            qtd = self.quantiProdutoEdit.text()
            prc = self.valProdutoEdit.text()
            res = float(qtd) * float(prc)
            self.subTotalEdit.setText(str(res))





app = QApplication(sys.argv)

janela = GuiDuasColunas()

janela.show()

app.exec_()