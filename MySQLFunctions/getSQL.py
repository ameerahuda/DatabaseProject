import mysql.connector
from DBandTables.ConnectionToDB import DatabaseConnection
from flask import Flask, render_template


def getAllStudents():
    try:
        mydb = DatabaseConnection()
        mycursor = mydb.cursor()

        statement = "SELECT * FROM Students"
        mycursor.execute(statement)
        data = mycursor.fetchall()
        return render_template("personnel_approval.html", data=data)
    except (mysql.connector.Error, mysql.connector.Warning) as e:
        print(e)
        print('FAILED TO SELECT: TRY AGAIN')
        exit(0)

