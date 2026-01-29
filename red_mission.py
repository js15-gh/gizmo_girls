import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)
    gizmo.reset_defaults()

    gizmo.change_speed(400)#300
    gizmo.go_forward(6.1)
    gizmo.turn_right_degrees(42)
    gizmo.go_forward(11.57)#removed the "false" so instead drive forwards first before lifting
    gizmo.go_reverse(18.5) #20
    gizmo.turn_left_degrees(16.67)#22
    # gizmo.go_reverse(6)
    gizmo.wait(900)
    # gizmo.go_forward(19)
    # gizmo.turn_right_degrees(17)
    gizmo.go_forward(24.5)
    gizmo.go_reverse(30)
    gizmo.wait(1000)
    gizmo.change_turn_speed(50)
    gizmo.change_turn_speed(50)
    gizmo.turn_right_degrees(105)
    gizmo.go_forward(30)
    gizmo.turn_left_degrees(47)
    gizmo.go_forward(21.5)
    gizmo.go_reverse(2)


    # gizmo.change_speed(200)#300
    # gizmo.go_forward(6.2)
    # gizmo.turn_right_degrees(37)
    # gizmo.go_forward(11.5) #12.25
    # gizmo.d_turn_angle(-300,300)
    # gizmo.change_speed(200)
    # gizmo.turn_left_degrees(10.5)#10
    # gizmo.turn_right_degrees(25)#30
    # gizmo.d_turn_angle(40,99)#
    # gizmo.wait(0.5)#1
    # gizmo.change_speed(300)
    # gizmo.d_turn_angle(40,99)#
    # gizmo.wait(0.5)#1
    # gizmo.change_speed(300)#200
    # #gizmo.d_turn_angle(300,180,False) #100
    # gizmo.d_turn_angle(300,160,False) #180
    # gizmo.go_forward(3)#2.5
    # gizmo.turn_right_degrees(10)
    # gizmo.change_speed(300)#500
    # gizmo.go_reverse(12)
    # gizmo.wait(30)
    # gizmo.go_forward(19)
    # #gizmo.turn_right_degrees(42)
    # gizmo.turn_right_degrees(41)
    # gizmo.go_forward(7.67)
    # gizmo.go_reverse(7)
#2) Bring items to forum
    # gizmo.change_speed(250)
    # gizmo.go_forward(19)
    # gizmo.go_reverse(9.9) #10.5
    # gizmo.change_speed(500)
    # gizmo.turn_right_degrees(45)
    # gizmo.go_forward(19.7)#18.5
    # gizmo.c_turn_angle(300,330)
    # gizmo.change_speed(200)
    # gizmo.turn_left_degrees(26) #28
    # gizmo.c_turn_angle(100,-100)
    # gizmo.go_reverse(30)
    # gizmo.wait_for_reflection(14)
    # gizmo.wait(200)
    # gizmo.go_forward(1.2)
    # gizmo.turn_right_degrees(102)
    # gizmo.go_forward(6)
    # gizmo.change_speed(500)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.turn_right_degrees(50)
    # gizmo.turn_left_degrees(50)
    # gizmo.go_reverse(6)
    # gizmo.turn_left_degrees(100)
    # gizmo.change_speed(500)
    # gizmo.go_reverse(36.7)



# --- RUN THE MAIN PROGRAM ---
#main_program())#1