import yaml
import json
import requests
import pygelf
from grr_api_client import api

GRR_SERVER_URL = "http://192.168.213.141:8000"
GRR_SERVER_USERNAME = "admin"
GRR_SERVER_PASSWORD = "demo"


def yaml_to_json(yaml_file):
    yaml_object = yaml.safe_load(yaml_file)
    return json.dumps(yaml_object)


def grr_server_connect():
    return api.InitHttp(api_endpoint=GRR_SERVER_URL,auth=(GRR_SERVER_USERNAME, GRR_SERVER_PASSWORD))


# def processes()


def main():
    yaml_file = open("from_Process-exported-process.yaml", 'r')
    json_file = open("test.json", 'w')
    json_data = yaml_to_json(yaml_file)
    json_data = json.loads(json_data)
    # json_file.write(json_data)
    json_data = json_data
    
    client = "localhost"
    url = "http://localhost:12201/gelf"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    count = 0
    for obj in json_data:
        # if count > 0:
        #     break
        count += 1
        data = {
            "version": "1.1",
            "host": client,
            "short_message": "Testing multiple",
            "grr_data": obj
        }
        json.dump(data, json_file)
        r = requests.post(url, data=json.dumps(data), headers=headers)
        # print(data)
    # print(r.headers)
    # print(r.status_code)

    

main()


# grrapi = grr_server_connect()
    # client = "C.88b6cc9cbab27be3"
    # ubuntu_client = grrapi.Client(client)
    # flow = ubuntu_client.Flow("AAF4EAA3")
    # processes = []
    # count = 0
    # for data in flow.ListResults():
    #     if (count > 0):
    #         break
    #     count += 1

    #     process_object = data.payload
    #     print(type(process_object))

    #     processes.append(data.payload)

    # print(json_data)
    # print(type(json_data))
