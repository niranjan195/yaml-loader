#! /usr/bin/python3

import yaml
from pathlib import Path
import os
import time
import sys

class Loader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        print (self._root,stream.name)
        time.sleep(1)
        super(Loader, self).__init__(stream)
    
    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)

Loader.add_constructor('!import', Loader.include)

cur_dir = Path(__file__).resolve().parent
# file = cur_dir.parent / 'yaml_files' / 'simple_yaml.yaml'

def open_files(file,out_file):
    with open(file) as f:
        data = yaml.load(f,Loader=Loader)
        print (data)
        with open(out_file,'a') as f1:
            document=yaml.dump(data,f1)

def get_data(key):
    return data[key]

def main():
    if len(sys.argv) != 3:
        sys.stdout.write("usage: ./yaml_merger.py yaml_file_name out_file_name\n")
        sys.exit(1)
    print (sys.argv)
    file = sys.argv[1]
    out_file = sys.argv[2]
    open_files(file,out_file)

if __name__ == "__main__":
    # print (len(sys.argv))
    # print (sys.argv)
    main()