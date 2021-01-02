cmake_minimum_required(VERSION 3.4...3.18)

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

find_package(re2 CONFIG REQUIRED NAMES re2)

get_target_property(include_dirs re2::re2 INTERFACE_INCLUDE_DIRECTORIES)
message("re2_include_dirs=${include_dirs}")

get_target_property(link_libraries re2::re2 INTERFACE_LINK_LIBRARIES)
message("re2_extra_objects=${link_libraries}")
