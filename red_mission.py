import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)


#2) Bring items to forum
    gizmo.go_forward(16)
    gizmo.change_turn_speed(20)
    gizmo.turn_right_degrees(85)
    gizmo.go_forward(10)
    gizmo.go_reverse(9)
    gizmo.change_turn_speed(40)
    gizmo.turn_right_degrees(25.5)
    gizmo.change_speed(200)
    gizmo.go_forward(27)
    gizmo.turn_right_degrees(22.6)
    gizmo.go_forward(9.5)
    gizmo.d_turn_angle(1000,1800)
    gizmo.go_reverse(9)



# --- RUN THE MAIN PROGRAM ---
#main_program()