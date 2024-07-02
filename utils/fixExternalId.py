#changes external ids from "a": {"id": "b"} to "a_id": "b"

import json
from copy import deepcopy

def fixExternalId(data):
    new_data = deepcopy(data)
    for table in data:
        for i in range(len(data[table])):
            for key in data[table][i]:
                if isinstance(data[table][i][key], dict):
                    new_key = key + "_id"
                    new_data[table][i][new_key] = new_data[table][i][key]["id"]
                    del new_data[table][i][key]
    return new_data

if __name__=="__main__":
    with open("./utils/external_id_test_data.json") as user_file:
        file_contnents = user_file.read()
    data = json.loads(file_contnents)

    print(fixExternalId(data))