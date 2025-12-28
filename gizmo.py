import umath
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.pupdevices import ColorSensor

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

# Dedicated color sensor on Port F. Instantiate once to avoid I2C bus resets.
PORT_F_SENSOR = ColorSensor(Port.F)
_LAST_PORT_F_READING = None

cur = robot.settings()
straight_speed, straight_accel, turn_rate, turn_accel = cur

# print("Current DriveBase settings:")
# print(f" straight_speed : {straight_speed} mm/s")
# print(f" straight_accel : {straight_accel} mm/s2")
# print(f" turn_rate : {turn_rate} deg/s")
# print(f" turn_accel : {turn_accel} deg/s2")

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

def change_turn_speed(pct):
    s_speed, s_acc, t_rate, t_acc = robot.settings()
    t_rate = turn_rate * pct/100 
    t_acc = turn_accel * pct/100
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
    print(f"c_turn_angle_back2zero speed={speed}, angle={angle}")
    C_ATTACHMENT.run_angle(speed, angle)
    C_ATTACHMENT.run_target(speed, 0)

def d_turn_angle_back2zero(speed, angle):
    print(f"d_turn_angle_back2zero speed={speed}, angle={angle}")
    D_ATTACHMENT.run_angle(speed, angle)
    D_ATTACHMENT.run_target(speed, 0)

def c_turn_time(speed, time):
    C_ATTACHMENT.run_time(speed, time * 1000)

def d_turn_time(speed, time):
    D_ATTACHMENT.run_time(speed, time * 1000)

def d_turn_angle_comeback(speed, angle):
    D_ATTACHMENT.run_angle(speed, angle)
    D_ATTACHMENT.run_angle(speed*2, -angle)

def c_turn_angle(speed, angle):
   C_ATTACHMENT.run_angle(speed, angle)

def d_turn_angle(speed, angle, wait_value=True):
   print(f"d_turn_angle speed ={speed}, angle = {angle}, wait_value={wait_value}")
   D_ATTACHMENT.run_angle(speed, angle, wait=wait_value)

# example stored color data (add more later)
COLOR_REFERENCES = {
    "MAGENTA": {"hsv": (339, 77, 36), "ambient": 0.6},
    "BLUE": {"hsv": (214, 85, 32), "ambient": 0.5},
    "GREEN": {"hsv": (158, 65, 24), "ambient": 0.4},
    "RED": {"hsv": (352, 87, 43), "ambient": 0.4},
    "YELLOW": {"hsv": (50, 71, 70), "ambient": 0.3},
    "BLACK": {"hsv": (0, 0, 11), "ambient": 0.3},
    "ORANGE": {"hsv": (3,83,64), "ambient": 0.4},
    "GREY": {"hsv": (205, 25, 42), "ambient": 0.0}    
}

def read_port_f_color():
    """
    Reads the Port F color sensor once and caches the latest reading.
    Returns a dict containing hsv tuple, ambient light and the raw color value.
    """
    global _LAST_PORT_F_READING
    h, s, v = PORT_F_SENSOR.hsv()
    ambient = PORT_F_SENSOR.ambient()
    detected_color = PORT_F_SENSOR.color()
    reading = {
        "hsv": (h, s, v),
        "ambient": ambient,
        "detected_color": detected_color,
    }
    _LAST_PORT_F_READING = reading
    print(f"Port.F reading -> hsv={reading['hsv']}, ambient={ambient}, color={detected_color}")
    return reading


def color_check(
    color_name,
    hue_tol=8,
    sat_tol=8,
    val_tol=8,
    amb_tol=10,
    reading=None,
):
    """
    Checks if the provided (or freshly sampled) reading matches the reference color.
    Pass a shared reading when multiple colors need to be tested to avoid extra samples.
    """
    if color_name not in COLOR_REFERENCES:
        raise ValueError(f"Color '{color_name}' not in reference dictionary!")

    reading_provided = reading is not None
    reading = reading or read_port_f_color()

    h, s, v = reading["hsv"]
    ambient = reading["ambient"]
    detected_color = reading.get("detected_color")

    if not reading_provided:
        print(f"h={h}, s={s}, v={v}")
        print(f"ambient={ambient}")
        print(f"color = {detected_color}")

    ref = COLOR_REFERENCES[color_name]
    ref_h, ref_s, ref_v = ref["hsv"]
    ref_amb = ref["ambient"]

    print(f"[{color_name}] ref_h={ref_h}, ref_s={ref_s}, ref_v={ref_v}, ref_amb={ref_amb}")

    hue_delta = abs(h - ref_h)
    sat_delta = abs(s - ref_s)
    val_delta = abs(v - ref_v)
    amb_delta = abs(ambient - ref_amb)

    hue_match = hue_delta < hue_tol
    sat_match = sat_delta < sat_tol
    val_match = val_delta < val_tol
    amb_match = amb_delta < amb_tol

    debug_msg = (
        "[{color}] hue_delta={hue}({h_tol}), sat_delta={sat}({s_tol}), "
        "val_delta={val}({v_tol}), amb_delta={amb}({a_tol}) -> "
        "{h_match},{s_match},{v_match},{a_match}"
    ).format(
        color=color_name,
        hue=hue_delta,
        h_tol=hue_tol,
        sat=sat_delta,
        s_tol=sat_tol,
        val=val_delta,
        v_tol=val_tol,
        amb=amb_delta,
        a_tol=amb_tol,
        h_match=hue_match,
        s_match=sat_match,
        v_match=val_match,
        a_match=amb_match,
    )
    print(debug_msg)

    return hue_match and sat_match and val_match and amb_match

# function to wait for the desired color
def wait_for_color(desired_color):
    sensor = ColorSensor(Port.E)
    print("wait_for_color starting..")
    # start driving the robot
    robot.drive(200,0)
    # while the desired color is not detected, keep waiting
    while sensor.color() != desired_color:
        print(f"Color = {sensor.color()} , Reflection = {sensor.reflection()}")
        wait(20)
    # if we are here, desired color must be detected, so we can stop
    robot.stop()

# function to wait for the desired reflection number
def wait_for_reflection(desired_number):
    sensor = ColorSensor(Port.E)
    print(f"wait_for_reflection {desired_number} starting..")
    # start driving the robot
    robot.drive(200,0)

    # while the desired reflection is not detected, keep waiting
    while sensor.reflection() >= desired_number:
        print(f"Color = {sensor.color()} , Reflection = {sensor.reflection()}")
        wait(20)

    # if we are here, desired reflection must be detected, so we can stop
    print(f"reached desired reflection {sensor.reflection()}, which is less than or equal to {desired_number}, so stop")
    robot.stop()

def wait_for_reflection_pick_speed(desired_number, speed):
    sensor = ColorSensor(Port.E)
    print(f"wait_for_reflection {desired_number}, and going at speed {speed}")
    # start driving the robot
    robot.drive(speed,0)

    # while the desired reflection is not detected, keep waiting
    while sensor.reflection() >= desired_number:
        print(f"Color = {sensor.color()} , Reflection = {sensor.reflection()}")
        wait(20)

    # if we are here, desired reflection must be detected, so we can stop
    print(f"reached desired reflection {sensor.reflection()}, which is less than or equal to {desired_number}, so stop")
    robot.stop()

# function to only turn one motor
def turn_single_motor_A(speed, degrees):
    LEFT_MOTOR.run_angle(speed, degrees, Stop.BRAKE)

# function to only turn one motor
def turn_single_motor_B(speed, degrees):
    RIGHT_MOTOR.run_angle(speed, degrees, Stop.BRAKE)

def drive_forward(left_power, right_power, distance_inches):
    wheel_circumference = 3.1416 * WHEEL_DIAMETER_MM
    degrees_to_rotate = (distance_inches * 25.4) / wheel_circumference * 360

    LEFT_MOTOR.reset_angle(0)
    RIGHT_MOTOR.reset_angle(0)

    LEFT_MOTOR.run(left_power)
    RIGHT_MOTOR.run(right_power)

    while True:
        avg_angle = (abs(LEFT_MOTOR.angle()) + abs(RIGHT_MOTOR.angle())) / 2
        if avg_angle >= degrees_to_rotate:
            break
        wait(10)

    LEFT_MOTOR.stop()
    RIGHT_MOTOR.stop()
