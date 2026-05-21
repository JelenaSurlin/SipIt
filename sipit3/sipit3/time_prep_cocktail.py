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
inputdict_mod = {}
inputdict["time"] = "10-20 minuta"

inputdict_mod["time"] = inputdict["time"].replace(" minuta", "")

inputdict_split = {}
if "-" in inputdict["time"]:
   inputdict_split["time"] = inputdict_mod["time"].split("-")

elif ">" in inputdict["time"]:
    inputdict_split["time"] = inputdict_mod["time"].split(">")


print(inputdict_split)

outdict ={}
outdict["name"] =[]
for cocktail in cocktails_info:
    time_prep = cocktail["duljina_pripreme"].replace(" min", "")
    print(time_prep)
    if inputdict_split["time"][0] == "" and int(time_prep) > int(inputdict_split["time"][1]):
        outdict["name"].append(cocktail["naziv"])

    else:
        if int(time_prep) >= int(inputdict_split["time"][0]) and int(time_prep) <= int(inputdict_split["time"][1]):
            outdict["name"].append(cocktail["naziv"])



#logging.debug(outdict)

print(json.dumps(outdict, ensure_ascii=False))
