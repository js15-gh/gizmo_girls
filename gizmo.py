import umath
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- CONFIGURATION VARIABLES ---
# These are the only variables you should need to change for a new robot.
# -----------------------------
# Motor and Port configuration
# Set the motor objects, ensuring the left motor turns the same way as the right.
# You determined that you need to use Direction.COUNTERCLOCKWISE for the right motor.
LEFT_MOTOR = Motor(Port.A, Direction.COUNTERCLOCKWISE)
RIGHT_MOTOR = Motor(Port.B)
C_ATTACHMENT = Motor(Port.C, Direction.COUNTERCLOCKWISE)
D_ATTACHMENT = Motor(Port.D, Direction.COUNTERCLOCKWISE)

# DriveBase measurements
# Measured in millimeters (mm).
WHEEL_DIAMETER_MM = 62.4  # The diameter of the robot's wheels.
AXLE_TRACK_MM = 113      # The distance between the centers of the wheels.

# Movement constants
# You determined that a negative angle makes the robot turn right.
RIGHT_TURN_ANGLE_SIGN = 1
# You determined that a negative radius forces a forward curve.
CURVE_RADIUS_SIGN = -1

# --- END OF CONFIGURATION ---


# --- INITIALIZATION ---
# Create the robot objects based on the configuration.
hub = PrimeHub()
robot = DriveBase(LEFT_MOTOR, RIGHT_MOTOR, WHEEL_DIAMETER_MM, AXLE_TRACK_MM)

cur = robot.settings()
straight_speed, straight_accel, turn_rate, turn_accel = cur

print("Current DriveBase settings:")
print(f" straight_speed : {straight_speed} mm/s")
print(f" straight_accel : {straight_accel} mm/s2")
print(f" turn_rate : {turn_rate} deg/s")
print(f" turn_accel : {turn_accel} deg/s2")


# --- LIBRARY FUNCTIONS ---
# Functions that hide the complexity of the robot's specific configurations.

def change_speed(pct):
    s_speed, s_acc, t_rate, t_acc = robot.settings()
    s_speed = straight_speed * pct/100 
    print("Changing DriveBase settings:")
    print(f" straight_speed : {s_speed} mm/s")
    print(f" straight_accel : {s_acc} mm/s2")
    print(f" turn_rate : {t_rate} deg/s")
    print(f" turn_accel : {t_acc} deg/s2")
    robot.settings(s_speed, s_acc, t_rate, t_acc)

def go_forward(distance_inches):
    """Drives the robot straight forward for a specified distance in inches."""
    print(f"Action: Going forward {distance_inches} inches...")
    distance_mm = distance_inches * 25.4
    robot.straight(distance_mm)
    wait(100)  # Pause briefly for stability.


def go_reverse(distance_inches):
    """Drives the robot straight backward for a specified distance in inches."""
    print(f"Action: Going reverse {distance_inches} inches...")
    distance_mm = distance_inches * 25.4
    robot.straight(-distance_mm)
    wait(100)  # Pause briefly for stability.


def turn_right_degrees(degrees):
    """Turns the robot right for a specified number of degrees."""
    print(f"Action: Turning right {degrees} degrees...")
    robot.turn(degrees * RIGHT_TURN_ANGLE_SIGN)
    wait(100)  # Pause briefly for stability.


def turn_left_degrees(degrees):
    """Turns the robot left for a specified number of degrees."""
    print(f"Action: Turning left {degrees} degrees...")
    robot.turn(degrees * -RIGHT_TURN_ANGLE_SIGN)
    wait(100)  # Pause briefly for stability.


def proportional_turn_duration(speed_mm_s, turn_rate_deg_s, duration_s):
    """
    Performs a continuous proportional turn for a specified duration.
    A positive turn rate turns right; a negative turns left.
    """
    if turn_rate_deg_s > 0:
        turn_rate = turn_rate_deg_s * RIGHT_TURN_ANGLE_SIGN
        direction_str = "right"
    else:
        # Bug fix: A left turn rate should be a positive value to counteract
        # the RIGHT_TURN_ANGLE_SIGN logic.
        turn_rate = abs(turn_rate_deg_s) * -RIGHT_TURN_ANGLE_SIGN
        direction_str = "left"

    print(f"Action: Proportional turn {direction_str} at speed {speed_mm_s} mm/s for {duration_s} seconds...")
    robot.drive(speed_mm_s, turn_rate)
    wait(duration_s * 1000)
    robot.stop()


def proportional_turn_distance(distance_inches, angle_degrees):
    """
    Performs a proportional turn that covers a specific distance while
    completing a certain angle. A positive angle turns right, negative turns left.
    """
    distance_mm = distance_inches * 25.4
    if angle_degrees > 0:
        direction_str = "right"
    else:
        direction_str = "left"
        
    print(f"Action: Proportional turn {direction_str} over {distance_inches} inches while turning {angle_degrees} degrees...")

    # Calculate the radius based on the desired distance and angle.
    radius_in_mm = (360 * abs(distance_mm)) / (2 * umath.pi * abs(angle_degrees))
    
    # radius is derived from angle and distance
    robot.curve(radius_in_mm, angle_degrees)

def c_turn_angle_back2zero(speed, angle):
    C_ATTACHMENT.run_angle(speed, angle)
    C_ATTACHMENT.run_target(speed, 0)

def d_turn_angle_back2zero(speed, angle):
    D_ATTACHMENT.run_angle(speed, angle)
    D_ATTACHMENT.run_target(speed, 0)

def c_turn_angle(speed, angle):
    C_ATTACHMENT.run_angle(speed, angle)

def d_turn_angle(speed, angle):
    D_ATTACHMENT.run_angle(speed, angle)
