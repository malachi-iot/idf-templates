import os, sys, shutil

#project_name = "{{ cookiecutter.project_name }}"

# We want src, test, tools as root folder, not nested in 'project_name'/.  This moves
# them up and removes aforementioned 'project_name'.

root_dir = os.getcwd()

# path to the generated folder (parent folder of the current cwd)
parent_dir = os.path.dirname(root_dir)

# move everything from root_dir up to parent_dir
for item in os.listdir(root_dir):
    shutil.move(os.path.join(root_dir, item), parent_dir)

# remove the now-empty generated folder
os.rmdir(root_dir)
