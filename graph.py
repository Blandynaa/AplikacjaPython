import sys
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QPoint, QEvent
from PyQt5.QtGui import QMouseEvent
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Personnal modules
from drag import DraggablePoint
from mebell import DraggableImage


class MyGraph(FigureCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, parent, width=18, height=12, dpi=80):
        self.parent = parent
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(0, 30)
        self.axes.set_ylim(0, 20)
        self.axes.locator_params(axis='x', nbins=30)
        self.axes.locator_params(axis='y', nbins=20)
        self.axes.grid(True)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.list_points = []
        self.list_images = []
        # self.list_points   #= self.parent.list_points
        # print(self.list_points)

        self.show()
        # self.plotFirstPoint()
        # self.plotDraggablePoints()
        # self.plotDraggablePoints2(2, 2)
        # self.add_image()
        # self.list_points.pop(-1)
        # self.updateFigure()

    #
    # def add_image(self):
    #     print("Dodawanie obrazka")
    #     #image_path = 'C:\Users\win10\Desktop\zrzut.jpg'
    #     self.list_images.append(DraggableImage(self))
    #     self.updateFigure()
    #     print("koniec dodawania obrazka")

    def plotFirstPoint(self, size=1):
        """Plot and define the 2 draggable points of the baseline"""
        print("Dodanie początkowego punktu:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, 2, 2, size))
        print("Dodano 1. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points

    def plotDraggablePoints(self, size=1):
        """Plot and define the 2 draggable points of the baseline"""
        print("Rozpoczecie dodawania:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, 5, 5, size))
        print("Dodano 1. punkt")
        self.list_points.append(DraggablePoint(self, 10, 10, size))
        print("Dodano 2. punkt")
        # self.list_points.append(DraggablePoint(self, 15, 10, size))
        # print("Dodano 3. punkt")
        # self.list_points.append(DraggablePoint(self, 20, 10, size))
        # print("Dodano 4. punkt")
        # self.list_points.append(DraggablePoint(self, 20, 5, size))
        # self.list_points.append(self.list_points[0])
        # print("Dodano 5. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points

    def plotDraggablePoints2(self, x, y):
        """Plot and define the 2 draggable points of the baseline"""
        print("Rozpoczecie dodawania:")
        # del(self.list_points[:])
        self.list_points.append(DraggablePoint(self, x, y, 1))
        print("2Dodano 1. punkt")
        # self.list_points.append(DraggablePoint(self, 10, 10, 1))
        # print("2Dodano 2. punkt")
        self.updateFigure()
        self.parent.list_points = self.list_points
        print("Lista parenta po 2 dodaniu punktow:", self.parent.list_points)

    def clearFigure(self):
        """Clear the graph"""

        self.axes.clear()
        self.axes.set_xlim(0, 30)
        self.axes.set_ylim(0, 20)
        self.axes.locator_params(axis='x', nbins=30)
        self.axes.locator_params(axis='y', nbins=20)
        del (self.list_points[:])
        del (self.list_images[:])
        self.updateFigure()

    def updateFigure(self):
        """Update the graph. Necessary, to call after each plot"""

        self.draw()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        x = event.x()
        y = self.fig.canvas.height() - event.y()
        point = self.axes.transData.inverted().transform((x, y))
        x, y = point[0], point[1]
        size = 1  # Default size of the point
        self.list_points.append(DraggablePoint(self, x, y, size))
        # self.list_images.append(DraggableImage(self))
        print("lista obrazkow", self.list_images)

        self.updateFigure()

    def fotelAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.6, sizey=0.6, image_path='fotel.jpg'))
        self.updateFigure()

    def kanapaAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.8, sizey=0.6, image_path='kanapa.jpg'))
        self.updateFigure()

    def kwiat1Add(self):
        self.list_images.append(DraggableImage(self, sizex=0.5, sizey=0.5, image_path='kwiat.jpg'))
        self.updateFigure()

    def kwiat2Add(self):
        self.list_images.append(DraggableImage(self, sizex=0.5, sizey=0.5, image_path='kwiat2.jpg'))
        self.updateFigure()

    def kwiat3Add(self):
        self.list_images.append(DraggableImage(self, sizex=1.0, sizey=1.0, image_path='kwiat3.jpg'))
        self.updateFigure()


    def lezakAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.5, sizey=1.0, image_path='lezak.jpg'))
        self.updateFigure()

    def lozkoAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.4, sizey=1.5, image_path='lozko.jpg'))
        self.updateFigure()

    def naroznikAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.8, sizey=1.0, image_path='naroznik.jpg'))
        self.updateFigure()

    def pralkaAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.6, sizey=0.6, image_path='pralka.jpg'))
        self.updateFigure()

    def schody1Add(self):
        self.list_images.append(DraggableImage(self, sizex=1.2, sizey=1.2, image_path='schody1.jpg'))
        self.updateFigure()

    def schody2Add(self):
        self.list_images.append(DraggableImage(self, sizex=1.3, sizey=1.3, image_path='schody2.jpg'))
        self.updateFigure()

    def stolAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.8, sizey=1.5, image_path='stol.jpg'))
        self.updateFigure()

    def szafki_pionAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.5, sizey=1.5, image_path='szafki3pion.jpg'))
        self.updateFigure()

    def szafki_poziomAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.5, sizey=0.5, image_path='szafki3poziom.jpg'))
        self.updateFigure()

    def telewizorAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.0, sizey=0.2, image_path='telewizor.jpg'))
        self.updateFigure()

    def wannaAdd(self):
        self.list_images.append(DraggableImage(self, sizex=0.6, sizey=1.2, image_path='wanna.jpg'))
        self.updateFigure()

    def zlewAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.0, sizey=0.5, image_path='zlew.jpg'))
        self.updateFigure()

    def jacuzziAdd(self):
        self.list_images.append(DraggableImage(self, sizex=1.5, sizey=1.5, image_path='jaccuzi.jpg'))
        self.updateFigure()

    def siatkaRemove(self):
        self.axes.grid(False)
        self.updateFigure()

    def siatkaAdd(self):
        self.axes.grid(True)
        self.updateFigure()