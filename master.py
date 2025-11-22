import gizmo
import black_mission
import pink_mission
import blue_mission
import yellow_mission
import green_mission
import red_mission

COLOR_MISSIONS = (
    ("MAGENTA", pink_mission.main_program),
    ("ORANGE", black_mission.main_program),
    ("BLUE", blue_mission.main_program),
    ("RED", red_mission.main_program),
    ("YELLOW", yellow_mission.main_program),
    ("GREEN", green_mission.main_program),
)


def master():
    """
    Detect the color on Port F once, then dispatch the matching mission.
    Reading once avoids recreating the sensor and keeps HSV/ambient consistent.
    """
    reading = gizmo.read_port_f_color()

    for color_name, mission in COLOR_MISSIONS:
        if gizmo.color_check(color_name, reading=reading):
            print(color_name)
            mission()
            return

    print("NO COLOR IDENTIFIED")


master()

