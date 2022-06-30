#!/usr/bin/env python

""" generated source for module FPoint """
# 
#  * FPoint represents a point on the floating-point Cartesian plane
#  * (i.e., it is an (x, y) pair, with x and y represented as doubles.
#  *
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael
#  *     Gauland</a>
#  * @version 1.
#  
class FPoint(object):
    """ generated source for class FPoint """
    #  The horizontal coordinate. 
    x = float()

    #  The vertical coordinate. 
    y = float()

    #  Default constructor; both coordinates set to Java default of 0.0. 
    def __init___0(self, x=0.0, y=0.0):
        """ generated source for method __init___0 """
        set(x, y)

    # 
    #      * Copy another FPoint object.
    #      
    def set(self, fp):
        """ generated source for method set """
        self.x = fp.x
        self.y = fp.y

    # 
    #      * Set both coordinates, specified as doubles.
    #      
    def set_0(self, x, y):
        """ generated source for method set_0 """
        self.x = x
        self.y = y

    # 
    #      * Add the same value to both coordinates.
    #      
    def add(self, k):
        """ generated source for method add """
        return FPoint(self.x + k, self.y + k)

    # 
    #      * Add one FPoint to another.  This can be used to
    #      * add separate offsets to each coordinate.
    #      
    def add_0(self, fp):
        """ generated source for method add_0 """
        return FPoint(self.x + fp.x, self.y + fp.y)

    # 
    #      * Multiply both coordinate by the same value.
    #      
    def scale(self, k):
        """ generated source for method scale """
        return FPoint(self.x * k, self.y * k)

    # 
    #      * Multiple each coordinate by different values.
    #      
    def scale_0(self, fp):
        """ generated source for method scale_0 """
        return FPoint(self.x * fp.x, self.y * fp.y)

    # 
    #      * Returns the coordinates as a string, for printing or display.
    #      
    def __str__(self):
        """ generated source for method toString """
        return str("(" + self.x + ", " + self.y + ")")
