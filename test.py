import mysql.connector
mydb = mysql.connector.connect(
    user="pma",
    host = "localhost",
    password ="pma_user560",
    database ="library_project",
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)


def enter_data(name_b,author_b,total_b,available_b):
    sql = "INSERT INTO book_detail (name, author,total,available) VALUES (%s, %s,%s,%s)"
    val = (name_b,author_b,total_b,available_b)
    mycursor.execute(sql, val)
    mydb.commit()



str_2 = "-"
print(str_2.center(50,'-'))
name_b = input("\nEnter the name of the book : ")


author_b = input("Enter the Name of the author :")
total_b = input(("Enter the Total numbers of copies :"))
available_b = input("Enter the currently available number of copies: ")


while name_b and author_b  and total_b and available_b != "":


    enter_data(name_b, author_b,total_b,available_b)


    print("Data entry successful!")

    print(str_2.center(50,'-'))
    break