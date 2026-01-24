import gizmo
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import wait

import orange_mission, pink_mission, blue_mission, yellow_mission
import green_mission, red_mission, grey_mission, magenta_mission

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
    hub = PrimeHub()

    while True:
        try:
            # 1. IDLE STATE: Battery saving (Lights/Display off)
            hub.light.off()
            print("Idle: Press Left or Right to kick in color detection...")

            # 2. WAIT FOR ARROW BUTTON (Kicks in sensing)
            arrow_pressed = None
            while True:
                pressed = hub.buttons.pressed()
                if Button.LEFT in pressed:
                    arrow_pressed = Button.LEFT
                    break
                if Button.RIGHT in pressed:
                    arrow_pressed = Button.RIGHT
                    break
                wait(50)

            # Wait for button release to prevent initial jolts
            while hub.buttons.pressed():
                wait(10)

            # 3. COLOR SENSING: Detected as soon as arrow is pressed
            hub.light.on(Color.WHITE)
            hub.display.char("?")
            reading = gizmo.read_port_f_color()
            
            selected_mission = None
            selected_name = None

            for color_name, mission in COLOR_MISSIONS:
                if gizmo.color_check(color_name, reading=reading):
                    selected_mission = mission
                    selected_name = color_name
                    break
            
            # 4. CONDITIONAL EXECUTION
            if selected_mission:
                hub.display.char(selected_name[0])
                hub.light.on(Color.CYAN)

                # Check specific restrictions
                if selected_name == "RED":
                    if arrow_pressed == Button.LEFT:
                        hub.display.char("R")
                        red_mission.main_program()
                    elif arrow_pressed == Button.RIGHT:
                        hub.display.char("G")
                        grey_mission.main_program()
                # Check specific restrictions
                if selected_name == "MAGENTA":
                    if arrow_pressed == Button.LEFT:
                        hub.display.char("P")
                        pink_mission.main_program()
                    elif arrow_pressed == Button.RIGHT:
                        hub.display.char("M")
                        magenta_mission.main_program()
            
                else:
                    # Execute immediately with single click logic
                    selected_mission()
            else:
                print("No color detected.")
                wait(1000)

        except SystemExit:
            # 5. RESET: Triggered by Center Button (default stop behavior)
            print("System Reset: Returning to idle...")
            wait(500) # Debounce delay before restart
            break

if __name__ == "__main__":
    master()
