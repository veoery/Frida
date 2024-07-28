from robot import Dobot

dobot=Dobot()
dobot.good_morning_robot()

positions = [565, 157, 240]
orientations = [-0.045, 0.956, 0.563, -0.124]
dobot.go_to_cartesian_pose(positions, orientations)
