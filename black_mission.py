import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # 1) Release boulders and flip city
    gizmo.change_speed(200)
    gizmo.go_forward(27.5)
    gizmo.change_speed(100)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(2.5)
    gizmo.go_reverse(2)
    gizmo.turn_right_degrees(8)
    gizmo.go_reverse(3)
    gizmo.turn_left_degrees(9)
    gizmo.go_reverse(4.5)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.go_reverse(1.8)
    gizmo.d_turn_angle(300, 130)
    gizmo.go_reverse(8.6)

    print("Black mission complete.")



# --- RUN THE MAIN PROGRAM ---
# main_program()
