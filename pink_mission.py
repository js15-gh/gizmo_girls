import gizmo


def main_program():
    #Surface Brushing 
    #start 5th line form start/left
    gizmo.change_speed(150)
    gizmo.go_reverse(26)
    gizmo.go_forward(9)
    gizmo.d_turn_angle(-400, 250)
    gizmo.go_reverse(5)
    gizmo.d_turn_angle(200, 375)
    gizmo.wait(1.67)
    gizmo.d_turn_angle(-400, 275)
    gizmo.turn_right_degrees(55)
    gizmo.go_reverse(9.4)
    gizmo.turn_left_degrees(120)
    # Map Reveal
    gizmo.change_speed(100)
    gizmo.go_reverse(10)
    gizmo.c_turn_angle(500,600)
    gizmo.go_forward(7.0)
    gizmo.turn_right_degrees(50)







# --- RUN THE MAIN PROGRAM ---
# main_program()
