cmake_minimum_required(VERSION 2.8.3)
project(baxter_urdf_parsing)

find_package(catkin
  REQUIRED
  COMPONENTS
  rospy
  geometry_msgs
  sensor_msgs
  urdfdom
  python_orocos_kdl
  tf
  baxter_core_msgs
  baxter_interface
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS
  rospy
  geometry_msgs
  sensor_msgs
  urdfdom
  python_orocos_kdl
  tf
  baxter_interface
  baxter_core_msgs
)

install(
  DIRECTORY scripts/
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
