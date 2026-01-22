import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)
    gizmo.reset_defaults()
    gizmo.change_speed(200)
    # gizmo.go_forward(3)
    # gizmo.turn_left_degrees(47)
    gizmo.go_forward(13.5)
    # gizmo.turn_left_degrees(80)
    # gizmo.turn_right_degrees(80)  
    gizmo.c_turn_angle(500, 460)  
    gizmo.d_turn_angle(300, 220)
    gizmo.c_turn_angle(-400, 450)
    gizmo.go_reverse(4.5)
    gizmo.d_turn_angle(-300, 220)
    gizmo.go_reverse(15)
    # gizmo.turn_left_degrees(45)
    # gizmo.go_reverse(6)

# main_program()