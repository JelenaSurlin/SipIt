import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

#inputdict=json.loads(base64.b64decode(sys.argv[1]))

#logging=myLogging("/var/log/spitit.log")

with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)


#filter po posebnosti
inputdict={}
inputdict["category"] = ["Dairy", "Gluten", "Vegan"]

outdict ={}
outdict["name"] =[]

contains = 0

for cocktail in cocktails_info:
    if cocktail["posebnosti"]:
        for specialItem in cocktail["posebnosti"]:
            for specialFilterItem in  inputdict["category"]:
                if specialFilterItem.lower() in specialItem.lower():
                    contains+=1

    if contains == len(inputdict["category"]):
        outdict["name"].append(cocktail["naziv"])

    contains = 0


#logging.debug(outdict)

print(json.dumps(outdict, ensure_ascii=False))