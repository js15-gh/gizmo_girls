import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(91)
    gizmo.go_forward(20.8)
    gizmo.turn_left_degrees(86)
    gizmo.go_forward(5.5)
    gizmo.turn_left_degrees(17)
    gizmo.d_turn_angle(2000, 650)
    gizmo.go_reverse(10)
    gizmo.change_speed(500)
    gizmo.go_forward(5)
    gizmo.turn_right_degrees(110)
    gizmo.go_forward(10)
    gizmo.turn_left_degrees(30)
    gizmo.go_forward(30)