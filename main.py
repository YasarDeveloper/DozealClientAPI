from flask import Flask, jsonify, request
from flask_cors import CORS
import client
import get_project_data
# import test_document_upload as tst;
import project

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app


@app.route('/create_account', methods=['POST'])
def create_account():
    try:
        client_data = request.get_json()
        login_token = client.create_account(client_data)
        # print("successfully")
        # You can now use the 'phone_number' variable for further processing.
        return jsonify({'message': 'Account Created Successfully', "token": login_token})
    except Exception as e:
        return jsonify({'message': e})
    
@app.route('/update_account', methods=['POST'])
def update_account():
    try:
        client_data = request.get_json()
        login_token = client.update_account(client_data)
        # print("successfully")
        # You can now use the 'phone_number' variable for further processing.
        return jsonify({'message': 'Account Updated Successfully'})
    except Exception as e:
        return jsonify({'message': e})


@app.route('/get_data/<int:client_id>', methods=['GET'])
def get_data(client_id):
    print(client_id)
    project_data = get_project_data.get_project_data(client_id)
    print(project_data)
    projects = [{'project_id': row[0], 'project': row[1], 'project_description': row[2],'status': row[3]} for row in project_data]
    return jsonify(projects)

@app.route('/get_client_data/<int:client_id>', methods=['GET'])
def get_client_data(client_id):
    print(client_id)
    project_data = client.get_data(client_id)
    print(project_data)
    # name,phone_number,company_name,job_position,email_address
    projects = [{'name': row[0], 'phone_number': row[1], 'company_name': row[2],'job_position': row[3], 'email_address': row[4]} for row in project_data]
    return jsonify(projects)

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        project_title = request.form.get('project_title')
        project_description = request.form.get('project_description')
        client_id = request.form.get('client_id')

        # print(project_title,project_description,client_id)
        uploaded_files = request.files.getlist('file[]')
        # print(uploaded_files)
        # tst.db_save(uploaded_files)
        project.create(uploaded_files,project_title,project_description,client_id)
        
        return "Files uploaded and saved successfully", 200
    except Exception as e:
        print(e)
        # Handle the exception here, you can log it or provide an appropriate response to the client
        return f"An error occurred: {str(e)}", 500


if __name__ == '__main__':
    app.run()
