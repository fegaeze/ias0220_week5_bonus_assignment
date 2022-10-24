cmake_minimum_required(VERSION 3.0.2)
project(machine_vision_bonus)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  gazebo_ros
)

catkin_package(
  LIBRARIES machine_vision_bonus
  CATKIN_DEPENDS rospy std_msgs geometry_msgs gazebo_ros
)

catkin_install_python(PROGRAMS
  scripts/locomotion.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
