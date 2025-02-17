import os

file_path = "test.txt"
file_path2 = "folder/test.txt"

if os.path.exists(file_path):
    print(f"It exists {file_path}")

    if os.path.isfile(file_path):
        print("This is a file")

    if os.path.isdir(file_path):
        print("This is a folder")
else:
    print("The location does not exist")