import gizmo


def main_program():
    #Surface Brushing 
    #start 5th line form start/left
    gizmo.change_speed(150)
    gizmo.go_reverse(24.67)
    gizmo.go_forward(6)
    gizmo.turn_right_degrees(55)
    gizmo.go_reverse(9.4)
    gizmo.turn_left_degrees(138)
    # Map Reveal
    gizmo.change_speed(100)
    gizmo.go_reverse(10)
    gizmo.c_turn_angle(500,300)
    gizmo.go_forward(7.0)
    gizmo.turn_right_degrees(50)







# --- RUN THE MAIN PROGRAM ---
main_program()
