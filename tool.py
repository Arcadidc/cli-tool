import os
import time
import json
import requests
import argparse
import random
from tabulate import tabulate
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import configparser


def make_api_request(method, API_URL, data=None):

    """
    Makes an API request using the specified method and API URL.

    Args:
        method (str): The HTTP method to use ('get', 'post', or 'delete').
        API_URL (str): The URL of the API that we got from config.ini.
        data (dict): The data to be sent with the request (for 'post' or 'delete' method).

    Returns:
        dict or None: The response data in JSON format if the request is successful, None otherwise.
    """

    session = requests.Session()
    retry = Retry(connect=10, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)

    if method == "get":
        response = session.get(API_URL)
    elif method == "post":
        response = session.post(API_URL, data)
    elif method == "delete":
        url = str(API_URL) + "/" + str(data)
        response = session.delete(url)
    else:
        print("Invalid method. Please choose either 'get', 'post', or 'delete'")
        return None

    if response.status_code == 200:
        print(f"Request successful!")
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

def save_output(data, output_format, output_path):

    """
    Saves the data to an output file based on the specified format.

    Args:
        data: The data to be saved.
        output_format (str): The output format (json, txt, or table).
        output_path (str): The destination path for the output file.
    """

    if output_format == "json":
        file_path = os.path.join(output_path, "output.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Output saved as {file_path}")

    elif output_format == "txt":
        file_path = os.path.join(output_path, "output.txt")
        with open(file_path, "w") as f:
            f.write(str(data))
        print(f"Output saved as {file_path}")

    elif output_format == "table":
        headers = data[0].keys() if data else []
        rows = [list(item.values()) for item in data]
        table = tabulate(rows, headers, tablefmt="grid")
        file_path = os.path.join(output_path, "output_table.txt")
        with open(file_path, "w") as f:
            f.write(table)
        print(f"Output saved as {file_path}")
    else:
        print("Invalid output format. Please choose either 'json', 'txt', or 'table'.")

def workflow(data, output_path, API_URL):
        
        """
        Executes a workflow consisting of multiple steps:
        1. Creates a random number of elements in the backend.
        2. Gets all elements in JSON format and saves it to a file.
        3. Gets all elements in text format and saves it to a file.
        4. Gets all elements in table format and saves it to a file.
        5. Deletes all stored elements from the backend.

        Args:
            data (dict): Data to be sent to the backend.
            output_path (str): Destination path for output files.
        """       
        
        # Create a random number of elements between 10 and 100
        num_elements = random.randint(10, 100)
        
        for _ in range(num_elements):
            data['text'] = str(_)
            make_api_request("post",API_URL , data)

        # Step 2: Get all elements in JSON format and save it to a file.
        json_data = make_api_request("get", API_URL)
        if json_data:
            save_output(json_data, "json", output_path)

        # Step 3: Get all elements in text format save it to a file.
        text_data = json.dumps(json_data, indent=4)
        if text_data:
            save_output(text_data, "txt", output_path)

        # Step 4: Get all elements in table format and save it to a file.
        table_data = json_data
        if table_data:
            save_output(table_data, "table", output_path)

        # Step 5: Clean all stored elements generated during the workflow
        for obj in json_data:
            if '_id' in obj:
                make_api_request("delete",API_URL,obj['_id'])   

        print("All elements have been deleted from the backend!")

def main():

    # Read API_URL from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')
    API_URL = config.get('IP', 'API_URL')

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="CLI tool for making API requests")
    parser.add_argument("--get", "-g", choices=["json", "txt", "table"], default="json", help="Output format (json, txt, or table)")
    parser.add_argument("--path", "-p", default="./", help="Destination path for the output file")
    parser.add_argument("--add", "-a", help="Data to be sent to the backend as string")
    parser.add_argument("--delete", "-d", help="Data to be deleted from the database")
    parser.add_argument("--workflow", "-w", action="store_true", help="Execute the workflow")
    args = parser.parse_args()

    output_format = args.get
    output_path = args.path

    # Prepare data dictionary if add or workflow flag is provided
    data = None
    if args.add or args.workflow:
        data = {
            'text': args.add,
            'done': False
        }


    # Execute corresponding functions based on the arguments
    if args.workflow:
        workflow(data, output_path, API_URL)
    elif args.add:
        print(make_api_request("post", API_URL, data))
    elif args.delete:
        make_api_request("delete", API_URL, args.delete)
    elif args.get:
        save_output(make_api_request("get", API_URL), output_format, output_path)
    
if __name__ == "__main__":
    main()