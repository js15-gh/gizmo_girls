import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)






# Actual black mission
#     1) Release boulders and flip city
    gizmo.change_speed(200)
    gizmo.go_forward(27.7)
    gizmo.change_speed(100)
    gizmo.turn_left_degrees(95)
    gizmo.go_forward(3)
    gizmo.go_reverse(10.5)
    gizmo.c_turn_angle(-2000, 240)
    gizmo.c_turn_angle(2000, 240)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 240)
    gizmo.c_turn_angle(2000, 240)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 235)
    gizmo.c_turn_angle(2000, 260)
    gizmo.go_reverse(4.8)
    gizmo.go_forward(3)
    gizmo.change_speed(75)
    gizmo.d_turn_angle(300, 150)
    gizmo.go_reverse(8.6)

    print("Black mission complete.")



# --- RUN THE MAIN PROGRAM ---
# main_program()
