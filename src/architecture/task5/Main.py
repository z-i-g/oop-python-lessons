from RobotCleanerModule import RobotCleanerModule
work_programm = ("move 100", "turn -90", "set soap", "start", "move 50", "stop")

robot = RobotCleanerModule()
robot.execute(work_programm)