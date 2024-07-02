from utils.DBWriter import DBWriter
from utils.filterKeyNames import filterKeyNames
from utils.fixExternalId import fixExternalId
from utils.keyNamesToLowerCase import keyNamesToLowerCase
import asyncio, json

#takes out data from response from GQL database
def peelResponse(response):
    return response["data"][list(response["data"].keys())[0]]

#formats data to be usable as demodata for uois
def formatData(data, filt):
  data = fixExternalId(data)
  data = keyNamesToLowerCase(data)
  data = filterKeyNames(data, filt)
  return data

def getDemoData():
  with open('queries.json') as user_file:
    file_contnents = user_file.read()
  queries = json.loads(file_contnents)
  dbw = DBWriter()
  output = {}
  for key in queries:
      response = asyncio.run(dbw.queryGQL(queries[key]))
      output[key] = response["data"][list(response["data"].keys())[0]]
  output = formatData(output, "utils/key_name_filter.json")
  return output

if __name__=="__main__":
  file = open('demodata.json', 'w')
  file.write(json.dumps(getDemoData(), sort_keys=False, indent=4, default=str, ensure_ascii=False))