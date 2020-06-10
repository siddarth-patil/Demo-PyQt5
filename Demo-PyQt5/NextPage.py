import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Form import My_Form


class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form")
        self.ui = My_Form()
        self.ui.setupUi(self)
        self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
