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

    # TODO check code on set/add/scale usage (with fp, or constant factor k)

    def set_fp(self, fp):
        self.x = fp.x
        self.y = fp.y

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def add_k(self, k):
        return FPoint(self.x + k, self.y + k)

    def add_fp(self, fp):
        return FPoint(self.x + fp.x, self.y + fp.y)

    def scale_k(self, k):
        return FPoint(self.x * k, self.y * k)

    def scale_fp(self, fp):
        return FPoint(self.x * fp.x, self.y * fp.y)

    def __str__(self):
        return f"( {self.x:.2f}, {self.y:.2f})"
