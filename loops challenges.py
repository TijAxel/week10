#challenge
list_of_names={'John', 'paul', 'George', 'Ringo'}
#If the name is 'George' , print 'Geore was found:'
#otherwise, print "George wa not found" and print out the other names using a loop
#Loop through the list_of_names2
list_of_names2=['Thanos', 'Ironman', 'Thor', 'Hulk']

for name in list_of_names:
    if name == 'George':
        print("George has been found!!")
else:
    print('George was not found :(')
    print(name)
for name in list_of_names2:
    if name =='Thanos':
        name=='Black Widow'
    print(name)

list_of_names2 = ['Thanos', 'Ironman', 'Thor', 'Hulk']
for i in range(len(list_of_names2)):
    if list_of_names2[i]== 'Thanos':
        list_of_names2[i]='Black Widow'
        print(list_of_names2[i])