cmake_minimum_required(VERSION 3.4...3.18)

set(CMAKE_VERBOSE_MAKEFILE ON)

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

message("re2 CMAKE_CXX_STANDARD=${CMAKE_CXX_STANDARD}")

find_package(re2 CONFIG REQUIRED NAMES re2)

get_target_property(include_dirs re2::re2 INTERFACE_INCLUDE_DIRECTORIES)
message("re2_include_dirs=${include_dirs}")

get_target_property(link_libraries re2::re2 INTERFACE_LINK_LIBRARIES)
message("re2_extra_objects=${link_libraries}")


message(STATUS "<<< re2 Build configuration >>>
Build type      ${CMAKE_BUILD_TYPE}
Install path    ${CMAKE_INSTALL_PREFIX}
Compiler flags:
C               ${CMAKE_C_FLAGS}
C++             ${CMAKE_CXX_FLAGS}
Linker flags:
Executable      ${CMAKE_EXE_LINKER_FLAGS}
Module          ${CMAKE_MODULE_LINKER_FLAGS}
Shared          ${CMAKE_SHARED_LINKER_FLAGS}

ToolchainFile:
    ${CMAKE_TOOLCHAIN_FILE}\n")
