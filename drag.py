import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D


class DraggablePoint:
    lock = None

    def __init__(self, parent, x=0.1, y=0.1, size=0.001):

        self.parent = parent
        self.point = patches.Circle((x,y), size*0.2, edgecolor="black", fc="black")
        self.x = x
        self.y = y
        parent.fig.axes[0].add_patch(self.point)
        self.press = None
        self.background = None
        self.connect()
        self.line = None

        if self.parent.list_points:
            line_x = [self.parent.list_points[-1].x, self.x]
            line_y = [self.parent.list_points[-1].y, self.y]

            self.line = Line2D(line_x, line_y, color='black', alpha=1)
            parent.fig.axes[0].add_line(self.line)

    def connect(self):

        self.cidpress = self.point.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.point.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.cidmotion = self.point.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

    def on_press(self, event):

        if event.inaxes != self.point.axes: return
        if DraggablePoint.lock is not None: return
        contains, attrd = self.point.contains(event)
        if not contains: return
        self.press = self.point.center, event.xdata, event.ydata
        DraggablePoint.lock = self

        canvas = self.point.figure.canvas
        axes = self.point.axes
        self.point.set_animated(True)

        point_number = self.parent.list_points.index(self)

        if self == self.parent.list_points[0]:
            self.parent.list_points[1].line.set_animated(True)
        elif self == self.parent.list_points[-1]:
            self.line.set_animated(True)
        else:
            self.line.set_animated(True)
            self.parent.list_points[point_number + 1].line.set_animated(True)

        canvas.draw()
        self.background = canvas.copy_from_bbox(self.point.axes.bbox)

        axes.draw_artist(self.point)

        canvas.blit(axes.bbox)

    def on_motion(self, event):

        if DraggablePoint.lock is not self:
            return
        if event.inaxes != self.point.axes: return
        self.point.center, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.point.center = (self.point.center[0] + dx, self.point.center[1] + dy)

        canvas = self.point.figure.canvas
        axes = self.point.axes
        canvas.restore_region(self.background)

        axes.draw_artist(self.point)

        point_number = self.parent.list_points.index(self)
        self.x = self.point.center[0]
        self.y = self.point.center[1]

        if self == self.parent.list_points[0]:
            self.parent.list_points[1].line.set_animated(True)
            axes.draw_artist(self.parent.list_points[1].line)

        elif self == self.parent.list_points[-1]:
            axes.draw_artist(self.line)

        else:
            axes.draw_artist(self.line)
            axes.draw_artist(self.parent.list_points[point_number + 1].line)

        if self == self.parent.list_points[0]:
            line_x = [self.x, self.parent.list_points[1].x]
            line_y = [self.y, self.parent.list_points[1].y]
            self.parent.list_points[1].line.set_data(line_x, line_y)

        elif self == self.parent.list_points[-1]:
            line_x = [self.parent.list_points[-2].x, self.x]
            line_y = [self.parent.list_points[-2].y, self.y]
            self.line.set_data(line_x, line_y)
        else:
            line_x = [self.x, self.parent.list_points[point_number + 1].x]
            line_y = [self.y, self.parent.list_points[point_number + 1].y]
            self.parent.list_points[point_number + 1].line.set_data(line_x, line_y)

            line_x = [self.parent.list_points[point_number - 1].x, self.x]
            line_y = [self.parent.list_points[point_number - 1].y, self.y]
            self.line.set_data(line_x, line_y)

        canvas.blit(axes.bbox)

    def on_release(self, event):

        if DraggablePoint.lock is not self:
            return

        self.press = None
        DraggablePoint.lock = None

        self.point.set_animated(False)

        point_number = self.parent.list_points.index(self)

        if self == self.parent.list_points[0]:
            self.parent.list_points[1].line.set_animated(False)
        elif self == self.parent.list_points[-1]:
            self.line.set_animated(False)
        else:
            self.line.set_animated(False)
            self.parent.list_points[point_number + 1].line.set_animated(False)

        self.background = None

        self.point.figure.canvas.draw()

        self.x = self.point.center[0]
        self.y = self.point.center[1]

    def disconnect(self):
        self.point.figure.canvas.mpl_disconnect(self.cidpress)
        self.point.figure.canvas.mpl_disconnect(self.cidrelease)
        self.point.figure.canvas.mpl_disconnect(self.cidmotion)
