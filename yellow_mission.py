import gizmo

def main_program():
    #Mission 3 + 4
    #start last second line from end/right
    gizmo.change_speed(500)
    gizmo.go_forward(38.5) #39
    gizmo.turn_single_motor_B(200,-325) #340
    gizmo.c_turn_angle(200,-500)
    gizmo.d_turn_time(500,0.7)
    gizmo.wait_for_reflection(14)
    gizmo.wait(200)
    gizmo.d_turn_time(-300,0.9)
    gizmo.c_turn_angle(200,52) #40
    gizmo.wait(100)
    #gizmo.c_turn_angle(200,-20)
    gizmo.go_reverse(5)
    gizmo.wait(100)
    gizmo.c_turn_angle(500,100)
    gizmo.turn_right_degrees(25)
    gizmo.go_forward(3)
    gizmo.turn_right_degrees(20)
    gizmo.d_turn_time(500,0.7)
    gizmo.go_forward(13.5) #12.5
    gizmo.d_turn_time(-500,0.7)
    gizmo.go_reverse(5)
    gizmo.turn_right_degrees(130)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(20)
    #coolll





























    # gizmo.go_forward(1.2)
    # gizmo.turn_left_degrees(100)
    # gizmo.wait_for_reflection(14)


    







   




  
# --- RUN THE MAIN PROGRAM ---
# main_program()


