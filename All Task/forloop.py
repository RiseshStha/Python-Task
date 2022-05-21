# from operator import le


# for i in range(100):
#     print("Hello World")
    
# print("Python")
# print("hello world\n" * 10)  #not loop

# for a in range(500):
#     print("Python")  
    
# for b in range(20):
#     print("hello world")
#     #explain range function with example.
    
# a = "Risesh"
# for i in range(5):
#     print(a)
#     print()
    
# for letter in a:
#     print(letter)
    
# from re import L


# i = 0
# for i in range(51):
#     print(i)
#     i+=1
# a = "Python"   
# for letter in a:
#     print(a.index(letter),letter, sep="=")
   

# for i in range(1,11):
#     print('2',"*", i,'=',i*2)
    
# for i in range(10,0,-1):
#     print('2',"*", i,'=',i*2)
# else:
#     print("Hello Python")# else will execute even if condition will be false.
   
# st = "Python" 
# for i in st:
#     print(i)
# else:
#     print("Hello")
    
# a = "Python"
# for i in range(-1,-(len(a)+1),-1):
#     print(a[i])  
    
# b = "Python"[::-1]  # reverse
# print(b)
# user = input("Enter your id: ")
# pinNUmber = int(input())

# if():
# a = [1,2,3,4][::-1] 
# print(a)

# a = [1,2,3,4]
# for i in range(3,-1,-1):
#     print(a[i])   
# for i in reversed(a):
#     print(i)
# for i in reversed(a):
#     a.append(i)
# print(a)# append insert value at last for eg 5 is printed first then  
# reversed_list = [5]
# for i in reversed(a):
#     reversed_list.append(i)
# print(reversed_list)

#   Adding Numbers In List. 
# a = [1,2,3,4,5]
# sum = 0
# for i in (a):
#     sum += i  # or sum = sum + i
# print(sum)
# sum = 1
# for i in (a):
#     sum *= i
# print(sum)

user = int(input("ENter a number :"))
if user > 1:
    for i in range(2, user): # i is started from 2 because range is given. (2, user)
        if user % i==0:
            print(" is not Prime number")
            break
    else:
            print("prime number")
    





    