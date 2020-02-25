#!/usr/bin/env python3
"""
This is a program showing the use of the RobotDrive class,
specifically it contains the code necessary to operate a robot with
a single joystick
"""

import wpilib
import wpilib.drive
import wpilib.cameraserver as cameraserver
from wpilib.DoubleSolenoid.Value import kOff, kForward, kReverse
# from cscore import CameraServer
import rev

class Robot(wpilib.IterativeRobot):
  """2020 robot code"""

  # stick 1
  AXIS_THROTTLE = 1  # l stick
  AXIS_STEER = 0  # l stick
  BUTTON_SHIFT = 6  # r bumper

  def robotInit(self):
    """Robot initialization function"""

    self.motors = {
      "left": [rev.CANSparkMax(3), rev.CANSparkMax(4)],
      "right": [rev.CANSparkMax(1), rev.CANSparkMax(2)],
    }

    self.drive = wpilib.drive.DifferentialDrive(
      wpilib.SpeedControllerGroup(*self.motors["left"]),
      wpilib.SpeedControllerGroup(*self.motors["right"]),
    )
    # self.drive.setExpiration(0.5)

    self.shifter = wpilib.DoubleSolenoid(0, 1)

    self.compressor = wpilib.Compressor(0)

    # wpilib.CameraServer.launch()
    # camera_alpha = cameraserver.getInstance().startAutomaticCapture(0)
    # camera_beta = cameraserver.getInstance().startAutomaticCapture(1)
    # cameraserver.CameraServer.launch()
    cameraserver.CameraServer.launch("camera.py:main")

    # camera.setResolution(426, 240)
    # camera.setFPS(15)

  def autonomousInit(self):
    self.teleopInit()

  def autonomousPeriodic(self):
    self.teleopPeriodic()

  def teleopInit(self):
    """Executed at the start of teleop mode"""
    # self.drive.setSafetyEnabled(True)
    self.compressor.start()

  def teleopPeriodic(self):
    """Does stuff"""
    x = self.stick_drive.getRawAxis(self.AXIS_THROTTLE)
    y = self.stick_drive.getRawAxis(self.AXIS_STEER)
    a = self.stick_drive.getRawButton(self.BUTTON_A)

    self.drive.arcadeDrive(-x, y)

    self.shifter.set(kForward if a else kReverse)

  def testInit(self):
    self.compressor.stop()  # disable compressor for testing use in quiet environments

  testPeriodic = teleopPeriodic

if __name__ == "__main__":
  wpilib.run(Robot)
