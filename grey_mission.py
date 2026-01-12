import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_reverse(7.5)
    gizmo.go_forward(37)
    gizmo.wait_for_reflection_pick_speed(14,400)
    gizmo.go_reverse(5.3) #4.8
    gizmo.turn_left_degrees(86)
    gizmo.go_forward(6.8)
    gizmo.turn_left_degrees(31.5)
    gizmo.d_turn_angle(2000, 950)
    gizmo.go_reverse(12.2)
    gizmo.change_speed(500)
    gizmo.go_forward(5)
    gizmo.turn_right_degrees(116)
    gizmo.go_forward(9.85)
    gizmo.change_turn_speed(52)
    gizmo.turn_left_degrees(29)
    gizmo.change_speed(500)
    gizmo.go_forward(39)
