idf_component_register(SRC_DIRS "."
    INCLUDE_DIRS "."
    REQUIRES
        {{ cookiecutter.project_name }}-lib
        cmock unity)