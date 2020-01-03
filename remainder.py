from datetime import date

today = date.today()
print("Today's date:", today)


from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
    	mySql_insert_query = """INSERT INTO USER(Id, Name, lastname, date,age)VALUES(1, 'sethu', 'kc', '2020-01-02',26) """

    	cursor = connection.cursor()
    	cursor.execute(mySql_insert_query)
    	connection.commit()
    	print(cursor.rowcount, "Record inserted successfully into user table")
   	cursor.execute("SELECT date FROM USER")

    	myresult = cursor.fetchall()

    	for x in myresult:
        	if (x==today):

            	for row in x:
        
          		sql="UPDATE USER SET age=age+1"
          		print("HAI..",row[1])
          		print("HAPPY BIRTHDAY")
       		else:
                	print("no birthday")

   	cursor.close()

	except mysql.connector.Error as error:
    		print("Failed to insert record into user table {}".format(error))

	finally:
   		if (connection.is_connected()):
        	connection.close()
        	print("MySQL connection is closed")







