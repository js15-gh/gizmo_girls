import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(10)
    gizmo.turn_left_degrees(91)
    gizmo.wait_for_reflection_pick_speed(14,400)
    gizmo.go_reverse(4.67)
    gizmo.turn_left_degrees(86)
    gizmo.go_forward(6.6)
    gizmo.turn_left_degrees(28)
    gizmo.d_turn_angle(2000, 950)
    gizmo.go_reverse(11.5)
    gizmo.change_speed(500)
    gizmo.go_forward(5)
    gizmo.turn_right_degrees(145)
    gizmo.go_forward(7.76)
    gizmo.turn_left_degrees(85)
    gizmo.go_forward(30)