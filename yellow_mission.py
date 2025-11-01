import gizmo


def main_program():
    #Mission 3 + 4
    gizmo.change_speed(100)
    ##gizmo.go_forward(39)
    # gizmo.wait(200)
    #gizmo.go_forward(1)
    #gizmo.turn_left_degrees(95)
    gizmo.turn_single_motor_B(200,-340)
    gizmo.c_turn_angle(200,-500)
    gizmo.wait_for_reflection(14)
    gizmo.wait(200)
    gizmo.c_turn_angle(200,40)
    gizmo.wait(100)
    gizmo.c_turn_angle(200,-20)
    gizmo.go_reverse(5)
    gizmo.wait(100)
    gizmo.c_turn_angle(500,100)


    # gizmo.go_forward(1.2)
    # gizmo.turn_left_degrees(100)
    # gizmo.wait_for_reflection(14)


    







   




  
# --- RUN THE MAIN PROGRAM ---
main_program()


