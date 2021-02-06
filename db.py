import sqlite3

connection = sqlite3.connect("identity.db")
cur =connection.cursor()
'''
   

    cur.execute("CREATE TABLE identity(\
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
    Names VARCHAR(200) UNIQUE NOT NULL,\
    Nid VARCHAR(27) NOT NULL UNIQUE,\
    Email VARCHAR(200) DEFAULT 'NOT CONFIGURED' )")
'''
print("WELCOME TO BANK ACCOUNT MANAGEMNET\n***********************************\n")
try:
    choice = int(input("Enter\n 1. To add a user\n 2. To preview users\n 3. To delete a user\n\t\t\t=>"))
    if choice == 1 :
        Enames = str(input("Enter The New User's Names:\t"))
        ENid = str(input("Enter Your Account Id     :\t"))
        Email =str(input("Enter Your Email          :\t"))
        cur.execute("INSERT INTO identity(Names,Nid,Email) VALUES(?,?,?)",(Enames,ENid,Email))
        connection.commit()
        cur.execute("SELECT * FROM identity WHERE Nid=?",[ENid])
        var = cur.fetchall()
        print("\n\n-------------------------------------------------------\n")
        print("Your User database Id :\t %d"%var[0][0])
        print("Your Names are        :\t %s"%var[0][1])
        print("Your Email Address is :\t %s"%var[0][3])
        print("Your Account Number   :\t %s"%var[0][2])
        print("--------------------------------------------------------\n")
    if choice == 2:
        cur.execute("SELECT * FROM identity")
        var = cur.fetchall()
        for row in var:
            print("----------------")
            for col in row:
                print("  |  {0}  ".format(col))
                # print(col)
    if choice == 3:
        delet = int(input("enter Bank DB Id of the user:\n"))
        
        cur.execute("DELETE  FROM identity WHERE Id=? ",[delet])
        cur.execute("SELECT Id FROM identity WHERE Id =?",[delet])
        vardel = cur.fetchall() 
        connection.commit()  
        # connection.close()
        #cur.close() 
        #print(vardel)
        if vardel == []:
            print("User Deleted Sucessfully or non-existing User")
            
        else:
            print("No such User In Our DATABASE\n\n Please ADD HIM")
except ValueError:
    print("The choice is not taken into consideration\nBye Database Administrator\nShutting Down")