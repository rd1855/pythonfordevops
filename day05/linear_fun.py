def linear_search(list_of_envs,key):
    is_Found = False

    for i in list_of_envs:
        if i== key:
            is_Found = True
    
    return is_Found

# list_of_envs = ["dev", "staging", "prod", "test", "uat"]
# key = "test"

# found = linear_search(list_of_envs,key)
# print(found)