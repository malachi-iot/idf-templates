idf_component_register(SRCS "main.cpp"
    INCLUDE_DIRS "."
    REQUIRES {{ cookiecutter.project_name }}-lib
)
