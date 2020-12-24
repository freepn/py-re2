cmake_minimum_required(VERSION 3.14...3.18)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/CMake)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(re2 LANGUAGES CXX C)
#include(GNUInstallDirs)

find_package(PythonInterp)
find_package(PythonLibs)
find_package(PythonExtensions)
find_package(Cython)

find_package(re2 CONFIG REQUIRED NAMES re2)

include_directories(${PROJECT_SOURCE_DIR}/src)
add_subdirectory(src)

# Ignore unused variable warning from scikit-build
set(ignoreMe "${SKBUILD}")
