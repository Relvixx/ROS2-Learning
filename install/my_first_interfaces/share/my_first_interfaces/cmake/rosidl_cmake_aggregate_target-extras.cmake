# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target my_first_interfaces::my_first_interfaces
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${my_first_interfaces_TARGETS}.
if(my_first_interfaces_TARGETS AND NOT TARGET my_first_interfaces::my_first_interfaces)
  add_library(my_first_interfaces::my_first_interfaces INTERFACE IMPORTED)
  set_target_properties(my_first_interfaces::my_first_interfaces PROPERTIES
    INTERFACE_LINK_LIBRARIES "${my_first_interfaces_TARGETS}")
endif()
