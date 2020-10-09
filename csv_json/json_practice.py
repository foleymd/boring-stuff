# json practice

import json

#creating some input
string_of_json_data = '{"name": "Marjorie", "is_cat": false, "mice_caught": 12, "feline_iq": null}'

# translating to python dictionary values
python_values = json.loads(string_of_json_data)

print(python_values)

# you can now translate it back the other way - from python to json

json_values = json.dumps(python_values)

print(json_values)
