# Importing os library to use operating system dependent functionality
import os
# Take file path where it have all the packages(distributions)
file_path = "dependencies.txt"
# Read file
dependencies = open(file_path,"r")
# Initializing dictionary to store the successfully installed and failed packages
result = {"success": [], "failure": []}
# This loop will install packages line by line using pip package manager
for package in dependencies:
    response = os.system("pip install "+package)
    # This condition  will append packages based on os response value
    if (response == 0):
        result["success"].append(package)
    elif (response > 0):
        result["failure"].append(package)
# This condition will return success if all the packages are installed successfully
# Else return packages which are failed to install
if len(result["failure"]) == 0:
    print("All the packages are installed successfully")
else:
    for failed in result["failure"]:
        print(failed," is failed to install.")
