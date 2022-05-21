print("Set your name and Pincode")
user = input("Enter your name: ")
pincode = int(input("Enter your pincode:"))
print("Verifying your Details...")
print("Enter your Details")
user1 = input("Name: ")
pincode1 = int(input("Pincode: "))
if user == user1 and pincode == pincode1:
    print("Verified!!")
else:
    print("Invalid Name Or Pincode")
    