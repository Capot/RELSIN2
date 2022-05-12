import bot
from PyQt5 import uic, QtWidgets


class janela():
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.formulario = uic.loadUi("D:\Projetos\Relsin2\janelas\janela.ui")
        self.formulario.btn_consultar.clicked.connect(self.consultaJanela)

    def consultaJanela(self):
        empresa = self.formulario.txt_empresa.text()
        print(empresa)
        robo = bot.bot()
        robo.logIn()
        robo.buscaInfo(empresa)
        robo.logOff()


    def constroetela(self):
        self.formulario.show()
        self.app.exec()
