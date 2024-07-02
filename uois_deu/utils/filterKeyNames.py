#Function that renames keys in dictionary using filter(json file) and returns changed dictionary

#Filter syntax:
#{
# "tableName(eg.:programs)" : {
#       "originalKey": "newKey"
#   }
# }

import json

def filterKeyNames(data, filter="./utils/key_name_filter.json"):
    with open(filter) as user_file:
        file_contnents = user_file.read()
    filter = json.loads(file_contnents)

    for table in filter:
        for key in filter[table]:
            if data[table]:
                for i in range(len(data[table])):
                    if key in data[table][i].keys():
                        data[table][i][filter[table][key]] = data[table][i][key]
                        del data[table][i][key]
                    else:
                        print(f"Failed to filter {table}: {key}")
            else:
                print(f"Failed to filter {table}")
    return data

if __name__=="__main__":
    with open("./utils/filter_test_data.json") as user_file:
        file_contnents = user_file.read()
    data = json.loads(file_contnents)

    print(filterKeyNames(data))