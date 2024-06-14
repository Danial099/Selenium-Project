import os
import json
import uuid


def read_json(relative_path):
    # Get the directory of the current script
    script_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the absolute path to the desired file
    file_path = os.path.join(script_dir, '..', relative_path)
    # Open and read the JSON file
    with open(file_path, 'r') as file:
        return json.load(file)


def update_user_creation_data_s3Folder(file_path):
    user_data_s3Folder = read_json(file_path)
    unique_id = str(uuid.uuid4())[:8]
    user_data_s3Folder["user_data"]["s3_folder"] = f"carros102_{unique_id}"
    with open(file_path, "w") as file:
        json.dump(user_data_s3Folder, file)
    return user_data_s3Folder["user_data"]


def update_user_creation_data_name(file_path):
    user_data_name = read_json(file_path)
    unique_id = str(uuid.uuid4())[:5]
    user_data_name["user_data"]["name"] = f"user_{unique_id}"
    with open(file_path, "w") as file:
        json.dump(user_data_name, file)
    return user_data_name["user_data"]

def save_credentials(email, password):
    user_credentials = {
        "email": email,
        "password": password,
        "expected_url": "https://testautomationchallenge-manager.testenv.impel.io/"
    }
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'new_login_data.json')
    with open(file_path, 'w') as file:
        json.dump(user_credentials, file)