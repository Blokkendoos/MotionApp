#!/usr/bin/env python

from fpoint import FPoint


class Position(FPoint):
    """
    Position describes where the robot is, by extending the FPoint class to
    add the direction the robot is facing.
    """
    # The direction the robot is facing.  Since this class provides no
    # functions that operate on theta, it is entirely up to the client
    # whether theta is in degrees or radians.
    theta = float()

    def __init__(self):
        """ generated source for method __init__ """
        super(Position, self).__init__()
        #  Rely on FPoint default constructor; Java will set theta to 0.

    def __init___(self, newX=0.0, newY=0.0, newTheta=0.0):
        """
        param: newX: The initial X coordinate (float)
        param: newY: The initial Y coordinate (float)
        param: newTheta: The initial direction (float)
        """
        super().__init__(newX, newY)
        self.theta = newTheta

    def set(self, newLocation, newTheta):
        """ generated source for method set """
        super(Position, self).set(newLocation)
        self.theta = newTheta
        """
        Set the location and direction of the robot.

        param: newLocation: The coordinates of the new position (FPoint)
        param: newTheta: The direction the robot is now facing
        """
