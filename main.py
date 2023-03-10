import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAcceptDrops(True)

        self.setFixedSize(1150, 800)
        self.setWindowTitle('Picture Aspect Changer')

        self.origin_url = QLabel(self)
        self.origin_image = QLabel(self)
        self.fixed_image = QLabel(self)

        image = QImage('3731.jpg')
        self.origin_image.setPixmap(QPixmap.fromImage(
            QImage(image)).scaledToWidth(500))
        self.origin_image.move(50, 50)

        self.fixed_image.setPixmap(QPixmap.fromImage(
            QImage(image)).scaledToWidth(500))
        self.fixed_image.move(600, 50)

    def dragEnterEvent(self, event):
        origin = event.mimeData().urls()[0].toString()
        self.origin_url.setText(f"Origin: {origin}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
