#Question 1
age= int(input("How old are you? "))
member= input("Are you a member?Y/N?: ")

if age <18:
    print("Youth ticket price is $10")
 
if age >=18 and age <65 and member=="Y":
    print("Discounted adult ticket price is $12")
if age >=18 and age <65 and member=="N":
    print("Regular adult ticket price is $15")
if age >=65:
    print("Senior discount price is $8")




#Question 18
length= int(input("What is the length of your password?: "))
special=(input("Does your password have any special charcters? Yes or No?: "))

if special == "Yes" or "yes": #this part will create a readable yes or no varaible for the computer
    special=1
else:
 special=0

if length > 12 and special:
    print("Very nice long and strong password")
elif length >= 12:
    print("Consider adding special characters")


if (8<=length<=12) and special :
    print("Moderate password strength")
elif 8<=length<=12 :
    print("Weak password. Consider adding special characters")
if length < 8:
    print("Password is too short.")