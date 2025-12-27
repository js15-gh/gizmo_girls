import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(47)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(80)
    gizmo.turn_right_degrees(80)    
    gizmo.d_turn_angle(300, 220)
    gizmo.go_reverse(4.5)
    gizmo.d_turn_angle(-300, 220)
    gizmo.go_reverse(16)

# main_program()