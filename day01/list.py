names = list(["Alice", "Bob", "Charlie", "Diana"])
print(names)

print("First name:", names[0])
print("Last name:", names[-1])

names.append("Rohit")
names.append("Reetu")
print("Updated names list:", names)

names.remove("Bob")
print("Names list after removal:", names)

print("Total names in the list:", len(names))