import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import Image


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAcceptDrops(True)

        self.setFixedSize(1150, 450)
        self.setWindowTitle('Picture Aspect Changer')

        self.origin_url = QLabel(self)
        self.origin_image = QLabel(self)
        self.fixed_image = QLabel(self)

        # pillowで画像の縦横比を取得
        pil_image = Image.open('DSC02046.jpg')
        width, height = pil_image.size
        print("元画像の縦横比: {}/{} = {}".format(width, height, width / height))

        # 幅は維持したまま21:9までトリミング
        new_height = int(width / (21 / 9))
        new_image = pil_image.crop((0, (height - new_height) / 2,
                                    width, (height + new_height) / 2))
        print("新しい縦横比: {}/{} = {}".format(width, new_height, width / new_height))

        # 黒背景の画像を作成
        background_color = (0, 0, 0)
        black_image = Image.new('RGB', (width, height), background_color)

        # 重ねる
        black_image.paste(new_image, (0, int((height - new_height) / 2)))
        black_image.save('output.jpg')

        origin_image = QImage('DSC02046.jpg')
        fixed_image = QImage('output.jpg')

        self.origin_image.setPixmap(QPixmap.fromImage(
            QImage(origin_image)).scaledToWidth(500))
        self.origin_image.move(50, 50)

        self.fixed_image.setPixmap(QPixmap.fromImage(
            QImage(fixed_image)).scaledToWidth(500))
        self.fixed_image.move(600, 50)

    def dragEnterEvent(self, event):
        origin = event.mimeData().urls()[0].toString()
        self.origin_url.setText(f"Origin: {origin}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
