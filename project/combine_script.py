import csv
import json
import boto3
import pandas as pd
import os
import glob


s3 = boto3.resource('s3', aws_access_key_id="123", aws_secret_access_key="124", endpoint_url="http://s3.localhost.localstack.cloud:4566")
sess = boto3.client("s3", endpoint_url="http://s3.localhost.localstack.cloud:4566/", region_name='us-east-1')

bucket_name = 'my_bucket'

sess.create_bucket(Bucket=bucket_name)


files = os.path.join("example*.csv")
files = glob.glob(files)
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_json('Combined_files.json')


with open ("Combined_files.json", "w") as f:
    s3object = s3.Object(bucket_name, "Combined_files.json")

    s3object.put(Body=(bytes(json.dumps("Combined_files.json").encode("UTF-8"))))
