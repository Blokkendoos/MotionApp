import tkinter as tk
from tkinter.font import Font
from pubsub import pub

from point import Point, FPoint


class FloatCanvas(tk.Canvas):
    """
    FloatCanvas implements a floating-point cartesian plane.
    @author <a href="mailto:MikeGauland@users.sourceforge.net">
    Michael Gauland</a>
    """
    # Space between the top of the plot area and the top of the
    # graphics context.
    topMargin = 1

    # Space between the bottom of the plot area, and the bottom of the
    # graphics context.  This must leave room for the X-axis labels.
    bottomMargin = 50

    # Space between the left edge of the plot area, and the left edge of
    # the graphics context.  This must leave room for the Y-axis labels.
    leftMargin = 50

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
        master.update()  # mainloop is not started yet
        # Derive my size from the master (Frame).
        # Reckon with the master border and the
        # offset of this Canvas within the master.
        self.master_offset = 10
        self.width = master.winfo_width() - self.master_offset
        self.height = master.winfo_height() - self.master_offset
        self.configure(background=self.defaultBackground)
        master.bind('<Configure>', self.resize)

        # All FloatCanvas objects are displayed using this font
        self.fontHeight = 11
        self.labelFont = Font(family="Times",
                              weight=tk.font.NORMAL,
                              size=self.fontHeight)

        # The minimum and maximun x/y values in the plot area
        self.xMin = -1
        self.xMax = +1
        self.yMin = -1
        self.yMax = +1

        # The scaling to apply to convert from floating-point coordinates
        # to screen pixels.  It will be recalculated when the window is
        # resized, or any of xMin, xMax, yMin, or yMax change.
        self.scaleFactor = 1

        pub.subscribe(self.set_limits, 'set_limits')
        pub.subscribe(self.draw_text, 'draw')
        pub.subscribe(self.draw_polyline, 'draw_polyline')
        pub.subscribe(self.draw_polygon, 'draw_polygon')
        pub.subscribe(self.draw_polygon_filled, 'draw_polygon_filled')
        pub.subscribe(self.draw_scales, 'draw_scales')

    def resize(self, event):
        self.width = event.width - self.master_offset
        self.height = event.height - self.master_offset
        pub.sendMessage('update_simulation')

    def set_limits(self, value):
        """
        Set the floating-point boundaries of the plot area, rounded
        to one decimal place (e.g., 1.00 would be treated as 1.00,
        but 1.01 would become 1.1).
        """
        xMin, xMax, yMin, yMax = value
        self.xMin = round(xMin, 1)
        self.xMax = round(xMax, 1)
        self.xMax = max(self.xMax, self.xMin + 1)
        self.yMin = round(yMin, 1)
        self.yMax = round(yMax, 1)
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
        # plus the plot area border width.
        border_width = 2
        yScale = self.height -\
            (self.bottomMargin + self.topMargin + border_width)
        yScale /= (self.yMax - self.yMin)
        xScale = self.width -\
            (self.leftMargin + self.rightMargin + border_width)
        xScale /= (self.xMax - self.xMin)
        self.scaleFactor = min(xScale, yScale)

    def scalePoint(self, fp):
        """
        Translate and scale the point, to convert it to a pixel location
        in the graphics context.
        """
        x = (round((fp.x - self.xMin) * self.scaleFactor + self.leftMargin))
        y = (round(self.height - self.bottomMargin -
                   (fp.y - self.yMin) * self.scaleFactor))
        return Point(x, y)

    def draw_text(self, value):
        # TEST
        text = value
        self.create_text(50,  # self.width / 2,
                         50,  # self.height / 2,
                         font=self.labelFont,
                         text=text)

    def _draw_polygon(self, points, fill, outline):
        vertices_scaled = []
        for pt in points:
            pt_scaled = self.scalePoint(pt)
            vertices_scaled.append((pt_scaled.x, pt_scaled.y))
        self.create_polygon(vertices_scaled, fill=fill, outline=outline)

    def _draw_polyline(self, points, numPoints, fill):
        if fill is None:
            fill = self.defaultForeground
        vertices_scaled = []
        for i in range(numPoints):
            pt_scaled = self.scalePoint(points[i])
            vertices_scaled.append(pt_scaled)
        for i in range(1, len(vertices_scaled)):
            x0 = vertices_scaled[i - 1].x
            y0 = vertices_scaled[i - 1].y
            x1 = vertices_scaled[i].x
            y1 = vertices_scaled[i].y
            self.create_line(x0, y0, x1, y1, fill=fill)

    def draw_polyline(self, value):
        points, numPoints, color = value
        if color is None:
            color = self.defaultForeground
        self._draw_polyline(points, numPoints, fill=color)

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
        """
        Draw the a label along the Y axis, marking the floating-point value.
        """
        # Get the pixel coordinate of the point on the Y axis
        ticLoc = self.scalePoint(FPoint(0, value)).y
        # Generate a label string from the floating point value.
        label_str = f"{value:.1f}"
        # The label is located lower than the tic mark, by half the
        # height of the string.
        labelLoc = ticLoc + self.fontHeight / 2 + 1
        # If the label is at or near the top of the window, force
        # it down so that it will be visible.
        labelLimit = self.fontHeight + 1
        labelLoc = max(labelLoc, labelLimit)
        # Draw the tic mark, and the label string.
        self.create_line(self.leftMargin - self.ticLength,
                         ticLoc,
                         self.leftMargin,
                         ticLoc)
        # 2 pixels between tic & string
        x = self.leftMargin -\
            self.labelFont.measure(label_str) - self.ticLength - 2
        y = labelLoc
        self.create_text(x, y, font=self.labelFont, text=label_str)

    def drawXLabel(self, value):
        """
        Draw the a label along the X axis, marking the floating-point value.
        """
        # Get the pixel coordinate of the point on the X axis
        ticLoc = self.scalePoint(FPoint(value, 0)).x
        # Generate a label string from the floating point value.
        label_str = f"{value:.1f}"
        # The label starts to the left of the tic mark, so it will be
        # centered on the tic.
        labelLoc = ticLoc  # - self.labelFont.measure(label_str) / 2
        # If the label is at or near the right of the window, force
        # it left so that it will be visible.
        labelLimit = self.width -\
            self.rightMargin - self.labelFont.measure(label_str) - 3
        labelLoc = min(labelLimit, labelLoc)
        # Draw the tic mark, and the label string.
        self.create_line(ticLoc,
                         self.height - self.bottomMargin,
                         ticLoc,
                         self.height - self.bottomMargin + self.ticLength)
        # 2 pixels btw tic & string
        x = labelLoc
        y = self.height -\
            self.bottomMargin + self.fontHeight + self.ticLength + 2,
        self.create_text(x, y, font=self.labelFont, text=label_str)

    def draw_scales(self):
        """ Draw the X and Y axes, and label them. """
        self.delete('all')  # clear the canvas

        # Along with the axes, we draw a line across the top and right
        # edges of the plot area.  It's not really necessary, but it
        # looks good, and is easy to do.
        color = self.defaultScaleColor
        self.create_rectangle(self.leftMargin,
                              self.topMargin,
                              self.width - self.rightMargin - 1,
                              self.height - self.bottomMargin - 1,
                              outline=color)
        # Draw the labels for the min and max points to be plotted.
        self.drawYLabel(self.yMin)
        self.drawYLabel(self.yMax)
        self.drawXLabel(self.xMin)
        self.drawXLabel(self.xMax)
