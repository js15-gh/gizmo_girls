import gizmo


def main_program():
    gizmo.reset_defaults()
    gizmo.change_speed(500)
    # gizmo.go_reverse(8)
    gizmo.go_forward(33.5)
    gizmo.wait(300)
    gizmo.change_turn_speed(150)
    gizmo.change_turn_speed(50)
    gizmo.turn_right_degrees(57) #68 before attachment makeover
    gizmo.change_turn_speed(300)
    gizmo.go_forward(14)
    # gizmo.d_turn_angle(850, 1300)
    # gizmo.stally
    gizmo.go_reverse(8.6)
    gizmo.change_speed(500)
    gizmo.change_turn_speed(500)
    gizmo.turn_left_degrees(42)
    gizmo.go_reverse(33)