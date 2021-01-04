cmake_minimum_required(VERSION 3.4...3.18)

if(DEFINED ENV{VCPKG_ROOT} AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

set(Python_FIND_IMPLEMENTATIONS CPython)
find_package(Python REQUIRED COMPONENTS Interpreter Development)
find_package(pybind11 CONFIG REQUIRED)

find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

include_directories(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(src)
