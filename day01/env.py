env = input("Enter the cloud platform (aws/gcp/azure): ")

if env == "aws" or env == "AWS":
    print("Setting up AWS environment...")

else:
    print("Setting up GCP/Azure environment...")
    