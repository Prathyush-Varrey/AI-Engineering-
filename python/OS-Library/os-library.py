"""
Os lib is able to interact with our OS and can let us work with Multiple
Directories and files


"""

import os

current_path = os.getcwd()
#print("Current Working Directory is: ", current_path)

# mkdir() -> helps to create the directory

new_path = "New_Folder"
#os.mkdir(new_path)
print(f"The new directory {new_path} id created successfully")

#listdir() -> use for listing all the directories present
all_list = os.listdir('.')
#print(all_list)

# joining multiple paths togeather

#os.path.join()

dir_name = "folder_data"
file_name = "file_data"
full_path = os.path.join(dir_name, file_name)
#print(full_path)


# join multiple path with current path
current_full_path = os.path.join(os.getcwd(),dir_name,file_name)
#print(f"The Current Full Path is: {current_full_path}")

## os.path.exists()
given_path = 'python\OS-Library'
if os.path.exists(given_path):
    print("Yes path exists")
else:
    print("Path Does not exist")
check_file = os.path.isfile("python\OS-Library\os-library.py")
check_folder = os.path.isdir("python")
print(check_file)
print(check_folder)

check_file =  os.path.isfile("python")
check_folder =  os.path.isdir("python\OS-Library\os-library.py")
print(check_file)
print(check_folder)

print(os.path.abspath("os-library.py"))