#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jul 02, 2022 12:38:45 AM CEST  platform: Darwin
#    Jul 02, 2022 08:16:36 AM CEST  platform: Darwin
#    Jul 04, 2022 01:57:20 PM CEST  platform: Darwin

import tkinter as tk
from pubsub import pub
from math import floor, degrees, radians

import motionapp_gui
from floatcanvas import FloatCanvas

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol('WM_DELETE_WINDOW', quit_click)
    root.bind('<Control-q>', quit_click)
    global _top1, _w1
    _top1 = root
    _w1 = motionapp_gui.Toplevel1(_top1)
    initial_values()
    root.mainloop()

def initial_values():
    _w1.x_pos_org.set(0.0)
    _w1.y_pos_org.set(0.0)
    _w1.theta_org.set(90.0)  # degrees
    _w1.body_width.set(1.0)
    _w1.acceleration_left.set(0.0)
    _w1.acceleration_right.set(0.0)
    _w1.velocity_left.set(2.5)
    _w1.velocity_right.set(2.4)
    _w1.animation_duration.set(2)
    _w1.dead_reckoning_interval.set(0.1)
    _w1.dead_reckoning_interval.set(0.5)

    pub.subscribe(set_computed_values, 'set_computed_values')

    # trigger update after (Tkinter) main loop has started
    wait_time = 50  # ms
    root.after(wait_time, trigger_update)

def quit_click(event=None):
    root.destroy()

def trigger_update():
    original_position_changed()
    velocity_changed()
    acceleration_changed()
    body_width_changed()
    simulation_changed()

def radians_to_degrees(angle):
    # Convert from radians to degrees, and coerce to range (-180, 180]
    deg = degrees(angle)
    if deg < 0:
        deg *= -1
    deg = deg - 360.0 * floor(deg / 360.0)
    if angle < 0:
        deg = 360.0 - deg
    if deg > 180.0:
        deg -= 360
    return deg

# Gui callback-function definitions

def original_position_changed(*args):
    x = _w1.x_pos_org.get()
    y = _w1.y_pos_org.get()
    theta = radians(_w1.theta_org.get())
    value = (x, y, theta)
    pub.sendMessage('position_changed', value=value)

def velocity_changed(*args):
    left = _w1.velocity_left.get()
    right = _w1.velocity_right.get()
    value = (left, right)
    pub.sendMessage('velocity_changed', value=value)

def acceleration_changed(*args):
    left = _w1.acceleration_left.get()
    right = _w1.acceleration_right.get()
    value = (left, right)
    pub.sendMessage('acceleration_changed', value=value)

def body_width_changed(*args):
    value = _w1.body_width.get()
    pub.sendMessage('body_width_changed', value=value)

def simulation_changed(*args):
    duration = _w1.duration.get()
    interval = _w1.dead_reckoning_interval.get()
    value = (duration, interval)
    pub.sendMessage('simulation_changed', value=value)

def format_err_value(a, b=None, angle=False):
    if angle is True:
        degree_sign = '\u00b0'
    else:
        degree_sign = ''
    if b is None:
        err_str = ''
    else:
        err = b - a
        err_str = f" ({err:.2f}{degree_sign})"
    a_str = f"{a:.2f}{degree_sign}"
    return f"{a_str}{err_str}"


def set_computed_values(value):
    x, y, theta, x_dr, y_dr, theta_dr, x_drm, y_drm, theta_drm, v_left, v_right = value

    theta = radians_to_degrees(theta)
    theta_dr = radians_to_degrees(theta_dr)
    theta_drm = radians_to_degrees(theta_drm)

    _w1.x_actual.set(format_err_value(x))
    _w1.y_actual.set(format_err_value(y))
    _w1.theta_actual.set(format_err_value(theta, angle=True))

    _w1.x_dr.set(format_err_value(x_dr, x))
    _w1.y_dr.set(format_err_value(y_dr, y))
    _w1.theta_dr.set(format_err_value(theta_dr, theta, angle=True))

    _w1.x_drm.set(format_err_value(x_drm, x))
    _w1.y_drm.set(format_err_value(y_drm, y))
    _w1.theta_drm.set(format_err_value(theta_drm, theta, angle=True))

    _w1.v_final_left.set(format_err_value(v_left))
    _w1.v_final_right.set(format_err_value(v_right))


Custom = FloatCanvas  # To be updated by user with name of custom widget.


if __name__ == '__main__':
    motionapp_gui.start_up()
