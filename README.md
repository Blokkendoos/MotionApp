# MotionApp
This is a pythonized version of the Java [MotionApplet](http://rossum.sourceforge.net/tools/MotionApplet/) version 1.3.
The original Java applet version was created by Michael Gauland. Later additions have been made by Jing YE, and Tom Brown.
It illustrates different algorithms for computing the path of a small wheeled robot.

The Java code has been refactored into Python with the aid of [java2python](https://github.com/natural/java2python).

Working on a positioning algorithm for a two-wheeled robot, I came across the MotionApplet. Although outdated, I liked the simplicity and demonstrative power of it.  As often in life, one action led to another. Hence this conversion into Python code.

The Tkinter GUI has been created with [PAGE](http://page.sourceforge.net/).

![Screenshot](./screenshots/2022-07-06%20om%2015.24.32.png "Screenshot")

### Dependencies
python3
pypubsub
tkinter

### Run
```
$ cd MotionApp
$ python3 motionapp.py
```

### Related links
* [A Tutorial and elementary Trajectory Model for the differential steering system of robot wheel actuators](http://rossum.sourceforge.net/papers/DiffSteer/DiffSteer.html) by G.W. Lucas [2001]
* [Where am I?](http://www-personal.umich.edu/~johannb/position.htm) by J. Borenstein, et al. [1996]
* [The Rossum Project](http://rossum.sourceforge.net)


