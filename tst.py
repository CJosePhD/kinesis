import json


a = open ("c", "r" )
for line in a:
   #print (line)
   b = json.loads(line)
   print (b["TICKER"])
