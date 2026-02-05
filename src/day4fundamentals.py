# a = {"name" : "Achinthya","age" : 21}
# print(a)

# student = {"name": "Amit","age":21,"course":"engineering"}
# print(student["name"])
# student["age"]=22
# student["city"]="Delhi"
# print(student)

# marks={"math":80,"science":75,"english":85}
# print(marks.get("math"))
# print(marks.get("history",0))
# for subject,score in marks.items():
#     print(subject,score)
# marks.update({"history":70})
# print(marks)

# purchases={"Alice":250,"Bob":400,"Charlie":150}
# for name,amount in purchases.items():
#     print(f"{name} spent ₹{amount}")
# print("Total customers:",len(purchases))
# print("Cutomer names:",purchases.keys())
# print("Purchase values:",purchases.values())

#Input dictionary from user
# n=int(input("Enter number of customers:"))
# purchases={}
# for i in range(n):
#     name=input("Enter customer name:")
#     amount=int(input(f"Enter purchase amount for {name}:"))
#     purchases[name]=amount
# print("Customer purchase data:",purchases)

# top_customer=max(purchases,key=purchases.get)
# print("top spending customer:",top_customer)

# min_customer=min(purchases,key=purchases.get)
# print("lowest spending customer:",min_customer)

# top_value=max(purchases.values())
# print("top spending value:",top_value)

# min_value=min(purchases.values())
# print("lowest spending value:",min_value)

#sets
# num={1,2,3,3,4}
# print(num)
# num.add(5)
# print(num)

#Set operations
# A={1,2,3}
# B={3,4,5}
# print(A|B)
# print(A&B)
# print(3 in A)
# print(2 in B)

#task 1
# contacts={"Achinthya":"9876543210","Ankitha":"8765432109","Aravinda":"7654321098"}
# print(contacts)
# contacts["Shyamala"]="6543210987"
# print(contacts)
# contacts.update({"Achinthya":"9638520741"})
# print("Contact updated successfully")
# existing_contacts=contacts.get("Ankitha","Contact not found")
# missing_contact=contacts.get("Rama","Contact not found")
# print("Safe lookups:")
# print("Ankitha's contact:",existing_contacts)
# print("Rama's contact:",missing_contact)  
# print("All contacts:")
# for name, number in contacts.items():
#     print(f"Contact: {name} | Phone Number: {number}")

#task 2
# raw_logs=["ID01","ID02","ID01","ID05","ID02","ID08","ID01"]
# unique_users=set(raw_logs)
# print("Unique users are:",unique_users)
# print("Is ID05 in the logs?", "ID05" in unique_users)
# print("Length of original list:", len(raw_logs))
# print("Length of the unique set:", len(unique_users))

#task 3
friend_a = {"Python","Cooking","Hiking","Movies"}
friend_b = {"Hiking","Gaming","Photography","Python"}
common_interests = friend_a & friend_b
all_interets = friend_a | friend_b
unique_to_a = friend_a - friend_b
print("Common interets:",common_interests)
print("All interests:",all_interets)
print("Unique interests (Friend A):",unique_to_a)