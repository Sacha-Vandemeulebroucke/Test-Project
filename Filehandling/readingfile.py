import csv
import json
file_path = "C:\\Users\\sacha\\OneDrive\\Desktop\\New folder\\new.csv"


try :
    with open(file_path, "r") as file:
        # content = json.load(file)
        content = csv.reader(file)
        # content = file.read()
        for line in content:
            print(line)
        print(content)

except FileNotFoundError:
    print(f"The file {file_path} was not found")