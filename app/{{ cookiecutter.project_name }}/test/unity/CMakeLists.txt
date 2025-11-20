cmake_minimum_required(VERSION 3.21)

include(../../tools/esp-idf/setenv.cmake)

set(TEST_COMPONENTS "{{ cookiecutter.project_name }}-lib" CACHE STRING "List of components for Unity to pick up")

list(APPEND EXTRA_COMPONENT_DIRS ${ROOT_DIR}/src/components)

# setenv sets COMPONENTS purely to main which is generally a good optimization.  Here
# we need to bring in TEST_COMPONENTS too, since we aren't generally specifying them
# in REQUIRES clause
set(COMPONENTS main ${TEST_COMPONENTS})

include($ENV{IDF_PATH}/tools/cmake/project.cmake)

project({{ cookiecutter.project_name }}-unity)
