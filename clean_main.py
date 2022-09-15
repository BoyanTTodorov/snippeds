import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from os import path
from PyQt5.uic import loadUiType
FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), 'untitled.ui'))

class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent= None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()