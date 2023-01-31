import sys
import time
import mysql.connector
import os
import maskpass
import Config 
from Config1 import save1 as save1
from Config import keys_stored as keys



version = "1.0.0 : 22-01-2023 "


def tips():
    print("\nAn error occured!")
    time.sleep(0.6)
    print("\n ~ Try using the keywords mention within brackets - ()")
    time.sleep(0.5)
    print("\n ~ Try closing the program and restarting it")
    time.sleep(0.5)
    print("\n ~ Check your connection to the server")
    time.sleep(0.5)
    print("\n ~ Contact Admin and make sure server is running properly.")
    time.sleep(0.5)
    restart()


def restart():
    restart = input("\nRestart the program? \n YES [Y] NO [N] \n  ")
     
    if restart == 'Y':
        use_same = input("Restart using same credential? \n [Y]  [N]\n  ")
        if use_same == 'Y':
            get_Cred(get_key_dup)
        else :
            use_svdCred(1)

    else:
        pass

 

def shutdown_error():
    i = 5
    while i > 0:
        print("Exiting in ", i, "seconds")
        i -= 1
    print("EXIT")
    sys.exit("Program is SHUTDOWN because a FATAL ERROR OCCURED!")

def start_frame():
    str_1 = "Welcome to Library System"
    print(str_1.center(100))
    str_5 = "Verison is "+version
    print(f"{str_5:>110}")

def view(mycursor,TABLE):
    view_db = input("View Database? \nYes[Y]  No[N] \n  ")
    if view_db == 'Y':
            str_6 = "SELECT * FROM %s"%TABLE
            mycursor.execute(str_6)
            result = mycursor.fetchall()
            how_fast = input("Enter the speed at which results are display.\n |Some table may contain a lot of records. In such situation customizing speed is advised].\n [Default is 0.5 secs per record.]\n [Leave blank or any non-numerical value to use default]\n  ")
            while how_fast != "" and how_fast != " ":
                while  type(how_fast) == 'int'  or type(how_fast) == 'float' :
                    for x in result:
                        print(x)
                        time.sleep(how_fast)
                break
            for x in result:
                print(x)
                time.sleep(0.5)

            
    else:
        pass
    restart()


 

def end_frame(mycursor,TABLE,mydb):
    view(mycursor,TABLE)
    time.sleep(0.2)
    print("Ending session...")
    mycursor.close()
    mydb.close()
    time.sleep(0.4)
    str_4 = "Session ENDED"
    print(str_4.center(100))

def frame(mycursor, mydb,TABLE):
    start_frame()
    time.sleep(0.2)
    multi = input("\nChoose type of Entry - Single (s) or Multiple (m) :")
    multi.casefold()
    if multi == 's':
        main(mycursor, mydb,TABLE)
        end_frame(mycursor,TABLE)
    elif multi == 'm':
        main(mycursor, mydb,TABLE)
        main(mycursor, mydb,TABLE)
        Multiple(mycursor, mydb,TABLE)
        end_frame(mycursor,TABLE,mydb)
    else:
        tips()

def enter_data(name_b, author_b, total_b, available_b, mycursor, mydb,TABLE):
  
    sql = "INSERT INTO  %s (name, author,total,available) VALUES (%%s, %%s,%%s,%%s);"%TABLE
    val = (name_b, author_b, total_b, available_b)
    mycursor.execute(sql, val)
    mydb.commit()

def main(mycursor, mydb,TABLE):
    try:
        str_2 = "-"
        print(str_2.center(50, '-'))
        time.sleep(0.2)
        name_b = input("\nEnter the name of the book : ")
        time.sleep(0.2)
        author_b = input("Enter the Name of the author :")
        time.sleep(0.2)
        total_b = input(("Enter the Total numbers of copies :"))
        time.sleep(0.2)
        available_b = input("Enter the currently available number of copies: ")
        while name_b and author_b and total_b and available_b != "":
            enter_data(name_b, author_b, total_b,available_b, mycursor, mydb, TABLE)
            time.sleep(0.3)
            print("\nData entry successful!")
            print(str_2.center(50, '-'))
            break
    except TypeError as error :
        print("Error LID - 04",error)
        restart()

def Multiple(mycursor, mydb,TABLE):
    another_entry = input("Do another entry? (y/n): ")
    another_entry.casefold()
    if another_entry == 'y':
        main(mycursor, mydb,TABLE)
        Multiple(mycursor, mydb,TABLE)

    elif another_entry == 'n':
        pass

    else:
        print("Error occured LID - 03")
        restart()

def checkTableExists(dbcur, tablename,mydb):
     
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        
         
        print("Requested database table does EXISTS...")
        return True
    print("Requested database table does NOT EXIST...")
    print("Creating a table...")
    dbcur.execute("CREATE TABLE IF NOT EXISTS  %s (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), author VARCHAR(255), total VARCHAR(255), available VARCHAR(255))"%tablename)
 
    return False

def save0(HOST,USER,PASSWORD,DATABASE,TABLE):
    ask_2save = input("Save Credentials? \n |Your credentials will be encrypted and safely stored for quick access in future...|\n  [Y] [N]\n  ")
    try :
        if ask_2save == 'Y':
            save1(HOST,USER,PASSWORD,DATABASE,TABLE)
        else:
            pass
    except Exception as error:
        print("Error LID - 01 :\n    ",error)
    finally:
        pass

def get_Cred(get_key) :
    try:
        key_list = Config.key_list
        get_key = int(get_key)
        final_key = key_list[get_key]
        print('final ',final_key)
        setup(**final_key)
    except Exception as error:
        if '1045 (28000)' in str(error):
            print("\nAccess to Server was Denied. Try Checking User Name Password combo.")
            time.sleep(1)
        else:
            print("Error  LID - 07 : \n  ",error) 
        tips()
     


 
def use_svdCred(stat):
    if stat == 0 :
        return 
    ask_2useCred = input("Use a locally stored Credntial? \n [Y] [N]\n  ")
    if ask_2useCred == 'Y':
        try:
            print("Here's what we found ....")
            time.sleep(0.3)
            print("Total Credentials stored - ",keys,"\n")
            if keys != 0 :
                show_key(keys)
            else:
                print('No Credntials found')
                config_(0)
        except TypeError :
            print("Error LID - 02 : \n   ",error)
            
    else:
        config_(0)

def show_key(keys):
    try:
        key_list = Config.key_list
        key_opt =[]
        for key0 in range(0,keys):
            key_opt.append(key0)
        i = 0 
        for values in key_list :
            values = str(values)
        
            print(key_opt[i],' ~ '," [",values.strip('}{').replace('[', '').replace(']', '').replace("'","").replace(","," | "),"] ")
            i +=1
            time.sleep(0.6)
 
 
        
        print("\nChoose a set ")
        print(key_opt)
        global get_key_dup
         
        get_key = get_key_dup =input("")
        get_Cred(get_key)
    except Exception as error :
        print("Error LID -06 \n   ",error)

def setup(HOST,USER,PASSWORD,DATABASE,TABLE):
    time.sleep(0.2)
    print("Starting up...")
    try:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
            )

        mycursor = mydb.cursor()

    except:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pma",
            password="pma_user560",
        )

        mycursor = mydb.cursor()
        print("Requested database does not exist...\nCreating a database...")
        mycursor.execute("CREATE DATABASE %s" %DATABASE)
        
    
    finally:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
            )

        mycursor = mydb.cursor()
        time.sleep(0.2)
        print("SQL connection successful...")
        time.sleep(0.2)
        print("Checking database...")
        
        checkTableExists(mycursor,TABLE,mydb)
        time.sleep(0.2)
        
        #print("Error!... \nCreating a temporary table... \nContact Admin later for rectification of the issue... ")
        #mycursor.execute("CREATE TABLE book_detail (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), author VARCHAR(255), total VARCHAR(255), available VARCHAR(255))")
        
    
        
    time.sleep(0.2)
    print("connected to database... ")
    frame(mycursor, mydb,TABLE)

def config_(cred_stat):
    print(".")
    time.sleep(0.1)
    print(".")
    time.sleep(0.1)
    print(".")
    time.sleep(0.1)
    print("Preparing Server details...")
    use_svdCred(cred_stat)
    time.sleep(0.1)
    HOST = input("Enter Host : \n |Localhost | Port | IP | \n  ")
    USER = input("Enter your user name  :")
    PASSWORD = maskpass.askpass("Enter your Password :")
    DATABASE = input("Enter your Database : \n |A New 'Database' will be created if it doesn't already exists|\n  ")
    TABLE = input("Enter your database Table :\n |A New Database 'Table' will be created if it doesn't already exists\n  ")
    save0(HOST,USER,PASSWORD,DATABASE,TABLE)    
    setup(HOST,USER,PASSWORD,DATABASE,TABLE)

def run():
    use_svdCred(1)
 
    
 
     
