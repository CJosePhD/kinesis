from __future__ import print_function
import boto3
from datetime import datetime
import time
import json
import base64
	

def lambda_handler(event, context ):
	output [ ]
	try :
		for record in event['records']):
		   print (record['recordId'])
		   payload = base64.b64decode(record['data']).decode('utf-8')
		   print (payload)
		   output_record = {
                    'recordId': record['TICKER'], # is this the problem? I used sequenceNumber, it is not right. 
                    'result': 'Ok',
                    'data': base64.b64encode(json.dumps(json_object).encode('utf-8')).decode('utf-8')
                   output.append(output_record)

		print('Successfully processed {} records.'.format(len(event['Records'])))
		return {'records': output}		   
	except Exception as e:
		print ( e ) 
                return ("Oops!")


if __name__ == '__main__':
	        lambda_handler ()
