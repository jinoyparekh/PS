import sys
import json
import yaml

# load json data
json_load = json.loads(open(sys.argv[1]).read())

# convert unicode to string
converted_json_data = json.dumps(json_load)

# output yaml
print(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))
