import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)


#1) Raise the ship
    gizmo.change_speed(500)
    gizmo.drive_forward(505,490,19.8)
    #gizmo.wait(100)
    gizmo.c_turn_angle(-400,120) # drop flag
    gizmo.go_reverse(2)
    #gizmo.drive_forward(500,490,1)
    gizmo.d_turn_time(500,1.5) # # drop right lever
    gizmo.change_speed(500)
    gizmo.go_reverse(5)
    gizmo.d_turn_time(-500,0.7) # lift of right lever
    gizmo.change_speed(500)
    gizmo.go_reverse(14)






 # 3) 


# --- RUN THE MAIN PROGRAM ---
# main_program()
