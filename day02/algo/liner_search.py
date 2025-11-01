list_of_envs = ["dev", "staging", "prod", "test", "uat"]

key = "test"
is_Found = False

for i in list_of_envs:
    if i== key:
        print(f"Found the key: {key}")
        is_Found = True
        break
    
if is_Found:
    print("Found the key")
else:
    print("Key not found")