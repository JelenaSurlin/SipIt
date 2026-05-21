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


#filter po težini
inputdict={}
inputdict["difficulty"] = ["lako","teško"]

outdict ={}
outdict["name"] =[]
for cocktail in cocktails_info:
    for diffItem in  inputdict["difficulty"]:
        if cocktail["tezina"].lower() in diffItem.lower():
            outdict["name"].append(cocktail["naziv"])



#logging.debug(outdict)

print(json.dumps(outdict, ensure_ascii=False))
