import os
import time
import json
import requests
import argparse
from tabulate import tabulate

API_URL = "http://172.23.212.136:31856/api/todos"


def make_api_request(data=None):
    if data is None:
        response = requests.get(API_URL)
    else:
        response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")
        return None

## This will transform the JSON into a .TXT or a Table if the user requested it.
def save_output(data, output_format, output_path):
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
        file_path = os.path.join(output_path, "output.txt")
        with open(file_path, "w") as f:
            f.write(table)
        print(f"Output saved as {file_path}")
    else:
        print("Invalid output format. Please choose either 'json', 'txt', or 'table'.")


def main():
    parser = argparse.ArgumentParser(description="CLI tool for making API requests")
    parser.add_argument("--output", "-o", choices=["json", "txt", "table"], default="json", help="Output format (json, txt, or table)")
    parser.add_argument("--path", "-p", default="./", help="Destination path for the output file")
    parser.add_argument("--data", "-d", help="Data to be sent to the backend as a JSON string")

    args = parser.parse_args()
    output_format = args.output
    output_path = args.path
    data = json.loads(args.data) if args.data else None

    result = make_api_request(data)
    if result:
        save_output(result, output_format, output_path)

if __name__ == "__main__":
    main()