import sqlite3 as sql #Import for working with sql
import xlsxwriter #for working with files
import sys  # only for exit
###Functions for backend program work###

def UserChoice():  # User Choice (where each number is functions)
    import sys  # only for exit
    print(
        "1 - add User\n2 - Show Users Info"
        "\n3 - delete user\n4 - add category"
        "\n5 - delete category\n6 - show category list"
        "\n7 - delete user from category\n8 - add category to user"
        "\n9 - exit from program"
        "\n10 - Save information to file")
    choice = int(input("> "))
    if choice == 1:
        CreateUser()  # Model of creating User
    if choice == 3:
        DeleteUser()  # Model of creating
    if choice == 6:
        ShowCategoryList()  # Model of creating
    if choice == 5:
        CategoryDelete()  # Model of category delete
    if choice == 4:
        CategoryAdd()  # Model of creating User
    if choice == 2:
        subchoice = int(
            input("if you want find user by ID, please select '1'. If you want to see all users list, enter '2': "))
        if subchoice == 2:
            ShowInfoFullUsers()  # Model of Showing Full user info
        if subchoice == 1:
            FindUserByID()  # Mobel of search user info by ID
    if choice == 7:
        DelUserCategory()  # delete category for user
    if choice == 8:
        UserGotCategory()  # Give category to user
    if choice == 9: #Exit from program
        sys.exit()
    if choice == 10:
        SaverToFile()
    if choice == 1111:  # DEBUG functions
        TestDelTables()
    # else: NOT WORKING STILL. Every time show this message after end of function
    # print("Wrong choice, man. Check your keyboard and try again :D")


def FindUserByID():  #Function for finding user by unique ID
    con = sql.connect('clients.db') #Sql connection
    with con:
        userid = input("Write User ID")
        cur = con.cursor()
        cur.execute(
            f"SELECT `rowid`, `Cname`, `Cemail`, `Cnumber`, `Cadress`,  `CategoryID` FROM `clients` WHERE rowid = {userid}")

        rows = cur.fetchall()
        for row in rows:
            print("ID: ", row[0], "Name:", row[1], "Email: ", row[2], "Number: ", row[3], "Adress:", row[4],
                  "Have product with ID:", row[5])
        con.commit() #save changes
        cur.close() #closing
        UserChoice() #returning to user choice


def CreateUser():  # Creating user
    con = sql.connect('clients.db')  # conencting to db
    with con:
        cur = con.cursor()  # turning data edit
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `clients` (`Cname` STRING, `Cemail` STRING, `Cnumber` STRING, `Cadress` STRING, `CategoryID` STRING )")  # Creating table if table not exists
        name = input("Enter Full Name\n> ")  # inputing information
        email = input("Enter email:\n> ")
        number = input("Enter Mobile Number:\n> ")
        adress = input("Enter Adress:\n> ")
        cur.execute(f"INSERT INTO `clients` VALUES ('{name}', '{email}','{number}','{adress}',NULL)")
        print("User ", name, " sucessfully added")
        con.commit()  # save
        cur.close()  # close connection
        UserChoice()  # returning to userchoice


def DeleteUser():  # Delete user
    con = sql.connect('clients.db')  # connecting to db
    with con:
        ShowUsers()
        uid = input("Write User ID, that you want delete: \n> ")  # inputing information
        cur = con.cursor()
        cur.execute(f"DELETE FROM `clients` WHERE `rowid`={uid}")  # insert input informaation to table
        print("User with ID " + uid + " " + " sucessfully deleted")
        con.commit() # save
        cur.close()  # close connection
        UserChoice()  # returning to userchoice


def ShowInfoFullUsers():  # Showing all users (with additional info)
    con = sql.connect('clients.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT `rowid`, `Cname`, `Cemail`, `Cnumber`, `Cadress`,  `CategoryID` FROM `clients` ")
        # part of code for showing information from db as Massiv

        rows = cur.fetchall()
        for row in rows:
            print("ID: ", row[0], "Name:", row[1], "Email: ", row[2], "Number: ", row[3], "Adress:", row[4],
                  "Have product with ID:", row[5])
        con.commit()
        cur.close()
        UserChoice()


def ShowInfoQuickUsers():  # Showing all equipment info
    con = sql.connect('clients.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT `rowid`, `Cname` FROM `clients` ")
        # part of code for showing information from db as Massiv

        rows = cur.fetchall()
        for row in rows:
            print("ID: ", row[0], "Name:", row[1])
        con.commit()
        cur.close()


def CategoryAdd():
    con = sql.connect('clients.db')  # conencting to db
    with con:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS `category` ( `catName` STRING, `catDesc` STRING)")  # Creating table if table not exists

        name = input("Category name is\n> ")
        desc = input("Category description is\n> ")
        cur.execute(f"INSERT INTO `category` VALUES ( '{name}','{desc}')")
        print("Category " + name + " sucessfully added")
        con.commit()
        cur.close()
        UserChoice()


def CategoryDelete():  # Delete
    ShowCategoryList()
    con = sql.connect('clients.db')  # connecting to db
    with con:
        eid = input("Write Equipment ID \n> ")  # inputing information
        cur = con.cursor()
        cur.execute(f"DELETE FROM `category` WHERE `rowid`={eid}")  # deleting rows with choosen ID
        print("Category with ID " + eid + " " + " sucessfully deleted")
        con.commit()
        cur.close()
        UserChoice()


def ShowCategoryList():  # Showing all users
    con = sql.connect('clients.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT `rowid`, `catName`, `CatDesc` FROM `category` ")
        rows = cur.fetchall()
        for row in rows:
            print('Category ID:', row[0], 'Name:', row[1], 'Description:', row[2])
        con.commit()
        cur.close()
        # UserChoice()


# Таблица где есть ClientID И EquipmentID
# выбираем чувака типо есть лист пользователей
# введите ID пользователя, потом выбираем селектом это пользователя и пихаем в переменную
# Just written for myself, doesnt matter for code
def UserGotCategory():  # giving equipment to user
    con = sql.connect('clients.db')  # conencting to db
    with con:
        cur = con.cursor()
        ShowCategoryList()
        eid = (input("Choice category ID\n> "))
        ShowInfoQuickUsers()
        userid = int(input("Choice user ID\n> "))  # inputing information
        cur.execute(
            f"UPDATE clients SET CategoryID = '{eid}' WHERE rowid = '{userid}' ")  # old var#(f"INSERT INTO `orders` (`UserID`,`EquipmentID`) SELECT `rowid` FROM `clients` WHERE `rowid`= {userid}") #not work JOIN (SELECT `IDCODE` FROM `equipment` WHERE `IDCODE`= {eid}) ")
        print("Client with ID ", userid, " sucessfully got category with ID ", eid)
        con.commit()
        cur.close()
        UserChoice()


def DelUserCategory():  # giving equipment to user
    con = sql.connect('clients.db')  # conencting to db
    with con:
        cur = con.cursor()
        ShowUsers()
        userid = int(input("Choice user ID\n> "))
        cur.execute(
            f"UPDATE clients SET CategoryID = NULL WHERE rowid = '{userid}' ")  # old var#(f"INSERT INTO `orders` (`UserID`,`EquipmentID`) SELECT `rowid` FROM `clients` WHERE `rowid`= {userid}") #not work JOIN (SELECT `IDCODE` FROM `equipment` WHERE `IDCODE`= {eid}) ")
        print("Client with ID ", userid, " not have more category")
        con.commit()
        cur.close()
        UserChoice()


def TestDelTables():  # for debugg
    con = sql.connect('clients.db')
    with con:
        cur = con.cursor()
        UserCh = int(input(
            "Deleting Tables and check. Only for debugging. Write number of table, where  2 is equipments, 3 is clients, 4 showing all tables"))
        mes = print('Table with id', UserCh, ' deleted sucesfully')
        if UserCh == 2:
            cur.execute("DROP TABLE `category` ")
            mes
        if UserCh == 3:
            cur.execute("DROP TABLE `clients` ")
            mes
        if UserCh == 4:
            cur.execute("SELECT * FROM `clients`, `category` ")

        con.commit()
        cur.close()


def SaverToFile():
    import sqlite3
    from xlsxwriter.workbook import Workbook
    workbook = Workbook('clients.xlsx')
    worksheet = workbook.add_worksheet()

    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("select `rowid`, `Cname`, `Cemail`, `Cnumber`, `Cadress`,  `CategoryID`  from clients")
    mysel = c.execute("select `rowid`, `Cname`, `Cemail`, `Cnumber`, `Cadress`,  `CategoryID`  from clients")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, value)
    workbook.close()
