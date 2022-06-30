#!/usr/bin/env python

from fpoint import FPoint

""" generated source for module Position """
# 
#  * Position describes where the robot is, by extending the FPoint class to 
#  * add the direction the robot is facing.
#  * 
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael
#  *     Gauland</a>
#  * @version 1.
#  
class Position(FPoint):
    """ generated source for class Position """
    # 
    #      * The direction the robot is facing.  Since this class provides no
    #      * functions that operate on theta, it is entirely up to the client
    #      * whether theta is in degrees or radians.
    #      
    theta = float()

    def __init__(self):
        """ generated source for method __init__ """
        super(Position, self).__init__()
        #  Rely on FPoint default constructor; Java will set theta to 0.

    # 
    #      * Constructor to initialize the object with x and y coordinates, and
    #      * the direction.
    #      *
    #      * @param newX The initial X coordinate.
    #      * @param newY The initial Y coordinate.
    #      * @param newTheta The initial direction.
    #      
    def __init___0(self, newX, newY, newTheta):
        """ generated source for method __init___0 """
        super(Position, self).__init__()
        super(Position, self).set(newX, newY)
        self.theta = newTheta

    # 
    #      * Set the location and direction of the robot.
    #      *
    #      * @param newLocation The coordinates of the new position.
    #      * @param newTheta The direction the robot is now facing.
    #      
    def set(self, newLocation, newTheta):
        """ generated source for method set """
        super(Position, self).set(newLocation)
        self.theta = newTheta

