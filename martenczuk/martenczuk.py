# KAMIL MARTENCZUK 13.03.2022
# FULL ACCESS TO DB TABLES VIEWS AND SCALAR FUNCTION
import json
import csv

class JSONFile:
    def __init__(self, path, name):
        self.filepath = path
        self.filename = name
        self.data = json.load(open(self.filepath + '/' + self.filename + '.json'))

class CSVFile:
    def __init__(self, path, name, delimiter):
        self.filepath = path
        self.filename = name
        self.delim = delimiter
        with open(self.filepath + '/' + self.fileName + '.csv', mode='r') as sourcefile:
            self.data = csv.reader(sourcefile, delimiter=self.delim)

