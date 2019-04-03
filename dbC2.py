import pymysql
import pymysql.cursors

connection = pymysql.connect(host="localhost", user="root", passwd="", database="python")

def isInDb(username):
    cursor = connection.cursor()
    query = "SELECT * from user where username = '{}'".format(username)
    cursor.execute(query)
    count = cursor.fetchall()
    print(len(count))
    if len(count) == 1:
        #print("\nExists in db! \n")
        return True
    else :
    	#print("\nDoesn't exists in db! Add the name in database first!\n")
    	return False