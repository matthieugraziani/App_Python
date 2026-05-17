import math
import sys
from datetime import datetime

from PySide6.QtGui import QPainter, QColor, QCloseEvent, QLinearGradient, QPen
from PySide6.QtCore import QPoint, Qt, QPointF, QTimer
from PySide6.QtGui import QPaintEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QApplication


class ClockWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.__timer = QTimer(self)
        self.__timer.timeout.connect(self.repaint)
        self.__timer.start(1000)

    def closeEvent(self, event:QCloseEvent) -> None:
        self.__timer.stop()

    def paintEvent(self, event:QPaintEvent) -> None:
        super().paintEvent(event)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing);

        # On dessine le cercle de l'horloge avec un dégradé autour
        radius = 0.95 * (min(self.width(), self.height()) / 2)

        centerX = int(self.width() / 2)
        centerY = int(self.height() / 2)

        linearGradient = QLinearGradient(QPointF(0, 0), QPointF(0, radius*2))
        linearGradient.setColorAt(0, QColor(0xE0, 0xE0, 0xE0))
        linearGradient.setColorAt(0.5, QColor(0x6E, 0x77, 0x74))
        linearGradient.setColorAt(0.51, QColor(0x0a, 0x0e, 0x0a))
        linearGradient.setColorAt(1, QColor(0x0a, 0x08, 0x09))

        painter.setPen(QPen(linearGradient, 8))
        painter.setBrush(QColor(0x21, 0x21, 0x21))
        painter.drawEllipse(QPoint(centerX, centerY), radius, radius)

        # On s'apprète à dessiner les graduations sur l'horloge
        font = painter.font()
        font.setPointSize(16)
        painter.setFont(font)

        angle = -math.pi / 2 + math.pi / 30
        for hour, _ in enumerate(range(12 * 5), start=2):
            angle += math.pi / 30
            painter.setPen(Qt.white)
            painter.setBrush(Qt.white)

            if hour % 5 == 0:
                # Tracé d'une graduation d'heure
                painter.drawPolygon([
                    QPointF(centerX + math.cos(angle - 0.02) * radius * 0.9, centerY + math.sin(angle - 0.02) * radius * 0.9),
                    QPointF(centerX + math.cos(angle - 0.01) * radius * 0.8, centerY + math.sin(angle - 0.01) * radius * 0.8),
                    QPointF(centerX + math.cos(angle + 0.01) * radius * 0.8, centerY + math.sin(angle + 0.01) * radius * 0.8),
                    QPointF(centerX + math.cos(angle + 0.02) * radius * 0.9, centerY + math.sin(angle + 0.02) * radius * 0.9)
                ])
                delta = radius * 0.04
                painter.drawText(int(centerX + math.cos(angle) * radius * 0.7) - 8,
                                 int(centerY + math.sin(angle) * radius * 0.7 + delta),
                                 str(hour // 5))
            else:
                # Tracé d'une graduation de minute
                painter.drawLine(
                    QPointF(centerX + math.cos(angle) * radius * 0.85,
                            centerY + math.sin(angle) * radius * 0.85),
                    QPointF(centerX + math.cos(angle) * radius * 0.9,
                            centerY + math.sin(angle) * radius * 0.9)
                )

        now = datetime.now()

        # On dessine la trotteuse
        painter.setPen(QPen(QColor(255, 0, 0, int(256 * 0.6)), 3))
        angle = - math.pi / 2 + now.second * math.pi / 30
        destX = math.cos(angle) * radius * 0.95
        destY = math.sin(angle) * radius * 0.95
        painter.drawLine(centerX, centerY, int(centerX + destX), int(centerY + destY))

        # On dessine l'aiguille des minutes
        painter.setPen(QColor(255, 0, 0))
        painter.setBrush(QColor(255, 0, 0, 150))

        minuteAngle = math.pi * 2 * (now.minute / 60 + now.second / 3600)
        minuteAngle = -(math.pi / 2 - minuteAngle)

        painter.drawPolygon([
            QPointF(centerX + math.cos(minuteAngle) * radius * 0.93, centerY + math.sin(minuteAngle) * radius * 0.93),
            QPointF(centerX + math.cos(minuteAngle - 0.4) * radius * 0.1, centerY + math.sin(minuteAngle - 0.4) * radius * 0.1),
            QPointF(centerX + math.cos(minuteAngle + 0.4) * radius * 0.1, centerY + math.sin(minuteAngle + 0.4) * radius * 0.1)
        ])

        # On dessine l'aiguille des heures
        hourAngle = math.pi * 2 * ((now.hour % 12 + now.minute / 60) / 12)
        hourAngle = -(math.pi / 2 - hourAngle)

        painter.drawPolygon([
            QPointF(centerX + math.cos(hourAngle) * radius * 0.6, centerY + math.sin(hourAngle) * radius * 0.6),
            QPointF(centerX + math.cos(hourAngle - 0.3) * radius * 0.1, centerY + math.sin(hourAngle - 0.3) * radius * 0.1),
            QPointF(centerX + math.cos(hourAngle + 0.3) * radius * 0.1, centerY + math.sin(hourAngle + 0.3) * radius * 0.1)
        ])

        # On dessine le disque interne
        painter.setPen(QPen(linearGradient, 8))
        painter.setBrush(QColor(0x21, 0x21, 0x21))
        painter.drawEllipse(QPoint(centerX, centerY), radius * 0.18, radius * 0.18)


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de création d'un Widget Horloge")
        self.resize(400, 400)

        # On instancie notre nouveau widget et on l'ajoute à la fenêtre
        clock = ClockWidget()
        self.setCentralWidget(clock)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec())