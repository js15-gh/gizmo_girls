import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)
    gizmo.reset_defaults()

    # gizmo.change_speed(400)#300
    # gizmo.go_forward(6.1)
    # gizmo.turn_right_degrees(42)
    # gizmo.go_forward(11.57)#removed the "false" so instead drive forwards first before lifting
    # gizmo.go_reverse(18.5) #20
    # gizmo.turn_left_degrees(23.67)#22
    # # gizmo.go_reverse(6)
    # gizmo.wait(900)
    # # gizmo.go_forward(19)
    # # gizmo.turn_right_degrees(17)
    # gizmo.go_forward(24.5)
    # gizmo.go_reverse(25)
    # gizmo.wait(1000)
    # gizmo.change_turn_speed(50)
    # gizmo.change_turn_speed(50)
    # gizmo.turn_right_degrees(60)
    # gizmo.go_forward(30)
    # gizmo.turn_left_degrees(37)
    # gizmo.go_forward(21.5)
    # gizmo.go_reverse(2)

    gizmo.change_speed(300)
    gizmo.go_forward(15)
    gizmo.c_turn_angle(234,280)
    gizmo.c_turn_angle(100,60)
    gizmo.wait(240)
    gizmo.c_turn_angle(400,-340)
    gizmo.go_reverse(10)
    gizmo.turn_right_degrees(44)
    gizmo.go_forward(27)
    gizmo.turn_right_degrees(25)
    gizmo.go_forward(38)
# --- RUN THE MAIN PROGRAM ---
#main_program())#1