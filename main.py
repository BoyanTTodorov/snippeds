
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from os import path
from PyQt5.uic import loadUiType
FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), 'untitled.ui'))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.update_ui()

    def update_ui(self):
        wh = ['MKI', 'JTS1', 'JTS2']
        racks_mki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J']
        racks_jts1 = []
        racks_jts2 = []
        self.comboBox.addItems(wh)
        if (self.comboBox.currentText() == 'MKI'):
            self.comboBox_2.addItems(racks_mki)
        elif (self.comboBox.currentText() == 'JTS1'):
            self.comboBox_2.addItems(racks_jts1)
        elif (self.comboBox.currentText() == 'JTS2'):
            self.comboBox_2.addItems(racks_jts2)
def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()