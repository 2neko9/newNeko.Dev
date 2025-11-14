import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="" ,
    database = "students"
)
status = True
print("\n\nThis Program simulates the CRUD operations using user's input. This is connected to a MySQL database.\n ")
while status:
    print("\n[1] Add data. [2] View data. [3] Update data. [4] Delete data. [5] Exit")
    choice = int(input("Enter your choice: "))

    mycursor = mydb.cursor()

    if choice == 1: # ADD DATA TOH!!!
        print("Please fill all Information about you!!\n")
        firstname = input("Enter your First Name               : ")
        midname =   input("Enter your Middle Name              : ")
        surname =   input("Enter your Sur Name                 : ")
        sect =      input("Enter your Section                  : ")
        addr =      input("Enter your Address                  : ")
        year =      input("Enter what Year you are currently in: ")
        age =       input("Enter your Age                      : ")
        sex =       input("Enter your Sex                      : ")
        motto =     input("What is your Motto                  : ")

        sql = "INSERT INTO information (First_Name, Middle_Name, Sur_name, Section, Address, Year, Age, Sex, Motto) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (firstname, midname, surname, sect, addr, year, age, sex, motto)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Data Inserted")

    elif choice == 2: # VIEW DATA TOH!!!
        mycursor.execute("SELECT * FROM information")
        result = mycursor.fetchall()
        for row in result:
            print(row)

    elif choice == 3: #UPDATE DATA TOH!!!
        id_choice = input("Enter what id do you want to Update: ")
        print("Please fill ALL Information about you again then change what you want to replace!!!\n")
        new_firstname = input("Enter your First Name               : ")
        new_midname =   input("Enter your Middle Name              : ")
        new_surname =   input("Enter your Sur Name                 : ")
        new_sect =      input("Enter your Section                  : ")
        new_addr =      input("Enter your Address                  : ")
        new_year =      input("Enter what Year you are currently in: ")
        new_age =       input("Enter your Age                      : ")
        new_sex =       input("Enter your Sex                      : ")
        new_motto =     input("What is your Motto                  : ")

        sql = "UPDATE information SET First_Name = %s, Middle_Name = %s, Sur_name = %s, Section = %s, Address = %s, Year = %s, Age = %s, Sex = %s, Motto = %s WHERE Id = %s"
        val = (new_firstname, new_midname, new_surname, new_sect, new_addr, new_year, new_age, new_sex, new_motto , id_choice )
        mycursor.execute(sql,val)
        mydb.commit()

        print(mycursor.rowcount, "Data Updated")

    elif choice == 4:
        id_choice = input("Enter what id you want to Delete: ")
        sql = "DELETE FROM information WHERE Id = %s"
        val = (id_choice,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Deleted")

    elif choice == 5:
        print("\nThank You!!! THE END!!!\n")
        status = False
    
    else:
        print("\nINVALID CHOICE!!! TRY AGAINN!!!\n")


status = True
print("\n\nThis Program simulates the CRUD operations using user's input. This is connected to a MySQL database.\n ")
while status:
    print("\n[1] Add data. [2] View data. [3] Update data. [4] Delete data. [5] Exit")
    choice = int(input("Enter your choice: "))

    mycursor = mydb.cursor()

    if choice == 1: # ADD DATA TOH!!!
        print("Please fill all Information about you!!\n")
        firstname = input("Enter your First Name               : ")
        midname =   input("Enter your Middle Name              : ")
        surname =   input("Enter your Sur Name                 : ")
        sect =      input("Enter your Section                  : ")
        addr =      input("Enter your Address                  : ")
        year =      input("Enter what Year you are currently in: ")
        age =       input("Enter your Age                      : ")
        sex =       input("Enter your Sex                      : ")
        motto =     input("What is your Motto                  : ")

        sql = "INSERT INTO information (First_Name, Middle_Name, Sur_name, Section, Address, Year, Age, Sex, Motto) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (firstname, midname, surname, sect, addr, year, age, sex, motto)
        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "Data Inserted")

    elif choice == 2: # VIEW DATA TOH!!!
        mycursor.execute("SELECT * FROM information")
        result = mycursor.fetchall()
        for row in result:
            print(row)

    elif choice == 3: #UPDATE DATA TOH!!!
        id_choice = input("Enter what id do you want to Update: ")
        print("Please fill ALL Information about you again then change what you want to replace!!!\n")
        new_firstname = input("Enter your First Name               : ")
        new_midname =   input("Enter your Middle Name              : ")
        new_surname =   input("Enter your Sur Name                 : ")
        new_sect =      input("Enter your Section                  : ")
        new_addr =      input("Enter your Address                  : ")
        new_year =      input("Enter what Year you are currently in: ")
        new_age =       input("Enter your Age                      : ")
        new_sex =       input("Enter your Sex                      : ")
        new_motto =     input("What is your Motto                  : ")

        sql = "UPDATE information SET First_Name = %s, Middle_Name = %s, Sur_name = %s, Section = %s, Address = %s, Year = %s, Age = %s, Sex = %s, Motto = %s WHERE Id = %s"
        val = (new_firstname, new_midname, new_surname, new_sect, new_addr, new_year, new_age, new_sex, new_motto , id_choice )
        mycursor.execute(sql,val)
        mydb.commit()

        print(mycursor.rowcount, "Data Updated")

    elif choice == 4:
        id_choice = input("Enter what id you want to Delete: ")
        sql = "DELETE FROM information WHERE Id = %s"
        val = (id_choice,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Data Deleted")

    elif choice == 5:
        print("\nThank You!!! THE END!!!\n")
        status = False
    
    else:
        print("\nINVALID CHOICE!!! TRY AGAINN!!!\n")
