cmake_minimum_required(VERSION 3.4)

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(CMAKE_CXX_COMPILER_ID STREQUAL Clang)
  set(CLANG_DEFAULT_CXX_STDLIB libc++)
  set(CLANG_DEFAULT_RTLIB compiler-rt)
endif()

find_package(re2 REQUIRED CONFIG)

get_target_property(include_dirs re2::re2 INTERFACE_INCLUDE_DIRECTORIES)
message("re2_include_dirs=${include_dirs}")

get_target_property(link_libraries re2::re2 INTERFACE_LINK_LIBRARIES)
message("re2_extra_objects=${link_libraries}")

message(STATUS "Set CMAKE_BUILD_OVERRIDE to change build type.")
message(STATUS "<<< Build configuration >>>
Build type      ${CMAKE_BUILD_TYPE}
Build override  ${CMAKE_BUILD_OVERRIDE}
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
