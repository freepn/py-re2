cmake_minimum_required(VERSION 3.15...3.18)

project(re2 LANGUAGES CXX C)

option(PY_DEBUG "Set if python being linked is a Py_DEBUG build" OFF)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(CMAKE_CXX_COMPILER_ID STREQUAL Clang)
  set(CLANG_DEFAULT_CXX_STDLIB libc++)
  set(CLANG_DEFAULT_RTLIB compiler-rt)
endif()

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "RelWithDebInfo" CACHE STRING
            "Default build type: RelWithDebInfo" FORCE)
endif()

include(GNUInstallDirs)

find_package(pybind11 CONFIG)

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

find_package(Threads REQUIRED)

if (${PYTHON_IS_DEBUG})
  set(PY_DEBUG ON)
endif()

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
    ${PROJECT_SOURCE_DIR}/cmake/modules/)

include_directories(${PROJECT_SOURCE_DIR}/src)

add_subdirectory(src)
