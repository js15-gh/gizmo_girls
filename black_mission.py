import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # # 1) Go to release boulders
    # gizmo.change_speed(200)
    # gizmo.go_forward(29.2)
    # gizmo.change_speed(100)
    # gizmo.turn_left_degrees(45)
    # print("-" * 20)

    # # 2) Pick up the stone mill
    # gizmo.d_turn_angle_comeback(30, -168)

    # # 3) Flip the city
    # gizmo.turn_left_degrees(20)
    # gizmo.go_forward(1.5)
    # gizmo.turn_left_degrees(25)
    # gizmo.go_forward(0.8)
    # print("-" * 20)

    # # 4) head to tip the scales
    # gizmo.go_reverse(0.5)
    # gizmo.turn_right_degrees(25)
    # gizmo.go_reverse(2.5)
    # gizmo.turn_left_degrees(30)
    # gizmo.go_forward(11)
    # gizmo.turn_left_degrees(20)
    # gizmo.go_forward(2)
    # print("-" * 20)

    # # 5) Tip the scale
    # gizmo.c_turn_angle_back2zero(5000, 300)

    # # 6) Raise market roof
    # gizmo.turn_right_degrees(20)
    # gizmo.go_forward(1.3)
    # #gizmo.go_reverse(1.8)
    # gizmo.turn_right_degrees(27)
    # gizmo.go_reverse(7)
    # print("-" * 20)

    # # 7) Head home
    # gizmo.go_forward(6)
    # gizmo.turn_left_degrees(35)
    # gizmo.go_reverse(5.5)
    # gizmo.turn_right_degrees(37)
    # gizmo.change_speed(300)
    # gizmo.go_reverse(34)
    # gizmo.change_speed(100)
    # print("-" * 20)

    # 1) Release boulders and flip city
    gizmo.change_speed(200)
    gizmo.go_forward(27.5)
    gizmo.change_speed(100)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(2.5)
    gizmo.go_reverse(2.5)
    gizmo.go_reverse(7)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.c_turn_angle_back2zero(-2000, 240)
    gizmo.go_reverse(1.8)
    gizmo.d_turn_angle(300, 155)
    gizmo.go_reverse(8.6)

    print("Black mission complete.")



# --- RUN THE MAIN PROGRAM ---
main_program()
