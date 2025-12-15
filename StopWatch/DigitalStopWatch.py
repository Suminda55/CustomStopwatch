import sys
from PyQt5.QtWidgets import (QApplication , QWidget,QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont,QFontDatabase,QPainter, QBrush, QColor, QPen

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        self.setWindowFlags(Qt.FramelessWindowHint)  # i used this for remove window borders
        self.setAttribute(Qt.WA_TranslucentBackground)  # from this i could be able to make background transparent

        font_id = QFontDatabase.addApplicationFont("I:/myPythonFirstProject/StopWatch/DS-DIGII.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family,42)
            self.time_label.setFont(my_font)

        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.dash_offset = 0

        self.border_timer = QTimer(self)
        self.border_timer.timeout.connect(self.animate_border)
        self.border_timer.start(30)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setStyleSheet("""
            QPushButton,QLabel{
                padding:20px;
                font-weight:bold;
                
            }
            QPushButton{
                font-size: 37px;
                font-family:Engravers MT;
            }
            QLabel{
                font-size: 100px;
                background-color: hsl(252, 94%, 69%);
                border-radius:30px;
                color:white;
            }""")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)


    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen=QPen(QColor(111, 255, 0, 180), 3)
        pen.setStyle(Qt.DashLine)
        pen.setDashOffset(self.dash_offset)
        painter.setPen(pen)

        painter.drawRoundedRect(2, 2, self.width()-4 , self.height()-4,30,30 )

        painter.setPen(QPen(QColor(111, 255, 0, 80), 1))
        painter.drawRoundedRect(10, 10, self.width()-20, self.height()-20,25,25 )

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()  # using this drag position i could dragg the window
            event.accept()

        # below mentioned  (mousePressEvent, mouseMoveEvent, mouseReleaseEvent) make window draggable
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None

    def animate_border(self):
        self.dash_offset +=1
        self.update()

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0 ,0 ,0 ,0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        millisecond = time.msec()//10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{millisecond:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())

