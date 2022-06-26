from __future__ import print_function
import boto3
from datetime import datetime
import time
import json
	

def lambda_handler():
	

 with open ( "a", "r+") as f:
   for line in f:
    j = line.replace('{', "")
    j = j.replace('}', "")
    j = j.replace("'EVENT_TIME'", "")
    j = j.replace("'TICKER'", "")
    j = j.replace("'PRICE'", "")
    j = j.replace(":", "")
    j = j.replace("'", "")
    #print (k)
    #l = json.loads(j)
    #print (type(l))
    print ( j )





if __name__ == '__main__':
	        lambda_handler ()
