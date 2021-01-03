set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

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

if (SKBUILD)
  find_package(PythonExtensions REQUIRED)
  find_package(Cython REQUIRED)
endif(SKBUILD)

set(cython_module re2)

set(re2_include_dir "${PROJECT_SOURCE_DIR}/src")
set(cython_output "${CMAKE_CURRENT_SOURCE_DIR}/${cython_module}.cpp")
set(cython_src ${cython_module}.pyx)
# Track cython sources
file(GLOB cy_srcs *.pyx *.pxi *.h)

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

add_library(${cython_module} MODULE ${cython_output})
set(site_packages "${PYTHON_RELATIVE_SITE_PACKAGES_DIR}")

if (SKBUILD)
  python_extension_module(${cython_module})
  install(TARGETS ${cython_module} LIBRARY DESTINATION ${site_packages})
else (SKBUILD)
  set_target_properties(${cython_module} PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
	    SUFFIX "${PYTHON_MODULE_EXTENSION}")
  set_target_properties(${cython_module} PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR})
endif(SKBUILD)

target_compile_definitions(${cython_module} PRIVATE PY2=0)
target_link_libraries(${cython_module} re2::re2)
