from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog
from checker import *
import sys
from libs.cpf import *


class Checker(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCpf.clicked.connect(self.gerarcpf)
        self.btnCheck.clicked.connect(self.valida_gerados)
        self.clearGerados.clicked.connect(self.clear_widget)
        self.clearChecker.clicked.connect(self.listChecker.clear)
        self.btnCheckSolo.clicked.connect(self.check_cpf)
        self.btnSave.clicked.connect(self.savetxt)
        self.itemsTextlist = []

    def clear_widget(self):
        self.listWidget.clear()
        self.itemsTextlist.clear()

    def savetxt(self):
        arquivo, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            "Salvar",
            r"C:\Users\rafel\Desktop",
        )
        if arquivo:
            with open(arquivo + ".txt", "w+") as arch:
                for i in self.itemsTextlist:
                    arch.write(i)
                    arch.write("\n")

    def gerarcpf(self):
        qtde = self.qtdeCpfs.text()

        if qtde:
            qtde = re.sub(r"[^0-9]", "", qtde)
            qtde = int(qtde)
        else:
            qtde = 1

        list_cpf = gerarcpf(qtde)
        for cpf in list_cpf:
            cpf1 = QListWidgetItem(cpf)
            self.listWidget.addItem(cpf1)

        self.itemsTextlist = [
            str(self.listWidget.item(i).text()) for i in range(self.listWidget.count())
        ]

    def valida_gerados(self):
        lst = self.itemsTextlist
        self.listChecker.clear()

        for cpf in lst:
            if valida(cpf):
                self.listChecker.addItem(cpf)

    def check_cpf(self):
        cpf = self.inputSolo.text()
        if valida(cpf):
            self.returnSolo.setStyleSheet("color: green;")
            self.returnSolo.setText("VÁLIDO")
        else:
            self.returnSolo.setStyleSheet("color: red;")
            self.returnSolo.setText("INVÁLIDO")


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = Checker()
    app.show()
    qt.exec_()
