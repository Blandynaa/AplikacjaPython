import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import AxesImage


class DraggableImage:
    lock = None  # only one can be animated at a time

    def __init__(self, parent, x=15, y=10, sizex=2, sizey=2, image_path='obraz.jpg'):
        self.parent = parent
        self.image = plt.imread(image_path)
        self.point = AxesImage(parent.fig.axes[0], cmap='gray', origin='upper', extent=(x-sizex, x+sizex, y-sizey, y+sizey), alpha=1)
        self.point.set_data(self.image)
        parent.fig.axes[0].add_artist(self.point)
        self.press = None
        self.background = None
        self.connect()

    def connect(self):
        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):
        if event.inaxes != self.point.axes: return
        if DraggableImage.lock is not None: return
        contains, attrd = self.point.contains(event)
        if not contains: return
        self.press = event.xdata, event.ydata
        DraggableImage.lock = self
        canvas = self.point.figure.canvas  #
        axes = self.point.axes  #
        self.point.set_animated(True)
        point_number = self.parent.list_image.index(self)  #
        #animowanie linii
        canvas.draw()  #
        self.background = canvas.copy_from_bbox(self.point.axes.bbox)
        #self.background = self.point.figure.canvas.copy_from_bbox(self.point.axes.bbox)
        axes.draw_artist(self.point)
        #self.point.axes.draw_artist(self.point)
        #self.point.figure.canvas.blit(self.point.axes.bbox)  #???
        canvas.blit(axes.bbox)  #

    def on_motion(self, event):
        if DraggableImage.lock is not self: return
        #if self.press is None: return
        if event.inaxes != self.point.axes: return
        dx = event.xdata - self.press[0]
        dy = event.ydata - self.press[1]
        self.press = event.xdata, event.ydata
        self.point.set_extent((self.point.get_extent()[0] + dx, self.point.get_extent()[1] + dx,
                               self.point.get_extent()[2] + dy, self.point.get_extent()[3] + dy))
        #self.point.center = (self.point.center[0] + dx, self.point.center[1] + dy)  #

        canvas = self.point.figure.canvas  #
        axes = self.point.axes  #

        canvas.restore_region(self.background)
        #self.point.figure.canvas.restore_region(self.background)
        axes.draw_artist(self.point)
        #self.point.axes.draw_artist(self.point)
        canvas.blit(axes.bbox)
        #self.point.figure.canvas.blit(self.point.axes.bbox)

    def on_release(self, event):
        if DraggableImage.lock is not self: return
        self.press = None
        DraggableImage.lock = None
        self.point.set_animated(False)
        self.background = None
        self.point.figure.canvas.draw()

    def disconnect(self):

        'disconnect all the stored connection ids'

        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)

# class DraggableImage:
#     lock = None  # only one can be animated at a time
#
#     def __init__(self, parent, x=10, y=10, size=0.3, image_path='obraz.jpg'):
#         self.parent = parent
#         self.image = plt.imread(image_path)
#         self.point = AxesImage(parent.fig.axes[0], cmap='gray', origin='upper', extent=(x-size, x+size, y-size, y+size), alpha=1)
#         self.point.set_data(self.image)
#         parent.fig.axes[0].add_artist(self.point)
#
#     def connect(self):
#         'connect to all the events we need'
#         self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
#         self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
#         self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
#
#     def on_press(self, event):
#         if event.inaxes != self.point.axes: return
#         if DraggableImage.lock is not None: return
#         self.press = self.point.get_extent(), event.xdata, event.ydata
#         DraggableImage.lock = self
#         # draw everything but the selected rectangle and store the pixel buffer
#         canvas = self.point.figure.canvas
#         axes = self.point.axes
#         self.point.set_animated(True)
#         canvas.draw()
#         self.background = canvas.copy_from_bbox(self.point.axes.bbox)
#         # now redraw just the rectangle
#         axes.draw_artist(self.point)
#         # and blit just the redrawn area
#         canvas.blit(axes.bbox)
#
#     def on_motion(self, event):
#         if DraggableImage.lock is not self:
#             return
#         if event.inaxes != self.point.axes: return
#         x, y, xpress, ypress = self.press
#         dx = event.xdata - xpress
#         dy = event.ydata - ypress
#         self.point.set_extent([x[0] + dx, x[1] + dx, y[0] + dy, y[1] + dy])
#         canvas = self.point.figure.canvas
#         axes = self.point.axes
#         # restore the background region
#         canvas.restore_region(self.background)
#         # redraw just the current rectangle
#         axes.draw_artist(self.point)
#         # blit just the redrawn area
#         canvas.blit(axes.bbox)
#
#     def on_release(self, event):
#         'on release we reset the press data'
#         if DraggableImage.lock is not self:
#             return
