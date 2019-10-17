#!/usr/bin/python3

from sys import argv
import os.path
save = __import__('7-save_to_json_file').save
load = __import__('8-load_from_json_file').load


filename = 'add_item.json'
res = []
if os.path.exists(filename):
    res = load(filename)
save(res + argv[1:], filename)
