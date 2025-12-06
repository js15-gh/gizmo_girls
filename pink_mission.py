import gizmo


def main_program():
    #Surface Brushing 
    #start 5th line form start/left
    gizmo.change_speed(150)
    gizmo.go_reverse(26)
    gizmo.go_forward(9)
    gizmo.d_turn_angle(-500, 260)
    gizmo.go_reverse(5)
    gizmo.wait(1.67)
    gizmo.d_turn_angle(300, 300)
    gizmo.wait(1.67)
    gizmo.d_turn_angle(-400, 200)
    gizmo.turn_right_degrees(110)
    gizmo.go_reverse(9.2)
    gizmo.turn_left_degrees(180)
    # Map Reveal
    gizmo.change_speed(100)
    gizmo.go_reverse(9.5)
    gizmo.c_turn_angle(500,600)
    gizmo.go_forward(7.0)
    gizmo.turn_right_degrees(130)
    gizmo.change_speed(400)
    gizmo.go_forward(35)





# --- RUN THE MAIN PROGRAM ---
# main_program()
