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
    print("6. insert mark")
    print("7.view all mark")
    print("8.view subject wise mark")
    print("9.view individual mark")
    print("10.exit")

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
        admNo=input("enter addmission number:-")
        name=input("enter a name to be updated:-")
        rollno=input("enter rollno to be updated:-")
        college=input("enter college to be updated :-")
        sql="UPDATE `students` SET `name`='"+name+"',`rollno`='"+rollno+"',`college`='"+college+"' WHERE `admNo`=" +admNo
        mycursor.execute(sql)
        mydb.commit()
        print("Updated successfully..")
    elif(choice==5):
        print("delet student") 
        adm=input("enter the admission number:--")
        sql="DELETE FROM `students` WHERE `admNo`="+adm  
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully..") 
    elif(choice==6):
        print("insert mark")
        adm=input("enter the admission number:--")
        sql="SELECT `id`  FROM `students` WHERE `admNo`="+adm
        mycursor.execute(sql)
        result=mycursor.fetchall()
        id=0
        for i in result:
            id= str(i[0])
        print("student id is :",id)  

        physics=input("enter the physics mark:")
        chemistry=input("enter the cheistry mark:")
        mathematics=input("enter the mathematics mark:")
        sql="INSERT INTO `marks`(`studentid`, `physicsmark`, `chemistrymark`, `mathematicsmark`) VALUES (%s,%s,%s,%s)"
        data=(id,physics,chemistry,mathematics)
        mycursor.execute(sql,data)
        result=mycursor.fetchall()
        for i in result:
            print(i)
        print ("mark data inserted successfylly")    
    elif(choice==7):
        print("view all marks")
        sql="SELECT s.`name`, s.`rollno`, s.`admNo`, s.`college`, m.physicsmark , m.chemistrymark , m.mathematicsmark FROM `students` s JOIN marks m ON s.id=m.studentid"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)

    elif(choice==10):
        break        

              

