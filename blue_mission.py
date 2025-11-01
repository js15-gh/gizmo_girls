import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(47)
    gizmo.go_forward(9)
    gizmo.d_turn_angle(200, 220)
    gizmo.go_reverse(5)




main_program()