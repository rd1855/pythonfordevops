import builtins
cloud_envs = ["AWS", "GCP", "Azure"]

# print(cloud_envs[4])    # This will raise an IndexError because there is no index 4 in the list.

try:
    # print(cloud_envs[4])
    print(cloud_envs[2])
    raise Exception("This is an exception raised manually") 
except:
    print("Exception handled")
finally:
    print("I will execute no matter what")
    
print("This code should execute")

try:
    print(cloud_envs[200])
    a=10
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)
    
print(dir(builtins))

    


