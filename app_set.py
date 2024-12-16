from guizero import App, PushButton, Box, Text, CheckBox
#import gpiozero as gpio
from time import sleep

procedure_completed = False
stepper_running = False
stepper_dir = True
spindle_on = False
spindle_dir = True
upper_limit = False
lower_limit = False
bed_in_place = True

def stepper_move():
    #set dir pin
    while stepper_running and upper_limit and lower_limit:
        #pulse on
        sleep(0.001)
        #pulse off
        sleep(0.001)

def spindle_start():
    
    if upper_limit == False and lower_limit == False and bed_in_place == True:
        spindle_toggle_button.text =  "Spindle On"
        spindle_toggle_button.bg =  "light green"
        #set spindle on
        spindle_toggle_button.when_clicked =  spindle_stop
        
    else:
        setup.info("info","conditions not met")
        #highlight which error is present

def spindle_stop():
    spindle_toggle_button.text =  "Spindle Off"
    spindle_toggle_button.bg =  "pink"
    #set spindle off
    spindle_toggle_button.when_clicked =  spindle_start
    
def spindle_forward():
    spindle_dir_button.text = "spindle forward"
    spindle_dir_button.bg = "light green"
    #set spindle direction to forward
    spindle_dir_button.when_clicked = spindle_reverse
    down_button.enable()

def spindle_reverse():
    spindle_dir_button.text = "spindle reverse"
    spindle_dir_button.bg = "pink"
    #set spindle direction to reverse
    spindle_dir_button.when_clicked = spindle_forward
    down_button.disable()

def bed_drill():
    #set bed to drill
    #when confirmed proceed
    bed_toggle_button.bg = "green"
    bed_toggle_button.text = "Ready to drill"
    bed_toggle_button.when_clicked = bed_out
    down_button.enable()
    up_button.enable()

def bed_out():
    #set bed to out
    bed_toggle_button.bg = "pink"
    bed_toggle_button.text = "Bed Out"
    bed_toggle_button.when_clicked = bed_drill
    down_button.disable()
    up_button.disable()

def exit_setup():
    exit()
    
def goto_auto():
    if procedure_completed:#and no records found
        #Start Auto App
        exit()
    else:
        setup.info("info","No Stored movement limits to start auto procedure")

setup = App( title = "Setup Mode", bg = "light blue" )
#title Area
title_box = Box( setup, align = "top", width = "fill", height = 60, border = True ,layout ="grid" )
before_title = Box( title_box, grid = [0,0,5,1], height = 10 )
Auto_button = PushButton( title_box, text = "Goto Auto", grid = [0,1])
Auto_button.when_clicked = goto_auto
spacer_title = Box( title_box, grid = [1,1], width = 500)
title = Text(title_box , grid = [2,1], text = "Setup process", size = 20 )
spacer_exit_button = Box( title_box, width = 550, grid =[3,1])
exit_button = PushButton( title_box, text = "Exit", grid =[4,1] )
exit_button.when_clicked = exit_setup

#Vertical Motion Area
stepper_box = Box (setup, align = "right", height = "fill", border = True, width = 200)
spacer_stepper_box_start = Box(stepper_box, align = "top", height = 20 )
title_spindle_box = Text(stepper_box, align = "top", text = "Vertical Motion", size = 16 )

under_title_box = Box(stepper_box, align = "top", height = 40 )
current_dist_title = Text(stepper_box, align = "top", width = "fill", text = "Current distance", size = 14)
spacer_after_dist_title = Box(stepper_box, align = "top", height = 20 )
current_dist_text = Text(stepper_box, align = "top", width = "fill", text = "0.00", size = 12)
spacer_current_dist = Box(stepper_box, align = "top", height = 40 )

Upper_limit_text = Text(stepper_box, align = "top", width = "fill", text = "Upper limit", size = 14)
spacer_ul_text = Box(stepper_box, align = "top", height = 20 )
upper_limit_num = Text(stepper_box, align = "top", width = "fill", text = "0.00", size = 12)
spacer_ul = Box(stepper_box, align = "top", height = 40 )

LL_text = Text(stepper_box, align = "top", width = "fill", text = "Lower limit", size = 14)
spacer_ll_text = Box(stepper_box, align = "top", height = 20 )
lower_limit_num = Text(stepper_box, align = "top", width = "fill", text = "0.00", size = 12)
spacer_ll = Box(stepper_box, align = "top", height = 40 )

spacer_before_up = Box(stepper_box, align = "top", height = 20 )
up_button = PushButton ( stepper_box, text = "Go up", align = "top" ,width = "fill", padx = 20 )
spacer_before_down = Box(stepper_box, align = "top", height = 20 )
down_button = PushButton( stepper_box, text = "Go down", align ="top", width = "fill" )

# Spindle and bed control area
control_box = Box ( setup, align = "right", height = "fill", width =250 )
# Spindle Area
spindle_box = Box (control_box, align = "top", width = "fill", border = True )
spacer_spindle_box_start = Box ( spindle_box, align = "top", width = "fill", height = 20 )
spindle_title = Text( spindle_box , align ="top", text = "Spindle Control", size = 16 )
spacer_spindle_button = Box (spindle_box, align = "top", width = "fill", height = 20)

spindle_toggle_button = PushButton (spindle_box, align = "top", text = "Failed LOading")
spindle_stop()

spacer_spindle_dir_button = Box (spindle_box, align = "top", width = "fill", height = 20)

spindle_dir_button = PushButton (spindle_box, align = "top", text = "Loading failed")
spindle_forward()

spacer_spindle_box_end = Box (spindle_box, align = "top", width = "fill", height = 20)

# Bed Area
bed_box = Box (control_box, align = "top", width = "fill", border = True )
spacer_bed_box_start = Box ( bed_box, align = "top", width = "fill", height = 20 )
bed_title = Text( bed_box , align ="top", text = "Drillling Bed Control", size = 16 )
spacer_bed_toggle_start = Box ( bed_box, align = "top", width = "fill", height = 20 )

bed_toggle_button = PushButton (bed_box, align = "top", text = "Failed Loading")
bed_drill()

spacer_status_check = Box ( bed_box, align = "top", width = "fill", height = 20 )
bed_title = Text( bed_box , align ="top", text = "Locking check", size = 14 )
spacer_confirm_check =  Box ( bed_box, align = "top", width = "fill", height = 20 )
bed_title = Text( bed_box , align ="top", text = "Yes", size = 12 )
spacer_bed_box_end = Box ( bed_box, align = "top", width = "fill", height = 20 )
#set Area
set_box = Box ( control_box, align = "top", width = "fill", height = 200, border = True )
spacer_set_box = Box ( set_box, align = "top", width = "fill", height = 50 )
set_button = PushButton ( set_box, align = "top", text = "SET", pady = 20, padx = 60 )
set_button.text_size = 20
set_button.bg = "yellow"
spacer_set_button = Box ( set_box, align = "top", width = "fill", height = 50 )

#Setup Area
setup_box = Box ( setup, align = "left", height = "fill", width = 300, border = True )
spacer_setup_box = Box ( setup_box, align = "top", height = 20, width = "fill" )
setup_button = PushButton ( setup_box, align = "top", text = "Start Setup" )
setup_button.bg = "light green"
setup_button.text_size = 16
spacer_setup_button = Box ( setup_box, align = "top", height = 20, width = "fill" )

#Steps_area
Steps_box = Box ( setup, align = "right", width = "fill", height = "fill", enabled = False )
sub_steps_box_1 = Box ( Steps_box, align = "top", width = "fill", height = 60 )
checkbox_1 = CheckBox ( sub_steps_box_1, align = "left", text = "Started Procedure" )
checkbox_1.text_size = 16
sub_steps_box_2 = Box ( Steps_box, align = "top", width = "fill", height = 60 )
checkbox_2 = CheckBox ( sub_steps_box_2, align = "left", text = "Reaching Upper Limit Switch" )
checkbox_2.text_size = 16
sub_steps_box_3 = Box ( Steps_box, align = "top", width = "fill", height = 60 )
checkbox_3 = CheckBox ( sub_steps_box_3, align = "left", text = "Setting drilling limit" )
checkbox_3.text_size = 16
sub_steps_box_4 = Box ( Steps_box, align = "top", width = "fill", height = 60 )
checkbox_4 = CheckBox ( sub_steps_box_4, align = "left", text = "Setting pseudo upper limit" )
checkbox_4.text_size = 16
sub_steps_box_5 = Box ( Steps_box, align = "top", width = "fill", height = 60 )
checkbox_5 = CheckBox ( sub_steps_box_5, align = "left", text = "Procedure successfully completed" )
checkbox_5.text_size = 16


setup.set_full_screen()
setup.display()
