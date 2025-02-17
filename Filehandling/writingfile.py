import json
import csv


employees = [
    ["Name", "Age", "Salary"],
    ["Alice", 25, 50000],
    ["Bob", 30, 60000],
    ["Charlie", 35, 70000]
]



employee = {
    "name" : "Bob",
    "age" : 32,
    "job" : "waiter"
}

txt_data = "I like pizza"
# new .txt / .json / .csv
file_path = "C:\\Users\\sacha\\OneDrive\\Desktop\\New folder\\new.csv"

# def writingloop(list_,file):
#     for element in list_:
#         file.write(element + " ")



# with open(file_path, "w") as file:
#     file.write("\n" + txt_data + " ")
#     writingloop(employees,file)
#     print(f"text file :{file_path} was created")

# with open(file_path, "a") as file:
#     json.dump(employee, file, indent=4)
#     print(f"json file :{file_path} was created")


# "w" will create a new file and overwrite the file that was existing
try :
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file :{file_path} was created")
except FileExistsError:
    print("That file already exists ! ")

