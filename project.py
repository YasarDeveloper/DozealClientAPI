import pyodbc
import sql_conn

# Database connection string
conn, cursor = sql_conn.get_sql_conn()

def create(uploaded_files, title, description, client_id):
    cursor = conn.cursor()
    print("*********************************")
    
    try:
        # Insert into client.project and use INSERTED to fetch the generated project_id
        cursor.execute(
            "INSERT INTO client.project(title, description, client_id) OUTPUT INSERTED.id VALUES (?, ?, ?);",
            (title, description, client_id)
        )
        
        project_id = cursor.fetchone()[0]

        print("Inserted project with ID:", project_id)

        # Loop through the uploaded files and insert them into client.project_document
        for file in uploaded_files:
            # Read the file's binary data
            binary_data = file.read()
            # Get the file name
            file_name = file.filename

            # Insert binary data into SQL Server along with file name
            cursor.execute(
                "INSERT INTO client.project_document (project_id, filename, file_data) VALUES (?, ?, ?)",
                (project_id, file_name, pyodbc.Binary(binary_data))
            )
            conn.commit()

        print("Files inserted successfully.")

    except Exception as e:
        print("Error:", str(e))
        conn.rollback()

    finally:
        cursor.close()
