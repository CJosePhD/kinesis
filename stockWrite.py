import datetime
import json
import ast
import random
import boto3
import time

STREAM_NAME = "stock"


def get_data():
    return {
        "EVENT_TIME": datetime.datetime.now().isoformat(),
        "TICKER": random.choice(["AAPL", "AMZN", "MSFT", "INTC", "TBV"]),
        "PRICE": round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    response = kinesis_client.describe_stream(StreamName=stream_name)
    print (response)
    time.sleep (1)
    while True:
        data = get_data()
        print ( data )
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")
        time.sleep(5)
if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis'))
