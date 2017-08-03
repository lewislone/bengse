# coding: UTF-8
import json
import csv
import os

def loadtojson(file):
    with open('account.json', 'w') as json_file:
        with open(file, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != '':
                    print row
                    account = {}
                    account['email'] = row[0]
                    account['pw'] = row[1]
                    json_file.write(json.dumps(account))


def loadjson(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data
