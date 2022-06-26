#! /bin/sh
/usr/local/bin/aws kinesis create-stream --stream-name $1 --shard-count 1
