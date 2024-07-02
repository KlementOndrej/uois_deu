#Changes all key names to lowercase, also changes nameen to name_en!!!!

import json
from copy import deepcopy

def keyNamesToLowerCase(data):
    new_data = deepcopy(data)
    for table in data:
        for i in range(len(data[table])):
            for key in data[table][i]:
                if key!=key.lower():
                    new_data[table][i][key.lower()] = new_data[table][i][key]
                    del new_data[table][i][key]
    return new_data

if __name__=="__main__":
    with open("test.json") as user_file:
        file_contnents = user_file.read()
    data = json.loads(file_contnents)

    print(keyNamesToLowerCase(data))