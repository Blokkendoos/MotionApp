#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Jul 02, 2022 10:56:50 AM CEST  platform: Darwin

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import motionapp_gui_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40' # X11 color: #666666
        _ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 
        _tabbg1 = 'grey75' 
        _tabbg2 = 'grey89' 
        _bgmode = 'light' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("969x675+890+350")
        top.minsize(1, 1)
        top.maxsize(2545, 1388)
        top.resizable(1,  1)
        top.title("MotionApp")
        top.configure(highlightcolor="black")

        self.top = top
        self.x_pos_org = tk.DoubleVar()
        self.y_pos_org = tk.DoubleVar()
        self.theta_org = tk.DoubleVar()
        self.body_width = tk.DoubleVar()
        self.velocity_right = tk.DoubleVar()
        self.velocity_left = tk.DoubleVar()
        self.acceleration_right = tk.DoubleVar()
        self.acceleration_left = tk.DoubleVar()
        self.animation_duration = tk.DoubleVar()
        self.dead_reckoning_interval = tk.DoubleVar()

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.031, rely=0.044, relheight=0.899
                , relwidth=0.496)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")

        self.Canvas1 = tk.Canvas(self.Frame1)
        self.Canvas1.place(relx=0.021, rely=0.016, relheight=0.957
                , relwidth=0.958)
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")

        self.style.map('TNotebook.Tab', background =
            [('selected', _bgcolor), ('active', _tabbg1),
            ('!active', _tabbg2)], foreground =
            [('selected', _fgcolor), ('active', _tabfg1), ('!active',  _tabfg2)])
        self.TNotebook1 = ttk.Notebook(self.top)
        self.TNotebook1.place(relx=0.543, rely=0.046, relheight=0.65
                , relwidth=0.44)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text='''Robot''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text='''Speed''', compound="left"
                ,underline='''-1''', )
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(2, text='''Timing''', compound="left"
                ,underline='''-1''', )

        self.TLabelframe1 = ttk.Labelframe(self.TNotebook1_t1)
        self.TLabelframe1.place(relx=0.05, rely=0.027, relheight=0.621
                , relwidth=0.917)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Original Position''')

        self.x_pos =  tk.Scale(self.TLabelframe1, from_=-10.0, to=10.0, resolution=0.1)
        self.x_pos.place(relx=0.028, rely=0.089, relheight=0.331, relwidth=0.931)

        self.x_pos.configure(activebackground="beige")
        self.x_pos.configure(command=motionapp_gui_support.original_position_changed)
        self.x_pos.configure(label="X")
        self.x_pos.configure(length="350")
        self.x_pos.configure(orient="horizontal")
        self.x_pos.configure(troughcolor="#d9d9d9")
        self.x_pos.configure(variable=self.x_pos_org)

        self.y_pos =  tk.Scale(self.TLabelframe1, from_=-10.0, to=10.0, resolution=0.1)
        self.y_pos.place(relx=0.028, rely=0.366, relheight=0.331, relwidth=0.923)

        self.y_pos.configure(activebackground="beige")
        self.y_pos.configure(command=motionapp_gui_support.original_position_changed)
        self.y_pos.configure(label="Y")
        self.y_pos.configure(length="347")
        self.y_pos.configure(orient="horizontal")
        self.y_pos.configure(troughcolor="#d9d9d9")
        self.y_pos.configure(variable=self.y_pos_org)

        self.theta =  tk.Scale(self.TLabelframe1, from_=-180.0, to=180.0, resolution=1.0)
        self.theta.place(relx=0.028, rely=0.638, relheight=0.331, relwidth=0.928)

        self.theta.configure(activebackground="beige")
        self.theta.configure(command=motionapp_gui_support.original_position_changed)
        self.theta.configure(label="Theta")
        self.theta.configure(length="349")
        self.theta.configure(orient="horizontal")
        self.theta.configure(troughcolor="#d9d9d9")
        self.theta.configure(variable=self.theta_org)

        self.TLabelframe2 = ttk.Labelframe(self.TNotebook1_t1)
        self.TLabelframe2.place(relx=0.052, rely=0.686, relheight=0.287
                , relwidth=0.922)
        self.TLabelframe2.configure(relief='')
        self.TLabelframe2.configure(text='''Body Settings''')

        self.body_width =  tk.Scale(self.TLabelframe2, from_=0.1, to=2.1, resolution=0.1)
        self.body_width.place(relx=0.028, rely=0.227, relheight=0.622
                , relwidth=0.918)
        self.body_width.configure(activebackground="beige")
        self.body_width.configure(command=motionapp_gui_support.body_width_changed)
        self.body_width.configure(label="Width")
        self.body_width.configure(length="346")
        self.body_width.configure(orient="horizontal")
        self.body_width.configure(troughcolor="#d9d9d9")
        self.body_width.configure(variable=self.body_width)

        self.TLabelframe4 = ttk.Labelframe(self.TNotebook1_t2)
        self.TLabelframe4.place(relx=0.05, rely=0.039, relheight=0.476
                , relwidth=0.88)
        self.TLabelframe4.configure(relief='')
        self.TLabelframe4.configure(text='''Velocities''')

        self.v_right =  tk.Scale(self.TLabelframe4, from_=-5.0, to=5.0, resolution=0.1)
        self.v_right.place(relx=0.056, rely=0.107, relheight=0.411
                , relwidth=0.871)
        self.v_right.configure(activebackground="beige")
        self.v_right.configure(command=motionapp_gui_support.velocity_changed)
        self.v_right.configure(label="Right")
        self.v_right.configure(length="304")
        self.v_right.configure(orient="horizontal")
        self.v_right.configure(troughcolor="#d9d9d9")
        self.v_right.configure(variable=self.velocity_right)

        self.Scale1_1 =  tk.Scale(self.TLabelframe4, from_=-5.0, to=5.0, resolution=0.1)
        self.Scale1_1.place(relx=0.056, rely=0.431, relheight=0.411
                , relwidth=0.871)
        self.Scale1_1.configure(activebackground="beige")
        self.Scale1_1.configure(command=motionapp_gui_support.velocity_changed)
        self.Scale1_1.configure(label="Left")
        self.Scale1_1.configure(length="314")
        self.Scale1_1.configure(orient="horizontal")
        self.Scale1_1.configure(troughcolor="#d9d9d9")
        self.Scale1_1.configure(variable=self.velocity_left)

        self.TLabelframe5 = ttk.Labelframe(self.TNotebook1_t2)
        self.TLabelframe5.place(relx=0.05, rely=0.541, relheight=0.423
                , relwidth=0.88)
        self.TLabelframe5.configure(relief='')
        self.TLabelframe5.configure(text='''Accelerations''')

        self.a_right =  tk.Scale(self.TLabelframe5, from_=-1.0, to=1.0, resolution=0.1)
        self.a_right.place(relx=0.054, rely=0.114, relheight=0.463
                , relwidth=0.871)
        self.a_right.configure(activebackground="beige")
        self.a_right.configure(command=motionapp_gui_support.acceleration_changed)
        self.a_right.configure(label="Right")
        self.a_right.configure(length="314")
        self.a_right.configure(orient="horizontal")
        self.a_right.configure(troughcolor="#d9d9d9")
        self.a_right.configure(variable=self.acceleration_right)

        self.a_left =  tk.Scale(self.TLabelframe5, from_=-1.0, to=1.0, resolution=0.1)
        self.a_left.place(relx=0.056, rely=0.486, relheight=0.463
                , relwidth=0.871)
        self.a_left.configure(activebackground="beige")
        self.a_left.configure(command=motionapp_gui_support.acceleration_changed)
        self.a_left.configure(label="Left")
        self.a_left.configure(length="314")
        self.a_left.configure(orient="horizontal")
        self.a_left.configure(troughcolor="#d9d9d9")
        self.a_left.configure(variable=self.acceleration_left)

        self.TLabelframe6 = ttk.Labelframe(self.TNotebook1_t3)
        self.TLabelframe6.place(relx=0.047, rely=0.048, relheight=0.348
                , relwidth=0.88)
        self.TLabelframe6.configure(relief='')
        self.TLabelframe6.configure(text='''Simulation''')

        self.duration =  tk.Scale(self.TLabelframe6, from_=0.0, to=30.0, resolution=0.1)
        self.duration.place(relx=0.056, rely=0.299, relheight=0.493
                , relwidth=0.871)
        self.duration.configure(activebackground="beige")
        self.duration.configure(command=motionapp_gui_support.simulation_changed)
        self.duration.configure(label="Duration")
        self.duration.configure(length="314")
        self.duration.configure(orient="horizontal")
        self.duration.configure(troughcolor="#d9d9d9")
        self.duration.configure(variable=self.animation_duration)

        self.TLabelframe7 = ttk.Labelframe(self.TNotebook1_t3)
        self.TLabelframe7.place(relx=0.047, rely=0.435, relheight=0.372
                , relwidth=0.88)
        self.TLabelframe7.configure(relief='')
        self.TLabelframe7.configure(text='''Dead reckoning''')

        self.interval =  tk.Scale(self.TLabelframe7, from_=0.0, to=1.0, resolution=0.1)
        self.interval.place(relx=0.056, rely=0.344, relheight=0.461
                , relwidth=0.871)
        self.interval.configure(activebackground="beige")
        self.interval.configure(command=motionapp_gui_support.simulation_changed)
        self.interval.configure(label="Interval")
        self.interval.configure(length="314")
        self.interval.configure(orient="horizontal")
        self.interval.configure(troughcolor="#d9d9d9")
        self.interval.configure(variable=self.dead_reckoning_interval)

        self.TLabelframe3 = ttk.Labelframe(self.top)
        self.TLabelframe3.place(relx=0.543, rely=0.707, relheight=0.24
                , relwidth=0.436)
        self.TLabelframe3.configure(relief='')
        self.TLabelframe3.configure(text='''Actual and Dead reckoned Position''')

        self.Label1 = tk.Label(self.TLabelframe3)
        self.Label1.place(relx=0.033, rely=0.278, height=24, width=102
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(compound='left')
        self.Label1.configure(text='''X:''')

        self.Label2 = tk.Label(self.TLabelframe3)
        self.Label2.place(relx=0.036, rely=0.42, height=24, width=103
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(compound='left')
        self.Label2.configure(text='''Y:''')

        self.Label3 = tk.Label(self.TLabelframe3)
        self.Label3.place(relx=0.033, rely=0.568, height=23, width=103
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(compound='left')
        self.Label3.configure(text='''Theta:''')

        self.Label4 = tk.Label(self.TLabelframe3)
        self.Label4.place(relx=0.033, rely=0.71, height=23, width=102
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(anchor='w')
        self.Label4.configure(compound='left')
        self.Label4.configure(text='''Final Vel L/R:''')

        self.Label5 = tk.Label(self.TLabelframe3)
        self.Label5.place(relx=0.379, rely=0.123, height=24, width=51
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(anchor='w')
        self.Label5.configure(compound='left')
        self.Label5.configure(text='''Actual''')

        self.Label6 = tk.Label(self.TLabelframe3)
        self.Label6.place(relx=0.609, rely=0.123, height=23, width=61
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(anchor='w')
        self.Label6.configure(compound='left')
        self.Label6.configure(text='''DR (Err)''')

        self.Label7 = tk.Label(self.TLabelframe3)
        self.Label7.place(relx=0.803, rely=0.123, height=23, width=72
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(anchor='w')
        self.Label7.configure(compound='left')
        self.Label7.configure(text='''DR2 (Err)''')

        self.x_actual = tk.Entry(self.TLabelframe3)
        self.x_actual.place(relx=0.365, rely=0.278, height=20, relwidth=0.18
                , bordermode='ignore')
        self.x_actual.configure(background="white")
        self.x_actual.configure(font="TkFixedFont")
        self.x_actual.configure(selectbackground="#c4c4c4")
        self.x_actual.configure(state='disabled')

        self.y_actual = tk.Entry(self.TLabelframe3)
        self.y_actual.place(relx=0.365, rely=0.42, height=20, relwidth=0.18
                , bordermode='ignore')
        self.y_actual.configure(background="white")
        self.y_actual.configure(font="TkFixedFont")
        self.y_actual.configure(selectbackground="#c4c4c4")
        self.y_actual.configure(state='disabled')

        self.theta_actual = tk.Entry(self.TLabelframe3)
        self.theta_actual.place(relx=0.365, rely=0.568, height=20, relwidth=0.18
                , bordermode='ignore')
        self.theta_actual.configure(background="white")
        self.theta_actual.configure(font="TkFixedFont")
        self.theta_actual.configure(selectbackground="#c4c4c4")
        self.theta_actual.configure(state='disabled')

        self.v_final_left = tk.Entry(self.TLabelframe3)
        self.v_final_left.place(relx=0.365, rely=0.71, height=20, relwidth=0.18
                , bordermode='ignore')
        self.v_final_left.configure(background="white")
        self.v_final_left.configure(font="TkFixedFont")
        self.v_final_left.configure(selectbackground="#c4c4c4")
        self.v_final_left.configure(state='disabled')

        self.x_dr = tk.Entry(self.TLabelframe3)
        self.x_dr.place(relx=0.581, rely=0.278, height=20, relwidth=0.18
                , bordermode='ignore')
        self.x_dr.configure(background="white")
        self.x_dr.configure(font="TkFixedFont")
        self.x_dr.configure(selectbackground="#c4c4c4")
        self.x_dr.configure(state='disabled')

        self.y_dr = tk.Entry(self.TLabelframe3)
        self.y_dr.place(relx=0.581, rely=0.42, height=20, relwidth=0.18
                , bordermode='ignore')
        self.y_dr.configure(background="white")
        self.y_dr.configure(font="TkFixedFont")
        self.y_dr.configure(selectbackground="#c4c4c4")
        self.y_dr.configure(state='disabled')

        self.theta_dr = tk.Entry(self.TLabelframe3)
        self.theta_dr.place(relx=0.581, rely=0.556, height=20, relwidth=0.18
                , bordermode='ignore')
        self.theta_dr.configure(background="white")
        self.theta_dr.configure(font="TkFixedFont")
        self.theta_dr.configure(selectbackground="#c4c4c4")
        self.theta_dr.configure(state='disabled')

        self.v_final_right = tk.Entry(self.TLabelframe3)
        self.v_final_right.place(relx=0.581, rely=0.71, height=20, relwidth=0.18
                , bordermode='ignore')
        self.v_final_right.configure(background="white")
        self.v_final_right.configure(font="TkFixedFont")
        self.v_final_right.configure(selectbackground="#c4c4c4")
        self.v_final_right.configure(state='disabled')

        self.x_dr2 = tk.Entry(self.TLabelframe3)
        self.x_dr2.place(relx=0.806, rely=0.278, height=20, relwidth=0.18
                , bordermode='ignore')
        self.x_dr2.configure(background="white")
        self.x_dr2.configure(font="TkFixedFont")
        self.x_dr2.configure(selectbackground="#c4c4c4")
        self.x_dr2.configure(state='disabled')

        self.y_dr2 = tk.Entry(self.TLabelframe3)
        self.y_dr2.place(relx=0.806, rely=0.42, height=20, relwidth=0.18
                , bordermode='ignore')
        self.y_dr2.configure(background="white")
        self.y_dr2.configure(font="TkFixedFont")
        self.y_dr2.configure(selectbackground="#c4c4c4")
        self.y_dr2.configure(state='disabled')

        self.theta_dr2 = tk.Entry(self.TLabelframe3)
        self.theta_dr2.place(relx=0.806, rely=0.556, height=20, relwidth=0.18
                , bordermode='ignore')
        self.theta_dr2.configure(background="white")
        self.theta_dr2.configure(font="TkFixedFont")
        self.theta_dr2.configure(selectbackground="#c4c4c4")
        self.theta_dr2.configure(state='disabled')

def start_up():
    motionapp_gui_support.main()

if __name__ == '__main__':
    motionapp_gui_support.main()



