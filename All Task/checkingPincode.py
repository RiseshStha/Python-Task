username = input("Enter your name :")
password = int(input("Enter password : "))

for i in range(0,3):
    print("enter your credentials")
    username1=input("Enter your username")
    password1= input("Enter your password :")
    if username==username1 and password==password1:
        print("You are successfully logged.")
        break
    else:
        if(username!=username1 or password!=password1):
            print("Invalid Credentials")
else:
    print("attempt finished")
    
    #Hw
    #Use loop to solve problems
    #print ****
    #print
    #*
    # **
    # ***
    # ****
    # *****
    #print
    #******
    # *****
    # ****
    # ***
    # **