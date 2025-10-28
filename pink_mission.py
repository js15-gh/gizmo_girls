import gizmo


def main_program():
    #Surface Brushing 
    gizmo.change_speed(500)
    gizmo.go_reverse(24.0)
    gizmo.go_forward(6)
    gizmo.c_turn_angle(100,-520)
    gizmo.turn_right_degrees(30)
    gizmo.go_reverse(11.5)
    gizmo.turn_left_degrees(75)
    # # Map Reveal
    gizmo.go_reverse(5.0)
    gizmo.c_turn_angle(200,400)


    gizmo.go_forward(5.0)
    gizmo.proportional_turn_distance(5,-180)
    gizmo.go_forward(11.0)
    gizmo.turn_right_degrees(165)









    # gizmo.go_forward(7.0)
    # gizmo.c_turn_angle(200,50)
    #gizmo.turn_left_degrees(157)
    # gizmo.c_turn_angle(100,-480)
    # gizmo.go_forward(13.0)




    # gizmo.proportional_turn_distance(10,100)
    # gizmo.go_reverse(4.0)
    # gizmo.c_turn_angle(100,-40)
    # gizmo.go_forward(5.0)
    # gizmo.c_turn_angle(100,55)
    # gizmo.go_reverse(6.0)
# --- RUN THE MAIN PROGRAM ---
main_program()
