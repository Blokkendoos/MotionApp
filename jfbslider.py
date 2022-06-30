#!/usr/bin/env python
""" generated source for module JFBSlider """
import javax.swing

import javax.swing.event

import java.awt

import java.text

import java.util

# 
#  * JFBSlider creates a new control element, by combining a slider,
#  * with a textbox showing the current setting of the slider.  The limits
#  * of the slider are set as floating-point numbers, and the number
#  * of decimal places dislayed in the feedback window is adjustable.
#  *
#  * @author <a href="mailto:MikeGauland@users.sourceforge.net">Michael
#  *     Gauland</a>
#  * @version 1.
#  
class JFBSlider(JPanel, ChangeListener):
    """ generated source for class JFBSlider """
    # 
    #      * All JFBSliders use this font for the feedback window.
    #      
    textFont = Font("Monospaced", Font.PLAIN, 12)

    # 
    #      * All JFBSliders use this font for the slider labels.
    #      
    sliderFont = Font("Serif", Font.BOLD, 10)

    #  Horizontal padding on the outside edges of the JFBSlider. 
    outerPad = Dimension(10, 1)

    #  Horizontal adding between the elements of the JFBSlider. 
    innerPad = Dimension(5, 1)

    #  The lower limit of the control range. 
    lowerLimit = float()

    #  The upper limit of the control range. 
    upperLimit = float()

    #  The number of steps in the slider. 
    steps = int()

    #  The actual slider control. 
    theSlider = JSlider()

    #  The feedback text field. 
    theTextField = JTextField()

    #  Controls the formatting of the feedback number. 
    formatter = NumberFormat.getInstance()

    #  The units for the control (e.g., "&deg;") can be specified. 
    units = ""

    # 
    #      * This constructor requires
    #      * @param name A string which will become the label of the slider.
    #      * @param min The minimum floating-point value of the control.
    #      * @param max The maximum floating-point value of the control.
    #      * @param numSteps The number of discrete steps along the slider.
    #      * @param digits The number of digits to the right of the decimal
    #      *     point to display in the feedback window.
    #      * @param units A string representing measurement units that
    #      *     will be displayed with the value in the feedback window.
    #      
    @overloaded
    def __init__(self, name, min, max, numSteps, digits, units):
        """ generated source for method __init__ """
        super(JFBSlider, self).__init__()
        self.units = units
        setup(name, min, max, numSteps, digits)

    # 
    #      * This constructor does not require a units string.
    #      * @param name A string which will become the label of the slider.
    #      * @param min The minimum floating-point value of the control.
    #      * @param max The maximum floating-point value of the control.
    #      * @param numSteps The number of discrete steps along the slider.
    #      * @param digits The number of digits to the right of the decimal
    #      *     point to display in the feedback window.
    #      * @param units A string representing measurement units that
    #      *     will be displayed with the value in the feedback window.
    #      
    @__init__.register(object, str, float, float, int, int)
    def __init___0(self, name, min, max, numSteps, digits):
        """ generated source for method __init___0 """
        super(JFBSlider, self).__init__()
        setup(name, min, max, numSteps, digits)

    # 
    #      * This is a private function to help the two constructors set up
    #      * the control.  It is only called during contruction.
    #      *
    #      * The parameters are the same as for the constructors.
    #      
    def setup(self, name, min, max, numSteps, digits):
        """ generated source for method setup """
        #  Set the limits and number of steps for the slider: 
        self.lowerLimit = min
        self.upperLimit = max
        self.steps = numSteps
        # 
        #          * Set up the number formatter.  By setting both "...Min..."
        #          * and "...Max..." to the same value, the same number of
        #          * fractional digits will always be displayed.
        #          
        self.formatter.setMinimumFractionDigits(digits)
        self.formatter.setMaximumFractionDigits(digits)
        # 
        #          * Create the slider, and set the font.
        #          
        self.theSlider = JSlider(0, steps)
        self.theSlider.setFont(self.sliderFont)
        # 
        #          * Create a HashTable for the slider labels, then add 
        #          * strings for to label the limits and center of the
        #          * slider.
        #          
        labelStrings = Hashtable()
        #  Label the minimum (left limit)
        label = JLabel(self.formatter.format(min))
        label.setFont(self.sliderFont)
        labelStrings.put(int(0), label)
        #  Label the midpoint
        label = JLabel(formatter.format((min + max) / 2))
        label.setFont(self.sliderFont)
        labelStrings.put(int(self.steps / 2), label)
        #  Label the maximum (right limit)
        label = JLabel(formatter.format(max))
        label.setFont(self.sliderFont)
        labelStrings.put(int(self.steps), label)
        # 
        #          * Install the labels on the slider, and turn them on.
        #          
        self.theSlider.setLabelTable(labelStrings)
        self.theSlider.setPaintLabels(True)
        # 
        #          * Create the label for the slider, using the name string
        #          * passed in to the constructor.
        #          
        theLabel = JLabel(name)
        theLabel.setHorizontalTextPosition(JLabel.RIGHT)
        theLabel.setLabelFor(self.theSlider)
        # 
        #          * Set the layout or the JFBSlider, and install the
        #          * label an the slider, with horizontal padding.
        #          
        self.setLayout(BoxLayout(self, BoxLayout.X_AXIS))
        self.add(Box.createRigidArea(self.outerPad))
        self.add(theLabel)
        self.add(Box.createRigidArea(self.innerPad))
        self.add(self.theSlider)
        # 
        #          * Set up the text field.  Note that it cannot be edited.  It
        #          * would be cool to allow a user to enter a value into the box,
        #          * as an alternative to setting the slider, but that is not
        #          * implemented in this class.
        #          
        self.theTextField.setEditable(False)
        self.theTextField.setHorizontalAlignment(JTextField.RIGHT)
        self.theTextField.setFont(self.textFont)
        # 
        #              * Set the width of the text box to be wide enough to
        #              * show the full range of values.
        #              
        len1 = len(self.formatter.format(min))
        len2 = len(self.formatter.format(max))
        places = len1 if (len1 >= len2) else len2
        places += len(units)
        self.theTextField.setColumns(places + 1)
        #  1 extra space for clarity
        # 
        #          * Set the maximum size to the preferred size, so the box
        #          * won't stretch to fill large windows.
        #          
        self.theTextField.setMaximumSize(self.theTextField.getPreferredSize())
        # 
        #          * Add the text box, with padding, to the JFBSlider panel.
        #          
        self.add(Box.createRigidArea(self.innerPad))
        self.add(self.theTextField)
        self.add(Box.createRigidArea(self.outerPad))
        # 
        #          * Add this object as a ChangeListener to the slider.  Whenever
        #          * the slider moves, we need to update the text box.
        #          
        self.theSlider.addChangeListener(self)
        # 
        #          * Force a change so the text box will be correct.
        #          
        setValue(getValue())

    # 
    #      * The client can add tick marks to the JFBSlider, as
    #      * with any JSlider object.
    #      *
    #      * @param major The spacing between major tick marks.
    #      * @param minor The spacing between minor tick marks.
    #      
    def addTicks(self, major, minor):
        """ generated source for method addTicks """
        self.theSlider.setMajorTickSpacing(major)
        self.theSlider.setMinorTickSpacing(minor)
        self.theSlider.setPaintTicks(True)

    # 
    #      * This is called when the slider value is set, and just
    #      * updates the feedback text box.
    #      *
    #      * @param e The event, which is ignored, since we know
    #      *     it must have come from the slider.
    #      
    def stateChanged(self, e):
        """ generated source for method stateChanged """
        self.theTextField.setText(self.formatter.format(getValue()) + self.units)

    # 
    #      * Add a ChangeListener to the slider. This lets the client
    #      * react to changes to the control (which is, after all, the point
    #      * of having a control at all, isn't it?).
    #      *
    #      * @param l The ChangeListener object to add.
    #      
    def addChangeListener(self, l):
        """ generated source for method addChangeListener """
        self.theSlider.addChangeListener(l)

    # 
    #      * This returns the value of the slider, scaled based on the
    #      * floating-point min and max values supplied at instantiation.
    #      
    def getValue(self):
        """ generated source for method getValue """
        return self.lowerLimit + self.theSlider.getValue() * (self.upperLimit - self.lowerLimit) / self.steps

    # 
    #      * Force a new value on the control, by setting the slider to
    #      * the point closest to the supplied floating-point value.  This
    #      * will reslt in all ChangeListeners being called, including this
    #      * object, so this function needn't update the feedback text box.
    #      *
    #      * @param value The new value for the control.
    #      
    def setValue(self, value):
        """ generated source for method setValue """
        self.theSlider.setValue((Math.round(((value - self.lowerLimit) / (self.upperLimit - self.lowerLimit) * self.steps))))

    # 
    #      * When a client is notified that the control changed (through
    #      * the ChangeListener mechanism), it can pass the event to this
    #      * function to determine whether this control generated the message.
    #      
    def isEventSource(self, e):
        """ generated source for method isEventSource """
        return e.getSource() == theSlider

    # 
    #      * Returns the context of the feedback text field.  This can be useful
    #      * when a client wants to print or display the control value, without
    #      * having to format it.
    #      
    def getText(self):
        """ generated source for method getText """
        return self.theTextField.getText()

