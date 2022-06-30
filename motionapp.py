#!/usr/bin/env python
""" generated source for module MotionApplet """
from __future__ import print_function
# 
#  * This is to top-level class for the applet.  It demonstrates the errors
#  * that occur with "dead-reckoning" navigation.
#  *
#  * To include it in a web page, use a tag like this:
#  *     <applet code="MotionApplet.class" width=600 height=400></applet>
#  
# 
#  * This is to top-level class for the applet.  It demonstrates the errors
#  * that occur with "dead-reckoning" navigation.
#  *
#  * To include it in a web page, use a tag like this:
#  * <CENTER>
#  *     &lt;applet code="MotionApplet.class" width=600 height=400&gt;
#  *     &lt;/applet&gt;
#  * </CENTER>
#  *
#  * Original version by
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael
#  *     Gauland</a>
#  *
#  * Model for acceleration added by
#  * @author Jing YE, a student at the University of Melbourne
#  *
#  * Revision to use (theta_old+theta_new)/2 and show error amounts by
#  * @author <a href="mailto:tdbrown@uiuc.edu">Tom Brown</a>
#  *
#  * @version 1.3
#  *
#  
class MotionApplet(JApplet, ChangeListener, DrawInterface):
    """ generated source for class MotionApplet """
    #  These variables are used for the controls in the applet.
    #  Adjustment for the initial position "X" coordinate. 
    controlPositionX = JFBSlider("X:", -10, 10, 200, 1)

    #  Adjustment for the initial position "Y" coordinate. 
    controlPositionY = JFBSlider("Y:", -10, 10, 200, 1)

    #  Adjustment for the initial direction. 
    controlPositionTheta = JFBSlider("Theta", -180, 180, 144, 1, "\u00b0")

    #  Adjustment for the velocity of the left wheel. 
    controlVelocityLeft = JFBSlider("L: ", -5.00, 5.00, 100, 2)

    #  Adjustment for the velocity of the right wheel. 
    controlVelocityRight = JFBSlider("R: ", -5.00, 5.00, 100, 2)

    #  Adjustment for the acceleration of the left wheel. 
    controlAccelerationLeft = JFBSlider("L: ", -1.00, 1.00, 200, 2)

    #  Adjustment for the acceleration of the right wheel. 
    controlAccelerationRight = JFBSlider("R: ", -1.00, 1.00, 200, 2)

    #  Adjustment for the width of the robot's body. 
    controlBodyWidth = JFBSlider("Width: ", 0.1, 2.5, 120, 2)

    #  Adjustment for the duration of the simulation. 
    controlDuration = JFBSlider("Duration: ", 0.0, 30.0, 300, 1)

    #  Adjustment for the interval between dead-reckonings. 
    controlDeadReckoningInterval = JFBSlider("Interval:", 0.0, 1.0, 100, 2)

    #  END of controls variables.
    #  These variables will contain the display elements.
    #  Display group for the control tabs. 
    paneControls = JTabbedPane()

    #  Control group for the robot body settings. 
    controlsRobot = JPanel()

    #  Control group for timing settings. 
    controlsTiming = JPanel()

    #  Control group for the speed settings. 
    controlsSpeed = JPanel()

    #  The canvas for displaying the robot's tracks. 
    paneTracks = FloatCanvas()

    #  Display group for the position information (text). 
    panePosition = None

    #  END of display elements variables.
    #  These variables contain spacings used in the display.
    #  Constant padding vertical padding of 3 pixels. 
    vpad3 = Dimension(1, 3)

    #  Constant padding vertical padding of 5 pixels. 
    vpad5 = Dimension(1, 5)

    #  Constant padding horizontal padding of 5 pixels. 
    hpad5 = Dimension(5, 1)

    #  END of display spacings variables.
    #  These variables are used for storing robot attributes used
    #  in the simulation, and for storing the results of the simulation
    #  (e.g., true position of each wheel).
    #  The duration of the simulation, in seconds. 
    simulationTime = 2.0

    #  The time between dead-reckoning calculations, in seconds. 
    deadReckoningInterval = 0.01

    #  This is the object used to simulate the robot's movements. 
    theWheels = IdealDrive()

    #  The number of steps used for displaying the true path and
    #      *  the dead-reckoned path.   numSteps is computed and used
    #      *  throughout the class as the number of steps for displaying the
    #      *  true path.  maxDRSegments are used to limit the number
    #      *  of segments we use for the DR track.   maxNumSteps could
    #      *  benefit from going a bit bigger than the 250 that is wired in,
    #      *  but the number of cases for which we need more steps
    #      *  is small and we wish to avoid excessive memory consumption.
    #      *  When more than maxNumSteps are required, the path will tend
    #      *  to exhibit places where it makes sharp bends rather than
    #      *  smooth changes in direction.   These bends are artifact of
    #      *  the graphics routines, not errors in the position calculations.
    #      
    maxNumSteps = 250
    numSteps = 100
    maxDRSegments = 100

    # 
    #      * A temporary variable used to determine the time between each
    #      * simulated leg used for drawing the true path.
    #      
    stepSize = float()

    #  Temporary storage for the robot's position. 
    pos = Position()

    #  This variable is used to store the  path of the center of the robot,
    #      * which is then used to derive the position of the wheels.
    #      
    plotData = [None] * maxNumSteps + 1

    #  Storage for the path of the center of the robot, which will
    #      * be used for drawing the track.
    #      
    centerPoints = [None] * maxNumSteps + 1

    #  Storage for the path of the left wheel of the robot, which will
    #      * be used for drawing the track.
    #      
    leftPoints = [None] * maxNumSteps + 1

    #  Storage for the path of the right wheel of the robot, which will
    #      * be used for drawing the track.
    #      
    rightPoints = [None] * maxNumSteps + 1

    #  Storage for the dead-reckoned path of the robot. 
    deadReckonPos = [None] * maxDRSegments + 1

    #  Storage for the dead-reckoned path of the robot using the mean of theta. 
    deadReckonMeanPos = [None] * maxDRSegments + 1

    #  Storage for the true path of the robot. 
    trueReckonPos = [None] * maxDRSegments + 1

    #  Temporary variable. 
    nSegment = int()

    #  END of simulation variables.
    # 
    #      * Initialize the applet.
    #      * @param None No explanation necessary.
    #      
    def init(self):
        """ generated source for method init """
        # 
        #     * Set up controls for Robot tab, which includes:
        #     *     Initial Position
        #     *         Slider for X coordinate
        #     *         Slider for Y coordinate
        #     *         Slider for direction (theta)
        #     *     Body Settings
        #     *         Body Width
        #     
        #  Basic set up for the tab:
        self.controlsRobot.setLayout(BoxLayout(self.controlsRobot, BoxLayout.Y_AXIS))
        self.controlsRobot.setBorder(LineBorder(Color.magenta, 1))
        self.controlsRobot.add(Box.createRigidArea(self.vpad5))
        #  Create a panel for the Initial Position controls:
        theSliderPanel = JPanel()
        theSliderPanel.setLayout(BoxLayout(theSliderPanel, BoxLayout.Y_AXIS))
        theSliderPanel.setBorder(TitledBorder("Initial Position"))
        # 
        #     * Add tick marks for the initial position sliders, and
        #     * add this object as a "ChangeListener" to each.
        #     
        self.controlPositionX.addTicks(10, 5)
        self.controlPositionX.addChangeListener(self)
        self.controlPositionY.addTicks(10, 5)
        self.controlPositionY.addChangeListener(self)
        self.controlPositionTheta.addTicks(10, 5)
        self.controlPositionTheta.addChangeListener(self)
        # 
        #     * Add the sliders to the panel, with some spacing
        #     * between them, then add the panel to the robot panel.
        #     * Insert some spacing as well.
        #     
        theSliderPanel.add(Box.createRigidArea(self.vpad3))
        theSliderPanel.add(self.controlPositionX)
        theSliderPanel.add(Box.createRigidArea(self.vpad3))
        theSliderPanel.add(self.controlPositionY)
        theSliderPanel.add(Box.createRigidArea(self.vpad3))
        theSliderPanel.add(self.controlPositionTheta)
        self.controlsRobot.add(theSliderPanel)
        self.controlsRobot.add(Box.createRigidArea(self.vpad3))
        # 
        #     * Create a panel for the Body Settings controls
        #     * (of which "Width" is currently the only one).  Add
        #     * tick marks to the Body Width control, add this object
        #     * as a change listener, and add the new panel to the
        #     * robot tab panel.
        #     
        theBodyPanel = JPanel()
        theBodyPanel.setLayout(BoxLayout(theBodyPanel, BoxLayout.Y_AXIS))
        theBodyPanel.setBorder(TitledBorder("Body Settings"))
        self.controlBodyWidth.addTicks(5, 5)
        self.controlBodyWidth.addChangeListener(self)
        theBodyPanel.add(self.controlBodyWidth)
        self.controlsRobot.add(theBodyPanel)
        self.controlsRobot.add(Box.createRigidArea(self.vpad3))
        # 
        #     * Set up the controls for Speed tab, which include
        #     * sliders for the velocity and acceleration of each
        #     * wheel.
        #     
        #  Basic setup for the panel:
        self.controlsSpeed.setLayout(BoxLayout(self.controlsSpeed, BoxLayout.Y_AXIS))
        self.controlsSpeed.setBorder(LineBorder(Color.red, 1))
        self.controlsSpeed.add(Box.createRigidArea(self.vpad5))
        # 
        #     * Create a panel for the velocity sliders.  Add the
        #     * controls to this panel, then add the panel to the Speed
        #     * tab panel.
        #     
        theVelocityPanel = JPanel()
        theVelocityPanel.setLayout(BoxLayout(theVelocityPanel, BoxLayout.Y_AXIS))
        theVelocityPanel.setBorder(TitledBorder("Velocities"))
        self.controlVelocityLeft.addTicks(10, 5)
        self.controlVelocityLeft.addChangeListener(self)
        self.controlVelocityRight.addTicks(10, 5)
        self.controlVelocityRight.addChangeListener(self)
        # 
        #     * Create a panel for the Acceleration sliders.  Add the
        #     * controls to this panel, then add the panel to the Speed
        #     * tab panel.
        #     
        theAccelerationPanel = JPanel()
        theAccelerationPanel.setLayout(BoxLayout(theAccelerationPanel, BoxLayout.Y_AXIS))
        theAccelerationPanel.setBorder(TitledBorder("Accelerations"))
        self.controlAccelerationLeft.addTicks(10, 5)
        self.controlAccelerationLeft.addChangeListener(self)
        self.controlAccelerationRight.addTicks(10, 5)
        self.controlAccelerationRight.addChangeListener(self)
        theVelocityPanel.add(Box.createRigidArea(self.vpad3))
        theVelocityPanel.add(self.controlVelocityRight)
        theVelocityPanel.add(Box.createRigidArea(self.vpad3))
        theVelocityPanel.add(self.controlVelocityLeft)
        theVelocityPanel.add(Box.createRigidArea(self.vpad3))
        theAccelerationPanel.add(Box.createRigidArea(self.vpad3))
        theAccelerationPanel.add(self.controlAccelerationRight)
        theAccelerationPanel.add(Box.createRigidArea(self.vpad3))
        theAccelerationPanel.add(self.controlAccelerationLeft)
        theAccelerationPanel.add(Box.createRigidArea(self.vpad3))
        self.controlsSpeed.add(theVelocityPanel)
        self.controlsSpeed.add(theAccelerationPanel)
        # 
        #     * Set up the controls for the Timing tab, which
        #     * consist of two panels:  one for the simlulation
        #     * duration slider, and one for the dead-reckoning
        #     * interval slider.
        #     
        #  Basic panel setup:
        self.controlsTiming.setLayout(BoxLayout(self.controlsTiming, BoxLayout.Y_AXIS))
        self.controlsTiming.setBorder(LineBorder(Color.cyan, 1))
        self.controlsTiming.add(Box.createRigidArea(self.vpad5))
        # 
        #     * Create a panel for the Simulation section.  Add the
        #     * duration slider control, and add the panel to the
        #     * Timing tab panel.
        #     
        theTimePanel = JPanel()
        theTimePanel.setLayout(BoxLayout(theTimePanel, BoxLayout.Y_AXIS))
        theTimePanel.setBorder(TitledBorder("Simulation"))
        self.controlDuration.addTicks(10, 5)
        self.controlDuration.addChangeListener(self)
        theTimePanel.add(self.controlDuration)
        self.controlsTiming.add(theTimePanel)
        # 
        #     * Create a panel for the Dead-Reckoning section.  Add the
        #     * interval slider control, and add the panel to the
        #     * Timing tab panel.
        #     
        theDeadReckoningPanel = JPanel()
        theDeadReckoningPanel.setLayout(BoxLayout(theDeadReckoningPanel, BoxLayout.Y_AXIS))
        theDeadReckoningPanel.setBorder(TitledBorder("Dead Reckoning"))
        theDeadReckoningPanel.add(self.controlDeadReckoningInterval)
        self.controlDeadReckoningInterval.addTicks(10, 5)
        self.controlDeadReckoningInterval.addChangeListener(self)
        self.controlsTiming.add(theDeadReckoningPanel)
        # 
        #     * Add the tab panels to the Controls panel.
        #     
        self.paneControls.addTab("Robot", self.controlsRobot)
        self.paneControls.addTab("Speed", self.controlsSpeed)
        self.paneControls.addTab("Timing", self.controlsTiming)
        # 
        #     * Create a panel for displaying the robot's path:
        #     
        canvasPanel = JPanel(GridLayout())
        canvasPanel.add(self.paneTracks)
        canvasPanel.setBorder(LineBorder(Color.blue, 1))
        #  Create & setup the new panel:
        self.panePosition = PositionPanel()
        # 
        #     * Set up the layout for the main window.  Set up the
        #     * layout for and insert the canvas panl, controls pane,
        #     * and position feedback pane.
        #     
        gbl = GridBagLayout()
        gbc = GridBagConstraints()
        getContentPane().setLayout(gbl)
        #  Add the canvas pane to the main window
        gbc.anchor = gbc.NORTHWEST
        gbc.fill = gbc.BOTH
        gbc.gridx = 0
        gbc.gridy = 0
        gbc.gridheight = 2
        gbc.gridwidth = 1
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(canvasPanel, gbc)
        getContentPane().add(canvasPanel)
        #  Add the controls pane to the main window
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 1
        gbc.gridy = 0
        gbc.gridheight = 1
        gbc.gridwidth = 1
        gbc.weightx = 0
        gbc.weighty = 0
        gbl.setConstraints(self.paneControls, gbc)
        getContentPane().add(self.paneControls)
        #  Add the position feedback pane to the main window
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 1
        gbc.gridy = 1
        gbc.gridheight = 1
        gbc.gridwidth = 1
        gbc.weightx = 0
        gbc.weighty = 0
        gbl.setConstraints(self.panePosition, gbc)
        getContentPane().add(self.panePosition)
        # 
        #     * Set all the controls to known initial values
        #     
        self.controlPositionX.setValue(0)
        self.controlPositionY.setValue(0)
        self.controlPositionTheta.setValue(90)
        self.controlVelocityLeft.setValue(2.5)
        self.controlVelocityRight.setValue(2.4)
        self.controlAccelerationLeft.setValue(0.0)
        self.controlAccelerationRight.setValue(0.0)
        self.controlBodyWidth.setValue(1.0)
        self.controlDuration.setValue(self.simulationTime)
        self.controlDeadReckoningInterval.setValue(0.1)
        self.controlDeadReckoningInterval.setValue(0.5)
        # 
        #     * Now that the controls have been set, calculate and
        #     * display the position data.
        #     
        computePositionData()
        # 
        #     * Finally, install this object as a paint function for the
        #     * canvas pane.
        #     
        self.paneTracks.installPaintFunc(self)

    # 
    #      * Handle "ChangeEvents", which occur when a slider changes
    #      * value.  Use the "isEventSource" functions for each
    #      * "JFBSlider" object to determine which control generated the
    #      * event.  For most events, we just get the new value, and pass
    #      * it to the appropriate function to set the corresponding
    #      * control.
    #      
    def stateChanged(self, e):
        """ generated source for method stateChanged """
        if self.controlPositionX.isEventSource(e):
            self.theWheels.setX0(self.controlPositionX.getValue())
        elif self.controlPositionY.isEventSource(e):
            self.theWheels.setY0(self.controlPositionY.getValue())
        elif self.controlPositionTheta.isEventSource(e):
            self.theWheels.setTheta0(self.controlPositionTheta.getValue())
        elif self.controlVelocityLeft.isEventSource(e):
            self.theWheels.setVelocityLeft(self.controlVelocityLeft.getValue())
        elif self.controlVelocityRight.isEventSource(e):
            self.theWheels.setVelocityRight(self.controlVelocityRight.getValue())
        elif self.controlAccelerationLeft.isEventSource(e):
            self.theWheels.setAccelerationLeft(self.controlAccelerationLeft.getValue())
        elif self.controlAccelerationRight.isEventSource(e):
            self.theWheels.setAccelerationRight(self.controlAccelerationRight.getValue())
        elif self.controlBodyWidth.isEventSource(e):
            self.theWheels.setBodyWidth(self.controlBodyWidth.getValue())
        elif self.controlDuration.isEventSource(e):
            self.simulationTime = self.controlDuration.getValue()
        elif self.controlDeadReckoningInterval.isEventSource(e):
            t = self.controlDeadReckoningInterval.getValue()
            # 
            #              * Since a dead-reckoning interval of 0 is not
            #              * possible, set it to 0.1 instead.  I did this
            #              * instead of setting the minimum limit of the control
            #              * to 0.1, because it gives the control a nice, even
            #              * midpoint label.
            #              
            if t == 0:
                t = 0.1
                self.controlDeadReckoningInterval.setValue(t)
            self.deadReckoningInterval = t
        else:
            print(e.__str__())
        # 
        #          * Whatever the event, update the position feedback
        #          * readouts, and redraw the paths.
        #          
        computePositionData()
        updatePositionValues()
        self.paneTracks.repaint()

    # 
    #      * Paint the applet&mdash;redraw the scales and the paths.
    #      *
    #      * @param g The graphics context in which to draw.
    #      
    def paint(self, g):
        """ generated source for method paint """
        # Draw a Rectangle around the applet's display area.
        g.drawRect(0, 0, getSize().width - 1, getSize().height - 1)
        #  Redraw all the contents of the applet window.
        paintComponents(g)

    # 
    #      * Update the true and dead-reckoned fields in the
    #      * position feedback pane.
    #      
    def updatePositionValues(self):
        """ generated source for method updatePositionValues """
        if self.panePosition == None:
            return
        #  do nothing
        pos = self.theWheels.positionAt(self.simulationTime)
        vLeft = self.theWheels.getVelocityLeft(self.simulationTime)
        vRight = self.theWheels.getVelocityRight(self.simulationTime)
        self.panePosition.setComputedValues(pos.x, pos.y, pos.theta, self.deadReckonPos[self.nSegment].x, self.deadReckonPos[self.nSegment].y, self.deadReckonPos[self.nSegment].theta, self.deadReckonMeanPos[self.nSegment].x, self.deadReckonMeanPos[self.nSegment].y, self.deadReckonMeanPos[self.nSegment].theta, vLeft, vRight)

    def computePositionData(self):
        """ generated source for method computePositionData """
        self.numSteps = self.theWheels.getSimpsonIntervals(self.simulationTime)
        if self.numSteps < 30:
            self.numSteps = 30
        elif self.numSteps > self.maxNumSteps:
            self.numSteps = self.maxNumSteps
        self.stepSize = self.simulationTime / self.numSteps
        i = 0
        while i <= self.numSteps:
            self.pos = self.theWheels.positionAt(i * self.stepSize)
            self.plotData[i] = self.pos
            self.centerPoints[i] = self.pos
            self.leftPoints[i] = self.theWheels.LeftWheelLoc(self.pos)
            self.rightPoints[i] = self.theWheels.RightWheelLoc(self.pos)
            i += 1
        self.nSegment = int(floor(self.simulationTime / self.deadReckoningInterval))
        deltaT = self.deadReckoningInterval
        if self.simulationTime - self.nSegment * deltaT > 0.01:
            self.nSegment += 1
        if self.nSegment > self.maxDRSegments:
            self.nSegment = self.maxDRSegments
            deltaT = self.simulationTime / self.maxDRSegments
        self.deadReckonPos[0] = self.theWheels.positionAt(0)
        self.deadReckonMeanPos[0] = self.deadReckonPos[0]
        self.trueReckonPos[0] = self.deadReckonPos[0]
        trueTime = 0
        vLeft0 = float()
        vLeft1 = float()
        vRight0 = float()
        vRight1 = float()
        vLeft1 = self.theWheels.getVelocityLeft(0.0)
        vRight1 = self.theWheels.getVelocityRight(0.0)
        iSegment = 1
        while iSegment <= self.nSegment:
            if iSegment == self.nSegment:
                deltaT = self.simulationTime - (iSegment - 1) * deltaT
            trueTime += deltaT
            vLeft0 = vLeft1
            vRight0 = vRight1
            vLeft1 = self.theWheels.getVelocityLeft(trueTime)
            vRight1 = self.theWheels.getVelocityRight(trueTime)
            sLeft = deltaT * (vLeft0 + vLeft1) / 2.0
            sRight = deltaT * (vRight0 + vRight1) / 2.0
            sMean = (sRight + sLeft) / 2
            wTrack = self.theWheels.getBodyWidth()
            theta = self.deadReckonPos[iSegment - 1].theta + (sRight - sLeft) / wTrack
            theta_mean = (theta + self.deadReckonPos[iSegment - 1].theta) / 2
            self.deadReckonPos[iSegment] = Position(self.deadReckonPos[iSegment - 1].x + sMean * cos(theta), self.deadReckonPos[iSegment - 1].y + sMean * sin(theta), theta)
            self.deadReckonMeanPos[iSegment] = Position(self.deadReckonMeanPos[iSegment - 1].x + sMean * cos(theta_mean), self.deadReckonMeanPos[iSegment - 1].y + sMean * sin(theta_mean), theta)
            self.trueReckonPos[iSegment] = self.theWheels.positionAt(trueTime)
            iSegment += 1

    def drawFunc(self, theFloatCanvas):
        """ generated source for method drawFunc """
        i = int()
        shadow = Color(232, 232, 232)
        fpd = [None] * 3
        xMin = self.plotData[0].x
        xMax = xMin
        yMin = self.plotData[0].y
        yMax = yMin
        while i <= self.numSteps:
            if self.plotData[i].x < xMin:
                xMin = self.plotData[i].x
            elif self.plotData[i].x > xMax:
                xMax = self.plotData[i].x
            if self.plotData[i].y < yMin:
                yMin = self.plotData[i].y
            elif self.plotData[i].y > yMax:
                yMax = self.plotData[i].y
            i += 1
        bodyWidth = self.theWheels.getBodyWidth()
        xMin -= bodyWidth
        xMax += bodyWidth
        yMin -= bodyWidth
        yMax += bodyWidth
        theFloatCanvas.setLimits(xMin, xMax, yMin, yMax)
        dPoly = [None] * 5
        dPoly[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[0])
        dPoly[1] = self.theWheels.RightWheelLoc(self.deadReckonPos[0])
        iSegment = 1
        while iSegment <= self.nSegment:
            dPoly[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[iSegment])
            dPoly[3] = self.theWheels.LeftWheelLoc(self.deadReckonPos[iSegment])
            dPoly[4] = dPoly[0]
            theFloatCanvas.fillPolygon(dPoly, shadow)
            theFloatCanvas.drawPolygon(dPoly, Color.white)
            dPoly[0] = dPoly[3]
            dPoly[1] = dPoly[2]
            iSegment += 1
        fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[self.nSegment])
        fpd[1] = self.theWheels.NoseLoc(self.deadReckonPos[self.nSegment])
        fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[self.nSegment])
        theFloatCanvas.fillPolygon(fpd, shadow)
        iSegment = 1
        while iSegment <= self.nSegment:
            fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.deadReckonPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[iSegment])
            theFloatCanvas.drawPolygon(fpd, Color.darkGray)
            fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonMeanPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.deadReckonMeanPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonMeanPos[iSegment])
            theFloatCanvas.drawPolygon(fpd, Color.cyan)
            iSegment += 1
        theFloatCanvas.drawPolyline(self.centerPoints, self.numSteps + 1)
        theFloatCanvas.drawPolyline(self.leftPoints, self.numSteps + 1, Color.green)
        theFloatCanvas.drawPolyline(self.rightPoints, self.numSteps + 1, Color.red)
        iSegment = 0
        while iSegment <= self.nSegment:
            fpd[0] = self.theWheels.LeftWheelLoc(self.trueReckonPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.trueReckonPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.trueReckonPos[iSegment])
            theFloatCanvas.drawPolygon(fpd, Color.blue)
            iSegment += 1
