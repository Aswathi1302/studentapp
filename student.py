import mysql.connector
mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database='studendb')
mycursor= mydb.cursor()

from secrets import choice


while True:
    print("select an option from the menu")
    print("1. add student")
    print("2.view student")
    print("3.search student")
    print("4.upadte student")
    print("5. delete student")
    print("6.exit")

    choice=int(input("enter your choice"))
    if(choice==1):
        print("student enter selected")
        name=input("enter a name")
        rollno=input("enter rollno")
        admNo=input("enter addmission number")
        college=input("enter college ")
        sql="INSERT INTO `students`(`name`, `rollno`, `admNo`, `college`) VALUES (%s,%s,%s,%s)"
        data=(name,rollno,admNo,college)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==2):
        sql="SELECT * FROM `students` "
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print("view student")
    elif(choice==3):
        print("search a student")
        adm=input("enter the admission number:--")
        sql="SELECT * FROM `students` WHERE `admNo` = "+adm
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    elif(choice==4):
        print("update student")
    elif(choice==5):
        print("delet student") 
        adm=input("enter the admission number:--")
        sql="DELETE FROM `students` WHERE `admNo`="+adm  
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully..") 
    elif(choice==6):
        break                