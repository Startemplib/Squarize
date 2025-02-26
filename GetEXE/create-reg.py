import os
import sys

# Get the base path of the current folder
base_path = sys.argv[1].replace(os.sep, "\\\\")
base_path = base_path[0].upper() + base_path[1:-1]

# Define the content of the .reg install file
install_reg_content = f"""Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\\*\\shell\\Squarize]
@="lemeow~"

[HKEY_CLASSES_ROOT\\*\\shell\\Squarize]
"Icon"="{base_path}\\\\Squarize.exe"

[HKEY_CLASSES_ROOT\\*\\shell\\Squarize\\command]
@="\\"{base_path}\\\\Squarize.exe\\" \\"%1\\""
"""

# Define the content of the .reg uninstall file (removing the created keys)
uninstall_reg_content = """Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\\*\\shell\\Squarize]
"""

# Specify the output file names
install_output_file = "Squarize-install.reg"
uninstall_output_file = "Squarize-uninstall.reg"

# Write the content to the install .reg file
with open(install_output_file, "w") as file:
    file.write(install_reg_content)

# Write the content to the uninstall .reg file
with open(uninstall_output_file, "w") as file:
    file.write(uninstall_reg_content)

print(f"Squarize-install.reg file has been created at {install_output_file}")
print(f"Squarize-uninstall.reg file has been created at {uninstall_output_file}")
