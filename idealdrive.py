#!/usr/bin/env python3

from point import FPoint
from position import Position
import math


class IdealDrive():
    """
    IdealDrive simulates a differential-drive robot, with no slippage,
    and other simplifications.

    All linear measurements (i.e., body width, distance traveled, etc.) are
    assumed to be in the same units (e.g., meters), as are all time settings
    in the simulation (e.g., duration).  Velocity is also expressed in these
    same units (i.e., if you assume the velocity is in meters/second, then the
    duration of the simulation is expressed in seconds.).

    @author <a href="mailto:MikeGauland@users.sourceforge.net">
    Michael Gauland</a>
    @version 2.

    Addition of Simpson's Rule implementation to treat acceleration,
    contributed by Jing YE, Univeristy of Melbourne, Jan 2001
    """
    # The maximum-error criterion used for selecting intervals
    maxAllowableError = 0.01

    def __init__(self):
        # The starting position, for simulations.
        self.initialPos = Position()

        # The width of the robot's body -- i.e., the distance
        # between the drive wheels.
        self.bodyWidth = 0.7

        # The velocity of the drive wheels.
        # <P>See the note at the top of this file for information about
        # measurement units.</P>
        self.velocityLeft = 0.0
        self.velocityRight = 0.0

        # The acceleration of the drive wheels
        self.accelerationLeft = 0.0
        self.accelerationRight = 0.1

        # Since the sine and cosine of the starting angle is used whenever we
        # calculate the true position of the robot at a given time, it will be
        # calculated only when the angle is set.
        self.sinTheta0 = float()
        self.cosTheta0 = float()

    def main(cls, args):
        ix = IdealDrive()
        ix.setVelocityRight(2.5)
        ix.setVelocityLeft(2.0)
        ix.setAccelerationRight(0.70)
        ix.setAccelerationLeft(0.89)
        ix.setBodyWidth(0.1)
        for i in range(120, 130):
            n = ix.getSimpsonIntervals_0(i / 10.0)
            print(f"time: {(i / 10.0)}, intervals: {n}")

    def __str__(self):
        """
        To facilitate debugging, this function generates a string representing
        the settings of the robot.
        """
        return f"Start at: ({self.initialPos.x}," +\
               f"{self.initialPos.y}); facing " +\
               f"{math.degrees(self.initialPos.theta)}\u00b0 \n" +\
               f"Body: {self.bodyWidth} Vels: " +\
               f"{self.velocityLeft}, {self.velocityRight}"

    # TODO make all getters/setters properties instead

    def setInitialLocation(self, fp):
        self.initialPos.set(fp)

    def setX0(self, x0):
        self.initialPos.x = x0

    def setY0(self, y0):
        self.initialPos.y = y0

    def setTheta0(self, theta):
        """
        Set the initial facing angle of the robot.  The angle is expressed
        in degrees, measured counterclockwise from East (i.e., 0 deg;
        is facing right, 90 deg; is straight up, etc.).
        """
        #  Convert from degrees to radians
        self.initialPos.theta = math.radians(theta)
        #  Store the sin and cos of the angle, for use in later calculations
        self.sinTheta0 = math.sin(self.initialPos.theta)
        self.cosTheta0 = math.cos(self.initialPos.theta)

    def setBodyWidth(self, width):
        self.bodyWidth = width

    def getBodyWidth(self):
        return self.bodyWidth

    def setVelocityLeft(self, velocity):
        self.velocityLeft = velocity

    def setVelocityRight(self, velocity):
        self.velocityRight = velocity

    def getVelocityLeft(self, t):
        return self.velocityLeft + t * self.accelerationLeft

    def getVelocityRight(self, t):
        return self.velocityRight + t * self.accelerationRight

    def setAccelerationLeft(self, acceleration):
        self.accelerationLeft = acceleration

    def setAccelerationRight(self, acceleration):
        self.accelerationRight = acceleration

    def getAccelerationLeft(self):
        return self.accelerationLeft

    def getAccelerationRight(self):
        return self.accelerationRight

    def setMaximumAllowableError(self, maxAllowableError):
        self.maxAllowableError = maxAllowableError

    def getMaximumAllowableError(self):
        return self.maxAllowableError

    def getAbsoluteDeltaTheta(self, t):
        """
        deltaTheta lets us determine the total change in the
        system's orientation over a period of time from 0 to t.
        orientation is computed using a second degree polynomial
        for theta(t) = C*t^2 + D*t + theta0.

        If theta(t) is monotonically increasing or decreasing,
        then the total delta t is just a matter of evaluating
        it at f(t) and f(0) and taking the absolute value of
        the differences.  But suppose the robot starts out turning
        to the right, but over time (due to acceleration of the slower
        right wheel) ends up turning to the left.   This function
        is concerned about the total of the absolute delta thetas
        over both parts of the turn.
        """
        C = (self.accelerationRight -
             self.accelerationLeft) / (2 * self.bodyWidth)
        D = (self.velocityRight -
             self.velocityLeft) / self.bodyWidth
        ft = C * t * t + D * t
        if abs(C) < 1.0e-6:
            #  The function theta(t) is essentially a straight line,
            #  so there is no inflexion point and function is monotonically
            #  increasing or decreasing, we simply return |f(t)-f(0)|
            return abs(ft)

        #  There is an inflection-point/extrema at t=x
        x = D / (2 * C)
        if x < 0 or x > t:
            #  The inflection point is outside the range [0, t]
            #  so again, we ignore it
            return abs(ft)

        #  There is an inflection point in the interval, so we return
        #  | f(t)-f(x) |  +  | f(x)-f(0) |
        fx = C * x * x + D * x
        return abs(ft - fx) + abs(fx)

    def getSimpsonIntervals(self, A, B, C, D, x):
        """
        To use Simpson's Rule for approximating the value of an
        integral of f(x) over the interval [0, t], we need to
        select enough sub-intervals so that the absolute error
        is smaller than some arbitrary bound.
        Simpson's Rule provides a technique for estimating the upper limit of
        the magnitude of the error based on the 4th derivative of f(x):

           If |f4(x)| <= M for all x in interval a <= x <= b,
           and h = (b-a)/n  then
               Error <= M * h^4*(b-a)/180
           where n is the number of subintervals.

        For our position functions x(t)=(Ax+B)cos(Cx^2 +Dx +E), and
        y(t)=(Ax+B)sin(Cx^2+Dx+E), the 4th derivatives get a little involved,
        but fortunately we can take advantage of certain simplifications.
        The 4th derivative of of the function f(x) = (Ax+B)cos(Cx^2 + Dx + E)
        is:

            f4(x) = 4Asin(Cx^2 + Dx + E)(2Cx + D)^3
                  - 24Acos(Cx^2 + Dx + E) (2Cx+ D)C
                  + (Ax+b)cos(Cx^2 + Dx + E) (2Cx + D) ^4
                  + 12(Ax+B)sin(Cx^2 + Dx + E) (2Cx+D)^2 * C
                  - 12(Ax+B)cos(Cx^2 + Dx + E)C^2

        Because  |sin(x)| <= 1, |cos(x)|<=1, we know that the
        maximum contribution of the absolute value of the trig functions,
        no matter what the value of x, will be 1.  So we use that value,
        replacing all trig functions with 1.   Now in the expression
        (Ax+B)*sin(x), Ax+B may be less than zero.  But at the same
        time sin(x) may also be negative, giving us a positive
        value for (Ax+B)*sin(x).   Since we are interested in the
        absolute, worst case, maximum value of the 4th derivative over
        the interval, we assume that each term makes a positive
        contribution to the f4(x) but taking absolute values.

             M =  4|A(2Cx + D)^3| + 24|A(2Cx+ D)C|
               +   |(Ax+b)(2Cx + D) ^4|  + 12|(Ax+B)(2Cx+D)^2 * C|
               + 12|(Ax+B)C^2|

        The same rule applies for g(x) = (Ax+B)sin(Cx^2 + Dx + E)
        """
        # precompute some values...
        term1 = A * x + B
        term2 = 2 * C * x + D
        term2P2 = term2 * term2
        term2P3 = term2P2 * term2
        term2P4 = term2P2 * term2P2
        xP5 = math.pow(x, 5)

        Mcos = (abs(4 * A * term2P3) +
                abs(24 * A * C * term2) +
                abs(term1 * term2P4) +
                abs(12 * term1 * term2P2 * C) +
                abs(12 * term1 * C * C))

        Msin = (abs(4 * term2P3) +
                abs(24 * A * term2 * C) +
                abs(term1 * term2P4) +
                abs(12 * term1 * term2P2 * C) +
                abs(12 * term1 * C * C))

        ncos = abs(Mcos * xP5 / (self.maxAllowableError * 180))
        nsin = abs(Msin * xP5 / (self.maxAllowableError * 180))

        n = max(nsin, ncos)
        n = math.pow(n, 0.25)
        N = int(math.ceil(n))
        if (N % 2) == 1:
            N += 1
        N = max(N, 4)
        return N

    def getSimpsonIntervals_0(self, x):
        A = (self.accelerationLeft + self.accelerationRight) / 2
        B = (self.velocityLeft + self.velocityRight) / 2
        C = (self.accelerationRight -
             self.accelerationLeft) / (2 * self.bodyWidth)
        D = (self.velocityRight -
             self.velocityLeft) / self.bodyWidth
        return self.getSimpsonIntervals(A, B, C, D, x)

    def positionAt(self, t):
        """
        Calculate the position of the robot at a given point in time.
        Acceleration is also considered in the calculations.
        See the note at the top of this file for information about
        measurement units.
        (Contributed by Jing YE, University of Melbourne.)

        When acceleration is zero (wheel speeds are constant),
        there is a closed-form solution for both orientation and
        position as a function of time.  But when speeds change,
        there is no close-form solution for position.
        All we know are the derivatives x'(t), y'(t),
        So we need a numerical method to integrate them.
        In this case, we use Simpon's Rule from elementary calculus.
        """
        A = (self.accelerationLeft + self.accelerationRight) / 2
        B = (self.velocityLeft + self.velocityRight) / 2
        C = (self.accelerationRight -
             self.accelerationLeft) / (2 * self.bodyWidth)
        D = (self.velocityRight -
             self.velocityLeft) / self.bodyWidth

        theta0 = self.initialPos.theta
        theta = C * t * t + D * t + theta0

        start = 0
        end = t
        finalX = 0
        finalY = 0

        # Start of Simpson's rule...
        simpsonIntervals = self.getSimpsonIntervals(A, B, C, D, t)
        deltaT = t / simpsonIntervals

        # f(x0)
        finalX += (A * start + B) *\
            (math.cos(C * start * start + D * start + theta0))
        finalY += (A * start + B) *\
            (math.sin(C * start * start + D * start + theta0))

        # 4*f(x1) + 2*f(x2) + ... + 4*f(xn-1)
        for i in range(1, simpsonIntervals):
            start += deltaT
            if (i % 2) == 1:
                finalX += 4 * (A * start + B) *\
                    (math.cos(C * start * start + D * start + theta0))
                finalY += 4 * (A * start + B) *\
                    (math.sin(C * start * start + D * start + theta0))
            else:
                finalX += 2 * (A * start + B) *\
                    (math.cos(C * start * start + D * start + theta0))
                finalY += 2 * (A * start + B) *\
                    (math.sin(C * start * start + D * start + theta0))
        # f(xn)
        finalX += (A * end + B) * (math.cos(C * end * end + D * end + theta0))
        finalY += (A * end + B) * (math.sin(C * end * end + D * end + theta0))
        finalX = deltaT * finalX / 3.0
        finalY = deltaT * finalY / 3.0
        # End of simpson's rule...

        location = FPoint()
        location.x = finalX
        location.y = finalY
        location = location.add_fp(self.initialPos)
        return Position(location.x, location.y, theta)

    def DeadReckonAt(self, t):
        """
        Use dead-reckoning, as described in Gary Lucas' paper, to
        estimate where the robot will be after time t.
        """
        # First, calculate the distance traveled by each wheel:
        distanceLeft = self.velocityLeft * t
        distanceRight = self.velocityRight * t
        # Now, calculate the final angle, and use that to estimate
        # the final position.  See Gary Lucas' paper for derivations
        # of the equations.
        theta = self.initialPos.theta +\
            (distanceRight - distanceLeft) / self.bodyWidth
        x = self.initialPos.x +\
            (distanceRight + distanceLeft) / 2 * math.cos(theta)
        y = self.initialPos.y +\
            (distanceRight + distanceLeft) / 2 * math.sin(theta)
        return Position(x, y, theta)

    def LeftWheelLoc(self, p):
        """
        Given the position of the robot (i.e., location and direction),
        return the location of the left wheel.
        """
        result = FPoint()
        result.x = p.x + self.bodyWidth / 2 * math.cos(p.theta + math.pi / 2)
        result.y = p.y + self.bodyWidth / 2 * math.sin(p.theta + math.pi / 2)
        return result

    def RightWheelLoc(self, p):
        """
        Given the position of the robot (i.e., location and direction),
        return the location of the right wheel.
        """
        result = FPoint()
        result.x = p.x + self.bodyWidth / 2 * math.cos(p.theta - math.pi / 2)
        result.y = p.y + self.bodyWidth / 2 * math.sin(p.theta - math.pi / 2)
        return result

    def NoseLoc(self, p):
        """
        Given the position of the robot (i.e., location and direction),
        return the location of its nose (i.e., the "front".
        """
        result = FPoint()
        # "bodyWidth/2" is the distance from the centerpoint of the drive
        # wheels, to the "nose".  This can be changed if you want the
        # triangle representing the robot to have a different shape,
        # without affecting the rest of the code.
        result.x = p.x + self.bodyWidth / 2 * math.cos(p.theta)
        result.y = p.y + self.bodyWidth / 2 * math.sin(p.theta)
        return result


if __name__ == '__main__':
    import sys
    IdealDrive.main(sys.argv)
