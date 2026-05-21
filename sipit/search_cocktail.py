import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

inputdict=json.loads(base64.b64decode(sys.argv[1]))

logging=myLogging("/var/log/spitit.log")

inputdict_split = {}
inputdict_split["name"] = inputdict["name"].split(" ")

with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)

# input["name"] = inputdict["name"].split(" ")
#pretrazivanje

#LISTA OBJEKATA ?????

outdict = {}
outdict["all"] = []

for cocktail in cocktails_info:
    for searchItem in inputdict_split["name"]:
        if searchItem.lower() == cocktail["naziv"].lower():
            outdict["all"].append(cocktail)
            





#print(json.dumps(outdict))

print(json.dumps(outdict, ensure_ascii=False))
