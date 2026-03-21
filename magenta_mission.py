import gizmo


def main_program():
    gizmo.reset_defaults()
    # gizmo.go_forward(30)
    # gizmo.turn_left_degrees(90)
    # gizmo.go_forward(21.27)
    # gizmo.turn_left_degrees(45)
    # gizmo.go_forward(6.6)
    # gizmo.c_turn_angle(500,290)

    gizmo.change_speed(300)
    # gizmo.go_reverse(8)
    gizmo.go_forward(28)
    gizmo.wait_for_reflection_pick_speed(14, 200)
    # gizmo.go_reverse(1.1)
    gizmo.wait(100)
    gizmo.turn_right_degrees(68) #68 before attachment makeover
    gizmo.c_turn_angle(300, 240)
    gizmo.change_speed(150)
    gizmo.go_forward(7)
    gizmo.c_turn_angle(-170, 200)
    gizmo.stally
    gizmo.go_forward(2)
    # gizmo.turn_right_degrees(15)
    gizmo.go_reverse(6)
    gizmo.turn_right_degrees(135)
    gizmo.change_speed(500)
    gizmo.go_forward(40)