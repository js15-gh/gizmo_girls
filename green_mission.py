import gizmo

def main_program():
    print("Starting main program sequence...")
    print("-" * 20)

    # 1) Go forward 30 inches
    gizmo.go_forward(30.5)
    print("-" * 20)

 # 2) Turn left 50 degrees
    gizmo.turn_left_degrees(45)
    print("-" * 20)

 # 1) Go forward 1 inches
    gizmo.go_forward(1)
    print("-" * 20)

# --- RUN THE MAIN PROGRAM ---
main_program()
