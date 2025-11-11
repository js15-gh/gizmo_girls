import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    gizmo.change_speed(200)
    gizmo.go_forward(9)
    gizmo.turn_left_degrees(47)
    gizmo.go_forward(8.7)
    gizmo.d_turn_angle(300, 220)
    gizmo.go_reverse(4.5)
    gizmo.d_turn_angle(-300, 220)
    gizmo.go_reverse(2.9)
    gizmo.d_turn_angle(300, 200)
    gizmo.change_speed(50)
    gizmo.turn_left_degrees(54) #55
    gizmo.change_speed(200)
    gizmo.d_turn_angle(-300, 200)
    gizmo.go_forward(16.6) # o 16.7
    gizmo.turn_right_degrees(110)
    gizmo.wait(67)
    gizmo.go_forward(1)
    gizmo.turn_left_degrees(12)
    gizmo.go_forward(3.9)
    gizmo.d_turn_angle_back2zero(400,100)
    gizmo.go_reverse(5)
    gizmo.turn_left_degrees(83)
    gizmo.change_speed(400)
    gizmo.go_forward(40)
    gizmo.turn_left_degrees(52)
    gizmo.go_forward(6.7)


main_program()