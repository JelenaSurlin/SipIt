
import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

#inputdict=json.loads(base64.b64decode(sys.argv[1]))

logging=myLogging("/var/log/spitit.log")

with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)


#LISTA OBJEKATA???


#pretrazivanje
outdict = {}
for cocktail in cocktails_info:
    outdict["name"] = cocktail["naziv"]
    outdict["recipe"] = cocktail["priprema"]


print(json.dumps(outdict))

print(json.dumps(outdict, ensure_ascii=False))
