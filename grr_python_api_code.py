import yaml
import json
import requests
import pygelf
from grr_api_client import api

GRR_SERVER_URL = "http://192.168.213.141:8000"
GRR_SERVER_USERNAME = "admin"
GRR_SERVER_PASSWORD = "demo"

def grr_server_connect():
    return api.InitHttp(api_endpoint=GRR_SERVER_URL,auth=(GRR_SERVER_USERNAME, GRR_SERVER_PASSWORD))


# def processes()


def main():
    grrapi = grr_server_connect()
    client = "C.88b6cc9cbab27be3"
    ubuntu_client = grrapi.Client(client)
    flow = ubuntu_client.Flow("AAF4EAA3")
    processes = []
    count = 0
    for data in flow.ListResults():
        if (count > 0):
            break
        count += 1

        process_object = data.payload
        print(type(process_object))

        processes.append(data.payload)

    # url = "http://localhost:12201/gelf"
    # data = {
    #     "version": "1.1",
    #     "host": client,
    #     "short_message": "Process List for " + client,
    #     "process_list": processes
    # }
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)
    # print(r.headers)
    # print(r.status_code)

    
main()

# def start_hunt(grr_api, clients, flow_to_run):
#     flow_args = grr_api.types.CreateFlowArgs(flow_to_run["name"])
#     # print(type(flow_args))

#     hunt_runner_args = grr_api.types.CreateHuntRunnerArgs()
#     rule = hunt_runner_args.client_rule_set.rules.add()
#     rule.rule_type = rule.LABEL

#     hunt = grr_api.CreateHunt(flow_name=flow_to_run["name"], flow_args=flow_args,
#                          hunt_runner_args=hunt_runner_args)
#     # hunt = hunt.Start()
#     for data in hunt.ListResults(): 
#         print(data)


# def download_data_from_grr(json_config_data):
#     # print(json.dumps(json_config_data, sort_keys=True, indent=4))
#     clients = json_config_data["clients"]
#     flow_to_run = json_config_data["flow_to_run"]

#     grr_api = grr_server_connect()
#     start_hunt(grr_api, clients, flow_to_run)

    # grr_api = grr_server_connect()
    # ubuntu_client = grr_api.Client(client)
    # flow = ubuntu_client.Flow("AAF4EAA3")
    # start_hunt(clients, flows_to_run)

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

    #Grab Configuration Data from JSON File
    # json_config_file_path = gather_command_line_input()
    # json_config_data = grab_json_from_file(json_config_file_path)

    #Run Flows on Hosts and Download appropriate YAML Data from GRR
    # download_data_from_grr(json_config_data)


# def grr_server_connect():
#     return api.InitHttp(api_endpoint=GRR_SERVER_URL,auth=(GRR_SERVER_USERNAME, GRR_SERVER_PASSWORD))
# GRR_SERVER_URL = "http://192.168.213.141:8000"
# GRR_SERVER_USERNAME = "admin"
# GRR_SERVER_PASSWORD = "demo"