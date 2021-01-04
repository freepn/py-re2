cmake_minimum_required(VERSION 3.4...3.18)

project(re2 LANGUAGES CXX C)

option(PY_DEBUG "Set if python being linked is a Py_DEBUG build" OFF)

include(GNUInstallDirs)
include(cmake/python.cmake)
find_package(pybind11 CONFIG REQUIRED)

if (${PYTHON_IS_DEBUG})
  set(PY_DEBUG ON)
endif()

find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
    ${PROJECT_SOURCE_DIR}/cmake/modules/)

include_directories(${PROJECT_SOURCE_DIR}/src)

add_subdirectory(src)
