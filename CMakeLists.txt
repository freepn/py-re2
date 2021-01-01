cmake_minimum_required(VERSION 3.14...3.18)

project(re2 LANGUAGES CXX C)
include(GNUInstallDirs)

find_package(PythonInterp)
find_package(PythonLibs)

# TODO finish the required `find_` bits below in case skbuild is missing
if(NOT SKBUILD)
  message(FATAL_ERROR "Building requires scikit-build")
else()
  find_package(PythonExtensions)
  find_package(Cython)
endif()


find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

include_directories(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(src)

# Ignore unused variable warning from scikit-build
#set(ignoreMe "${SKBUILD}")
