import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

inputdict=json.loads(base64.b64decode(sys.argv[1]))

logging=myLogging("/var/log/spitit.log")

with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)

#pretrazivanje
# outdict = {}
# for cocktail in cocktails_info:
#     if cocktail["naziv"] == inputdict["name"]:
#         outdict = cocktail

#slike
# outdict = {}
# for cocktail in cocktails_info:
#     if cocktail["naziv"] == inputdict["name"]:
#         outdict["image"] = cocktail["slika"]

#filter po sastojcima

inputdict["ingredients"] = ["sol", "limun"]

outdict = {}
outdict["name"] = []

contains = 0
cocktatailsArray = []
for cocktail in cocktails_info:
    for ingredient in cocktail["sastojci"]:
        for ingredientItem in inputdict["ingredients"]:
            if ingredientItem in ingredient:
                contains+=1

    if contains == len(inputdict["ingredients"]):
        outdict["name"].append(cocktail["naziv"])

    contains = 0





# outdict={}
# outdict['find'] = inputdict['koktel']


#logging.debug(outdict)


#print(json.dumps(outdict))

print(json.dumps(outdict, ensure_ascii=False))
