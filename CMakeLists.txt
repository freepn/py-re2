cmake_minimum_required(VERSION 3.4...3.18)

project(re2 LANGUAGES CXX C)

option(PY_DEBUG "Set if python being linked is a Py_DEBUG build" OFF)

include(GNUInstallDirs)
include(cmake/python.cmake)

if (${PYTHON_IS_DEBUG})
  set(PY_DEBUG ON)
endif()

find_package(pybind11 CONFIG)
if(NOT pybind11_FOUND)
  find_package(pybind11)
endif()

if(pybind11_FOUND)
  message(STATUS "System pybind11 found")
else()
  message(STATUS "Fetching pybind11 from github")
  # Fetch pybind11
  include(FetchContent)

  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11
    GIT_TAG v2.6.1
  )
  FetchContent_MakeAvailable(pybind11)
endif()

find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
    ${PROJECT_SOURCE_DIR}/cmake/modules/)

include_directories(${PROJECT_SOURCE_DIR}/src)

add_subdirectory(src)
