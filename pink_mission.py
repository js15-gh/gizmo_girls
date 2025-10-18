import gizmo


def main_program():
    #Surface Brushing 
    gizmo.change_speed(500)
    gizmo.go_reverse(19.2)
    gizmo.go_forward(4.5)
    gizmo.turn_right_degrees(30)
    gizmo.go_reverse(11.0)
    gizmo.turn_left_degrees(75)
    # # Map Reveal
    gizmo.go_reverse(5.0)
    gizmo.c_turn_angle(200,400)
    gizmo.go_forward(5.0)
    gizmo.c_turn_angle(200,50)

# --- RUN THE MAIN PROGRAM ---
main_program()
