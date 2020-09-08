## For this homework, the user puts 10 numbers and the code will calculate some general statstics about from them. 

mylist = []        #Start out with an empty list. This will be used to store the ten numbers.
count = 0          #I am using a while loop and I want to stop the loop when the count reach ten. 
while True:
  if count == 10: 
    break

  mynumber = input(f"Please enter an integer:  ")
  try:
    mynumber = int(mynumber)
    mylist.append(mynumber)
    count = count + 1
  except:
    print("You have entered a non-integer. Please try again!")
#for i in range(0, 3):
#  mynumber = int(input())
#  mylist.append(mynumber)
list_sort =sorted (mylist)     #I decided to use the sort function to sort out my list members. I figured it may be easier to than comparing one member with the other. 
# print(mylist)
print(list_sort)
print("Average: ", sum(list_sort)/len(list_sort))
print("Maximum : ", list_sort[-1])
print("Minimum : ", list_sort[0])
print("Range : ", list_sort[-1] - list_sort[0])    #The difference between the first in the sort list and the last in th sorted list. 
MyMean = sum(list_sort)/len(list_sort)
Variance = sum([((x-MyMean)**2) for x in list_sort])/len(list_sort)
Standard_dev = Variance**0.5
print("Variance : ", Variance)
print("Standard Deviation : ", Standard_dev)