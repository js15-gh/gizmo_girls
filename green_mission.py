import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)


#1) Raise the ship
    gizmo.drive_forward(500,490,19.8)
    gizmo.wait(500)
    gizmo.c_turn_angle(-150,120) # drop flag
    gizmo.go_reverse(2)
    gizmo.drive_forward(500,490,1)
    gizmo.d_turn_angle(400,390) # # drop right lever
    gizmo.change_speed(200)
    gizmo.go_reverse(8)
    gizmo.d_turn_angle(300,-239) # lift of right lever
    gizmo.change_speed(300)
    gizmo.go_reverse(11)
#2) Bring items to forum
    gizmo.go_forward(5)





 # 3) 


# --- RUN THE MAIN PROGRAM ---
main_program()
