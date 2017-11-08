#!/usr/bin/env python3


"""
List contents of an AWS S3 bucket
Replace <bucketname> with a valid s3 bucket name
"""

import boto3

c = boto3.client('s3')

def main():
    try:
        r = c.list_objects(Bucket='<bucketname>')

        for i in range(len(r['Contents'])):
            print(r['Contents'][i]['Key'])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

