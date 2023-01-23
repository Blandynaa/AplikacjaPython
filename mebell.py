import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import AxesImage


class DraggableImage:
    lock = None

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
        point_number = self.parent.list_image.index(self)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.point.axes.bbox)
        axes.draw_artist(self.point)
        canvas.blit(axes.bbox)

    def on_motion(self, event):

        if DraggableImage.lock is not self: return
        if event.inaxes != self.point.axes: return
        dx = event.xdata - self.press[0]
        dy = event.ydata - self.press[1]
        self.press = event.xdata, event.ydata
        self.point.set_extent((self.point.get_extent()[0] + dx, self.point.get_extent()[1] + dx,
                               self.point.get_extent()[2] + dy, self.point.get_extent()[3] + dy))

        canvas = self.point.figure.canvas
        axes = self.point.axes

        canvas.restore_region(self.background)
        axes.draw_artist(self.point)
        canvas.blit(axes.bbox)

    def on_release(self, event):

        if DraggableImage.lock is not self: return
        self.press = None
        DraggableImage.lock = None
        self.point.set_animated(False)
        self.background = None
        self.point.figure.canvas.draw()

    def disconnect(self):

        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)
