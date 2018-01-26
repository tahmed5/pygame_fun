import csv_edit
import time
import random

import mysql.connector

"""
esportsuser
cscs1
"""

usr = 'esportsuser'
pwd = 'cscs1'
h = 'raspberrypi.local'
db = 'esports'
p = 3306

#query = ""
#query2 = "SELECT Game, Score, User, Timestamp FROM gamescores WHERE user = 'Hubble'"

# Select data from table using SQL query.
#num_rows = cursor.execute(query)

#cursor.execute(query2)
#for (Game, Score, User, Timestamp) in cursor:
#  print(Game, Score, User, Timestamp)

#print(num_rows)
#cnx.commit()
#cursor.close()
#cnx.close()



class User_Profile():
    def __init__(self , username_in):
        self.username = username_in
        self.start = 0
        self.end = 0
        self.score = 0
        self.file = csv_edit.CSV_File_Write("")

        self.db = None
        self.cursor = None
        if (self.username == ""):
            print ("Error - User_Profile::Constructor - Username is not valid. User data can not be saved.")
        else:
            self.file.create_file(self.username + "_game_data" , "esp")
            self.file.add_record([self.username])

    def update_score(self , score_in):
        self.score = score_in

    def start_timer(self):
        self.start = time.time()

    def end_timer(self):
        self.end = time.time()

    def open_file(self , filename):
        self.file.open_file(filename)


    def save(self):
        self.file.open_file(None)
        self.file.save(None) # make a local copy.

        game = self.file
        
      
        
    def add_game_record(self , game):
        self.file.add_record([game , self.score])

        self.db = mysql.connector.connect(user=usr, password=pwd, host=h, database=db, port=p) # connect to database
        self.cursor = self.db.cursor()
      
        self.cursor.execute("INSERT INTO gamescores (User, Game, Score) VALUES('{0}' , '{1}' , {2})".format(self.username , game , self.score)) # execute insert command
        self.db.commit() # commit changes.

        self.cursor.close()
        self.db.close()
        
    


input()
        


