import gizmo


def main_program():
    #Surface Brushing 
    #start 5th line form start/left
    gizmo.change_speed(300)
    gizmo.go_reverse(24.0)
    gizmo.go_forward(6)
    gizmo.turn_right_degrees(55)
    gizmo.go_reverse(10.5)
    gizmo.turn_left_degrees(120)
    # Map Reveal
    gizmo.go_reverse(9)
    gizmo.c_turn_angle(500,300)
    gizmo.go_forward(7.0)






# --- RUN THE MAIN PROGRAM ---
main_program()
