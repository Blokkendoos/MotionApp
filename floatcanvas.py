import tkinter as tk
from tkinter.font import Font
from pubsub import pub

from point import Point, FPoint


class FloatCanvas(tk.Canvas):
    """
    FloatCanvas implements a floating-point cartesian plane.
    @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael Gauland</a>
    """
    width = 400
    height = 400

    # All FloatCanvas objects are displayed using this font
    labelFont = None  # setup in __init__
    fontHeight = 22

    # The minimum and maximun x/y values in the plot area
    xMin = -1
    xMax = +1
    yMin = -1
    yMax = +1

    # The scaling to apply to convert from floating-point coordinates
    # to screen pixels.  It will be recalculated when the window is
    # resized, or any of xMin, xMax, yMin, or yMax change.
    scaleFactor = 1

    # Space between the top of the plot area and the top of the
    # graphics context.
    topMargin = 1

    # Space between the bottom of the plot area, and the bottom of the
    # graphics context.  This must leave room for the X-axis labels.
    bottomMargin = 20

    # Space between the left edge of the plot area, and the left edge of
    # the graphics context.  This must leave room for the Y-axis labels.
    leftMargin = 30

    # Space between the right edge of the plot area, and the right edge of
    # the graphics context.
    rightMargin = 1

    # The length of the tic-marks identifying the limits of the plot area.
    ticLength = 2

    # Colors
    defaultBackground = "white"
    defaultForeground = "blue"
    defaultScaleColor = "red"

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.configure(background=self.defaultBackground)
        self.labelFont = Font(family="Helvetica", weight="normal", size=8)

        pub.subscribe(self.set_limits, 'set_limits')
        pub.subscribe(self.draw_text, 'draw')
        pub.subscribe(self.draw_polygon, 'draw_polygon')
        pub.subscribe(self.draw_polygon_filled, 'draw_polygon_filled')
        pub.subscribe(self.draw_scales, 'draw_scales')

    def set_limits(self, value):
        """
        Set the floating-point boundariesof the plot area, rounded out
        to one decimal place (e.g., 1.00 would be treated as 1.00,
        but 1.01 would become 1.1).
        """
        xMin, xMax, yMin, yMax = value
        self.xMin = round(xMin)
        self.xMax = round(xMax)
        self.xMax = max(self.xMax, self.xMin + 1)
        self.yMin = round(yMin)
        self.yMax = round(yMax)
        self.yMax = max(self.yMax, self.yMin + 1)
        self.setScaleFactor()

    def setScaleFactor(self):
        """
        Calculate the scaling necessary to fit the full X and Y ranges into
        the graphics context.  To avoid distorting the image, we will calculate
        the scale factors independently, but use the smaller for both axes.
        """
        # For each axis, we want to represent a range of [Min, Max], over
        # the allotted number of pixels.  Note that the number of pixels
        # is determined by the top and bottom (or left and right) margins,
        # plus the "magic number" 2, which allows for the plot area border.
        yScale =\
            (self.height - (self.bottomMargin + self.topMargin + 2)) / (self.yMax - self.yMin)
        xScale =\
            (self.width - (self.leftMargin + self.rightMargin + 2)) / (self.xMax - self.xMin)
        if xScale < yScale:
            self.scaleFactor = xScale
        else:
            self.scaleFactor = yScale

    def scalePoint(self, fp):
        """
        Translate and scale the point, to convert it to a pixel location
        in the graphics context.
        """
        return Point((round((fp.x - self.xMin) * self.scaleFactor + self.leftMargin)),
                     (round(self.height - self.bottomMargin - (fp.y - self.yMin) * self.scaleFactor)))

    def draw_text(self, value):
        # TEST
        text = value
        self.create_text(50,  # self.width / 2,
                         50,  # self.height / 2,
                         text=text)

    def _draw_polygon(self, points, fill, outline):
        vertices_scaled = []
        for pt in points:
            pt_scaled = self.scalePoint(pt)
            vertices_scaled.append((pt_scaled.x, pt_scaled.y))
        self.create_polygon(vertices_scaled, fill=fill, outline=outline)

    def draw_polygon(self, value):
        points, color = value
        if color is None:
            color = self.defaultForeground
        self._draw_polygon(points, fill='', outline=color)

    def draw_polygon_filled(self, value):
        points, color = value
        if color is None:
            color = self.defaultForeground
        self._draw_polygon(points, fill=color, outline=color)

    def drawYLabel(self, value):
        """ Draw the a label along the Y axis, marking the floating-point value. """
        # Get the pixel coordinate of the point on the Y axis
        ticLoc = self.scalePoint(FPoint(0, value)).y
        # Generate a label string from the floating point value.
        label_str = f"{value:.2f}"
        # The label is located lower than the tic mark, by half the
        # height of the string.
        labelLoc = ticLoc + self.fontHeight / 2 + 1
        # If the label is at or near the top of the window, force
        # it down so that it will be visible.
        labelLimit = self.fontHeight + 1
        if labelLoc < labelLimit:
            labelLoc = labelLimit
        # Draw the tic mark, and the label string.
        self.create_line(self.leftMargin - self.ticLength,
                         ticLoc,
                         self.leftMargin,
                         ticLoc)
        self.create_text(self.leftMargin - self.labelFont.measure(label_str) - self.ticLength - 2,
                         labelLoc,
                         text=label_str)

    def drawXLabel(self, value):
        """ Draw the a label along the X axis, marking the floating-point value. """
        # Get the pixel coordinate of the point on the X axis
        ticLoc = self.scalePoint(FPoint(value, 0)).x
        # Generate a label string from the floating point value.
        label_str = f"{value:.2f}"
        # The label starts to the left of the tic mark, so it will be
        # centered on the tic.
        labelLoc = ticLoc - self.labelFont.measure(label_str) / 2
        # If the label is at or near the right of the window, force
        # it left so that it will be visible.
        labelLimit = self.width - self.rightMargin - self.labelFont.measure(label_str) - 3
        if labelLoc > labelLimit:
            labelLoc = labelLimit
        # Draw the tic mark, and draw the label string.
        self.create_line(ticLoc,
                         self.height - self.bottomMargin,
                         ticLoc,
                         self.height - self.bottomMargin + self.ticLength)
        # 2 pixels btw tic & string
        self.create_text(labelLoc,
                         self.height - self.bottomMargin + self.fontHeight + self.ticLength + 2,
                         text=label_str)

    def draw_scales(self):
        """ Draw the X and Y axes, and label them. """
        # Along with the axes, we draw a line across the top and right
        # edges of the plot area.  It's not really necessary, but it
        # looks good, and is easy to do.
        color = self.defaultScaleColor
        self.create_rectangle(self.leftMargin,
                              self.topMargin,
                              self.width - self.leftMargin - self.rightMargin - 1,
                              self.height - self.topMargin - self.bottomMargin - 1)
        # Draw the labels for the min and max points to be plotted.
        self.drawYLabel(self.yMin)
        self.drawYLabel(self.yMax)
        self.drawXLabel(self.xMin)
        self.drawXLabel(self.xMax)
