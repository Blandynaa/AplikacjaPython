import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from graph import MyGraph
from drag import DraggablePoint

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.list_points = []
        self.graph = MyGraph(self)
        self.list_points = self.graph.list_points
        print("lista punktów z maina: ", self.list_points)
        self.setCentralWidget(self.graph)

        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)

        self.clear_action = QAction("Wyczyść", self)
        self.clear_action.triggered.connect(self.graph.clearFigure)
        self.toolbar.addAction(self.clear_action)

        self.new_point_action = QAction("Dodaj ścianę", self)
        self.new_point_action.setCheckable(True)
        self.new_point_action.setChecked(False)
        self.toolbar.addAction(self.new_point_action)

        self.refresh_action = QAction("Odśwież", self)
        self.refresh_action.triggered.connect(self.graph.draw)
        self.toolbar.addAction(self.refresh_action)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Plik")
        self.file_menu.addAction(self.clear_action)

        self.setWindowTitle("Projekt mieszkania 2D")
        self.show()

    # def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent):
    #     self.graph.plotDraggablePoints()
    #     super().mouseDoubleClickEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())