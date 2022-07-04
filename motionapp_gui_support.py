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
    _w1.theta_org.set(90.0)
    _w1.body_width.set(1.0)
    _w1.acceleration_left.set(0.0)
    _w1.acceleration_right.set(0.0)
    _w1.velocity_left.set(2.5)
    _w1.velocity_right.set(2.4)
    _w1.animation_duration.set(2)
    _w1.dead_reckoning_interval.set(0.1)
    _w1.dead_reckoning_interval.set(0.5)

    pub.subscribe(set_computed_values, 'set_computed_values')

def quit_click(event=None):
    root.destroy()

# Gui callback-function definitions

def original_position_changed(*args):
    x = _w1.x_pos_org.get()
    y = _w1.y_pos_org.get()
    theta = _w1.theta_org.get()
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

def body_width_changed(value):
    pub.sendMessage('width_changed', value=value)

def simulation_changed(value):
    duration = _w1.duration.get()
    interval = _w1.dead_reckoning_interval.get()
    value = (duration, interval)
    pub.sendMessage('simulation_changed', value=value)

def format_err_value(a, b=None):
    if b is None:
        err_str = ""
    else:
        err = b - a
        err_str = f" ({err:.2f})"
    return f"{a:.2f}{err_str}"

def set_computed_values(value):
    x, y, theta, x_dr, y_dr, theta_dr, x_drm, y_drm, theta_drm, v_left, v_right = value

    _w1.x_actual.set(format_err_value(x))
    _w1.y_actual.set(format_err_value(y))
    _w1.theta_actual.set(format_err_value(theta))

    _w1.x_dr.set(format_err_value(x_dr, x))
    _w1.y_dr.set(format_err_value(y_dr, y))
    _w1.theta_dr.set(format_err_value(theta_dr, theta))

    _w1.x_drm.set(format_err_value(x_drm, x))
    _w1.y_drm.set(format_err_value(y_drm, x))
    _w1.theta_drm.set(format_err_value(theta_drm, x))

    _w1.v_final_left.set(format_err_value(v_left))
    _w1.v_final_right.set(format_err_value(v_right))

Custom = FloatCanvas  # To be updated by user with name of custom widget.

if __name__ == '__main__':
    motionapp_gui.start_up()





