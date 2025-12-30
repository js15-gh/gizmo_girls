import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)


#1) Raise the ship
    gizmo.drive_forward(500,490,19.8)
    gizmo.wait(500)
    gizmo.c_turn_angle(-150,120) # drop flag
    gizmo.go_reverse(2)
    #gizmo.drive_forward(500,490,1)
    gizmo.d_turn_time(300,1.8) # # drop right lever
    gizmo.change_speed(200)
    gizmo.go_reverse(6.7)
    gizmo.d_turn_time(-300,1.5) # lift of right lever
    gizmo.change_speed(300)
    gizmo.go_reverse(14)






 # 3) 


# --- RUN THE MAIN PROGRAM ---
# main_program()
