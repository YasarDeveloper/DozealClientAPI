import jwt_encode_decode
import sql_conn

class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def create_account(data):
    name = data.get('name')
    user_name = data.get('user_name')
    phone_number = data.get('phone_number')
    company_name = data.get('company_name')
    job_position = data.get('job_position')
    email_address = data.get('email_address')

    if not name and phone_number and company_name and job_position and email_address:
        raise CustomError("Mandatory field Missing are missing.")

    # Insert into the database
    sql_insert = """
                INSERT INTO client.profile(name, user_name, phone_number, company_name, job_position, email_address)
                OUTPUT INSERTED.client_id
                VALUES (?, ?, ?, ?, ?, ?)
            """
    conn,cursor=sql_conn.get_sql_conn()
    data_to_insert = (name, user_name, phone_number, company_name, job_position, email_address)
    cursor.execute(sql_insert, data_to_insert)
    client_id = cursor.fetchone()[0]

    # Commit the transaction
    conn.commit()

    # Return the JWT encoded token
    if client_id:
        return jwt_encode_decode.login_encode(client_id, phone_number)
    
def update_account(data):
    print(data)
    name = data.get('name')
    user_name = data.get('user_name')
    phone_number = data.get('phone_number')
    company_name = data.get('company_name')
    job_position = data.get('job_position')
    email_address = data.get('email_address')
    client_id = data.get('client_id')

    if not name and phone_number and company_name and job_position and email_address:
        raise CustomError("Mandatory field Missing are missing.")

    # Insert into the database
    sql_insert = """
                UPDATE client.profile set name =? , phone_number  =?, company_name  =?, job_position  =?, email_address =?
                where client_id =?
            """
    conn,cursor=sql_conn.get_sql_conn()
    data_to_insert = (name, phone_number, company_name, job_position, email_address,client_id)
    cursor.execute(sql_insert, data_to_insert)
    # Commit the transaction
    conn.commit()


def get_data(client_id):
    # Define the SQL query
    sql_query = """
        select name,phone_number,company_name,job_position,email_address from client.profile where client_id=?
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
            raise CustomError("Client Projects Found.")

    except Exception as e:
        raise CustomError("Unable to fetch Client.")