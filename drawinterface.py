#!/usr/bin/env python
""" generated source for module DrawInterface """
# 
#  * DrawInterface allows a class to be installed into a FloatCanvas,
#  * so that the object will be asked to draw itself whenever the canvas
#  * is redrawn.
#  *
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael
#  *     Gauland</a>
#  * @version 1.
#  * @see FloatCanvas
#  
class DrawInterface(object):
    """ generated source for interface DrawInterface """
    __metaclass__ = ABCMeta
    #  The implementation fo drawFunc() should draw the object.     
    @abstractmethod
    def drawFunc(self, fc):
        """ generated source for method drawFunc """

