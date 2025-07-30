import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QColor


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.timer = QTimer(self)
        self.initUi()

        self.setVisible(True)

    def initUi(self):
        self.setWindowTitle("DigitalClock")
        self.setGeometry(150, 170, 400, 130)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(600, 300)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        effect = QGraphicsDropShadowEffect(
            blurRadius=25, xOffset=0, yOffset=0, color=QColor(225, 225, 225, 200))
        self.label.setGraphicsEffect(effect)
        effect.setEnabled(True)

        self.label.setStyleSheet(
            "background-color:rgba(227, 154, 197, 150); border-radius:30px; color:rgb(255,255,255); font-size:100px; font-family:Georgia")
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.updateTime()

    def updateTime(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString("hh:mm:ss")
        self.label.setText(display_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
