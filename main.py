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
        #self.toolbar.addAction(self.clear_action)

        self.new_point_action = QAction("Ściana", self)
        self.new_point_action.setCheckable(True)
        self.new_point_action.setChecked(False)
        self.toolbar.addAction(self.new_point_action)

        self.fotel_action = QAction("Fotel", self)
        self.fotel_action.triggered.connect(self.graph.fotelAdd)
        self.toolbar.addAction(self.fotel_action)

        self.jacuzzi_action = QAction("Jacuzzi", self)
        self.jacuzzi_action.triggered.connect(self.graph.jacuzziAdd)
        self.toolbar.addAction(self.jacuzzi_action)

        self.kanapa_action = QAction("Kanapa", self)
        self.kanapa_action.triggered.connect(self.graph.kanapaAdd)
        self.toolbar.addAction(self.kanapa_action)

        self.kwiat1_action = QAction("Kwiat1", self)
        self.kwiat1_action.triggered.connect(self.graph.kwiat1Add)
        self.toolbar.addAction(self.kwiat1_action)

        self.kwiat2_action = QAction("Kwiat2", self)
        self.kwiat2_action.triggered.connect(self.graph.kwiat2Add)
        self.toolbar.addAction(self.kwiat2_action)

        self.kwiat3_action = QAction("Kwiat3", self)
        self.kwiat3_action.triggered.connect(self.graph.kwiat3Add)
        self.toolbar.addAction(self.kwiat3_action)

        self.lezak_action = QAction("Leżak", self)
        self.lezak_action.triggered.connect(self.graph.lezakAdd)
        self.toolbar.addAction(self.lezak_action)

        self.lozko_action = QAction("Łóżko", self)
        self.lozko_action.triggered.connect(self.graph.lozkoAdd)
        self.toolbar.addAction(self.lozko_action)

        self.naroznik_action = QAction("Narożnik", self)
        self.naroznik_action.triggered.connect(self.graph.naroznikAdd)
        self.toolbar.addAction(self.naroznik_action)

        self.pralka_action = QAction("Pralka", self)
        self.pralka_action.triggered.connect(self.graph.pralkaAdd)
        self.toolbar.addAction(self.pralka_action)

        self.schody1_action = QAction("Schody1", self)
        self.schody1_action.triggered.connect(self.graph.schody1Add)
        self.toolbar.addAction(self.schody1_action)

        self.schody2_action = QAction("Schody2", self)
        self.schody2_action.triggered.connect(self.graph.schody2Add)
        self.toolbar.addAction(self.schody2_action)

        self.stol_action = QAction("Stół", self)
        self.stol_action.triggered.connect(self.graph.stolAdd)
        self.toolbar.addAction(self.stol_action)

        self.szafki_pion_action = QAction("Szafki-pion", self)
        self.szafki_pion_action.triggered.connect(self.graph.szafki_pionAdd)
        self.toolbar.addAction(self.szafki_pion_action)

        self.szafki_poziom_action = QAction("Szafki-poziom", self)
        self.szafki_poziom_action.triggered.connect(self.graph.szafki_poziomAdd)
        self.toolbar.addAction(self.szafki_poziom_action)

        self.telewizor_action = QAction("Telewizor", self)
        self.telewizor_action.triggered.connect(self.graph.telewizorAdd)
        self.toolbar.addAction(self.telewizor_action)

        self.wanna_action = QAction("Wanna", self)
        self.wanna_action.triggered.connect(self.graph.wannaAdd)
        self.toolbar.addAction(self.wanna_action)

        self.zlew_action = QAction("Zlew", self)
        self.zlew_action.triggered.connect(self.graph.zlewAdd)
        self.toolbar.addAction(self.zlew_action)

        self.siatka1_action = QAction("Usuń siatkę", self)
        self.siatka1_action.triggered.connect(self.graph.siatkaRemove)
        #self.toolbar.addAction(self.siatka1_action)

        self.siatka2_action = QAction("Dodaj siatkę", self)
        self.siatka2_action.triggered.connect(self.graph.siatkaAdd)
        #self.toolbar.addAction(self.siatka2_action)

        self.refresh_action = QAction("Odśwież", self)
        self.refresh_action.triggered.connect(self.graph.draw)

        self.save_action = QAction("Zapisz jako...", self)
        self.save_action.triggered.connect(self.graph.save_as_image)

        self.del_walls_action = QAction("Usuń wszystkie ściany", self)
        self.del_walls_action.triggered.connect(self.graph.clearWalls)

        self.del_wall_action = QAction("Usuń ostatnio dodaną ścianę", self)
        self.del_wall_action.triggered.connect(self.graph.clearWall)

        self.del_images_action = QAction("Usuń wszystkie meble", self)
        self.del_images_action.triggered.connect(self.graph.clearImages)

        self.del_image_action = QAction("Usuń ostatnio dodany mebel", self)
        self.del_image_action.triggered.connect(self.graph.clearImage)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Plik")

        self.file_menu.addAction(self.refresh_action)
        self.file_menu.addAction(self.save_action)
        self.wall_menu = self.menu.addMenu("Obszar projektu")
        self.wall_menu.addAction(self.clear_action)
        #self.wall_menu.addAction(self.del_walls_action)  #usuń wszystkie ściany
        #self.wall_menu.addAction(self.del_wall_action)  #usuń ostatnio dodaną ścianę
        # self.meble_menu = self.menu.addMenu("Opcje mebli")
        # self.meble_menu.addAction(self.del_images_action)
        # self.meble_menu.addAction(self.del_image_action)
        self.siatka_menu = self.menu.addMenu("Ustawienia tła")
        self.siatka_menu.addAction(self.siatka1_action)
        self.siatka_menu.addAction(self.siatka2_action)
        self.setWindowTitle("Projekt mieszkania 2D")
        self.show()

    # def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent):
    #     self.graph.plotDraggablePoints()
    #     super().mouseDoubleClickEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())