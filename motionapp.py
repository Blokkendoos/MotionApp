from __future__ import print_function
from math import floor, cos, sin

import tkinter as tk
import motionapp_gui
from pubsub import pub

from idealdrive import IdealDrive
from position import Position


class MotionApp():
    """
    This is the top-level class for the app.  It demonstrates the errors
    that occur with "dead-reckoning" navigation.

    Original version by
    @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael Gauland</a>

    Model for acceleration added by
    @author Jing YE, a student at the University of Melbourne

    Revision to use (theta_old+theta_new)/2 and show error amounts by
    @author <a href="mailto:tdbrown@uiuc.edu">Tom Brown</a>
    @version 1.3
    """
    # The duration of the simulation
    simulationTime = 2.0  # seconds

    # The time between dead-reckoning calculations
    deadReckoningInterval = 0.01  # seconds

    # This is the object used to simulate the robot's movements
    theWheels = IdealDrive()

    # The number of steps used for displaying the true path and
    # the dead-reckoned path.   numSteps is computed and used
    # throughout the class as the number of steps for displaying the
    # true path.  maxDRSegments are used to limit the number
    # of segments we use for the DR track.   maxNumSteps could
    # benefit from going a bit bigger than the 250 that is wired in,
    # but the number of cases for which we need more steps
    # is small and we wish to avoid excessive memory consumption.
    # When more than maxNumSteps are required, the path will tend
    # to exhibit places where it makes sharp bends rather than
    # smooth changes in direction.   These bends are artifact of
    # the graphics routines, not errors in the position calculations.
    maxNumSteps = 250
    numSteps = 100
    maxDRSegments = 100

    # A temporary variable used to determine the time between each
    # simulated leg used for drawing the true path.
    stepSize = float()

    # Temporary storage for the robot's position.
    pos = Position()

    # This variable is used to store the  path of the center of the robot,
    # which is then used to derive the position of the wheels.
    plotData = [None] * (maxNumSteps + 1)

    # Storage for the path of the center of the robot, which will
    # be used for drawing the track.
    centerPoints = [None] * (maxNumSteps + 1)

    # Storage for the path of the left wheel of the robot, which will
    # be used for drawing the track.
    leftPoints = [None] * (maxNumSteps + 1)

    # Storage for the path of the right wheel of the robot, which will
    # be used for drawing the track.
    rightPoints = [None] * (maxNumSteps + 1)

    # Storage for the dead-reckoned path of the robot.
    deadReckonPos = [None] * (maxDRSegments + 1)

    # Storage for the dead-reckoned path of the robot using the mean of theta.
    deadReckonMeanPos = [None] * (maxDRSegments + 1)

    # Storage for the true path of the robot.
    trueReckonPos = [None] * (maxDRSegments + 1)

    # Temporary variable.
    nSegment = int()

    def __init__(self):
        """ calculate and display the position data. """
        self.compute_position_data()
        # self.paneTracks.installPaintFunc(self)

        pub.subscribe(self.position_changed, 'position_changed')
        pub.subscribe(self.velocity_changed, 'velocity_changed')
        pub.subscribe(self.acceleration_changed, 'acceleration_changed')
        pub.subscribe(self.body_width_changed, 'body_width_changed')
        pub.subscribe(self.simulation_changed, 'simulation_changed')

    def position_changed(self, value):
        x, y, theta = value
        self.theWheels.setX0(x)
        self.theWheels.setY0(y)
        self.theWheels.setTheta0(theta)
        self.update_simulation()

    def velocity_changed(self, value):
        v_left, v_right = value
        self.theWheels.setVelocityLeft(v_left)
        self.theWheels.setVelocityRight(v_right)
        self.update_simulation()

    def acceleration_changed(self, value):
        a_left, a_right = value
        self.theWheels.setAccelerationLeft(a_left)
        self.theWheels.setAccelerationRight(a_right)
        self.update_simulation()

    def body_width_changed(self, value):
        self.theWheels.setBodyWidth(value)
        self.update_simulation()

    def simulation_changed(self, value):
        duration, interval = value
        self.simulationTime = duration
        self.deadReckoningInterval = interval
        self.update_simulation()

    def update_simulation(self):
        self.compute_position_data()
        self.update_position_values()
        pub.sendMessage('draw', value='Hallo')

    def update_position_values(self):
        pos = self.theWheels.positionAt(self.simulationTime)
        v_left = self.theWheels.getVelocityLeft(self.simulationTime)
        v_right = self.theWheels.getVelocityRight(self.simulationTime)
        value = (pos.x, pos.y, pos.theta,
                 self.deadReckonPos[self.nSegment].x,
                 self.deadReckonPos[self.nSegment].y,
                 self.deadReckonPos[self.nSegment].theta,
                 self.deadReckonMeanPos[self.nSegment].x,
                 self.deadReckonMeanPos[self.nSegment].y,
                 self.deadReckonMeanPos[self.nSegment].theta,
                 v_left, v_right)
        pub.sendMessage('set_computed_values', value=value)

    def compute_position_data(self):
        '''
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

    def draw_func(self, theFloatCanvas):
        i = int()
        shadow = tk.Color(232, 232, 232)
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
        '''

if __name__ == '__main__':
    motionapp = MotionApp()
    motionapp_gui.start_up()
