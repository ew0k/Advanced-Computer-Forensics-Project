import yaml
import json

yaml_file = open("from_Process-exported-process.yaml", 'r')
json_file = open("test.json", 'w')
yaml_object = yaml.safe_load(yaml_file)
json.dump(yaml_object, json_file)

# print(type(json))
# parsed = json.loads(json[0])
# print(json.dumps(parsed, indent=4, sort_keys=True))