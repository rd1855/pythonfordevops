server1 = {
    "env":"dev",
    "server":"aws",
    "db":"mysql",
    "ram":"8gb",
    "cpu":"4cores",
    "active":True,
}

server2 = {
    "env":"staging",
    "server":"azure",
    "db":"postgresql",
    "ram":"16gb",
    "cpu":"8cores",
    "active":False,
}

env_details = [server1, server2]

for env in env_details:
    for key,value in env.items():
        if key == "active" and value == True:
            print(env.values())


print("Server Environment:", server1["env"])
print(server1.get("active"))
if server1.get("active"):
    print("Server Details:")
    for key in server1:
        print(f"{key}: {server1[key]}")
        
