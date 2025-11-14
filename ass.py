choice = True
name = []


while(choice == True):
    
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    name1 = (lname.capitalize() + ", " + fname.capitalize())
    name.append(name1)
    name = sorted(name)
    ch = input("Do another entry? (Y/N)").strip().upper()
    if ch == 'N':
        choice = False
    elif ch == 'Y':
         choice = True
    else:
        choice = False

    
print("\n  NAMES")
for i in range(len(name)):
 	print (i+1, name[i])
print("Total No. of Entries: ", len(name))

