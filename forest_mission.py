import gizmo

def main_program():
    gizmo.reset_defaults

    gizmo.change_speed(200)
    gizmo.go_forward(29)
    gizmo.change_turn_speed(50)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(14.5)
    gizmo.d_turn_angle(200,67)
    gizmo.turn_right_degrees(90)
    gizmo.go_forward(6.5)
    gizmo.d_turn_angle(200,-70)
    gizmo.go_reverse(5.5)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(15)
    gizmo.turn_left_degrees(45)
    gizmo.go_forward(10)
    gizmo.turn_left_degrees(45) 
    gizmo.go_forward(3)
    gizmo.d_turn_angle(200,200)

