#!/usr/bin/env python3


"""
List contents of an AWS S3 bucket
Replace <bucketname> with a valid s3 bucket name
"""

import argparse
import boto3

def main():
    """
    get s3 bucket contents and print
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("bucketname", help="A valid AWS S3 bucket name")
    args = parser.parse_args()

    try:
        client = boto3.client('s3')
        result = client.list_objects(Bucket=args.bucketname)

        for i in range(len(result['Contents'])):
            print(result['Contents'][i]['Key'])
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    main()
