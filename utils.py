# -*- coding: utf-8 -*-
import json



def open_json(path_json):
    json_message = open(path_json, 'r')
    message = json.load(json_message)
    return message


if __name__ == "__main__":
    print open_json('./message.json')
    print json.__file__