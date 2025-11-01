tuple_of_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# print(tuple_of_days)
# print(list_of_days)


#tuple_of_days[1]=="Tue"   //Tuples are immutable
print(tuple_of_days)

list_of_days[1]=="Tue" # Lists are mutable
print("List before modification:", list_of_days)
list_of_days[1]="Tue"
print("List after modification:", list_of_days)
