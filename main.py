import gizmo

# --- MAIN PROGRAM SEQUENCE ---

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # 1) Go forward 5 inches
    gizmo.go_forward(5)
    print("-" * 20)

    # 2) Turn right 90 degrees
    gizmo.turn_right_degrees(90)
    print("-" * 20)

    # 3) Go reverse 2 inches
    gizmo.go_reverse(2)
    print("-" * 20)

    # 4) Turn 90 degrees right
    gizmo.turn_right_degrees(90)
    print("-" * 20)

    # 5) Go forward 5 inches
    gizmo.go_forward(5)
    print("-" * 20)
#yayyyyyy
    # 6) Make left proportional turn and travel for 2 seconds
    gizmo.proportional_turn_duration(speed_mm_s=100, turn_rate_deg_s=-45, duration_s=2)
    print("-" * 20)
    
    # 7) Make left proportional turn and travel for 5 inches
    # Assume a 45-degree angle to make this a realistic arc.
    gizmo.proportional_turn_distance(distance_inches=5, angle_degrees=-45)
    print("-" * 20)

    print("Main program sequence complete.")


# --- RUN THE MAIN PROGRAM ---
main_program()