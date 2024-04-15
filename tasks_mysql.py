import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql#3",
    database="TASK_MANAGEMENT"
)
db_cursor = db_connection.cursor()

# Example: Insert a log entry into the database
sql_insert = "INSERT INTO TASKS (TASK_ID, TITLE, TASK_STATUS, CREATED_BY) VALUES (%s, %s, %s, %s)"
#log_data = (5, "MLGA", "COMPLETED","Smriti")  # Adjust values as needed
#db_cursor.execute(sql_insert, log_data)
#log_data = (6, "MLGA", "COMPLETED","Shreya")  # Adjust values as needed
#db_cursor.execute(sql_insert, log_data)
log_data = (7, "TDL", "COMPLETED","Yogita")  # Adjust values as needed
db_cursor.execute(sql_insert, log_data)
log_data = (8, "TDL", "COMPLETED","Rickvi")  # Adjust values as needed
db_cursor.execute(sql_insert, log_data)
log_data = (9, "NLP", "COMPLETED","Sahana")  # Adjust values as needed
db_cursor.execute(sql_insert, log_data)
log_data = (10, "MLGA", "COMPLETED","Aishwarya")  # Adjust values as needed
db_cursor.execute(sql_insert, log_data)
db_connection.commit()