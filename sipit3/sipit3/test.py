import sys
import json
import base64
from datetime import date
from datetime import datetime
from myLogging import myLogging

inputdict=json.loads(base64.b64decode(sys.argv[1]))
#inputdict=json.loads(sys.argv[1])


#logging=myLogging("/var/log/spitit.log")


outdict={}
outdict['ret']="Jupi radi"
outdict['test1'] = inputdict['text1']

#logging.debug(inputdict)


print(json.dumps(outdict))