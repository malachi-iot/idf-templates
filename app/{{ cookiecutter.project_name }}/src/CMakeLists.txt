cmake_minimum_required(VERSION 3.21)

include(../tools/esp-idf/setenv.cmake)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)

project({{ cookiecutter.project_name }})
