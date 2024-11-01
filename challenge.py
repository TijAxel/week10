score=int(input("What was your score?: "))

while score >= 0: #if your score is between or equal to the set numbers execute that code
 if score >89 and score <101:
   print("A, excellent") #if your score is between or equal to the set numbers execute that code
if score > 79 and score< 90 : #if your score is between or equal to the set numbers execute that code
    print("B, good job!")
if score>61 and score <80 : #if your score is between or equal to the set numbers execute that code
    print("C, You passed")
if score <60 and score >=0:
   print("D, You failed")#if your score is between or equal to the set numbers execute that code
   
else:
 print("Your score cant be negative")# if your score is none of the above then execute this code
print("try again")



# #problem 2

start=int(input("Please enter the starting number:"))#asks the user for the start number
end=int(input("Please enter the ending number:"))# asks the user for the end number
newend=(end + 1)# adds one to the end number because when put in a range the range takes the number before the one you entered

for i in range(start, newend): #print the numbers in between the start and stop 
    print(i)


for i in range(start, newend): # print the numbers in between the start and stop only if the are even and greater than 10
    if (i % 2 == 0) and i > 10:
        print(i)

for i in range(start, newend): #print the numbers in between the start and stop only if the are odd and less than 20
    if (i % 2 ) and i < 20:
        print(i)