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
    gizmo.turn_left_degrees(56) #54
    gizmo.change_speed(200)
    gizmo.d_turn_angle(-300, 200)
    gizmo.go_forward(16.6) # o 16.7
    gizmo.turn_right_degrees(110)
    gizmo.wait(67)
    gizmo.go_forward(1)
    gizmo.turn_left_degrees(18)
    gizmo.go_forward(3.9)
    gizmo.d_turn_angle(400,130)
    gizmo.d_turn_angle(-400,120)
    gizmo.go_reverse(4)
    gizmo.turn_left_degrees(80)
    gizmo.change_speed(500)
    gizmo.go_forward(14)
    gizmo.turn_left_degrees(30)
    gizmo.go_forward(27)



# main_program()