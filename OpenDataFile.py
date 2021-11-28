"""
#  _______    _          _______ 
# (       )  | \    /\  (  ____ \
# | () () |  |  \  / /  | (    \/
# | || || |  |  (_/ /   | |      
# | |(_)| |  |   _ (    | | ____ 
# | |   | |  |  ( \ \   | | \_  )
# | )   ( |  |  /  \ \  | (___) |
# |/     \|  |_/    \/  (_______)


# - - - With this code you can - - -
1: open. Write. Update Yaml file
2: open. Write. Update the Json file
3: open. Ini file
4: open. Write. Pickle file update

Made in Iran - by mkg
"""

""" - - - What is Update? - - -

open old file and Extraction data
old data + new data = Data
deleted old file yaml 
Created new File yaml and Writed Data in new file
"""


__version__ = "1.5.0"


import yaml          #YAML
import json          #JSON
import configparser  #INI
import pickle        #Pickle



# Open. Write. Update File Yaml
class Yaml: #V1.7
    def __init__(self, NameFile):
        self.NameFile = NameFile
    
    def read(self):
        with open(self.NameFile, "r") as FileYaml:
            try:
                return(yaml.safe_load(FileYaml))
            
            except yaml.YAMLError as exc:
                print(exc)
    
    def write(self, value, kind="a"):
        with open(self.NameFile, kind) as FileJson:
            yaml.dump(value, FileJson)
    
    def update(self, value):
        data = Yaml(self.NameFile).read()
        data.update(value)
        
        with open(self.NameFile, 'w') as yaml_file:
            yaml_file.write(yaml.dump(data, default_flow_style=False))


# Open. Write. Update File Json
class Json: #V1.5
    def __init__(self, NameFile):
        self.NameFile = NameFile
    
    def read(self):
        with open(self.NameFile) as FileJson:
            return(json.loads(FileJson.read()))
    
    def write(self, value, kind="a"):
        with open(self.NameFile, kind) as FileJson:
            json.dump(value, FileJson)
    
    def update(self, value, space=3):
        data = Json(self.NameFile).read()
        data.update(value)
        
        with open(self.NameFile, "w") as FileJson:
            json.dump(data, FileJson, indent=space)


# Open File Ini
class Ini:
    def __init__(self, NameFile):
        self.NameFile = NameFile
    
    def read(self):
        with open(self.NameFile): pass
        
        config = configparser.ConfigParser()
        config.read(self.NameFile)
        
        return{section: dict(config.items(section)) for section in config.sections()}


# Open. Write. Update File Pickle
class Pickle: #V1.7
    def __init__(self, NameFile):
        self.NameFile = NameFile
    
    def read(self):
        try:
            with open(self.NameFile, "rb") as FilePickle:
                return(pickle.load(FilePickle))
        
        except(EOFError):
            return({})
    
    def write(self, value, kind="a"):
        with open(self.NameFile, (kind+"b")) as FilePickle:
            pickle.dump(value, FilePickle)
    
    def update(self, value):
        data = Pickle(self.NameFile).read()
        data.update(value)
        
        with open(self.NameFile, "wb") as FilePickle:
            pickle.dump(data, FilePickle)


# The End
