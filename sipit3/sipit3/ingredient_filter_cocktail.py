import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

inputdict=json.loads(base64.b64decode(sys.argv[1]))

print(inputdict["ingredients"])

with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)


#filter po sastojcima

outdict = {}
outdict["name"] = []

contains = 0
check ={}

for ingredientFilter in inputdict["ingredients"]:
    check[ingredientFilter] = 0

for cocktail in cocktails_info:
    for ingredient in cocktail["sastojci"]:
        for ingredientItem in inputdict["ingredients"]:
            if ingredientItem.lower() in ingredient.lower():
                for ingredientFilter in inputdict["ingredients"]:
                    if ingredientFilter in ingredientItem and check[ingredientFilter] == 0:
                        check[ingredientFilter] = 1
                        contains+=1

                    else:
                        continue


    if contains == len(inputdict["ingredients"]):
        outdict["name"].append(cocktail["naziv"])


    for ingredientFilter in inputdict["ingredients"]:
        check[ingredientFilter] = 0

    contains = 0
    


print(json.dumps(outdict, ensure_ascii=False))
