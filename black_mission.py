import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # 1) Release boulders and flip city
    gizmo.change_speed(200)
    gizmo.go_forward(27.7)
    gizmo.change_speed(100)
    gizmo.turn_left_degrees(90)
    gizmo.go_forward(3.5)
    gizmo.go_reverse(3)
    gizmo.turn_right_degrees(10)
    gizmo.go_reverse(3.4)
    gizmo.turn_left_degrees(13)
    gizmo.go_reverse(4.4)
    gizmo.c_turn_angle(-2000, 230)
    gizmo.c_turn_angle(2000, 220)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 230)
    gizmo.c_turn_angle(2000, 220)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 230)
    gizmo.c_turn_angle(2000, 220)
    gizmo.wait(1.67)
    gizmo.c_turn_angle(-2000, 230)
    gizmo.c_turn_angle(2000, 220)
    gizmo.go_reverse(1.8)
    gizmo.change_speed(75)
    gizmo.d_turn_angle(300, 130)
    gizmo.go_reverse(8.6)

    print("Black mission complete.")



# --- RUN THE MAIN PROGRAM ---
# main_program()
