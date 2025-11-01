list_of_cloud = list(["aws", "azure", "gcp"])

list_of_envs = ["dev", "staging", "prod"]
list_of_envs.append("client")

for i in list_of_envs:
    print("Deployin to")
    print(i)

#Learning python using python official documentation    
#print(dir(list_of_envs))
print(list_of_envs.insert.__doc__)

list_of_envs.insert(1, "uat")
print("List after insertion:", list_of_envs)

a=2 
#print(dir(a))
print(a.bit_length.__doc__)