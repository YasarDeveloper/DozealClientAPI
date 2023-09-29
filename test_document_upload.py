import pyodbc
# from datetime import datetime
import sql_conn
import os

# Database connection string
# conn_str = 'DRIVER={SQL Server};SERVER=YourServerName;DATABASE=YourDatabaseName;UID=YourUsername;PWD=YourPassword'
conn, cursor = sql_conn.get_sql_conn()

# Read file as binary data
def db_save(uploaded_files):
    # Assuming conn is already established
    cursor = conn.cursor()

    # print(uploaded_files)

    for file in uploaded_files:
        # Read the file's binary data
        print(file)
        binary_data = file.read()
        print(binary_data )

        # Get the file name
        file_name = file.filename

        # Insert binary data into SQL Server along with file name and current date and time
        cursor.execute(
            "insert into client.project_document (project_id,filename,file_data) values (?, ?, ?)",
            (1, file_name, pyodbc.Binary(binary_data))
        )
        conn.commit()
    # Commit the transaction and close the cursor and connection
    # conn.commit()
    # cursor.close()
    # conn.close()



def db_retrive():
    # Query to retrieve data. Adjust the table and column names to your needs.
    query = "SELECT filename, file_data FROM client.project_document"  # Update the WHERE clause as needed

    cursor.execute(query)

    # Fetch the filename and file_data from the executed query
    rows = cursor.fetchall()

    if rows:
        # Define the directory path where you want to save the files
        save_path = r'C:\Users\moham\OneDrive\Documents\dozeal_client-1\rest_api'

        for row in rows:
            filename, file_data = row

            # Full path to save the file
            output_file_path = os.path.join(save_path, filename)

            # Save the binary data as a file
            with open(output_file_path, 'wb') as file:
                file.write(file_data)

            print(f"File saved at {output_file_path}")
    else:
        print("No data found!")

    # cursor.close()
    # conn.close()

db_retrive()