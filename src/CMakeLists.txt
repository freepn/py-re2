find_package(re2 CONFIG REQUIRED NAMES re2)
find_package(Threads REQUIRED)

find_package(pybind11 CONFIG REQUIRED)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/CMake)
#find_package(PythonLibs REQUIRED)
find_package(Cython)
set(CMAKE_VERBOSE_MAKEFILE ON)
set(cython_module re2)

#set_source_files_properties(
  #"${CMAKE_CURRENT_SOURCE_DIR}/${cython_module}.pyx"
  #PROPERTIES CYTHON_IS_CXX TRUE )

set(re2_include_dir "${PROJECT_SOURCE_DIR}/src")
set(cython_output "${CMAKE_CURRENT_SOURCE_DIR}/${cython_module}.cpp")
set(cython_src ${cython_module}.pyx)
# Track cython sources
file(GLOB cy_srcs *.pyx *.pxi *.h)

# Dont add build to RPATH
#set(CMAKE_SKIP_BUILD_RPATH TRUE)

# .pyx -> .cpp
add_custom_command(OUTPUT ${cython_output}
                   COMMAND ${CYTHON_EXECUTABLE}
                           -a -3
                           --fast-fail
                           --cplus -I ${re2_include_dir}
                           --output-file ${cython_output} ${cython_src}
                   WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                   DEPENDS ${cy_srcs}
                   COMMENT "Cythonizing extension ${cython_src}")

pybind11_add_module(${cython_module} ${cython_output})
target_compile_definitions(${cython_module} PRIVATE VERSION_INFO=${SCM_VERSION_INFO})
target_compile_definitions(${cython_module} PRIVATE PY2=0)

target_compile_features(${cython_module} INTERFACE cxx_std_11)
target_link_libraries(${cython_module} PRIVATE re2::re2)

#pybind11_add_module(${cython_module} ${cython_output})
#add_library(${cython_module} SHARED ${cython_output})

#set_target_properties(${cython_module} PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
#      SUFFIX "${PYTHON_MODULE_EXTENSION}")
#set_target_properties(${cython_module} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})

#target_compile_definitions(${cython_module} PRIVATE VERSION_INFO=${SCM_VERSION_INFO})
#target_compile_definitions(${cython_module} PRIVATE PY2=0)

#target_compile_features(${cython_module} INTERFACE cxx_std_11)
#target_link_libraries(${cython_module} PRIVATE re2::re2)

#install(TARGETS ${cython_module} LIBRARY DESTINATION ${site_packages})
