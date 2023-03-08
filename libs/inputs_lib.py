import json
import os
import classes

from variables import URLS_PATH, JSON_PATH

def input_json(path):
    jsons = []
    files = os.listdir(path)
    for f in files:
        with open(path + f, 'r') as file:
            data = json.load(file)
        jsons.append(data)
    return jsons

def input_urls(path):
    data = []
    file = open(path)
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace('\n', '')
        if line != '':
            data.append(line)
    return data

def consolidate_for_mock():
    urls = input_urls(URLS_PATH)
    json = input_json(JSON_PATH)
    obj = classes.Variant()
    result = []
    for i in range(len(urls)):
        obj.string_for_mock = urls[i]
        obj.json_for_mock = json[i]
        result.append(obj)
    return result
