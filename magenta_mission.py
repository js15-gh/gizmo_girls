import gizmo


def main_program():
    gizmo.reset_defaults()
    gizmo.change_speed(300)
    # gizmo.go_reverse(8)
    gizmo.go_forward(35)
    gizmo.wait(300)
    gizmo.change_turn_speed(150)
    gizmo.turn_right_degrees(57) #68 before attachment makeover
    gizmo.change_turn_speed(300)
    gizmo.go_forward(8.6)
    # gizmo.d_turn_angle(850, 1300)
    # gizmo.stally
    gizmo.go_reverse(8.6)
    gizmo.turn_left_degrees(42)
    gizmo.go_reverse(33)