import sql_conn


class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_project_data(client_id):
    # Define the SQL query
    sql_query = """
        SELECT id, title, description, status
        FROM client.project
        WHERE client_id = ?
    """

    # Establish a database connection
    conn, cursor = sql_conn.get_sql_conn()

    try:
        # Execute the SQL query with the client_id parameter
        cursor.execute(sql_query, (client_id,))

        # Fetch all rows of data
        project_data = cursor.fetchall()

        if project_data:
            # Return the list of projects
            return project_data
        else:
            raise CustomError("No Projects Found.")

    except Exception as e:
        raise CustomError("Unable to fetch project info.")

    # finally:
    #     # Close the cursor and the database connection
    #     cursor.close()
    #     conn.close()

# # Example usage
# client_id = 1
# projects = get_project_data(client_id)
# for project in projects:
#     print(project)
