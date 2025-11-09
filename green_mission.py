import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)


#1) Raise the ship
    gizmo.drive_forward(500,490,21)
    gizmo.wait(500)
    gizmo.c_turn_angle(-150,110) # drop flag
    gizmo.go_reverse(2)
    gizmo.d_turn_angle(500, 300) # # drop right lever
    gizmo.change_speed(200)
    gizmo.go_reverse(5)
    gizmo.d_turn_angle(400,-239) # lift of right lever
    gizmo.change_speed(300)
    gizmo.go_reverse(11)
   # i = 0
    #while i<8:
      #i = i + 1
      #gizmo.drive_forward(400,350,3)
      #gizmo.go_reverse(3)

# 2) Raise the ship
    #gizmo.go_forward(14)
    #gizmo.d_turn_angle(500,300)
    #gizmo.go_reverse(2)
    #gizmo.d_turn_angle(-500,300)





 # 3) 


# --- RUN THE MAIN PROGRAM ---
main_program()
