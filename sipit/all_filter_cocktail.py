import sys
import json
import base64
import yaml
from datetime import date
from datetime import datetime
from myLogging import myLogging

inputdict=json.loads(base64.b64decode(sys.argv[1]))


with open("cocktails.yaml", "r") as file:
    cocktails_info = yaml.safe_load(file)


#filter po sastojcima

# inputdict={}
# inputdict["category"] = ["Dairy", "Gluten", "Vegan"]
# inputdict["ingredients"] = ["led"]
# inputdict["difficulty"] = ["Srednje", "lako"]
# inputdict["time"] = ["5-10 minuta"]

outdict_ingredients = []

filteredIngredients=[]

contains = 0
check ={}



if(inputdict["ingredients"]):

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
            outdict_ingredients.append(cocktail)


        for ingredientFilter in inputdict["ingredients"]:
            check[ingredientFilter] = 0

        contains = 0

    
    filteredIngredients = outdict_ingredients

else:
    filteredIngredients = cocktails_info




#filter po posebnosti


outdict_specialities =[]

filteredSpecialities =[]

contains = 0

if(inputdict["category"]):

    for cocktail in filteredIngredients:
        if cocktail["posebnosti"]:
            for specialItem in cocktail["posebnosti"]:
                for specialItem in  inputdict["category"]:
                        if specialItem.lower() in specialItem.lower():
                            contains+=1

        if contains == len(inputdict["category"]):
            outdict_specialities.append(cocktail)

        contains = 0

    filteredSpecialities = outdict_specialities

else:
    filteredSpecialities = filteredIngredients





#filter po težini

outdict_difficulty =[]

filteredDifficulty = []

if(inputdict["difficulty"]):

    for cocktail in filteredSpecialities:
        for diffItem in  inputdict["difficulty"]:
            if cocktail["tezina"].lower() in diffItem.lower():
                outdict_difficulty.append(cocktail)

    filteredDifficulty = outdict_difficulty

else:
    filteredDifficulty = filteredSpecialities




#filter po vremenu
inputdict_mod={}
inputdict_mod["time"] = []
inputdict_split = {}
inputdict_split["time"] = []

outdict_time ={}
outdict_time["all"] = []

if(inputdict["time"]):

    for item in inputdict["time"]:
        inputdict_mod["time"].append(item.replace(" minuta", ""))
        
    for item in inputdict_mod["time"]:
        if "-" in item:
            inputdict_split["time"].append(item.split("-"))

        elif ">" in item:
            inputdict_split["time"].append(item.split(">"))



    for cocktail in filteredDifficulty:
        
        time_prep = cocktail["duljina_pripreme"].replace(" min", "")
        for item in inputdict_split["time"]:
            if item[0] == "" and int(time_prep) > int(item[1]):
                outdict_time["all"].append(cocktail)

            else:
                if int(time_prep) >= int(item[0]) and int(time_prep) <= int(item[1]):
                    outdict_time["all"].append(cocktail)

else:
    outdict_time["all"] = filteredDifficulty



#logging.debug(outdict)

print(json.dumps(outdict_time, ensure_ascii=False))







    










