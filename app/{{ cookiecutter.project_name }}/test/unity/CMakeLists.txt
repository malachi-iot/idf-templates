cmake_minimum_required(VERSION 3.21)

include(../../tools/esp-idf/setenv.cmake)

LIST(APPEND EXTRA_COMPONENT_DIRS ${ROOT_DIR}/src/components)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)

project({{ cookiecutter.project_name }}-unity)
