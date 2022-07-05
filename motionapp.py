from __future__ import print_function
from math import floor, cos, sin, degrees

import motionapp_gui
from pubsub import pub

from idealdrive import IdealDrive
from position import Position


def rgb2hex(rgb):
    return "#%02x%02x%02x" % rgb


class MotionApp():
    """
    This is the top-level class for the app.  It demonstrates the errors
    that occur with "dead-reckoning" navigation.

    Original (Java) version by
    @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael Gauland</a>

    Model for acceleration added by
    @author Jing YE, a student at the University of Melbourne

    Revision to use (theta_old+theta_new)/2 and show error amounts by
    @author <a href="mailto:tdbrown@uiuc.edu">Tom Brown</a>

    Refactored into Python/Tkinter by
    @author <a href="mailto:jvo@chaosgeordend.nl">Johan van Oostrum</a>

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
    minNumSteps = 30
    maxNumSteps = 250
    numSteps = 100
    maxDRSegments = 100

    # This variable is used to store the  path of the center of the robot,
    # which is then used to derive the position of the wheels.
    plotData = []

    # Storage for the path of the center of the robot, which will
    # be used for drawing the track.
    centerPoints = []

    # Storage for the path of the left wheel of the robot, which will
    # be used for drawing the track.
    leftPoints = []

    # Storage for the path of the right wheel of the robot, which will
    # be used for drawing the track.
    rightPoints = []

    # Storage for the dead-reckoned path of the robot.
    deadReckonPos = []

    # Storage for the dead-reckoned path of the robot using the mean of theta.
    deadReckonMeanPos = []

    # Storage for the true path of the robot.
    trueReckonPos = []

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
        self.theWheels.setTheta0(degrees(theta))
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
        self.draw_func()
        pub.sendMessage('set_computed_values', value=value)

    def compute_position_data(self):
        # Compute the true position
        self.numSteps = self.theWheels.getSimpsonIntervals_0(self.simulationTime)
        self.numSteps = max(self.numSteps, self.minNumSteps)  # floor
        self.numSteps = min(self.numSteps, self.maxNumSteps)  # ceiling
        stepSize = self.simulationTime / self.numSteps
        for i in range(self.numSteps + 1):
            pos = self.theWheels.positionAt(i * stepSize)
            self.plotData.append(pos)
            self.centerPoints.append(pos)
            self.leftPoints.append(self.theWheels.LeftWheelLoc(pos))
            self.rightPoints.append(self.theWheels.RightWheelLoc(pos))

        # Compute the dead-reckoned position
        self.nSegment = int(floor(self.simulationTime / self.deadReckoningInterval))
        deltaT = self.deadReckoningInterval
        if self.simulationTime - self.nSegment * deltaT > 0.01:
            # The simulation time does not come out to an even
            # multiple of deadReckoningIntervals
            self.nSegment += 1
        if self.nSegment > self.maxDRSegments:
            # the dead-reckoning interval results in too many segments
            # (more than that for which we wish to allocate memory),
            # so we need to make some adjustments.  Unfortunately,
            # the user will not see the results of the dead-reckoning
            # that he requested, but at this point it is using so fine
            # an interval that it doesn't matter anymore.
            self.nSegment = self.maxDRSegments
            deltaT = self.simulationTime / self.maxDRSegments

        self.deadReckonPos.append(self.theWheels.positionAt(0))
        self.deadReckonMeanPos.append(self.deadReckonPos[0])
        self.trueReckonPos.append(self.deadReckonPos[0])
        trueTime = 0
        vLeft1 = self.theWheels.getVelocityLeft(0.0)
        vRight1 = self.theWheels.getVelocityRight(0.0)
        for iSegment in range(1, self.nSegment + 1):
            if iSegment == self.nSegment:
                # we are on the last segment.  recall the simulation time
                # isn't necessarily an even multiple of the dead-reckoning
                # interval (both values are arbitrary user inputs), so this
                # last segment could be a little shorter than all the previous
                # ones.    we recompute it just in case.
                deltaT = self.simulationTime - (iSegment - 1) * deltaT
            trueTime += deltaT
            vLeft0 = vLeft1
            vRight0 = vRight1
            vLeft1 = self.theWheels.getVelocityLeft(trueTime)
            vRight1 = self.theWheels.getVelocityRight(trueTime)
            # Dead-reckon a new position:
            # sLeft and sRight are the displacements of the wheels (may be <0)
            # for the next segment, theta is the new orientation (at the end
            # of the segment).  This usage follows the results that are
            # obtained with the standard dead-reckoning approach.
            sLeft = deltaT * (vLeft0 + vLeft1) / 2.0
            sRight = deltaT * (vRight0 + vRight1) / 2.0
            sMean = (sRight + sLeft) / 2
            wTrack = self.theWheels.getBodyWidth()
            theta = self.deadReckonPos[iSegment - 1].theta + (sRight - sLeft) / wTrack
            theta_mean = (theta + self.deadReckonPos[iSegment - 1].theta) / 2
            self.deadReckonPos.append(
                Position(self.deadReckonPos[iSegment - 1].x + sMean * cos(theta),
                         self.deadReckonPos[iSegment - 1].y + sMean * sin(theta),
                         theta))
            self.deadReckonMeanPos.append(
                Position(self.deadReckonMeanPos[iSegment - 1].x + sMean * cos(theta_mean),
                         self.deadReckonMeanPos[iSegment - 1].y + sMean * sin(theta_mean),
                         theta))
            self.trueReckonPos.append(self.theWheels.positionAt(trueTime))

    def draw_func(self):
        pub.sendMessage('draw_scales')

        shadow = 'grey'
        xMin = self.plotData[0].x
        xMax = xMin
        yMin = self.plotData[0].y
        yMax = yMin
        for i in range(1, self.numSteps + 1):
            xMin = min(self.plotData[i].x, xMin)
            xMax = max(self.plotData[i].x, xMax)
            yMin = min(self.plotData[i].y, yMin)
            yMax = max(self.plotData[i].y, yMax)
        bodyWidth = self.theWheels.getBodyWidth()
        xMin -= bodyWidth
        xMax += bodyWidth
        yMin -= bodyWidth
        yMax += bodyWidth
        limits = (xMin, xMax, yMin, yMax)
        pub.sendMessage('set_limits', value=limits)

        # TODO refactor vertices construction
        dPoly = [None] * 5
        dPoly[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[0])
        dPoly[1] = self.theWheels.RightWheelLoc(self.deadReckonPos[0])
        for iSegment in range(1, self.nSegment + 1):
            dPoly[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[iSegment])
            dPoly[3] = self.theWheels.LeftWheelLoc(self.deadReckonPos[iSegment])
            dPoly[4] = dPoly[0]
            # TODO cleanup
            # theFloatCanvas.fillPolygon(dPoly, shadow)
            # theFloatCanvas.drawPolygon(dPoly, 'white')
            msg = (dPoly, shadow)
            pub.sendMessage('draw_polygon', value=msg)
            dPoly[0] = dPoly[3]
            dPoly[1] = dPoly[2]

        fpd = [None] * 3
        fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[self.nSegment])
        fpd[1] = self.theWheels.NoseLoc(self.deadReckonPos[self.nSegment])
        fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[self.nSegment])
        # TODO cleanup
        # theFloatCanvas.fillPolygon(fpd, shadow)
        msg = (fpd, shadow)
        pub.sendMessage('draw_polygon_filled', value=msg)

        for iSegment in range(1, self.nSegment + 1):
            fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.deadReckonPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonPos[iSegment])
            # TODO cleanup
            # theFloatCanvas.drawPolygon(fpd, 'darkgray')
            msg = (fpd, 'darkgray')
            pub.sendMessage('draw_polygon', value=msg)

            fpd[0] = self.theWheels.LeftWheelLoc(self.deadReckonMeanPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.deadReckonMeanPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.deadReckonMeanPos[iSegment])
            # TODO cleanup
            # theFloatCanvas.drawPolygon(fpd, 'cyan')
            msg = (fpd, 'cyan')
            pub.sendMessage('draw_polygon', value=msg)

        # TODO cleanup
        # theFloatCanvas.drawPolyline(self.centerPoints, self.numSteps + 1)
        # theFloatCanvas.drawPolyline(self.leftPoints, self.numSteps + 1, 'green')
        # theFloatCanvas.drawPolyline(self.rightPoints, self.numSteps + 1, 'red')
        print(f"#centerPoints:{len(self.centerPoints)}")
        msg = (self.centerPoints, 'blue')
        pub.sendMessage('draw_polygon', value=msg)
        print(f"#leftPoints:{len(self.leftPoints)}")
        msg = (self.leftPoints, 'green')
        pub.sendMessage('draw_polygon', value=msg)
        print(f"#rightPoints:{len(self.rightPoints)}")
        msg = (self.rightPoints, 'red')
        pub.sendMessage('draw_polygon', value=msg)

        for iSegment in range(1, self.nSegment + 1):
            fpd[0] = self.theWheels.LeftWheelLoc(self.trueReckonPos[iSegment])
            fpd[1] = self.theWheels.NoseLoc(self.trueReckonPos[iSegment])
            fpd[2] = self.theWheels.RightWheelLoc(self.trueReckonPos[iSegment])
            # TODO cleanup
            # theFloatCanvas.drawPolygon(fpd, 'blue')
            msg = (fpd, 'blue')
            pub.sendMessage('draw_polygon', value=msg)


if __name__ == '__main__':
    motionapp = MotionApp()
    motionapp_gui.start_up()
