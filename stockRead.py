import boto3
import datetime
import time


def stockRead():
	my_stream_name = 'stock'
	recs = []
	# the stream I defined in aws console
	kinesis_client = boto3.client('kinesis', region_name='us-east-1')
	response = kinesis_client.describe_stream(StreamName=my_stream_name)

	my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

	# We use ShardIteratorType of LATEST which means that we start to look
	# at the end of the stream for new incoming data. Note that this means
	# you should be running the this lambda before running any write lambdas
	#
	shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
	                                                      ShardId=my_shard_id,
	                                                      #ShardIteratorType='TRIM_HORIZON')
	                                                      ShardIteratorType='LATEST')
	# get your shard number and set up iterator
	my_shard_iterator = shard_iterator['ShardIterator']

	record_count = 5
	while True:
	     record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator, Limit=5)
	     #print (len(record_response))
	     #print (record_response)
	     if len(record_response["Records"])  == record_count:
	       for i in range(len(record_response["Records"])):
	        #print (i)
	        print (record_response["Records"][i]["Data"])
	        shard_iterator = record_response['NextShardIterator']
	       record_count = 5
	       my_shard_iterator = shard_iterator
	     else:
	        time.sleep (1)
	     #print ( "first record_response", record_response )
	     #shard_iterator = record_response['NextShardIterator']
	     #recs = record_response['Records']
	     #print ("")
	     #record_count += len(record_response["Records"])
	     #print (recs)
	     #yield recs

if __name__ == '__main__':
	print ("in main")
	stockRead()
	print ("after mail call")
