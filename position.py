from point import FPoint
from math import degrees


class Position(FPoint):
    """
    Position describes where the robot is, by extending the FPoint class to
    add the direction the robot is facing.
    """
    def __init__(self, newX=0.0, newY=0.0, newTheta=0.0):
        """
        param: newX: The initial X coordinate (float)
        param: newY: The initial Y coordinate (float)
        param: newTheta: The initial direction (float)
        """
        super().__init__(newX, newY)
        # The direction the robot is facing.  Since this class provides no
        # functions that operate on theta, it is entirely up to the client
        # whether theta is in degrees or radians.
        self.theta = newTheta

    def set(self, newLocation, newTheta):
        """
        Set the location and direction of the robot.

        param: newLocation: The coordinates of the new position (FPoint)
        param: newTheta: The direction the robot is now facing
        """
        super().set_fp(newLocation)
        self.theta = newTheta

    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f}, " +\
               f"{self.theta:.2f}({degrees(self.theta):.2f}\u00b0))"
