import gizmo
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait # Ensure wait is imported

import orange_mission
import pink_mission
import blue_mission
import yellow_mission
import green_mission
import red_mission
import grey_mission

COLOR_MISSIONS = (
    ("MAGENTA", pink_mission.main_program),
    ("ORANGE", orange_mission.main_program),
    ("BLUE", blue_mission.main_program),
    ("RED", red_mission.main_program),
    ("YELLOW", yellow_mission.main_program),
    ("GREEN", green_mission.main_program),
    ("GREY", grey_mission.main_program)
)


def master():
    # 1. Initialize objects once outside the loop if possible
    hub = PrimeHub()

    # 2. Add a loop to keep the robot "alive" after missions
    while True:
        hub.display.char("?")
        hub.light.on(Color.WHITE) # Optional: Reset light to white
        
        # 3. Wait for a color to be detected
        # Note: If reading once at start, move reading INSIDE the loop
        reading = gizmo.read_port_f_color()

        for color_name, mission in COLOR_MISSIONS:
            if gizmo.color_check(color_name, reading=reading):
                print(color_name)
                
                if color_name == "RED":
                    hub.light.on(Color.RED)
                    # Loop specifically for the Red/Grey branch
                    while True:
                        pressed = hub.buttons.pressed()
                        if Button.RIGHT in pressed:
                            hub.display.char("G")
                            grey_mission.main_program()
                            break # Exit Red-choice loop to return to '?'
                        if Button.LEFT in pressed:
                            hub.display.char("R")
                            red_mission.main_program()
                            break # Exit Red-choice loop to return to '?'
                        wait(10)
                else:
                    # Run all other missions
                    mission()
                
                # After any mission finishes, 'break' the for-loop 
                # to restart at the top of 'while True' (the '?' state)
                break 
        
        wait(100) # Small pause before next color scan

master()

