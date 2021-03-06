#############################################################################
# Generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#  Jul 06, 2022 03:23:35 PM CEST  platform: Darwin
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 969x675+932+319
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2545 1388
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "MotionApp"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 607 -highlightcolor red -width 491 
    vTcl:DefineAlias "$top.fra46" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    vTcl::widgets::ttk::custom::CreateCmd $site_3_0.cus47 \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$site_3_0.cus47" "FloatCanvas" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.cus47 \
        -in $site_3_0 -x 0 -relx 0.004 -y 0 -rely 0.003 -width 0 \
        -relwidth 0.99 -height 0 -relheight 0.992 -anchor nw \
        -bordermode ignore 
    ttk::style configure TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style map TNotebook.Tab -background [list selected $vTcl(actual_gui_bg) active $vTcl(tabbg1) !active $vTcl(tabbg2)]
    ttk::style map TNotebook.Tab -foreground [list selected $vTcl(actual_gui_fg) active $vTcl(tabfg1) !active $vTcl(tabfg2)]
    ttk::notebook $top.tNo46 \
        -width 424 -height 439 -takefocus {} 
    vTcl:DefineAlias "$top.tNo46" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.tNo46.t0 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo46.t0" "TNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo46 add $top.tNo46.t0 \
        -padding 0 -sticky nsew -state normal -text Robot -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo46.t0
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tLa46 \
        -text {Original Position} -width 389 -height 257 
    vTcl:DefineAlias "$site_4_0.tLa46" "TLabelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.tLa46
    scale $site_5_0.sca48 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command original_position_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -10.0 -highlightcolor black \
        -label X -length 350 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 10.0 -troughcolor #d9d9d9 -variable x_pos_org 
    vTcl:DefineAlias "$site_5_0.sca48" "x_pos" vTcl:WidgetProc "Toplevel1" 1
    scale $site_5_0.sca49 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command original_position_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -10.0 -highlightcolor black \
        -label Y -length 347 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 10.0 -troughcolor #d9d9d9 -variable y_pos_org 
    vTcl:DefineAlias "$site_5_0.sca49" "y_pos" vTcl:WidgetProc "Toplevel1" 1
    scale $site_5_0.sca50 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command original_position_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -180.0 -highlightcolor black \
        -label Theta -length 349 -orient horizontal -resolution 1.0 \
        -tickinterval 0.0 -to 180.0 -troughcolor #d9d9d9 -variable theta_org 
    vTcl:DefineAlias "$site_5_0.sca50" "theta" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca48 \
        -in $site_5_0 -x 0 -relx 0.029 -y 0 -rely 0.091 -width 0 \
        -relwidth 0.931 -height 85 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.sca49 \
        -in $site_5_0 -x 0 -relx 0.029 -y 0 -rely 0.366 -width 0 \
        -relwidth 0.923 -height 85 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.sca50 \
        -in $site_5_0 -x 0 -relx 0.029 -y 0 -rely 0.638 -width 0 \
        -relwidth 0.928 -height 85 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_0.tLa47 \
        -text {Body Settings} -width 391 -height 119 
    vTcl:DefineAlias "$site_4_0.tLa47" "TLabelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_0.tLa47
    scale $site_5_0.sca46 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command body_width_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from 0.1 -highlightcolor black \
        -label Width -length 346 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 2.5000000000000004 -troughcolor #d9d9d9 \
        -variable body_width 
    vTcl:DefineAlias "$site_5_0.sca46" "body_width" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca46 \
        -in $site_5_0 -x 0 -relx 0.029 -y 0 -rely 0.223 -width 0 \
        -relwidth 0.918 -height 74 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tLa46 \
        -in $site_4_0 -x 0 -relx 0.05 -y 0 -rely 0.027 -width 0 \
        -relwidth 0.917 -height 0 -relheight 0.621 -anchor nw \
        -bordermode ignore 
    place $site_4_0.tLa47 \
        -in $site_4_0 -x 0 -relx 0.052 -y 0 -rely 0.686 -width 0 \
        -relwidth 0.922 -height 0 -relheight 0.287 -anchor nw \
        -bordermode ignore 
    frame $top.tNo46.t1 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo46.t1" "TNotebook1_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo46 add $top.tNo46.t1 \
        -padding 0 -sticky nsew -state normal -text Speed -image {} \
        -compound left -underline -1 
    set site_4_1  $top.tNo46.t1
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_1.tLa46 \
        -text Velocities -width 360 -height 185 
    vTcl:DefineAlias "$site_4_1.tLa46" "TLabelframe4" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.tLa46
    scale $site_5_0.sca49 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command velocity_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -5.0 -highlightcolor black \
        -label Right -length 304 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 5.0 -troughcolor #d9d9d9 \
        -variable velocity_right 
    vTcl:DefineAlias "$site_5_0.sca49" "v_right" vTcl:WidgetProc "Toplevel1" 1
    scale $site_5_0.sca50 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command velocity_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -5.0 -highlightcolor black \
        -label Left -length 314 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 5.0 -troughcolor #d9d9d9 \
        -variable velocity_left 
    vTcl:DefineAlias "$site_5_0.sca50" "Scale1_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca49 \
        -in $site_5_0 -x 0 -relx 0.056 -y 0 -rely 0.108 -width 0 \
        -relwidth 0.872 -height 81 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.sca50 \
        -in $site_5_0 -x 0 -relx 0.056 -y 0 -rely 0.432 -width 0 \
        -relwidth 0.872 -height 81 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_1.tLa47 \
        -text Accelerations -width 360 -height 165 
    vTcl:DefineAlias "$site_4_1.tLa47" "TLabelframe5" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_1.tLa47
    scale $site_5_0.sca51 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command acceleration_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -1.0 -highlightcolor black \
        -label Right -length 314 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 1.0 -troughcolor #d9d9d9 \
        -variable acceleration_right 
    vTcl:DefineAlias "$site_5_0.sca51" "a_right" vTcl:WidgetProc "Toplevel1" 1
    scale $site_5_0.sca52 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command acceleration_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from -1.0 -highlightcolor black \
        -label Left -length 314 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 1.0 -troughcolor #d9d9d9 \
        -variable acceleration_left 
    vTcl:DefineAlias "$site_5_0.sca52" "a_left" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca51 \
        -in $site_5_0 -x 0 -relx 0.054 -y 0 -rely 0.114 -width 0 \
        -relwidth 0.871 -height 81 -relheight 0 -anchor nw -bordermode ignore 
    place $site_5_0.sca52 \
        -in $site_5_0 -x 0 -relx 0.056 -y 0 -rely 0.485 -width 0 \
        -relwidth 0.872 -height 81 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_1.tLa46 \
        -in $site_4_1 -x 0 -relx 0.049 -y 0 -rely 0.039 -width 0 \
        -relwidth 0.88 -height 0 -relheight 0.476 -anchor nw \
        -bordermode ignore 
    place $site_4_1.tLa47 \
        -in $site_4_1 -x 0 -relx 0.049 -y 0 -rely 0.54 -width 0 \
        -relwidth 0.88 -height 0 -relheight 0.424 -anchor nw \
        -bordermode ignore 
    frame $top.tNo46.t2 \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.tNo46.t2" "TNotebook1_t3" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo46 add $top.tNo46.t2 \
        -padding 0 -sticky nsew -state normal -text Timing -image {} \
        -compound left -underline -1 
    set site_4_2  $top.tNo46.t2
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_2.tLa46 \
        -text Simulation -width 360 -height 135 
    vTcl:DefineAlias "$site_4_2.tLa46" "TLabelframe6" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_2.tLa46
    scale $site_5_0.sca49 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command simulation_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from 0.0 -highlightcolor black \
        -label Duration -length 314 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 30.0 -troughcolor #d9d9d9 \
        -variable animation_duration 
    vTcl:DefineAlias "$site_5_0.sca49" "duration" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca49 \
        -in $site_5_0 -x 0 -relx 0.056 -y 0 -rely 0.296 -width 0 \
        -relwidth 0.872 -height 71 -relheight 0 -anchor nw -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $site_4_2.tLa47 \
        -text {Dead reckoning} -width 360 -height 145 
    vTcl:DefineAlias "$site_4_2.tLa47" "TLabelframe7" vTcl:WidgetProc "Toplevel1" 1
    set site_5_0 $site_4_2.tLa47
    scale $site_5_0.sca48 \
        -activebackground $vTcl(analog_color_m) \
        -background $vTcl(actual_gui_bg) -bigincrement 0.0 \
        -command simulation_changed -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -from 0.1 -highlightcolor black \
        -label Interval -length 314 -orient horizontal -resolution 0.1 \
        -tickinterval 0.0 -to 1.0 -troughcolor #d9d9d9 \
        -variable dead_reckoning_interval 
    vTcl:DefineAlias "$site_5_0.sca48" "interval" vTcl:WidgetProc "Toplevel1" 1
    place $site_5_0.sca48 \
        -in $site_5_0 -x 0 -relx 0.056 -y 0 -rely 0.345 -width 0 \
        -relwidth 0.872 -height 71 -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_2.tLa46 \
        -in $site_4_2 -x 0 -relx 0.047 -y 0 -rely 0.048 -width 0 \
        -relwidth 0.88 -height 0 -relheight 0.348 -anchor nw \
        -bordermode ignore 
    place $site_4_2.tLa47 \
        -in $site_4_2 -x 0 -relx 0.047 -y 0 -rely 0.435 -width 0 \
        -relwidth 0.88 -height 0 -relheight 0.372 -anchor nw \
        -bordermode ignore 
    ttk::style configure TLabelframe.Label -background $vTcl(actual_gui_bg)
    ttk::style configure TLabelframe.Label -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabelframe.Label -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TLabelframe -background $vTcl(actual_gui_bg)
    ttk::labelframe $top.tLa46 \
        -text {Actual and Dead reckoned Position (DR2 uses mean Theta)} \
        -width 411 -height 157 
    vTcl:DefineAlias "$top.tLa46" "TLabelframe3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.tLa46
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text X: 
    vTcl:DefineAlias "$site_3_0.lab47" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Y: 
    vTcl:DefineAlias "$site_3_0.lab48" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Theta: 
    vTcl:DefineAlias "$site_3_0.lab49" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Final Vel L/R:} 
    vTcl:DefineAlias "$site_3_0.lab50" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab51 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Actual 
    vTcl:DefineAlias "$site_3_0.lab51" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {DR (Err)} 
    vTcl:DefineAlias "$site_3_0.lab52" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {DR2 (Err)} 
    vTcl:DefineAlias "$site_3_0.lab53" "Label7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab46 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable x_actual 
    vTcl:DefineAlias "$site_3_0.lab46" "lbl_x_actual" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable y_actual 
    vTcl:DefineAlias "$site_3_0.lab54" "lbl_y_actual" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable theta_actual 
    vTcl:DefineAlias "$site_3_0.lab55" "lbl_theta_actual" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable v_final_left 
    vTcl:DefineAlias "$site_3_0.lab56" "lbl_v_final_left" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable v_final_right 
    vTcl:DefineAlias "$site_3_0.lab57" "lbl_v_final_right" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab58 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable x_dr 
    vTcl:DefineAlias "$site_3_0.lab58" "lbl_x_dr" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab59 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable y_dr 
    vTcl:DefineAlias "$site_3_0.lab59" "lbl_y_dr" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab60 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable theta_dr 
    vTcl:DefineAlias "$site_3_0.lab60" "lbl_theta_dr" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab61 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable x_drm 
    vTcl:DefineAlias "$site_3_0.lab61" "lbl_x_drm" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab62 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable y_drm 
    vTcl:DefineAlias "$site_3_0.lab62" "lbl_y_drm" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab63 \
        -activebackground #f9f9f9 -activeforeground #000000 -anchor w \
        -background $vTcl(actual_gui_bg) -compound left -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -relief sunken \
        -text 0.0 -textvariable theta_drm 
    vTcl:DefineAlias "$site_3_0.lab63" "lbl_theta_drm" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.033 -y 0 -rely 0.278 -width 0 \
        -relwidth 0.242 -height 0 -relheight 0.148 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.036 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.244 -height 0 -relheight 0.148 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.033 -y 0 -rely 0.568 -width 0 \
        -relwidth 0.244 -height 0 -relheight 0.142 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.033 -y 0 -rely 0.71 -width 0 \
        -relwidth 0.242 -height 0 -relheight 0.142 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.379 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.121 -height 0 -relheight 0.148 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.569 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.145 -height 0 -relheight 0.142 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.791 -y 0 -rely 0.123 -width 0 \
        -relwidth 0.171 -height 0 -relheight 0.142 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab46 \
        -in $site_3_0 -x 0 -relx 0.379 -y 0 -rely 0.278 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.379 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.379 -y 0 -rely 0.568 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.379 -y 0 -rely 0.71 -width 0 \
        -relwidth 0.118 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.527 -y 0 -rely 0.71 -width 0 \
        -relwidth 0.117 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 0 -relx 0.527 -y 0 -rely 0.278 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 0 -relx 0.527 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 0 -relx 0.527 -y 0 -rely 0.568 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.761 -y 0 -rely 0.278 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.761 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.761 -y 0 -rely 0.568 -width 0 \
        -relwidth 0.199 -height 0 -relheight 0.123 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 0 -relx 0.031 -y 0 -rely 0.044 -width 0 -relwidth 0.495 \
        -height 0 -relheight 0.899 -anchor nw -bordermode ignore 
    place $top.tNo46 \
        -in $top -x 0 -relx 0.543 -y 0 -rely 0.046 -width 0 -relwidth 0.439 \
        -height 0 -relheight 0.65 -anchor nw -bordermode ignore 
    place $top.tLa46 \
        -in $top -x 0 -relx 0.543 -y 0 -rely 0.708 -width 0 -relwidth 0.441 \
        -height 0 -relheight 0.24 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}
proc original_position_changed {args} { }
proc original_position_changed {args} { }
proc original_position_changed {args} { }
proc body_width_changed {args} { }
proc velocity_changed {args} { }
proc velocity_changed {args} { }
proc acceleration_changed {args} { }
proc acceleration_changed {args} { }
proc simulation_changed {args} { }
proc simulation_changed {args} { }

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

