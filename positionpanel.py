#!/usr/bin/env python
""" generated source for module PositionPanel """
import javax.swing

import javax.swing.border

import java.text

import java.awt

# 
#  * This class is used to display both the true final position of the robot,
#  * and the dead-reckoned position.
#  *
#  * @author Various
#  * @version 1.
#  
class PositionPanel(JPanel):
    """ generated source for class PositionPanel """
    # 
    #      * The default constructor sets up all fields of the display, and
    #      * initially shows the time and all coordinates as 0, and the angles
    #      * as 90 degrees.
    #      
    def __init__(self):
        """ generated source for method __init__ """
        super(PositionPanel, self).__init__()
        # 
        #     * Set up the border for this panel
        #     
        tBorder = TitledBorder("Actual and Dead " + "Reckoned Position " + "(DR2 uses mean theta)")
        setBorder(tBorder)
        setForeground(tBorder.getTitleColor())
        # 
        #     * Use a "Grid Bag Layout" for this panel.  It will be laid
        #     * out like this:
        #     * X:          <actual X>    <dr X>    <dr X err>   <dr2 X>   <dr2 X err>
        #     * Y:          <actual Y>    <dr Y>    <dr Y err>   <dr2 Y>   <dr2 Y err>
        #     * Theta:      <actual deg>  <dr deg>  <dr deg err> <dr2 deg> <dr2 deg err>
        # 		* Final Vel:  <actual L Vel><actual R final Vel>
        #     
        gbl = GridBagLayout()
        gbc = GridBagConstraints()
        setLayout(gbl)
        gbc.anchor = gbc.NORTHWEST
        # 
        #     * Set up the "X" label
        #     
        gbc.fill = gbc.HORIZONTAL
        xJLabel = JLabel("X:")
        gbc.gridx = 0
        gbc.gridy = 1
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(xJLabel, gbc)
        add(xJLabel)
        # 
        #     * Set up the "Y" label
        #     
        yJLabel = JLabel("Y:")
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 0
        gbc.gridy = 2
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(yJLabel, gbc)
        add(yJLabel)
        # 
        #     * Set up the "Theta" label
        #     
        aJLabel = JLabel("Theta:")
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 0
        gbc.gridy = 3
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(aJLabel, gbc)
        add(aJLabel)
        # 
        #      * Set up the "Velocity" label
        #      
        vJLabel = JLabel("Final Vel L/R:")
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 0
        gbc.gridy = 4
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(vJLabel, gbc)
        add(vJLabel)
        # 
        #      * Set up the "Actual Pos" label
        #      
        aposJLabel = JLabel("Actual")
        aposJLabel.setHorizontalAlignment(JLabel.RIGHT)
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 1
        gbc.gridy = 0
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(aposJLabel, gbc)
        add(aposJLabel)
        # 
        #      * Set up the "Dead Rec Pos" label
        #      
        dJLabel = JLabel("DR (Err)")
        dJLabel.setHorizontalAlignment(JLabel.RIGHT)
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 2
        gbc.gridy = 0
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(dJLabel, gbc)
        add(dJLabel)
        # 
        #      * Set up the "Dead Rec w/ mean Pos" label
        #      
        dmJLabel = JLabel("DR2 (Err)")
        dmJLabel.setHorizontalAlignment(JLabel.RIGHT)
        gbc.fill = gbc.HORIZONTAL
        gbc.gridx = 4
        gbc.gridy = 0
        gbc.weightx = 0
        gbc.weighty = 1
        gbl.setConstraints(dmJLabel, gbc)
        add(dmJLabel)
        # 
        #     * Set up the text field for the actual X coordinate
        #     
        xField = JTextField(8)
        xField.setEditable(False)
        xField.setHorizontalAlignment(JTextField.RIGHT)
        xField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 1
        gbc.gridy = 1
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(xField, gbc)
        add(xField)
        # 
        #     * Set up the text field for the actual Y coordinate
        #     
        yField = JTextField(8)
        yField.setEditable(False)
        yField.setHorizontalAlignment(JTextField.RIGHT)
        yField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 1
        gbc.gridy = 2
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(yField, gbc)
        add(yField)
        # 
        #     * Set up the text field for the actual angle (theta)
        #     
        aField = JTextField(8)
        aField.setEditable(False)
        aField.setHorizontalAlignment(JTextField.RIGHT)
        aField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 1
        gbc.gridy = 3
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(aField, gbc)
        add(aField)
        # 
        #     * Set up the text field for the dead-reckoned X coordinate
        #     
        dxField = JTextField(8)
        dxField.setEditable(False)
        dxField.setHorizontalAlignment(JTextField.RIGHT)
        dxField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 2
        gbc.gridy = 1
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(dxField, gbc)
        add(dxField)
        # 
        #     * Set up the text field for the dead-reckoned Y coordinate
        #     
        dyField = JTextField(8)
        dyField.setEditable(False)
        dyField.setHorizontalAlignment(JTextField.RIGHT)
        dyField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 2
        gbc.gridy = 2
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(dyField, gbc)
        add(dyField)
        # 
        #     * Set up the text field for the dead-reckoned angle (theta)
        #     
        daField = JTextField(8)
        daField.setEditable(False)
        daField.setHorizontalAlignment(JTextField.RIGHT)
        daField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 2
        gbc.gridy = 3
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(daField, gbc)
        add(daField)
        # 
        #     * Set up the text fields for left and right velocities
        #     
        vLeftField = JTextField(8)
        vLeftField.setEditable(False)
        vLeftField.setHorizontalAlignment(JTextField.RIGHT)
        vLeftField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 1
        gbc.gridy = 4
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(vLeftField, gbc)
        add(vLeftField)
        vRightField = JTextField(8)
        vRightField.setEditable(False)
        vRightField.setHorizontalAlignment(JTextField.RIGHT)
        vRightField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 2
        gbc.gridy = 4
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(vRightField, gbc)
        add(vRightField)
        # 
        #     * Set up the text field for the dead-reckoned with mean theta X coordinate
        #     
        dmxField = JTextField(8)
        dmxField.setEditable(False)
        dmxField.setHorizontalAlignment(JTextField.RIGHT)
        dmxField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 4
        gbc.gridy = 1
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(dmxField, gbc)
        add(dmxField)
        # 
        #     * Set up the text field for the dead-reckoned with mean theta Y coordinate
        #     
        dmyField = JTextField(8)
        dmyField.setEditable(False)
        dmyField.setHorizontalAlignment(JTextField.RIGHT)
        dmyField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 4
        gbc.gridy = 2
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(dmyField, gbc)
        add(dmyField)
        # 
        #     * Set up the text field for the dead-reckoned with mean theta angle (theta)
        #     
        dmaField = JTextField(8)
        dmaField.setEditable(False)
        dmaField.setHorizontalAlignment(JTextField.RIGHT)
        dmaField.setBorder(None)
        gbc.fill = gbc.NONE
        gbc.gridx = 4
        gbc.gridy = 3
        gbc.weightx = 1
        gbc.weighty = 1
        gbl.setConstraints(dmaField, gbc)
        add(dmaField)
        # 
        #     * Create formatters for the coordinates and time (2 decimal places)
        #     * and the angles (1 decimal place, and the degrees symbol).
        #     
        df = DecimalFormat("####0.00")
        dfs = DecimalFormat("+####0.00;-####0.00")
        da = DecimalFormat("####0.0\u00b0")
        das = DecimalFormat("+####0.0\u00b0;-####0.0\u00b0")
        # 
        #     * Initialize all displayed values to 0, except the angles,
        #     * which are set to 90 degrees.
        #     
        setComputedValues(0.0, 0.0, 90.0, 0.0, 0.0, 90.0, 0.0, 0.0, 90.0, 0.0, 0.0)

    #  Convert from radians to degrees, and coerce to range (-180, 180] 
    def degree(self, a):
        """ generated source for method degree """
        d = a * 180.0 / Math.PI
        if d < 0:
            d = -d
        d = d - 360.0 * Math.floor(d / 360.0)
        if a < 0:
            d = 360.0 - d
        if d > 180.0:
            d -= 360
        return d

    # 
    #      * Display both the true and dead-reckoned positions
    #      * (location and direction).
    #      
    def setComputedValues(self, x, y, theta, xDR, yDR, thetaDR, xDRM, yDRM, thetaDRM, vLeft, vRight):
        """ generated source for method setComputedValues """
        xField.setText(df.format(x))
        yField.setText(df.format(y))
        aField.setText(da.format(self.degree(theta)))
        dxField.setText(df.format(xDR) + " (" + dfs.format(xDR - x) + ")")
        dyField.setText(df.format(yDR) + " (" + dfs.format(yDR - y) + ")")
        daField.setText(da.format(self.degree(thetaDR)) + " (" + das.format(self.degree(thetaDR - theta)) + ")")
        dmxField.setText(df.format(xDRM) + " (" + dfs.format(xDRM - x) + ")")
        dmyField.setText(df.format(yDRM) + " (" + dfs.format(yDRM - y) + ")")
        dmaField.setText(da.format(self.degree(thetaDRM)) + " (" + das.format(self.degree(thetaDRM - theta)) + ")")
        vLeftField.setText(df.format(vLeft))
        vRightField.setText(df.format(vRight))

    #  Formatter for the coordinates and time (2 decimal places). 
    df = DecimalFormat()

    #  Formatter for the errors (2 decimal places, allows shows + or -). 
    dfs = DecimalFormat()

    #  Formatter for the angles (1 decimal place, and the "&deg;" symbol). 
    da = DecimalFormat()

    #  Formatter for the angle errors (1 decimal place, allows include + or - 
    # 		 * and the "&deg;" symbol). 
    das = DecimalFormat()

    #  Field for displaying the "true" X coordinate. 
    xField = JTextField()

    #  Field for displaying the "true" Y coordinate. 
    yField = JTextField()

    #  Field for displaying the "true" direction. 
    aField = JTextField()

    #  Field for displaying the dead-reckoned X coordinate. 
    dxField = JTextField()

    #  Field for displaying the dead-reckoned Y coordinate. 
    dyField = JTextField()

    #  Field for displaying the dead-reckoned direction. 
    daField = JTextField()

    #  Field for displaying the dead-reckoned X coordinate. 
    dmxField = JTextField()

    #  Field for displaying the dead-reckoned Y coordinate. 
    dmyField = JTextField()

    #  Field for displaying the dead-reckoned direction. 
    dmaField = JTextField()

    #  Field for displaying the final velocities. 
    vLeftField = JTextField()
    vRightField = JTextField()

