import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # 1) Release boulders and flip city
    gizmo.change_speed(200)
    gizmo.go_forward(27.7)
    gizmo.change_speed(100)
    gizmo.turn_left_degrees(95)
    gizmo.go_forward(3)
    gizmo.go_reverse(10.5)
    gizmo.turn_left_degrees(5)
    # gizmo.turn_right_degrees(10)
    # gizmo.go_reverse(3.1)
    # gizmo.turn_left_degrees(13)
    # gizmo.go_reverse(4.35)
    gizmo.c_turn_angle(-2000, 240)
    gizmo.c_turn_angle(2000, 240)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 240)
    gizmo.c_turn_angle(2000, 240)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 235)
    gizmo.c_turn_angle(2000, 260)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 235)
    gizmo.c_turn_angle(2000, 240)
    gizmo.go_reverse(4)
    gizmo.go_forward(2.2)
    gizmo.change_speed(75)
    gizmo.d_turn_angle(300, 130)
    gizmo.change_speed(500)
    gizmo.go_reverse(8.6)

    print("Black mission complete.")



# --- RUN THE MAIN PROGRAM ---
# main_program()
