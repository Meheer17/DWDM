import json
from config.config import OUTPUT_JSON_PATH

def save_to_json(data, file_path=OUTPUT_JSON_PATH):
    """
    Save data to a JSON file.
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {file_path} successfully!")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")