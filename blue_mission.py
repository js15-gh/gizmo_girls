import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(47)
    gizmo.go_forward(8.7)
    gizmo.d_turn_angle(300, 220)
    gizmo.go_reverse(4.5)
    gizmo.d_turn_angle(-300, 220)
    gizmo.go_reverse(2.9)
    gizmo.d_turn_angle(300, 200)
    gizmo.turn_left_degrees(50)
    gizmo.d_turn_angle(-300, 200)
    gizmo.go_forward(15.5)
    gizmo.turn_right_degrees(80)
    gizmo.go_forward(2.8)
    gizmo.d_turn_angle_back2zero(400, 200)
    gizmo.go_reverse(3)
    gizmo.turn_left_degrees(83)
    gizmo.go_forward(12)


main_program()