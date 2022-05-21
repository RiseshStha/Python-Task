#QS_1
# a = ' "Python is a great language!",said Fred.\n "I dont ever remember having this much fun before. " '
# print(a)
#QS_2
# a = int(input("Enter a year: "))
# if a % 4 ==0 and (a % 400 !=0 and a % 100 != 0):
#     print("Its a leap year")
# else:
#     print("It is not a leap year")
#QS_3
# a = "ram"
# b = "are"
# count = 0
# for i in a:
#     for j in b:
#         if i == j:
#             count += 1
            
# if count == len(a):
#     print("Anagram")
# else:
#     print("NOt Anagram")  
#     Input two strings from the user.
# Initialize count=0.
# Using for loop, if i==j then count is increased by 1.
# Using if condition to compare the length of a with count, if true print “it is anagram”.
# Exit 
# #QS_4
# list = []
# list.append("Hari")
# list.append("Pari")
# print(list)
# print(id(list))
# list.append("Risesh")
# print(list)
# print(id(list))
# print("First item: ",list[0])
# print("Second item: ",list[1])
#QS_5
# firstName = "Risesh",
# lastName = "Shrestha",
# list = []
# list.append(firstName)
# list.append(lastName)
# print(list)
# print("First item: ",list[0])
# print("Second item: ",list[1])
# #QS_6
# list = ["John", "hari", "Raj","Rocky"]
# for i in list:
#     if i == "John":
#         print("Found")
#         break
# else:
#         print("Not found")
#QS_7
listFirstName = ["Rocky", "Pari","Pra"]
listLastName = ["Thapa", "Koju","Thapa"]
age = [13,19,19]
sum = 0;
average = 0
for i in age:
    # if age[i] == "None":
    #     pass
    sum += i
    i += 1
    
print("Average age is: ", sum/3)

    
    
      

