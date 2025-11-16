import gizmo
import black_mission
import pink_mission
import blue_mission
import yellow_mission
import green_mission
import red_mission

def master():
    if gizmo.color_check("MAGENTA"):
        print("MAGENTA")
        pink_mission.main_program()
    elif gizmo.color_check("ORANGE"):
        print("ORANGE")
        black_mission.main_program()
    elif gizmo.color_check("BLUE"):
        print("BLUE")
        blue_mission.main_program()
    elif gizmo.color_check("RED"):
        print("RED")
        red_mission.main_program()s
    elif gizmo.color_check("YELLOW"):
        print("YELLOW")
        yellow_mission.main_program()
    elif gizmo.color_check("GREEN"):
        print("GREEN")
        green_mission.main_program()
    else:  
        print("NO COLOR IDENTIFIED")

master()

