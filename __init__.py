from flask import Flask, request, url_for, render_template
import datetime
import os
import mysql.connector
app = Flask(__name__)


path2 = 'static/date.csv'

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='ss861008',
    database='memo'
)

@app.route('/', methods=['GET','POST'])
def index():
        if request.method == 'POST':
                mycursor = mydb.cursor()
                insert_stmt = (
                        "update sentence set poem=%s"
                )
                message = request.form["memo"]
                mycursor.execute(insert_stmt,(message,))
                select_stmt = "SELECT * FROM sentence WHERE poem = %(poem)s"                
                mycursor.execute(select_stmt, { 'poem': message })
                myresult = mycursor.fetchall()
                message = myresult
                message2 = print(message)
                mydb.commit()
                mydb.close()
                return render_template('index.html', message=message, message2=message2)
        else:
                mycursor = mydb.cursor()
                mycursor.execute('SELECT poem FROM sentence')
                myresult = mycursor.fetchall()
                message = myresult
                return render_template('index.html', message=message)



if __name__ == "__main__":
    app.run()