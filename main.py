from PySide2.QtWidgets import QApplication
import sys
from guiBoard import guiBoard
from PySide2.QtWidgets import QMainWindow
from guiGame import Ui_GameWindow


class GameWindow(QMainWindow):
    def __init__(self, parent=None, height=8, width=8, types=7):
        super().__init__(parent)
        self.ui = Ui_GameWindow(height, width, types)
        self.ui.setupUi(self)
        self.wysokość = height
        self.szerokość = width
        self.rodzaje = types


class DopasowanieMatch3Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = guiBoard()
        self.ui.setupUi(self)

        def updateSpinBoxSzerokość(val):
            self.ui.spin_szerokosc.setValue(val)
        self.ui.slider_szerokosc.valueChanged.connect(updateSpinBoxSzerokość)

        def updateSpinBoxWysokość(val):
            self.ui.spin_wysokosc.setValue(val)
        self.ui.slider_wysokosc.valueChanged.connect(updateSpinBoxWysokość)

        def updateSpinBoxRodzaje(val):
            self.ui.spin_rodzaje.setValue(val)
        self.ui.slider_rodzaje.valueChanged.connect(updateSpinBoxRodzaje)

        def updateSliderSzerokość(val):
            self.ui.slider_szerokosc.setSliderPosition(val)
        self.ui.spin_szerokosc.valueChanged.connect(updateSliderSzerokość)

        def updateSliderWysokość(val):
            self.ui.slider_wysokosc.setValue(val)
        self.ui.spin_wysokosc.valueChanged.connect(updateSliderWysokość)

        def updateSliderRodzaje(val):
            self.ui.slider_rodzaje.setValue(val)
        self.ui.spin_rodzaje.valueChanged.connect(updateSliderRodzaje)

        def play():
            width = self.ui.spin_szerokosc.value()
            height = self.ui.spin_wysokosc.value()
            types = self.ui.spin_rodzaje.value()
            QApplication.closeAllWindows()
            window = GameWindow(height=height, width=width,
                                types=types)
            window.show()

        self.ui.button_play.clicked.connect(play)


def guiMain(args):
    app = QApplication(args)
    window = DopasowanieMatch3Window()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
