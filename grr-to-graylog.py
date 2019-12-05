import yaml
import json
import requests
import pygelf
import sys
from grr_api_client import api


GRAYLOG_SERVER_GELF_URL = "http://localhost:12201/gelf"


def yaml_to_json(yaml_file):
    yaml_object = yaml.safe_load(yaml_file)
    return json.dumps(yaml_object)


def send_to_graylog(json_object, host, short_message):
    data = {
            "host": host,
            "short_message": short_message,
            "grr_data": json_object
        }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(GRAYLOG_SERVER_GELF_URL, data=json.dumps(data), headers=headers)


def grab_json_from_file(json_file_path):
    with open(json_file_path) as json_file:
        return json.load(json_file)


def gather_command_line_input():
    if len(sys.argv) != 4:
        print("Usage: python grr-to-graylog.py yaml_file_path client_id short_message")
        exit(1)
    else:

        return sys.argv[1:4]


def main():
    # Gather command line variables
    command_line_vars = gather_command_line_input()
    yaml_file_path = command_line_vars[0]
    client_id = command_line_vars[1]
    short_message = command_line_vars[2]

    # Convert GRR YAML data to JSON
    yaml_file = open(yaml_file_path, 'r')
    json_file = open("test.json", 'w')

    json_data = yaml_to_json(yaml_file)
    json_file.write(json_data)

    json_data = json.loads(json_data)
    
    #Send GRR JSON to Graylog
    for json_object in json_data:
        send_to_graylog(json_object, client_id, short_message)


main()
