#set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# this looks outside tox venv and finds python39 (which is not active)
#find_package(Python REQUIRED)
set(cython_module re2)

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


# aaand this barfs no matter what the arguments are
# add_cython_target(${cython_module} re2.pyx CXX PY3 OUTPUT_VAR re2.cpp)
#add_cython_target(${cython_module} re2.pyx OUTPUT_VAR sources)
#add_library(${cython_module} MODULE ${sources})
add_library(${cython_module} MODULE ${cython_output})
python_extension_module(${cython_module})

set(site_packages "${PYTHON_RELATIVE_SITE_PACKAGES_DIR}")

target_compile_definitions(${cython_module} PRIVATE PY2=0)
target_link_libraries(${cython_module} re2::re2)
install(TARGETS ${cython_module} LIBRARY DESTINATION ${site_packages})
