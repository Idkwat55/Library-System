import sys
import time
import mysql.connector
import os


version = "1.0.0"


def tips():
    print("An error occured!")
    print("\n ~ Try using the keywords mention within brackets - ()")
    print("\n ~ Try closing the program and restarting it")
    print("\n ~ Check your connection to the server")
    print("\n ~ Contact Admin and make sure server is running properly.")


def restart():
    restart = input("Enter 'restart' to try to  restart the program :")
    restart.casefold()
    if restart == 'restart':
        setup()
    else:
        sys.exit("User Exited .")

def shutdown(*restart_hard):
    print("Exiting because of a user-related error...")
    tips()
    restart()

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

def end_frame():
    print("Ending session...")
    str_4 = "Session ENDED"
    print(str_4.center(100))

def frame(mycursor, mydb):
    start_frame()
    time.sleep(0.2)
    multi = input("\nChoose type of Entry - Single (s) or Multiple (m) :")
    multi.casefold()
    if multi == 's':
        main(mycursor, mydb)
        end_frame()
    elif multi == 'm':
        main(mycursor, mydb)
        main(mycursor, mydb)
        Multiple(mycursor, mydb)
        end_frame()
    else:
        tips()

def enter_data(name_b, author_b, total_b, available_b, mycursor, mydb):
    sql = "INSERT INTO book_detail (name, author,total,available) VALUES (%s, %s,%s,%s)"
    val = (name_b, author_b, total_b, available_b)
    mycursor.execute(sql, val)
    mydb.commit()

def main(mycursor, mydb):
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
        enter_data(name_b, author_b, total_b, available_b, mycursor, mydb)
        time.sleep(0.3)
        print("\nData entry successful!")
        print(str_2.center(50, '-'))
        break

    else:
        print("Error")
        shutdown()

def Multiple(mycursor, mydb):
    another_entry = input("Do another entry? (y/n): ")
    another_entry.casefold()
    if another_entry == 'y':
        main(mycursor, mydb)
        Multiple(mycursor, mydb)

    elif another_entry == 'n':
        pass

    else:
        print("Error occured")
        shutdown()

def checkTableExists(dbcur, tablename,mydb):
     
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        
         
        print("true")
        return True
    print("flase")
    print("Error!... \nCreating a temporary table... \nContact Admin later for rectification of the issue... ")
    dbcur.execute("CREATE TABLE IF NOT EXISTS book_detail (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), author VARCHAR(255), total VARCHAR(255), available VARCHAR(255))")
 
    return False

def setup():
    time.sleep(0.2)
    print("Starting up...")
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pma",
            password="pma_user560",
            database="library_project"
            )

        mycursor = mydb.cursor()

    except:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pma",
            password="pma_user560",
        )

        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE library_project ")
        print("Error!...\nCreating a temporary database... \nContact Admin later for rectification of the issue... ")
    
    finally:
        mydb = mysql.connector.connect(
            host="localhost",
            user="pma",
            password="pma_user560",
            database="library_project"
            )

        mycursor = mydb.cursor()
        time.sleep(0.2)
        print("SQL connection successful...")
        time.sleep(0.2)
        print("Checking database...")
        
        checkTableExists(mycursor,'book_detail',mydb)
        time.sleep(3)
        
        #print("Error!... \nCreating a temporary table... \nContact Admin later for rectification of the issue... ")
        #mycursor.execute("CREATE TABLE book_detail (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), author VARCHAR(255), total VARCHAR(255), available VARCHAR(255))")
        
    
        
    time.sleep(0.2)
    print("connected to database... ")
    frame(mycursor, mydb)
 


def run():
    setup()
 
     
