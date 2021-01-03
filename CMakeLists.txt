cmake_minimum_required(VERSION 3.14...3.18)

if(DEFINED ENV{VCPKG_ROOT} AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
  set(CMAKE_TOOLCHAIN_FILE "$ENV{VCPKG_ROOT}/scripts/buildsystems/vcpkg.cmake"
      CACHE STRING "")
endif()

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

#find_package(PythonInterp)
#find_package(PythonLibs)

# TODO finish the required `find_` bits below in case skbuild is missing
#if(NOT SKBUILD)
  #message(FATAL_ERROR "Building requires scikit-build")
#else()
  #find_package(PythonExtensions)
  #find_package(Cython)
#endif()

# Currently, Scikit-build does not support FindPython, so we convert the
# provided hints ourselves.
if(SKBUILD)
  set(Python_EXECUTABLE "${PYTHON_EXECUTABLE}")
  set(Python_INCLUDE_DIR "${PYTHON_INCLUDE_DIR}")
  set(Python_LIBRARY "${PYTHON_LIBRARY}")
  set(DUMMY "${PYTHON_VERSION_STRING}")  # Not needed, silences a warning
endif()

set(Python_FIND_IMPLEMENTATIONS CPython)
find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Scikit-Build does not add your site-packages to the search path automatically,
# so we need to add it _or_ the pybind11 specific directory here.
execute_process(
  COMMAND
    "${Python_EXECUTABLE}" -c
    "import pybind11; print(pybind11.get_cmake_dir())"
  OUTPUT_VARIABLE _tmp_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")

find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

include_directories(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(src)

# Ignore unused variable warning from scikit-build
#set(ignoreMe "${SKBUILD}")
