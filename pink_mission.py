import gizmo


def main_program():
    # Surface Brushing 
    gizmo.go_reverse(24.2)
    gizmo.go_forward(4.0)
    gizmo.go_reverse(8.2)


    # Map Reveal
    gizmo.c_turn_angle(500,-260)
    gizmo.turn_left_degrees(20)
    print("I have turned left!!🌈")
# --- RUN THE MAIN PROGRAM ---
main_program()
