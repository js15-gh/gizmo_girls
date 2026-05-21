import gizmo

def main_program():
    gizmo.reset_defaults

    gizmo.change_speed(200)
    gizmo.go_forward(26.5)
    gizmo.change_turn_speed(50)
    gizmo.turn_left_degrees(80)
    gizmo.go_forward(19)
    # gizmo.d_turn_angle(200,67)
    gizmo.turn_right_degrees(80)
    # gizmo.go_forward(6.5)
    gizmo.d_turn_angle(200,147)
    # gizmo.go_reverse(5.5)
    # gizmo.turn_left_degrees(90)
    gizmo.go_forward(2.3)
    gizmo.d_turn_angle(200,-140)
    gizmo.stally
    # gizmo.go_reverse(2)
    # gizmo.turn_left_degrees(35)
    # gizmo.go_forward(1.4)
    gizmo.go_reverse(3.9)
    gizmo.turn_left_degrees(90) 
    gizmo.go_forward(6)
    gizmo.turn_left_degrees(45)
    gizmo.go_forward(6.15)
    gizmo.turn_right_degrees(9)
    gizmo.stally
    gizmo.go_forward(0.1)
    gizmo.stally
    gizmo.c_turn_angle(1000, 700)
    gizmo.go_reverse(0.5)
    gizmo.c_turn_angle(1000, 150)

