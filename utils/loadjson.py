# coding: UTF-8
import json

def loadtojson(data, file):
    with open(file, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()

def loadfromjson(file):
    if os.path.exists(file):
        with open(file) as json_file:
            data = json.load(json_file)
            json_file.close()
            return data
    else:
        return {}
