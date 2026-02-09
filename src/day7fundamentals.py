#task 1 
# name = input("Enter your name: ")
# goal = input("Enter your daily goal: ")
# with open("journal.txt", "a") as file:
#     file.write(f"Name: {name}, Daily Goal: {goal}\n")
# print("Entry saved successfully.")

#task 2
# import csv 
# with open("students.csv","r")as file:
#    reader = csv.DictReader(file)
#    print("Students who passed:")
#    for row in reader:
#         if row["Status"] == "Pass":
#             print(row["Name"])

#task 3
filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")