import json
import jsonschema
from jsonschema import validate

# Describe what kind of json you expect.
studentSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
}

def validateJson(jsonData):
    try:
       validate(instance=jsonData, schema=studentSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber":121, "marks": 72}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print("Given JSON data is Valid")
else:
    print("Given JSON data is InValid")
    