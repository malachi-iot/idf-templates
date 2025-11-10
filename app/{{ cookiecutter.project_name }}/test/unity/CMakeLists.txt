cmake_minimum_required(VERSION 3.21)

include(../../tools/esp-idf/setenv.cmake)

set(TEST_COMPONENTS "{{ cookiecutter.project_name }}-lib" CACHE STRING "List of components for Unity to pick up")

LIST(APPEND EXTRA_COMPONENT_DIRS ${ROOT_DIR}/src/components)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)

project({{ cookiecutter.project_name }}-unity)
