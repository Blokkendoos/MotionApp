#!/usr/bin/env python
""" generated source for module FloatCanvas """
# 
#  * FloatCanvas implements a floating-point cartesian plane.
#  
import java.awt.Canvas

import java.awt.event

import java.awt.Graphics

import java.awt

# 
#  * FloatCanvas implements a floating-point cartesian plane.
#  *
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
#  * Michael Gauland</a>
#  * @version 1.
#  
class FloatCanvas(Canvas, ComponentListener):
    """ generated source for class FloatCanvas """
    # 
    #      * All FloatCanvas objects are displayed using this font,
    #      * which is initialized to 8-point "Monospaced".
    #      *
    #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
    #      * FloatCanvas objects use the same font, but then it doesn't seem to
    #      * show up in the generated documents.)</I></FONT></P>
    #      
    labelFont = Font("Monospaced", Font.PLAIN, 8)

    # 
    #      * Metrics for the label font are stored here, but it cannot
    #      * be obtained until an object is instantiated, since we need
    #      * a graphics context to access the "getFontMetrics()" function.
    #      *
    #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
    #      * FloatCanvas objects use the same font, but then it doesn't seem to
    #      * show up in the generated documents.)</I></FONT></P>
    #      
    fontMetric = FontMetrics()

    # 
    #      * We'll grab the font height once, since we need it often, and it
    #      * won't change.
    #      *
    #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
    #      * FloatCanvas objects use the same font, but then it doesn't seem to
    #      * show up in the generated documents.)</I></FONT></P>
    #      
    fontHeight = int()

    # 
    #      * This will be set to the area used for the plot&mdash;i.e., the
    #      * graphics area, minus the border area used for the axis labels.
    #      * It is used to set the clipping region while drawing or plotting
    #      * to the graph.
    #      
    plotRect = Rectangle()

    # 
    #      * For smoother updates, data is plotted to this off-screen image,
    #      * then displayed all at once.
    #      
    imageBuffer = None

    # 
    #      * This variable stores one object that can be drawn in the canvas.
    #      * For MotionApplet, that will be the MotionApplet object, which will
    #      * draw the robot's paths in the canvas.  This could be changed to an
    #      * array or collection, to allow mutliple objects to be drawn onto the
    #      * same canvas.
    #      *
    #      * <P>The drawFunc() function for this object is called whenever the
    #      * FloatCanvas is drawn or refreshed.
    #      
    theInterface = DrawInterface()

    #  The minimum X value in the plot area 
    xMin = -1

    #  The maximum X value in the plot area 
    xMax = +1

    #  The minimum Y value in the plot area 
    yMin = -1

    #  The maximum Y value in the plot area 
    yMax = +1

    # 
    #      * The scaling to apply to convert from floating-point coordinates
    #      * to screen pixels.  It will be recalculated when the window is
    #      * resized, or any of xMin, xMax, yMin, or yMax change.
    #      
    scaleFactor = 1

    # 
    #      * Space between the top of the plot area and the top of the
    #      * graphics context.
    #      
    topMargin = 1

    # 
    #      * Space between the bottom of the plot area, and the bottom of the
    #      * graphics context.  This must leave room for the X-axis labels.
    #      
    bottomMargin = 20

    # 
    #      * Space between the left edge of the plot area, and the left edge of
    #      * the graphics context.  This must leave room for the Y-axis labels.
    #      
    leftMargin = 30

    # 
    #      * Space between the right edge of the plot area, and the right edge of
    #      * the graphics context.
    #      
    rightMargin = 1

    # 
    #      * The length of the tic marks identifying the limits of the plot area.
    #      
    ticLength = 2

    #  Default background color for a FloatCanvas object. 
    defaultBackground = Color.white

    #  Default foreground color for a FloatCanvas object. 
    defaultForeground = Color.blue

    #  Default color for scales. 
    defaultScaleColor = Color.red

    # 
    #      * Default constructor--set background and foreground colors to
    #      * defaults, and add the object as a "ComponentListener" of its
    #      * superclass.
    #      
    def __init__(self):
        """ generated source for method __init__ """
        super(FloatCanvas, self).__init__()
        setBackground(self.defaultBackground)
        setForeground(self.defaultForeground)
        super(FloatCanvas, self).addComponentListener(self)

    # 
    #      * getGraphics() overrides the superclass getGraphics function.  When
    #      * plotting the clients drawFunc() function, we draw the image off-screen,
    #      * then display the buffered image all at once, to reduce flicker.
    #     
    def getGraphics(self):
        """ generated source for method getGraphics """
        # 
        #     * If we're drawing off-screen, the imageBuffer member variable
        #     * will reference the off-screen graphics context we are drawing to.
        #     * If it is null, then we are not drawing off-screen, and should
        #     * use the superclass's getGraphics() function instead.
        #     
        if self.imageBuffer != None:
            return self.imageBuffer.getGraphics()
        else:
            return super(FloatCanvas, self).getGraphics()

    # 
    #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
    #      * then sets the clipping area so that anything drawn outside the plot
    #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
    #      * will be clipped.
    #      
    def getPlotGraphics(self):
        """ generated source for method getPlotGraphics """
        g = self.getGraphics()
        g.setClip(self.plotRect)
        return g

    # 
    #      * Required for the ComponentListener interface, but doesn't do
    #      * anything.
    #      
    def componentResized(self, e):
        """ generated source for method componentResized """

    # 
    #      * Required for the ComponentListener interface, but doesn't do
    #      * anything.
    #      
    def componentMoved(self, e):
        """ generated source for method componentMoved """

    # 
    #      * Required for the ComponentListener interface, but doesn't do
    #      * anything.
    #      
    def componentHidden(self, e):
        """ generated source for method componentHidden """

    # 
    #      * Required for the ComponentListener interface, but doesn't do
    #      * anything.
    #      
    def componentShown(self, e):
        """ generated source for method componentShown """

    # 
    #      * We need to grab the font metrics, but even though the font won't
    #      * change, we can't grab it until we have a graphics context from which
    #      * to call getFontMetrics().  Therefore, we can't call it from the
    #      * FloatCanvas constructor; instead, we'll call this function the
    #      * first time we need to use the font information.  After that, the
    #      * member variables fontMetric and fontHeight will be non-null, and
    #      * this function will not be called a second time.
    #      
    def grabFontInfo(self):
        """ generated source for method grabFontInfo """
        g = self.getGraphics()
        self.fontMetric = g.getFontMetrics(labelFont)
        self.fontHeight = fontMetric.getAscent()

    # 
    #      * setLimits() sets the floating-point boundariesof the plot area,
    #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
    #      * but 1.01 would become 1.1).
    #      
    def setLimits(self, xMin, xMax, yMin, yMax):
        """ generated source for method setLimits """
        # 
        #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
        #     * to one decimal place.  This works for the MotionApplet applet,
        #     * but should really be more flexible.
        #     
        self.xMin = Math.floor(xMin * 10.0) / 10.0
        self.xMax = Math.ceil(xMax * 10.0) / 10.0
        self.yMin = Math.floor(yMin * 10.0) / 10.0
        self.yMax = Math.ceil(yMax * 10.0) / 10.0
        # 
        #     * After changing the limits of the plot area, we need to recalculate
        #     * the scale factor for converting from floating-point values to
        #     * display pixels.
        #     
        setScaleFactor()

    # 
    #      * setScaleFactor() calculates the scaling necessary to fit the full
    #      * X and Y ranges into the graphics context.  To avoid distorting the
    #      * image, we will calculate the scale factors independently, but use the
    #      * smaller for both axes.
    #      
    def setScaleFactor(self):
        """ generated source for method setScaleFactor """
        # 
        #     * For each axis, we want to represent a range of [Min, Max], over
        #     * the allotted number of pixels.  Note that the number of pixels
        #     * is determined by the top and bottom (or left and right) margins,
        #     * plus the "magic number" 2, which allows for the plot area border.
        #     
        yScale = (getSize().height - (self.bottomMargin + self.topMargin + 2)) / (self.yMax - self.yMin)
        xScale = (getSize().width - (self.leftMargin + self.rightMargin + 2)) / (self.xMax - self.xMin)
        self.scaleFactor = xScale if (xScale < yScale) else yScale

    # 
    #      * Translate and scale the point, to convert it to a pixel location
    #      * in the graphics context.
    #      
    def scalePoint(self, fp):
        """ generated source for method scalePoint """
        return Point((Math.round((fp.x - self.xMin) * self.scaleFactor + self.leftMargin)), (Math.round(getSize().height - self.bottomMargin - (fp.y - self.yMin) * self.scaleFactor)))

    # 
    #      * Plot the point in the current foreground color.
    #      
    @overloaded
    def plot(self, fp):
        """ generated source for method plot """
        self.plot(fp, getForeground())

    # 
    #      * Plot the point in the specified color.
    #      
    @plot.register(object, FPoint, Color)
    def plot_0(self, fp, c):
        """ generated source for method plot_0 """
        # 
        #          * Get the graphics context, set to clip to the plot area.
        #          
        g = self.getPlotGraphics()
        g.setColor(c)
        #  Set the color
        p = self.scalePoint(fp)
        #  Convert to a pixel location
        # 
        #          * Draw the point as a tiny circle. When I tried to make it a
        #          * single pixel, it didn't show up on one system (Mac or Windows NT;
        #          * I don't remember which).
        #          
        g.fillOval(p.x - 1, p.y - 1, 3, 3)

    # 
    #      * This is similar to the "drawPolyline()" method of the Graphics
    #      * class, but uses floating-point coordinates.
    #      
    @overloaded
    def drawPolyline(self, fp, numPoints, c):
        """ generated source for method drawPolyline """
        x = [None]*numPoints
        #  Translated X values
        y = [None]*numPoints
        #  Translated Y values
        i = int()
        #  Loop index
        p = Point()
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  *
        #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
        #  * Michael Gauland</a>
        #  * @version 1.
        #  
        # 
        #      * All FloatCanvas objects are displayed using this font,
        #      * which is initialized to 8-point "Monospaced".
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * Metrics for the label font are stored here, but it cannot
        #      * be obtained until an object is instantiated, since we need
        #      * a graphics context to access the "getFontMetrics()" function.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * We'll grab the font height once, since we need it often, and it
        #      * won't change.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * This will be set to the area used for the plot&mdash;i.e., the
        #      * graphics area, minus the border area used for the axis labels.
        #      * It is used to set the clipping region while drawing or plotting
        #      * to the graph.
        #      
        # 
        #      * For smoother updates, data is plotted to this off-screen image,
        #      * then displayed all at once.
        #      
        # 
        #      * This variable stores one object that can be drawn in the canvas.
        #      * For MotionApplet, that will be the MotionApplet object, which will
        #      * draw the robot's paths in the canvas.  This could be changed to an
        #      * array or collection, to allow mutliple objects to be drawn onto the
        #      * same canvas.
        #      *
        #      * <P>The drawFunc() function for this object is called whenever the
        #      * FloatCanvas is drawn or refreshed.
        #      
        #  The minimum X value in the plot area 
        #  The maximum X value in the plot area 
        #  The minimum Y value in the plot area 
        #  The maximum Y value in the plot area 
        # 
        #      * The scaling to apply to convert from floating-point coordinates
        #      * to screen pixels.  It will be recalculated when the window is
        #      * resized, or any of xMin, xMax, yMin, or yMax change.
        #      
        # 
        #      * Space between the top of the plot area and the top of the
        #      * graphics context.
        #      
        # 
        #      * Space between the bottom of the plot area, and the bottom of the
        #      * graphics context.  This must leave room for the X-axis labels.
        #      
        # 
        #      * Space between the left edge of the plot area, and the left edge of
        #      * the graphics context.  This must leave room for the Y-axis labels.
        #      
        # 
        #      * Space between the right edge of the plot area, and the right edge of
        #      * the graphics context.
        #      
        # 
        #      * The length of the tic marks identifying the limits of the plot area.
        #      
        #  Default background color for a FloatCanvas object. 
        #  Default foreground color for a FloatCanvas object. 
        #  Default color for scales. 
        # 
        #      * Default constructor--set background and foreground colors to
        #      * defaults, and add the object as a "ComponentListener" of its
        #      * superclass.
        #      
        # 
        #      * getGraphics() overrides the superclass getGraphics function.  When
        #      * plotting the clients drawFunc() function, we draw the image off-screen,
        #      * then display the buffered image all at once, to reduce flicker.
        #     
        # 
        #     * If we're drawing off-screen, the imageBuffer member variable
        #     * will reference the off-screen graphics context we are drawing to.
        #     * If it is null, then we are not drawing off-screen, and should
        #     * use the superclass's getGraphics() function instead.
        #     
        # 
        #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
        #      * then sets the clipping area so that anything drawn outside the plot
        #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
        #      * will be clipped.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * We need to grab the font metrics, but even though the font won't
        #      * change, we can't grab it until we have a graphics context from which
        #      * to call getFontMetrics().  Therefore, we can't call it from the
        #      * FloatCanvas constructor; instead, we'll call this function the
        #      * first time we need to use the font information.  After that, the
        #      * member variables fontMetric and fontHeight will be non-null, and
        #      * this function will not be called a second time.
        #      
        # 
        #      * setLimits() sets the floating-point boundariesof the plot area,
        #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
        #      * but 1.01 would become 1.1).
        #      
        # 
        #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
        #     * to one decimal place.  This works for the MotionApplet applet,
        #     * but should really be more flexible.
        #     
        # 
        #     * After changing the limits of the plot area, we need to recalculate
        #     * the scale factor for converting from floating-point values to
        #     * display pixels.
        #     
        # 
        #      * setScaleFactor() calculates the scaling necessary to fit the full
        #      * X and Y ranges into the graphics context.  To avoid distorting the
        #      * image, we will calculate the scale factors independently, but use the
        #      * smaller for both axes.
        #      
        # 
        #     * For each axis, we want to represent a range of [Min, Max], over
        #     * the allotted number of pixels.  Note that the number of pixels
        #     * is determined by the top and bottom (or left and right) margins,
        #     * plus the "magic number" 2, which allows for the plot area border.
        #     
        # 
        #      * Translate and scale the point, to convert it to a pixel location
        #      * in the graphics context.
        #      
        # 
        #      * Plot the point in the current foreground color.
        #      
        # 
        #      * Plot the point in the specified color.
        #      
        # 
        #          * Get the graphics context, set to clip to the plot area.
        #          
        #  Set the color
        #  Convert to a pixel location
        # 
        #          * Draw the point as a tiny circle. When I tried to make it a
        #          * single pixel, it didn't show up on one system (Mac or Windows NT;
        #          * I don't remember which).
        #          
        # 
        #      * This is similar to the "drawPolyline()" method of the Graphics
        #      * class, but uses floating-point coordinates.
        #      
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        while i < numPoints:
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  *
            #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
            #  * Michael Gauland</a>
            #  * @version 1.
            #  
            # 
            #      * All FloatCanvas objects are displayed using this font,
            #      * which is initialized to 8-point "Monospaced".
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * Metrics for the label font are stored here, but it cannot
            #      * be obtained until an object is instantiated, since we need
            #      * a graphics context to access the "getFontMetrics()" function.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * We'll grab the font height once, since we need it often, and it
            #      * won't change.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * This will be set to the area used for the plot&mdash;i.e., the
            #      * graphics area, minus the border area used for the axis labels.
            #      * It is used to set the clipping region while drawing or plotting
            #      * to the graph.
            #      
            # 
            #      * For smoother updates, data is plotted to this off-screen image,
            #      * then displayed all at once.
            #      
            # 
            #      * This variable stores one object that can be drawn in the canvas.
            #      * For MotionApplet, that will be the MotionApplet object, which will
            #      * draw the robot's paths in the canvas.  This could be changed to an
            #      * array or collection, to allow mutliple objects to be drawn onto the
            #      * same canvas.
            #      *
            #      * <P>The drawFunc() function for this object is called whenever the
            #      * FloatCanvas is drawn or refreshed.
            #      
            #  The minimum X value in the plot area 
            #  The maximum X value in the plot area 
            #  The minimum Y value in the plot area 
            #  The maximum Y value in the plot area 
            # 
            #      * The scaling to apply to convert from floating-point coordinates
            #      * to screen pixels.  It will be recalculated when the window is
            #      * resized, or any of xMin, xMax, yMin, or yMax change.
            #      
            # 
            #      * Space between the top of the plot area and the top of the
            #      * graphics context.
            #      
            # 
            #      * Space between the bottom of the plot area, and the bottom of the
            #      * graphics context.  This must leave room for the X-axis labels.
            #      
            # 
            #      * Space between the left edge of the plot area, and the left edge of
            #      * the graphics context.  This must leave room for the Y-axis labels.
            #      
            # 
            #      * Space between the right edge of the plot area, and the right edge of
            #      * the graphics context.
            #      
            # 
            #      * The length of the tic marks identifying the limits of the plot area.
            #      
            #  Default background color for a FloatCanvas object. 
            #  Default foreground color for a FloatCanvas object. 
            #  Default color for scales. 
            # 
            #      * Default constructor--set background and foreground colors to
            #      * defaults, and add the object as a "ComponentListener" of its
            #      * superclass.
            #      
            # 
            #      * getGraphics() overrides the superclass getGraphics function.  When
            #      * plotting the clients drawFunc() function, we draw the image off-screen,
            #      * then display the buffered image all at once, to reduce flicker.
            #     
            # 
            #     * If we're drawing off-screen, the imageBuffer member variable
            #     * will reference the off-screen graphics context we are drawing to.
            #     * If it is null, then we are not drawing off-screen, and should
            #     * use the superclass's getGraphics() function instead.
            #     
            # 
            #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
            #      * then sets the clipping area so that anything drawn outside the plot
            #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
            #      * will be clipped.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * We need to grab the font metrics, but even though the font won't
            #      * change, we can't grab it until we have a graphics context from which
            #      * to call getFontMetrics().  Therefore, we can't call it from the
            #      * FloatCanvas constructor; instead, we'll call this function the
            #      * first time we need to use the font information.  After that, the
            #      * member variables fontMetric and fontHeight will be non-null, and
            #      * this function will not be called a second time.
            #      
            # 
            #      * setLimits() sets the floating-point boundariesof the plot area,
            #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
            #      * but 1.01 would become 1.1).
            #      
            # 
            #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
            #     * to one decimal place.  This works for the MotionApplet applet,
            #     * but should really be more flexible.
            #     
            # 
            #     * After changing the limits of the plot area, we need to recalculate
            #     * the scale factor for converting from floating-point values to
            #     * display pixels.
            #     
            # 
            #      * setScaleFactor() calculates the scaling necessary to fit the full
            #      * X and Y ranges into the graphics context.  To avoid distorting the
            #      * image, we will calculate the scale factors independently, but use the
            #      * smaller for both axes.
            #      
            # 
            #     * For each axis, we want to represent a range of [Min, Max], over
            #     * the allotted number of pixels.  Note that the number of pixels
            #     * is determined by the top and bottom (or left and right) margins,
            #     * plus the "magic number" 2, which allows for the plot area border.
            #     
            # 
            #      * Translate and scale the point, to convert it to a pixel location
            #      * in the graphics context.
            #      
            # 
            #      * Plot the point in the current foreground color.
            #      
            # 
            #      * Plot the point in the specified color.
            #      
            # 
            #          * Get the graphics context, set to clip to the plot area.
            #          
            #  Set the color
            #  Convert to a pixel location
            # 
            #          * Draw the point as a tiny circle. When I tried to make it a
            #          * single pixel, it didn't show up on one system (Mac or Windows NT;
            #          * I don't remember which).
            #          
            # 
            #      * This is similar to the "drawPolyline()" method of the Graphics
            #      * class, but uses floating-point coordinates.
            #      
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Convert each floating-point coordinate pair to
            #          * a pixel coordinate in the Graphics context.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            p = scalePoint(fp[i])
            x[i] = p.x
            y[i] = p.y
            i += 1
        # 
        #          * Get the graphics context, with the clipping region set to
        #          * the plot area; set the color; and draw the integer points.
        #          
        g = self.getPlotGraphics()
        g.setColor(c)
        g.drawPolyline(x, y, numPoints)

    # 
    #      * Draw a floating-point "polyline" in the current foreground color.
    #      
    @drawPolyline.register(object, FPoint, int)
    def drawPolyline_0(self, fp, numPoints):
        """ generated source for method drawPolyline_0 """
        self.drawPolyline(fp, numPoints, getForeground())

    # 
    #      * Provide the functionality of the Graphics class's "drawPolygon()"
    #      * method, using floating-point coordinates.
    #      
    @overloaded
    def drawPolygon(self, fp, c):
        """ generated source for method drawPolygon """
        numPoints = fp.length
        #  The number of points provided
        x = [None]*numPoints
        #  Translated X values
        y = [None]*numPoints
        #  Translated Y values
        i = int()
        #  Loop index
        p = Point()
        #  Temporary pixel coordinates
        # 
        #          * Translate all the points from floating-point coordinaates
        #          * to pixel coordinates.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  *
        #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
        #  * Michael Gauland</a>
        #  * @version 1.
        #  
        # 
        #      * All FloatCanvas objects are displayed using this font,
        #      * which is initialized to 8-point "Monospaced".
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * Metrics for the label font are stored here, but it cannot
        #      * be obtained until an object is instantiated, since we need
        #      * a graphics context to access the "getFontMetrics()" function.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * We'll grab the font height once, since we need it often, and it
        #      * won't change.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * This will be set to the area used for the plot&mdash;i.e., the
        #      * graphics area, minus the border area used for the axis labels.
        #      * It is used to set the clipping region while drawing or plotting
        #      * to the graph.
        #      
        # 
        #      * For smoother updates, data is plotted to this off-screen image,
        #      * then displayed all at once.
        #      
        # 
        #      * This variable stores one object that can be drawn in the canvas.
        #      * For MotionApplet, that will be the MotionApplet object, which will
        #      * draw the robot's paths in the canvas.  This could be changed to an
        #      * array or collection, to allow mutliple objects to be drawn onto the
        #      * same canvas.
        #      *
        #      * <P>The drawFunc() function for this object is called whenever the
        #      * FloatCanvas is drawn or refreshed.
        #      
        #  The minimum X value in the plot area 
        #  The maximum X value in the plot area 
        #  The minimum Y value in the plot area 
        #  The maximum Y value in the plot area 
        # 
        #      * The scaling to apply to convert from floating-point coordinates
        #      * to screen pixels.  It will be recalculated when the window is
        #      * resized, or any of xMin, xMax, yMin, or yMax change.
        #      
        # 
        #      * Space between the top of the plot area and the top of the
        #      * graphics context.
        #      
        # 
        #      * Space between the bottom of the plot area, and the bottom of the
        #      * graphics context.  This must leave room for the X-axis labels.
        #      
        # 
        #      * Space between the left edge of the plot area, and the left edge of
        #      * the graphics context.  This must leave room for the Y-axis labels.
        #      
        # 
        #      * Space between the right edge of the plot area, and the right edge of
        #      * the graphics context.
        #      
        # 
        #      * The length of the tic marks identifying the limits of the plot area.
        #      
        #  Default background color for a FloatCanvas object. 
        #  Default foreground color for a FloatCanvas object. 
        #  Default color for scales. 
        # 
        #      * Default constructor--set background and foreground colors to
        #      * defaults, and add the object as a "ComponentListener" of its
        #      * superclass.
        #      
        # 
        #      * getGraphics() overrides the superclass getGraphics function.  When
        #      * plotting the clients drawFunc() function, we draw the image off-screen,
        #      * then display the buffered image all at once, to reduce flicker.
        #     
        # 
        #     * If we're drawing off-screen, the imageBuffer member variable
        #     * will reference the off-screen graphics context we are drawing to.
        #     * If it is null, then we are not drawing off-screen, and should
        #     * use the superclass's getGraphics() function instead.
        #     
        # 
        #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
        #      * then sets the clipping area so that anything drawn outside the plot
        #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
        #      * will be clipped.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * We need to grab the font metrics, but even though the font won't
        #      * change, we can't grab it until we have a graphics context from which
        #      * to call getFontMetrics().  Therefore, we can't call it from the
        #      * FloatCanvas constructor; instead, we'll call this function the
        #      * first time we need to use the font information.  After that, the
        #      * member variables fontMetric and fontHeight will be non-null, and
        #      * this function will not be called a second time.
        #      
        # 
        #      * setLimits() sets the floating-point boundariesof the plot area,
        #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
        #      * but 1.01 would become 1.1).
        #      
        # 
        #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
        #     * to one decimal place.  This works for the MotionApplet applet,
        #     * but should really be more flexible.
        #     
        # 
        #     * After changing the limits of the plot area, we need to recalculate
        #     * the scale factor for converting from floating-point values to
        #     * display pixels.
        #     
        # 
        #      * setScaleFactor() calculates the scaling necessary to fit the full
        #      * X and Y ranges into the graphics context.  To avoid distorting the
        #      * image, we will calculate the scale factors independently, but use the
        #      * smaller for both axes.
        #      
        # 
        #     * For each axis, we want to represent a range of [Min, Max], over
        #     * the allotted number of pixels.  Note that the number of pixels
        #     * is determined by the top and bottom (or left and right) margins,
        #     * plus the "magic number" 2, which allows for the plot area border.
        #     
        # 
        #      * Translate and scale the point, to convert it to a pixel location
        #      * in the graphics context.
        #      
        # 
        #      * Plot the point in the current foreground color.
        #      
        # 
        #      * Plot the point in the specified color.
        #      
        # 
        #          * Get the graphics context, set to clip to the plot area.
        #          
        #  Set the color
        #  Convert to a pixel location
        # 
        #          * Draw the point as a tiny circle. When I tried to make it a
        #          * single pixel, it didn't show up on one system (Mac or Windows NT;
        #          * I don't remember which).
        #          
        # 
        #      * This is similar to the "drawPolyline()" method of the Graphics
        #      * class, but uses floating-point coordinates.
        #      
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #          * Get the graphics context, with the clipping region set to
        #          * the plot area; set the color; and draw the integer points.
        #          
        # 
        #      * Draw a floating-point "polyline" in the current foreground color.
        #      
        # 
        #      * Provide the functionality of the Graphics class's "drawPolygon()"
        #      * method, using floating-point coordinates.
        #      
        #  The number of points provided
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Translate all the points from floating-point coordinaates
        #          * to pixel coordinates.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        while i < numPoints:
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  *
            #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
            #  * Michael Gauland</a>
            #  * @version 1.
            #  
            # 
            #      * All FloatCanvas objects are displayed using this font,
            #      * which is initialized to 8-point "Monospaced".
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * Metrics for the label font are stored here, but it cannot
            #      * be obtained until an object is instantiated, since we need
            #      * a graphics context to access the "getFontMetrics()" function.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * We'll grab the font height once, since we need it often, and it
            #      * won't change.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * This will be set to the area used for the plot&mdash;i.e., the
            #      * graphics area, minus the border area used for the axis labels.
            #      * It is used to set the clipping region while drawing or plotting
            #      * to the graph.
            #      
            # 
            #      * For smoother updates, data is plotted to this off-screen image,
            #      * then displayed all at once.
            #      
            # 
            #      * This variable stores one object that can be drawn in the canvas.
            #      * For MotionApplet, that will be the MotionApplet object, which will
            #      * draw the robot's paths in the canvas.  This could be changed to an
            #      * array or collection, to allow mutliple objects to be drawn onto the
            #      * same canvas.
            #      *
            #      * <P>The drawFunc() function for this object is called whenever the
            #      * FloatCanvas is drawn or refreshed.
            #      
            #  The minimum X value in the plot area 
            #  The maximum X value in the plot area 
            #  The minimum Y value in the plot area 
            #  The maximum Y value in the plot area 
            # 
            #      * The scaling to apply to convert from floating-point coordinates
            #      * to screen pixels.  It will be recalculated when the window is
            #      * resized, or any of xMin, xMax, yMin, or yMax change.
            #      
            # 
            #      * Space between the top of the plot area and the top of the
            #      * graphics context.
            #      
            # 
            #      * Space between the bottom of the plot area, and the bottom of the
            #      * graphics context.  This must leave room for the X-axis labels.
            #      
            # 
            #      * Space between the left edge of the plot area, and the left edge of
            #      * the graphics context.  This must leave room for the Y-axis labels.
            #      
            # 
            #      * Space between the right edge of the plot area, and the right edge of
            #      * the graphics context.
            #      
            # 
            #      * The length of the tic marks identifying the limits of the plot area.
            #      
            #  Default background color for a FloatCanvas object. 
            #  Default foreground color for a FloatCanvas object. 
            #  Default color for scales. 
            # 
            #      * Default constructor--set background and foreground colors to
            #      * defaults, and add the object as a "ComponentListener" of its
            #      * superclass.
            #      
            # 
            #      * getGraphics() overrides the superclass getGraphics function.  When
            #      * plotting the clients drawFunc() function, we draw the image off-screen,
            #      * then display the buffered image all at once, to reduce flicker.
            #     
            # 
            #     * If we're drawing off-screen, the imageBuffer member variable
            #     * will reference the off-screen graphics context we are drawing to.
            #     * If it is null, then we are not drawing off-screen, and should
            #     * use the superclass's getGraphics() function instead.
            #     
            # 
            #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
            #      * then sets the clipping area so that anything drawn outside the plot
            #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
            #      * will be clipped.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * We need to grab the font metrics, but even though the font won't
            #      * change, we can't grab it until we have a graphics context from which
            #      * to call getFontMetrics().  Therefore, we can't call it from the
            #      * FloatCanvas constructor; instead, we'll call this function the
            #      * first time we need to use the font information.  After that, the
            #      * member variables fontMetric and fontHeight will be non-null, and
            #      * this function will not be called a second time.
            #      
            # 
            #      * setLimits() sets the floating-point boundariesof the plot area,
            #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
            #      * but 1.01 would become 1.1).
            #      
            # 
            #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
            #     * to one decimal place.  This works for the MotionApplet applet,
            #     * but should really be more flexible.
            #     
            # 
            #     * After changing the limits of the plot area, we need to recalculate
            #     * the scale factor for converting from floating-point values to
            #     * display pixels.
            #     
            # 
            #      * setScaleFactor() calculates the scaling necessary to fit the full
            #      * X and Y ranges into the graphics context.  To avoid distorting the
            #      * image, we will calculate the scale factors independently, but use the
            #      * smaller for both axes.
            #      
            # 
            #     * For each axis, we want to represent a range of [Min, Max], over
            #     * the allotted number of pixels.  Note that the number of pixels
            #     * is determined by the top and bottom (or left and right) margins,
            #     * plus the "magic number" 2, which allows for the plot area border.
            #     
            # 
            #      * Translate and scale the point, to convert it to a pixel location
            #      * in the graphics context.
            #      
            # 
            #      * Plot the point in the current foreground color.
            #      
            # 
            #      * Plot the point in the specified color.
            #      
            # 
            #          * Get the graphics context, set to clip to the plot area.
            #          
            #  Set the color
            #  Convert to a pixel location
            # 
            #          * Draw the point as a tiny circle. When I tried to make it a
            #          * single pixel, it didn't show up on one system (Mac or Windows NT;
            #          * I don't remember which).
            #          
            # 
            #      * This is similar to the "drawPolyline()" method of the Graphics
            #      * class, but uses floating-point coordinates.
            #      
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Convert each floating-point coordinate pair to
            #          * a pixel coordinate in the Graphics context.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            # 
            #          * Get the graphics context, with the clipping region set to
            #          * the plot area; set the color; and draw the integer points.
            #          
            # 
            #      * Draw a floating-point "polyline" in the current foreground color.
            #      
            # 
            #      * Provide the functionality of the Graphics class's "drawPolygon()"
            #      * method, using floating-point coordinates.
            #      
            #  The number of points provided
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Translate all the points from floating-point coordinaates
            #          * to pixel coordinates.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            p = scalePoint(fp[i])
            x[i] = p.x
            y[i] = p.y
            i += 1
        # 
        #          * Get the graphics context, with the clipping region set to
        #          * the plot area; set the color; and draw the integer polygon.
        #          
        g = self.getPlotGraphics()
        g.setColor(c)
        g.drawPolygon(x, y, numPoints)

    # 
    #      * Draw a floating-point polygon, using the current foreground color.
    #      
    @drawPolygon.register(object, FPoint)
    def drawPolygon_0(self, fp):
        """ generated source for method drawPolygon_0 """
        self.drawPolygon(fp, getForeground())

    # 
    #      * This is similar to the "fillPolygon()" method of the Graphics
    #      * class, but uses floating-point coordinates.
    #      
    @overloaded
    def fillPolygon(self, fp, c):
        """ generated source for method fillPolygon """
        numPoints = fp.length
        #  Number of points provided
        x = [None]*numPoints
        #  Translated X values
        y = [None]*numPoints
        #  Translated Y values
        i = int()
        #  Loop index
        p = Point()
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  
        # 
        #  * FloatCanvas implements a floating-point cartesian plane.
        #  *
        #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
        #  * Michael Gauland</a>
        #  * @version 1.
        #  
        # 
        #      * All FloatCanvas objects are displayed using this font,
        #      * which is initialized to 8-point "Monospaced".
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * Metrics for the label font are stored here, but it cannot
        #      * be obtained until an object is instantiated, since we need
        #      * a graphics context to access the "getFontMetrics()" function.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * We'll grab the font height once, since we need it often, and it
        #      * won't change.
        #      *
        #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
        #      * FloatCanvas objects use the same font, but then it doesn't seem to
        #      * show up in the generated documents.)</I></FONT></P>
        #      
        # 
        #      * This will be set to the area used for the plot&mdash;i.e., the
        #      * graphics area, minus the border area used for the axis labels.
        #      * It is used to set the clipping region while drawing or plotting
        #      * to the graph.
        #      
        # 
        #      * For smoother updates, data is plotted to this off-screen image,
        #      * then displayed all at once.
        #      
        # 
        #      * This variable stores one object that can be drawn in the canvas.
        #      * For MotionApplet, that will be the MotionApplet object, which will
        #      * draw the robot's paths in the canvas.  This could be changed to an
        #      * array or collection, to allow mutliple objects to be drawn onto the
        #      * same canvas.
        #      *
        #      * <P>The drawFunc() function for this object is called whenever the
        #      * FloatCanvas is drawn or refreshed.
        #      
        #  The minimum X value in the plot area 
        #  The maximum X value in the plot area 
        #  The minimum Y value in the plot area 
        #  The maximum Y value in the plot area 
        # 
        #      * The scaling to apply to convert from floating-point coordinates
        #      * to screen pixels.  It will be recalculated when the window is
        #      * resized, or any of xMin, xMax, yMin, or yMax change.
        #      
        # 
        #      * Space between the top of the plot area and the top of the
        #      * graphics context.
        #      
        # 
        #      * Space between the bottom of the plot area, and the bottom of the
        #      * graphics context.  This must leave room for the X-axis labels.
        #      
        # 
        #      * Space between the left edge of the plot area, and the left edge of
        #      * the graphics context.  This must leave room for the Y-axis labels.
        #      
        # 
        #      * Space between the right edge of the plot area, and the right edge of
        #      * the graphics context.
        #      
        # 
        #      * The length of the tic marks identifying the limits of the plot area.
        #      
        #  Default background color for a FloatCanvas object. 
        #  Default foreground color for a FloatCanvas object. 
        #  Default color for scales. 
        # 
        #      * Default constructor--set background and foreground colors to
        #      * defaults, and add the object as a "ComponentListener" of its
        #      * superclass.
        #      
        # 
        #      * getGraphics() overrides the superclass getGraphics function.  When
        #      * plotting the clients drawFunc() function, we draw the image off-screen,
        #      * then display the buffered image all at once, to reduce flicker.
        #     
        # 
        #     * If we're drawing off-screen, the imageBuffer member variable
        #     * will reference the off-screen graphics context we are drawing to.
        #     * If it is null, then we are not drawing off-screen, and should
        #     * use the superclass's getGraphics() function instead.
        #     
        # 
        #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
        #      * then sets the clipping area so that anything drawn outside the plot
        #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
        #      * will be clipped.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * Required for the ComponentListener interface, but doesn't do
        #      * anything.
        #      
        # 
        #      * We need to grab the font metrics, but even though the font won't
        #      * change, we can't grab it until we have a graphics context from which
        #      * to call getFontMetrics().  Therefore, we can't call it from the
        #      * FloatCanvas constructor; instead, we'll call this function the
        #      * first time we need to use the font information.  After that, the
        #      * member variables fontMetric and fontHeight will be non-null, and
        #      * this function will not be called a second time.
        #      
        # 
        #      * setLimits() sets the floating-point boundariesof the plot area,
        #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
        #      * but 1.01 would become 1.1).
        #      
        # 
        #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
        #     * to one decimal place.  This works for the MotionApplet applet,
        #     * but should really be more flexible.
        #     
        # 
        #     * After changing the limits of the plot area, we need to recalculate
        #     * the scale factor for converting from floating-point values to
        #     * display pixels.
        #     
        # 
        #      * setScaleFactor() calculates the scaling necessary to fit the full
        #      * X and Y ranges into the graphics context.  To avoid distorting the
        #      * image, we will calculate the scale factors independently, but use the
        #      * smaller for both axes.
        #      
        # 
        #     * For each axis, we want to represent a range of [Min, Max], over
        #     * the allotted number of pixels.  Note that the number of pixels
        #     * is determined by the top and bottom (or left and right) margins,
        #     * plus the "magic number" 2, which allows for the plot area border.
        #     
        # 
        #      * Translate and scale the point, to convert it to a pixel location
        #      * in the graphics context.
        #      
        # 
        #      * Plot the point in the current foreground color.
        #      
        # 
        #      * Plot the point in the specified color.
        #      
        # 
        #          * Get the graphics context, set to clip to the plot area.
        #          
        #  Set the color
        #  Convert to a pixel location
        # 
        #          * Draw the point as a tiny circle. When I tried to make it a
        #          * single pixel, it didn't show up on one system (Mac or Windows NT;
        #          * I don't remember which).
        #          
        # 
        #      * This is similar to the "drawPolyline()" method of the Graphics
        #      * class, but uses floating-point coordinates.
        #      
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #          * Get the graphics context, with the clipping region set to
        #          * the plot area; set the color; and draw the integer points.
        #          
        # 
        #      * Draw a floating-point "polyline" in the current foreground color.
        #      
        # 
        #      * Provide the functionality of the Graphics class's "drawPolygon()"
        #      * method, using floating-point coordinates.
        #      
        #  The number of points provided
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Translate all the points from floating-point coordinaates
        #          * to pixel coordinates.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        # 
        #          * Get the graphics context, with the clipping region set to
        #          * the plot area; set the color; and draw the integer polygon.
        #          
        # 
        #      * Draw a floating-point polygon, using the current foreground color.
        #      
        # 
        #      * This is similar to the "fillPolygon()" method of the Graphics
        #      * class, but uses floating-point coordinates.
        #      
        #  Number of points provided
        #  Translated X values
        #  Translated Y values
        #  Loop index
        #  Temporary pixel coordinates
        # 
        #          * Convert each floating-point coordinate pair to
        #          * a pixel coordinate in the Graphics context.
        #          *
        #          * Note:  the "scaleFactor" member variable must have been
        #          * correctly set for this routine to work.  Currently, scaleFactor
        #          * is recalculated whenever the Graphics size, or any of xMin,
        #          * xMax, yMin, or yMax is changed.
        #          
        while i < numPoints:
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  
            # 
            #  * FloatCanvas implements a floating-point cartesian plane.
            #  *
            #  * @author <a href="mailto:MikeGauland@users.sourceforge.net">
            #  * Michael Gauland</a>
            #  * @version 1.
            #  
            # 
            #      * All FloatCanvas objects are displayed using this font,
            #      * which is initialized to 8-point "Monospaced".
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * Metrics for the label font are stored here, but it cannot
            #      * be obtained until an object is instantiated, since we need
            #      * a graphics context to access the "getFontMetrics()" function.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * We'll grab the font height once, since we need it often, and it
            #      * won't change.
            #      *
            #      * <P><FONT SIZE=-1><I>(This could be a class variable, since all
            #      * FloatCanvas objects use the same font, but then it doesn't seem to
            #      * show up in the generated documents.)</I></FONT></P>
            #      
            # 
            #      * This will be set to the area used for the plot&mdash;i.e., the
            #      * graphics area, minus the border area used for the axis labels.
            #      * It is used to set the clipping region while drawing or plotting
            #      * to the graph.
            #      
            # 
            #      * For smoother updates, data is plotted to this off-screen image,
            #      * then displayed all at once.
            #      
            # 
            #      * This variable stores one object that can be drawn in the canvas.
            #      * For MotionApplet, that will be the MotionApplet object, which will
            #      * draw the robot's paths in the canvas.  This could be changed to an
            #      * array or collection, to allow mutliple objects to be drawn onto the
            #      * same canvas.
            #      *
            #      * <P>The drawFunc() function for this object is called whenever the
            #      * FloatCanvas is drawn or refreshed.
            #      
            #  The minimum X value in the plot area 
            #  The maximum X value in the plot area 
            #  The minimum Y value in the plot area 
            #  The maximum Y value in the plot area 
            # 
            #      * The scaling to apply to convert from floating-point coordinates
            #      * to screen pixels.  It will be recalculated when the window is
            #      * resized, or any of xMin, xMax, yMin, or yMax change.
            #      
            # 
            #      * Space between the top of the plot area and the top of the
            #      * graphics context.
            #      
            # 
            #      * Space between the bottom of the plot area, and the bottom of the
            #      * graphics context.  This must leave room for the X-axis labels.
            #      
            # 
            #      * Space between the left edge of the plot area, and the left edge of
            #      * the graphics context.  This must leave room for the Y-axis labels.
            #      
            # 
            #      * Space between the right edge of the plot area, and the right edge of
            #      * the graphics context.
            #      
            # 
            #      * The length of the tic marks identifying the limits of the plot area.
            #      
            #  Default background color for a FloatCanvas object. 
            #  Default foreground color for a FloatCanvas object. 
            #  Default color for scales. 
            # 
            #      * Default constructor--set background and foreground colors to
            #      * defaults, and add the object as a "ComponentListener" of its
            #      * superclass.
            #      
            # 
            #      * getGraphics() overrides the superclass getGraphics function.  When
            #      * plotting the clients drawFunc() function, we draw the image off-screen,
            #      * then display the buffered image all at once, to reduce flicker.
            #     
            # 
            #     * If we're drawing off-screen, the imageBuffer member variable
            #     * will reference the off-screen graphics context we are drawing to.
            #     * If it is null, then we are not drawing off-screen, and should
            #     * use the superclass's getGraphics() function instead.
            #     
            # 
            #      * getPlotGraphics() retrieves the graphics conext through getGraphics(),
            #      * then sets the clipping area so that anything drawn outside the plot
            #      * area (delimited by the floating-point values xMin, xMax, yMin, and yMax)
            #      * will be clipped.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * Required for the ComponentListener interface, but doesn't do
            #      * anything.
            #      
            # 
            #      * We need to grab the font metrics, but even though the font won't
            #      * change, we can't grab it until we have a graphics context from which
            #      * to call getFontMetrics().  Therefore, we can't call it from the
            #      * FloatCanvas constructor; instead, we'll call this function the
            #      * first time we need to use the font information.  After that, the
            #      * member variables fontMetric and fontHeight will be non-null, and
            #      * this function will not be called a second time.
            #      
            # 
            #      * setLimits() sets the floating-point boundariesof the plot area,
            #      * rounded out to one decimal place (e.g., 1.00 would be treated as 1.00,
            #      * but 1.01 would become 1.1).
            #      
            # 
            #     * The (yuck!) hard-coded "10.0"s round the limits "outwards"
            #     * to one decimal place.  This works for the MotionApplet applet,
            #     * but should really be more flexible.
            #     
            # 
            #     * After changing the limits of the plot area, we need to recalculate
            #     * the scale factor for converting from floating-point values to
            #     * display pixels.
            #     
            # 
            #      * setScaleFactor() calculates the scaling necessary to fit the full
            #      * X and Y ranges into the graphics context.  To avoid distorting the
            #      * image, we will calculate the scale factors independently, but use the
            #      * smaller for both axes.
            #      
            # 
            #     * For each axis, we want to represent a range of [Min, Max], over
            #     * the allotted number of pixels.  Note that the number of pixels
            #     * is determined by the top and bottom (or left and right) margins,
            #     * plus the "magic number" 2, which allows for the plot area border.
            #     
            # 
            #      * Translate and scale the point, to convert it to a pixel location
            #      * in the graphics context.
            #      
            # 
            #      * Plot the point in the current foreground color.
            #      
            # 
            #      * Plot the point in the specified color.
            #      
            # 
            #          * Get the graphics context, set to clip to the plot area.
            #          
            #  Set the color
            #  Convert to a pixel location
            # 
            #          * Draw the point as a tiny circle. When I tried to make it a
            #          * single pixel, it didn't show up on one system (Mac or Windows NT;
            #          * I don't remember which).
            #          
            # 
            #      * This is similar to the "drawPolyline()" method of the Graphics
            #      * class, but uses floating-point coordinates.
            #      
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Convert each floating-point coordinate pair to
            #          * a pixel coordinate in the Graphics context.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            # 
            #          * Get the graphics context, with the clipping region set to
            #          * the plot area; set the color; and draw the integer points.
            #          
            # 
            #      * Draw a floating-point "polyline" in the current foreground color.
            #      
            # 
            #      * Provide the functionality of the Graphics class's "drawPolygon()"
            #      * method, using floating-point coordinates.
            #      
            #  The number of points provided
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Translate all the points from floating-point coordinaates
            #          * to pixel coordinates.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            # 
            #          * Get the graphics context, with the clipping region set to
            #          * the plot area; set the color; and draw the integer polygon.
            #          
            # 
            #      * Draw a floating-point polygon, using the current foreground color.
            #      
            # 
            #      * This is similar to the "fillPolygon()" method of the Graphics
            #      * class, but uses floating-point coordinates.
            #      
            #  Number of points provided
            #  Translated X values
            #  Translated Y values
            #  Loop index
            #  Temporary pixel coordinates
            # 
            #          * Convert each floating-point coordinate pair to
            #          * a pixel coordinate in the Graphics context.
            #          *
            #          * Note:  the "scaleFactor" member variable must have been
            #          * correctly set for this routine to work.  Currently, scaleFactor
            #          * is recalculated whenever the Graphics size, or any of xMin,
            #          * xMax, yMin, or yMax is changed.
            #          
            p = scalePoint(fp[i])
            x[i] = p.x
            y[i] = p.y
            i += 1
        # 
        #          * Get the graphics context, with the clipping region set to the
        #          * plot area; set the color; and "fillPolygon()" the integer points.
        #          
        g = self.getPlotGraphics()
        g.setColor(c)
        g.fillPolygon(x, y, numPoints)

    # 
    #      * Draw a filled polygon using floating-point coordinates, and
    #      * the current foreground color.
    #      
    @fillPolygon.register(object, FPoint)
    def fillPolygon_0(self, fp):
        """ generated source for method fillPolygon_0 """
        self.fillPolygon(fp, getForeground())

    # 
    #      * Draw a line in a specified color, given a pair of floating-point
    #      * coordinates.
    #      
    @overloaded
    def line(self, fp1, fp2, c):
        """ generated source for method line """
        g = self.getPlotGraphics()
        #  Get the Graphics context
        g.setColor(c)
        #  Set the foreground color
        p1 = self.scalePoint(fp1)
        #  Convert the points to
        p2 = self.scalePoint(fp2)
        #  pixel coordinates.
        g.drawLine(p1.x, p1.y, p2.x, p2.y)
        #  Use the Graphics function.

    # 
    #      * Draw a line, using floating-point coordinates, in the current
    #      * foreground color.
    #      
    @line.register(object, FPoint, FPoint)
    def line_0(self, fp1, fp2):
        """ generated source for method line_0 """
        self.line(fp1, fp2, getForeground())

    # 
    #      * Draw the a label along the Y axis, marking the floating-point value.
    #      
    def drawYLabel(self, value):
        """ generated source for method drawYLabel """
        # 
        #          * Get the pixel coordinate of the point on the Y axis
        #          
        ticLoc = self.scalePoint(FPoint(0, value)).y
        # 
        #          * Generate a label string from the floating point value.
        #          
        s = Double.toString(value)
        # 
        #          * The label is located lower than the tic mark, by half the
        #          * height of the string.
        #          
        labelLoc = ticLoc + self.fontHeight / 2 + 1
        # 
        #          * If the label is at or near the top of the window, force
        #          * it down so that it will be visible.
        #          
        labelLimit = self.fontHeight + 1
        if labelLoc < labelLimit:
            labelLoc = labelLimit
        # 
        #          * Get the graphics context, draw the tic mark, and draw
        #          * the label string.
        #          
        g = self.getGraphics()
        g.drawLine(self.leftMargin - self.ticLength, ticLoc, self.leftMargin, ticLoc)
        g.drawString(s, self.leftMargin - self.fontMetric.stringWidth(s) - (self.ticLength + 2), labelLoc)

    # 
    #      * Draw the a label along the X axis, marking the floating-point value.
    #      
    def drawXLabel(self, value):
        """ generated source for method drawXLabel """
        # 
        #          * Get the pixel coordinate of the point on the X axis
        #          
        ticLoc = self.scalePoint(FPoint(value, 0)).x
        # 
        #          * Generate a label string from the floating point value.
        #          
        s = Double.toString(value)
        # 
        #          * The label starts to the left of the tic mark, so it will be
        #          * centered on the tic.
        #          
        labelLoc = ticLoc - self.fontMetric.stringWidth(s) / 2
        # 
        #          * If the label is at or near the right of the window, force
        #          * it left so that it will be visible.
        #          
        labelLimit = getSize().width - self.rightMargin - self.fontMetric.stringWidth(s) - 3
        if labelLoc > labelLimit:
            labelLoc = labelLimit
        # 
        #          * Get the graphics context, draw the tic mark, and draw
        #          * the label string.
        #          
        g = self.getGraphics()
        g.drawLine(ticLoc, getSize().height - self.bottomMargin, ticLoc, getSize().height - self.bottomMargin + self.ticLength)
        g.drawString(s, labelLoc, getSize().height - self.bottomMargin + self.fontHeight + self.ticLength + 2)
        #  2 pixels btw tic & string

    # 
    #      * Draw the X and Y axes, and label them.
    #      
    def drawScales(self):
        """ generated source for method drawScales """
        g = self.getGraphics()
        # 
        #          * If this is the first time we are drawing the labels, grab
        #          * the font data.  This will only need to be done once.
        #          
        if self.fontMetric == None:
            self.grabFontInfo()
        # 
        #          * Along with the axes, we draw a line across the top and right
        #          * edges of the plot area.  It's not really necessary, but it
        #          * looks good, and is easy to do.
        #          
        g.setColor(self.defaultScaleColor)
        g.drawRect(self.leftMargin, self.topMargin, getSize().width - (self.leftMargin + self.rightMargin + 1), getSize().height - (self.topMargin + self.bottomMargin + 1))
        # 
        #          * Draw the labels for the min and max points to be plotted.
        #          
        self.drawYLabel(self.yMin)
        self.drawYLabel(self.yMax)
        self.drawXLabel(self.xMin)
        self.drawXLabel(self.xMax)

    # 
    #      * Intall the callback function for drawing the contents of
    #      * the canvas.  As currently implemented, only the latest
    #      * function installed will be used (any previously-installed
    #      * functions will be lost).  This would be fairly straightforward
    #      * to change, should a future implementation need to allow more than
    #      * one object to draw to the canvas.
    #      
    def installPaintFunc(self, i):
        """ generated source for method installPaintFunc """
        self.theInterface = i

    # 
    #      * Painting consists of drawing the installed object (via the
    #      * callback to an off-screen buffer, adding the axes and labels,
    #      * then displaying the off-screen buffer.
    #      
    def paint(self, g):
        """ generated source for method paint """
        #  If there is no client function installed, do nothing:
        if self.theInterface != None:
            super(FloatCanvas, self).paint(g)
            #  Clear the canvas
            # 
            #              * Create an off-screen buffer, the same size as the
            #              * graphics context.
            #              
            self.imageBuffer = createImage(getSize().width, getSize().height)
            # 
            #              * Draw a border around the graphics context.
            #              
            self.plotRect.setBounds(self.leftMargin, 0, getSize().width - self.leftMargin, getSize().height - self.bottomMargin)
            # 
            #              * Invoke the client's draw function:
            #              
            self.theInterface.drawFunc(self)
            self.drawScales()
            #  Draw the scales & labels
            g.drawImage(self.imageBuffer, 0, 0, None)
            #  Display the buffer
            self.imageBuffer = None
            #  Release the buffer

    # 
    #      * To repaint the FloatCanvas, get the graphics context, and
    #      * pass it on to pain().
    #      
    def repaint(self):
        """ generated source for method repaint """
        self.paint(self.getGraphics())

