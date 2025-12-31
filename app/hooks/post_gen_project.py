import os, sys, shutil

#project_name = "{{ cookiecutter.project_name }}"

# We want src, test, tools as root folder, not nested in 'project_name'/.  This moves
# them up and removes aforementioned 'project_name'.

root_dir = os.getcwd()

# path to the generated folder (parent folder of the current cwd)
parent_dir = os.path.dirname(root_dir)

# 31DEC25 DEBT: Consider either using copytree or doing
# a recursion below to overwrite existing files

# move everything from root_dir up to parent_dir
for item in os.listdir(root_dir):
    # 31DEC25 Crude skip-existing code.  Only works
    # for top-level files
    src = os.path.join(root_dir, item)
    dst = os.path.join(parent_dir, item)
    if os.path.exists(dst) == False:
        shutil.move(src, parent_dir)
    else:
        os.remove(src)
        print(f"Skipping already existing {dst}")

# remove the now-empty generated folder
os.rmdir(root_dir)
