#!/usr/bin/env python3
# List contents of an AWS S3 bucket

import boto3

c = boto3.client('s3')
r = c.list_objects(Bucket='<bucketName>')

for i in range(len(r['Contents'])):
    print(r['Contents'][i]['Key'])

