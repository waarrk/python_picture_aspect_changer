import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setFixedSize(1200, 800)
        self.setWindowTitle('Picture Aspect Changer')


# ウィンドウを描画
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
