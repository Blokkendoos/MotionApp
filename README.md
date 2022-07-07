## MotionApp
This is a pythonized version of the Java [MotionApplet](http://rossum.sourceforge.net/tools/MotionApplet/) version 1.3.
The original Java applet version was created by Michael Gauland. Later additions have been made by Jing YE, and Tom Brown.
It illustrates different algorithms for computing the path of a small wheeled robot.

From the MotionApplet documentation:

>The first method models its true path which is shown as a set of parallel lines (green, blue, and red). A series of blue triangles shows intermediate positions. The second method computes an an approximated path using a simplified technique. The results of the approximation method are shown in the gray area that shadows the true path. In the text area in the panel on the right of the display, columns marked "DR" and "DR2" show the results of two slightly different ways of performing the approximations. 

Working on a positioning algorithm for a two-wheeled robot, I came across the MotionApplet. Although outdated, I liked the simplicity and demonstrative power of it.  As often in life, one action led to another. Hence this conversion into Python code.

### Code Conversion
The Java code has been refactored into Python with the aid of [java2python](https://github.com/natural/java2python).

For reference, the variable names used in the original applet have not been changed. Having a great preference for underscore names, this results in a mixed naming style of camel case and underscores.

The Tkinter GUI has been created with [PAGE](http://page.sourceforge.net/).

![Screenshot](./screenshots/2022-07-06%20om%2015.24.32.png "Screenshot")

### Dependencies
* python3
* pypubsub
* tkinter

### Run
```
$ cd MotionApp
$ python3 motionapp.py
```

### Related links
* [A Tutorial and elementary Trajectory Model for the differential steering system of robot wheel actuators](http://rossum.sourceforge.net/papers/DiffSteer/DiffSteer.html) by G.W. Lucas [2001]
* [Where am I?](http://www-personal.umich.edu/~johannb/position.htm) by J. Borenstein, et al. [1996]
* [The Rossum Project](http://rossum.sourceforge.net)

