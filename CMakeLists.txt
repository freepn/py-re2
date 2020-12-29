cmake_minimum_required(VERSION 3.4...3.18)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake)

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(CMAKE_CXX_COMPILER_ID STREQUAL Clang)
  set(CLANG_DEFAULT_CXX_STDLIB libc++)
  set(CLANG_DEFAULT_RTLIB compiler-rt)
endif()

find_package(PythonInterp)
find_package(PythonLibs)
# find_package(PythonExtensions)
find_package(Cython)

find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

include_directories(SYSTEM ${PYTHON_INCLUDE_DIR})
include_directories(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(src)

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
