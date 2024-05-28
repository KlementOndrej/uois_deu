from DBWriter import DBWriter
import asyncio, json

def peelResponse(response):
    return response["data"][list(response["data"].keys())[0]]

with open('queries_working.json') as user_file:
  file_contnents = user_file.read()

queries = json.loads(file_contnents)

dbw = DBWriter()

output = {}

for key in queries:
    response = asyncio.run(dbw.queryGQL(queries[key]))
    output[key] = peelResponse(response)


#result = asyncio.run(dbw.queryGQL("query { roleTypePage { id name nameEn changedby {id} created lastchange createdby {id} roles {id} rbacobject {id} } }"))

file = open('final.json', 'w')
file.write(json.dumps(output, sort_keys=False, indent=4, default=str, ensure_ascii=False))
