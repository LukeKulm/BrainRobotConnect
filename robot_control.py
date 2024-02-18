from gpiozero import Robot
import time

# Define the robot with motor pins
robot = Robot(left=(17, 18), right=(22, 23))

# Function to drive the robot forward
def drive_forward():
    robot.forward()

# Function to drive the robot backward
def drive_backward():
    robot.backward()

# Function to turn the robot left
def turn_left():
    robot.left()

# Function to turn the robot right
def turn_right():
    robot.right()

# Function to stop the robot
def stop_robot():
    robot.stop()

# Example usage
try:
    drive_forward()
    time.sleep(4)

    turn_left()
    time.sleep(2)

    stop_robot()
    time.sleep(2)

    turn_right()
    time.sleep(2)

    stop_robot()
    time.sleep(2)

    drive_backward()
    time.sleep(4)

    stop_robot()

except KeyboardInterrupt:
    stop_robot()
